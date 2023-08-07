from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import redirect, render
import requests
import base64
import jwt

import os
import environ

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '../../.env'))

CUSTOS_CLIENT_ID = env("CUSTOS_CLIENT_ID")
CUSTOS_CLIENT_SEC = env("CUSTOS_CLIENT_SEC")
CUSTOS_REDIRECT_URI = env("CUSTOS_REDIRECT_URI")
CUSTOS_API_URL = env("CUSTOS_API_URL")
CUSTOS_SUPER_CLIENT_ID = env("CUSTOS_SUPER_CLIENT_ID")
UNDER_MAINTENANCE = env("UNDER_MAINTENANCE")

ENDPOINTS = {
    "IDENTITY": "identity-management/v1.0.0",
    "USERS": "user-management/v1.0.0",
    "GROUPS": "group-management/v1.0.0",
    "TENANTS": "tenant-management/v1.0.0",
    "SHARING": "sharing-management/v1.0.0",
    "SECRETS": "resource-secret-management/v1.0.0"
}


# Create your views here.
@api_view()
def get_config(request):
    # Just a simple REST API view to show how to access VUE_APP_* settings
    return Response({"UNDER_MAINTENANCE": settings.UNDER_MAINTENANCE})


@api_view()
def get_userinfo(request):
    if 'access_token' not in request.session:
        return HttpResponse('Unauthorized', status=401)
    else:
        payload = jwt.decode(jwt=request.session['access_token'], verify=False)
        return Response(payload)


def get_client_sec(request, client_id):
    response = requests.get(
        url=f"{CUSTOS_API_URL}/{ENDPOINTS['IDENTITY']}/credentials",
        params={'client_id': client_id},
        headers={
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {request.session['access_token']}"
        }
    )

    response_json = response.json()
    client_sec = response_json["custos_client_secret"]

    return client_sec


def get_client_auth_base64(request, client_id=None, client_sec=None):
    if client_id is None and client_sec is None:
        client_id = CUSTOS_CLIENT_ID
        client_sec = CUSTOS_CLIENT_SEC
    elif client_id is not None and client_sec is None:
        client_sec = get_client_sec(request, client_id)

    client_auth_base64 = f"{client_id}:{client_sec}"
    client_auth_base64 = client_auth_base64.encode("utf-8")
    client_auth_base64 = base64.b64encode(client_auth_base64).decode('utf-8')
    client_auth_base64 = f"Bearer {client_auth_base64}"

    return client_auth_base64


@api_view()
def get_auth_callback(request):
    code = request.GET.get("code", None)

    client_auth_base64 = get_client_auth_base64(request)

    response = requests.post(
        url=f"{CUSTOS_API_URL}/{ENDPOINTS['IDENTITY']}/token",
        json={'code': code, 'redirect_uri': CUSTOS_REDIRECT_URI,
              'grant_type': 'authorization_code'},
        headers={
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Authorization': client_auth_base64
        }
    )

    set_token_response_session(request, response)

    return redirect("/")


def set_token_response_session(request, response):
    response_json = response.json()
    request.session.set_expiry(response_json["expires_in"])
    request.session['access_token'] = response_json["access_token"]
    request.session['refresh_token'] = response_json["refresh_token"]
    request.session['id_token'] = response_json["id_token"]


def remove_token_response_session(request):
    del request.session['access_token']
    del request.session['refresh_token']
    del request.session['id_token']


custos_resource_map = {
    "credentials": f"{ENDPOINTS['IDENTITY']}/credentials"
}


@api_view(["GET", "POST", "PUT", "DELETE"])
def get_custos_api(request, endpoint_path=""):
    client_auth_base64 = get_client_auth_base64(request)
    client_auth_cases_map = {
        "token_password": endpoint_path == f"{ENDPOINTS['IDENTITY']}/token" and "grant_type" in request.data
                          and request.data["grant_type"] == "password",
        "token_refresh_token": endpoint_path == f"{ENDPOINTS['IDENTITY']}/token" and "grant_type" in request.data
                               and request.data["grant_type"] == "refresh_token",
        "token_authorization_code": endpoint_path == f"{ENDPOINTS['IDENTITY']}/token" and "grant_type" in request.data
                                    and request.data["grant_type"] == "authorization_code",
        "token_openid-configuration": endpoint_path == f"{ENDPOINTS['IDENTITY']}/.well-known/openid-configuration",
        "logout": endpoint_path == f"{ENDPOINTS['IDENTITY']}/user/logout",
        "tenant_create": endpoint_path == f"{ENDPOINTS['TENANTS']}/oauth2/tenant" and request.method == "POST"
    }

    authorization_header = None
    if True in client_auth_cases_map.values():
        authorization_header = client_auth_base64
    elif "access_token" in request.session:
        authorization_header = f"Bearer {request.session['access_token']}"

    if client_auth_cases_map["tenant_create"] and "parent_client_id" in request.data:
        if request.data["parent_client_id"] == CUSTOS_SUPER_CLIENT_ID:
            authorization_header = None
        else:
            authorization_header = get_client_auth_base64(request, client_id=request.data["parent_client_id"])

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': authorization_header
    }

    url = f"{CUSTOS_API_URL}/{endpoint_path}?{request.GET.urlencode()}"
    data = request.data

    if client_auth_cases_map["token_refresh_token"] or client_auth_cases_map["logout"]:
        data['refresh_token'] = request.session['refresh_token']

    response = requests.request(
        method=request.method,
        url=url,
        json=data,
        headers=headers
    )
    response_json = response.json()

    if client_auth_cases_map["token_password"] or client_auth_cases_map["token_authorization_code"] or \
            client_auth_cases_map["token_refresh_token"]:
        set_token_response_session(request, response)
        return Response(data={}, status=response.status_code)
    elif client_auth_cases_map["token_openid-configuration"]:
        authorization_endpoint = response_json["authorization_endpoint"]
        url = f"{authorization_endpoint}?response_type=code&client_id={CUSTOS_CLIENT_ID}&redirect_uri={CUSTOS_REDIRECT_URI}&scope=openid"

        ciLogonInstitutionEntityId = False  # TODO

        if ciLogonInstitutionEntityId:
            url = f"{url}&kc_idp_hint=oidc&idphint={ciLogonInstitutionEntityId}"
        else:
            url = f"{url}&kc_idp_hint=oidc"

        return Response({"authorization_endpoint": url}, status=response.status_code)
    elif client_auth_cases_map["logout"]:
        remove_token_response_session(request)
        return Response(data=response_json, status=response.status_code)
    else:
        return Response(data=response_json, status=response.status_code)

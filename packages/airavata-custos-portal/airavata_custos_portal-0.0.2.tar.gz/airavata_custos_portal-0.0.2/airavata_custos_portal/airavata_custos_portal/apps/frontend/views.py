from django.shortcuts import render

# Create your views here.

def home(request, **kwags):
    return render(request, "airavata_custos_portal_frontend/index.html")


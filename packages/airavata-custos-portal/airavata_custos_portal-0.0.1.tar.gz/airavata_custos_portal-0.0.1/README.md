# custos-demo-gateway

## Project setup

```
yarn install
```

### Compiles and hot-reloads for development

```
yarn serve
```

### Compiles and minifies for production

```
yarn build
```

### Lints and fixes files

```
yarn lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

## Running the Django server locally

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd airavata_custos_portal/
./manage.py migrate
./manage.py runserver
```

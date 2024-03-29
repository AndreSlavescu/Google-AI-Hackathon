# Google-AI-Hackathon

## Setup 

### Install Dependencies

```bash
pipenv shell
pipenv install
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

### Initialize Google Cloud API

```bash
gcloud init
gcloud auth application-default login
```
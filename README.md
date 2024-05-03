# Google-AI-Hackathon

## Setup 

### Install Dependencies

```bash
pipenv shell
pipenv install
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# install bun >= 1.0.21 for ollama dependency
curl -fsSL https://bun.sh/install | bash

# support latest GCP AI platform
pip install --upgrade google-cloud-aiplatform
```

### Build Open Web UI

```bash
chmod +x ollama-reqs.sh
./ollama-reqs
```

### Run Open Web UI

### Initialize Google Cloud API

```bash
gcloud init
gcloud auth application-default login
```

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

### Setup Marqo
Assuming you have Docker installed:
```bash
docker pull marqoai/marqo:latest
docker rm -f marqo
docker run --name marqo -it -p 8882:8882 marqoai/marqo:latest
```
```bash
python setup_marqo.py
```

### Build Ollama webUI

```bash
chmod +x ollama-reqs.sh
./ollama-reqs
```

### Initialize Google Cloud API

```bash
gcloud init
gcloud auth application-default login
```
### Running the API Server

To run the API server from `app.py`, follow these steps:

```bash
pipenv run uvicorn app:app --reload
```

Then visit:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

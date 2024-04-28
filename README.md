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

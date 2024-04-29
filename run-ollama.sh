#!/bin/bash

docker run -d -p 3000:8080 \
  -e OLLAMA_API_BASE_URL=http://127.0.0.1:8000 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main

#!/bin/bash

git clone https://github.com/open-webui/open-webui.git
cd open-webui/
cp -RPp .env.example .env
npm i
npm run build
cd ./backend
pip install -r requirements.txt -U
bash start.sh

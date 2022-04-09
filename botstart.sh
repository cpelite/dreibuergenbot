#!/bin/sh
source venv/bin/activate
echo "Ziehe Änderungen aus dem Github-Repo"
git pull
echo "Starte Bot..."
nohup python3 dbbot.py
echo "Beende Bot."
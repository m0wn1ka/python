#!/bin/sh
python scrape.py
git add .
git commit -m "commit"
git pull
git push -u origin main

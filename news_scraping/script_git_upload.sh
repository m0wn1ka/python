#!/bin/sh
python scrape.py
git add .
git commit -m "commit"
git push

#!/bin/sh
python /home/radha/Downloads/downloads/python/news_scraping/scrape.py
touch file
sleep 5
xdg-open .

git add .
git commit -m "commit"
git push -u origin main

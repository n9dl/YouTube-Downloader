@echo off
title YouTube Downloader Server
echo Starting the server, please wait...


cd /d "D:\Web Codeing\Projects\youtube_downlodar"

start http://127.0.0.1:5000

python app.py

pause
# Local YouTube Downloader

A lightweight, locally hosted web application designed to download YouTube videos in the highest possible quality. By utilizing `yt-dlp` and `FFmpeg`, this tool seamlessly merges high-resolution video (such as 1080p and 4K) and audio streams directly on your local machine.

## Prerequisites

Ensure your system meets the following requirements before running the application:

1. **Python 3.x:** Must be installed and added to your system's PATH.
2. **FFmpeg:** Required for merging the separated video and audio streams. 
   * *Windows Installation:* Open PowerShell as an Administrator and execute: 
     `winget install ffmpeg`
     *(Note: A system restart is highly recommended after installation to update the PATH variables).*
3. **Python Dependencies:** Install the required libraries by running the following command in your terminal or command prompt:
   `pip install flask yt-dlp`

## Installation & Usage

1. Clone or download this repository to your local machine.
2. Open the `Start_Downloader.bat` file using any text editor and update the directory path to match the exact location of your project folder.
3. Double-click the `Start_Downloader.bat` file. This batch script will automatically launch the local Flask server and open the web interface (`http://127.0.0.1:5000`) in your default web browser.
4. Paste the desired YouTube URL, select your preferred video quality from the dropdown menu, and click "Download".
5. To stop the server and the application, simply close the active command prompt window.

## Features

* **High-Quality Downloads:** Capable of downloading actual 1080p+ videos with audio by processing them locally.
* **Automated Cleanup:** To optimize local storage, the application automatically deletes temporary files from the server's download directory that are older than one hour.
* **One-Click Startup:** The included `.bat` file streamlines the launch process, requiring no manual terminal commands for daily use.

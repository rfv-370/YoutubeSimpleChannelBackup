# YoutubeSimpleChannelBackup ( yt-scb )

Youtube Backup Channel Python Script
Backup your Youtube Channel rapidly.
This python script downloads videos from YouTube, Twitch, and related websites using the yt_dlp module. It can download a single video, all videos from a channel, or all videos from a playlist.

## Requirements
- Python 3
- yt_dlp
To install yt_dlp : goto : https://github.com/yt-dlp/yt-dlp

## Usage

- python3 yt_downloader.py URL_Youtube /folder_destination

URL: the URL of the video, channel, or playlist to download
folder_destination: the directory where the downloaded files will be saved
https://www.youtube.com/[@YourChannel]/videos

/folder_destination:
the folder must be created and existing. It deos not create the folder for many reasons...

#### Download format
The format variable sets the download format. By default, it is set to the best quality MP4 format.
It download to the bets available quality.

## Fixing characters
The script also includes a command to fix character encoding issues in the downloaded filenames using slugify. 

## Supported URLs
The script supports the following types of URLs:

YouTube channel: [https://www.youtube.com/@channel_name/videos]

And it does change the filenames so the OS (linux, windows and dropbox, Mac, etc...) can coope with the filenames.

## Platforms:
Tested Dec. 2024 on Ubuntu Server 24.x - should work on any Linux distro. - might need adjustment for Windows or Mac.


# YoutubeSimpleChannelBackup

Youtube Backup Channel Python Script

This script downloads videos from YouTube, Twitch, and related websites using the yt_dlp module. It can download a single video, all videos from a channel, or all videos from a playlist.

## Requirements
- Python 3
- yt_dlp
To install yt_dlp : goto : https://github.com/yt-dlp/yt-dlp

## Usage

- python3 yt_downloader.py <URL> /folder_destination

URL: the URL of the video, channel, or playlist to download
folder_destination: the directory where the downloaded files will be saved

#### Download format
The format variable sets the download format. By default, it is set to the best quality MP4 format.
It download to the bets available quality.

## Fixing characters
The script also includes a command to fix character encoding issues in the downloaded filenames using slugify. 

## Supported URLs
The script supports the following types of URLs:

YouTube channel: [https://www.youtube.com/@channel_name/videos]

And it does change the filenames so the OS (linux, windows and dropbox, Mac, etc...) can coope with the filenames.

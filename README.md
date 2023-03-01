# YoutubeSimpleChannelBackup

Youtube Backup Channel Python Script

This script downloads videos from YouTube, Twitch, and related websites using the yt_dlp module. It can download a single video, all videos from a channel, or all videos from a playlist.

## Requirements
- Python 3
- yt_dlp
- To install yt_dlp, run pip install yt-dlp.

## Usage

- python3 yt_downloader.py URL folder_destination

URL: the URL of the video, channel, or playlist to download
folder_destination: the directory where the downloaded files will be saved

## Options
#### Download rate limit

The ratelimit variable sets the download rate limit in bytes per second. By default, it is set to 5000000 bytes per second.

#### Download format
The format variable sets the download format. By default, it is set to the best quality MP4 format.

## Fixing characters
The script also includes a command to fix character encoding issues in the downloaded filenames. It runs a separate Python script fixChar.py located in the same directory as yt_downloader.py. The command is run automatically after the downloads are complete.

## Supported URLs
The script supports the following types of URLs:

YouTube channel: https://www.youtube.com/c/channel_name
YouTube user: https://www.youtube.com/user/username
YouTube playlist: https://www.youtube.com/playlist?list=playlist_id
YouTube video: https://www.youtube.com/watch?v=video_id
Twitch channel: https://www.twitch.tv/channel_name
Twitch clip: https://clips.twitch.tv/clip_id

And it does change the filenames so the OS (linux, windows and dropbox, Mac, etc...) can coope with the filenames.

# FixChar Script
This script replaces certain characters in the filenames of files in a specified directory. It is designed to be used with the yt_downloader.py script, which downloads videos from various websites, including YouTube and Twitch. Some video titles may contain characters that can cause problems when used as filenames. This script replaces those characters with a specified character (by default, an underscore).

## Usage

- python3 fixChar.py folder_path [char_op]

folder_path: the directory containing the files to be renamed
char_op (optional): the character to be replaced (default is None)

## Options
#### Replacement character

The outChar variable sets the replacement character. By default, it is set to an underscore (_).

#### Characters to replace
The chars list contains the characters that will be replaced in the filenames. By default, it includes the following characters:

- / \\ | \# / ? ¿

### Additional character to replace
The charOp variable sets an additional character to be replaced. By default, it is set to None.

#### Example:
To fix the filenames in a directory called videos, run the following command:

- python3 fixChar.py videos/

This will replace all instances of the characters listed in the chars list with underscores in the filenames of the files in the videos directory.

To replace an additional character (e.g. spaces) with underscores, run the following command:

- python3 fixChar.py videos/ " "

This will replace all instances of spaces with underscores in the filenames of the files in the videos directory.

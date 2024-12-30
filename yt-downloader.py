import os
import logging
import yt_dlp
from slugify import slugify
from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser

# Set up logging
LOG_FILE = "youtube_channel_backup.log"
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

def setup_output_directory(directory: str):
    """Ensure the target directory exists."""
    try:
        Path(directory).mkdir(parents=True, exist_ok=True)
        logging.info(f"Output directory set up: {directory}")
    except Exception as e:
        logging.error(f"Failed to set up output directory: {directory}. Error: {e}")
        raise

def get_yt_dlp_options(output_dir: str):
    """Configure yt-dlp options for downloading videos."""
    return {
        'format': 'best',
        'outtmpl': os.path.join(output_dir, '%(upload_date)s_%(title)s_%(id)s.%(ext)s'),
        'writeinfojson': True,
        'quiet': False,
        'noprogress': False,
        'retries': 3,
        'logger': logging.getLogger()
    }

def clean_filename(title: str):
    """Clean video title for safe filenames."""
    return slugify(title, max_length=200)

def download_videos(channel_url: str, output_dir: str):
    """Download all videos from the given YouTube channel or playlist."""
    options = get_yt_dlp_options(output_dir)
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            logging.info(f"Starting download for: {channel_url}")
            result = ydl.extract_info(channel_url, download=True)  # Ensure download=True

            if 'entries' in result:
                for entry in result['entries']:
                    video_url = entry.get('webpage_url', None)
                    video_title = clean_filename(entry.get('title', 'Unknown Title'))
                    if video_url:
                        logging.info(f"Preparing to download: {video_title} ({video_url})")
                        try:
                            ydl.download([video_url])
                            logging.info(f"Successfully downloaded: {video_title}")
                        except yt_dlp.utils.DownloadError as e:
                            logging.error(f"Failed to download {video_title}: {e}")
                        except Exception as ex:
                            logging.error(f"Unexpected error downloading {video_title}: {ex}")
                    else:
                        logging.warning(f"No URL found for video: {entry}")
            else:
                logging.warning("No entries found for the provided URL.")
        except yt_dlp.utils.DownloadError as e:
            logging.error(f"Error downloading videos: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

def validate_url(channel_url: str):
    """Ensure the provided URL is valid."""
    if not channel_url.startswith("http"):
        logging.error("Invalid URL. Ensure it starts with http or https.")
        raise ValueError("Invalid URL format.")

def main():
    """Main function to parse arguments and start the backup process."""
    parser = ArgumentParser(description="Backup all videos from a YouTube channel or playlist.")
    parser.add_argument("channel_url", help="YouTube channel or playlist URL")
    parser.add_argument("output_dir", help="Directory to save downloaded videos")

    args = parser.parse_args()

    try:
        validate_url(args.channel_url)
        setup_output_directory(args.output_dir)
        download_videos(args.channel_url, args.output_dir)
    except Exception as e:
        logging.error(f"Backup process failed: {e}")

if __name__ == "__main__":
    main()

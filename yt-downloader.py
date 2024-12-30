import yt_dlp
import argparse
from pathlib import Path
import logging
#revised with chatgpt dec 2024

def setup_logging():
    """Set up logging to console and file."""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler("youtube_channel_backup.log"),
                            logging.StreamHandler()
                        ])

def parse_arguments():
    """Parse command line arguments for URL and output directory."""
    parser = argparse.ArgumentParser(description='Download an entire YouTube channel or playlist for backup.')
    parser.add_argument('url', type=str, help='YouTube channel or playlist URL')
    parser.add_argument('output_path', type=str, help='Path where the videos will be saved')
    return parser.parse_args()

def get_ydl_options(output_path):
    """Configure yt-dlp options for downloading."""
    return {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': str(Path(output_path) / '%(uploader)s - %(upload_date)s - %(title)s [%(id)s].%(ext)s'),
        'merge_output_format': 'mp4',  # Ensure the output format is MP4 if merging is necessary
        'noplaylist': False,  # Download the entire playlist/channel
        'download_archive': str(Path(output_path) / 'downloaded_videos.txt'),  # Keep track of downloaded videos
        'progress_hooks': [progress_hook],  # Handle progress updates
        'postprocessors': [{
            'key': 'FFmpegMetadata',
            'add_metadata': True
        }]
    }

# Global counters
downloaded_videos = 0
errors = 0

def progress_hook(d):
    """Handle progress updates and logging."""
    global downloaded_videos, errors
    if d['status'] == 'finished':
        downloaded_videos += 1
        logging.info(f"Finished downloading {d['filename']}")
    elif d['status'] == 'error':
        errors += 1
        logging.error(f"Error downloading {d['filename']}")

def download_channel(url, output_path):
    """Use yt-dlp to download the entire YouTube channel or playlist."""
    ydl_opts = get_ydl_options(output_path)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    setup_logging()
    args = parse_arguments()
    download_channel(args.url, args.output_path)
    logging.info("Backup completed successfully.")
    logging.info(f"Summary: {downloaded_videos} videos downloaded successfully, {errors} errors encountered.")

if __name__ == '__main__':
    main()

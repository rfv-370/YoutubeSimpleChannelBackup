import yt_dlp
import argparse
from pathlib import Path
import logging

# Global counters
downloaded_videos = 0
errors = 0

def setup_logging():
    """Set up logging to console and file."""
    log_file = "youtube_channel_backup.log"
    logging.basicConfig(
        level=logging.DEBUG,  # Log all levels
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, mode='a'),  # Append to log file
            logging.StreamHandler()  # Print to terminal
        ]
    )
    logging.info(f"Logging initialized. Logs will be saved to {log_file}")

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

def progress_hook(d):
    """Handle progress updates and logging."""
    global downloaded_videos, errors
    if d['status'] == 'finished':
        downloaded_videos += 1
        logging.info(f"Finished downloading: {d['filename']}")
    elif d['status'] == 'error':
        errors += 1
        logging.error(f"Error downloading: {d['filename']}")

def download_channel(url, output_path):
    """Use yt-dlp to download the entire YouTube channel or playlist."""
    ydl_opts = get_ydl_options(output_path)
    logging.info(f"Starting download from {url} to {output_path}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    setup_logging()
    args = parse_arguments()

    # Create output directory if it doesn't exist
    output_path = Path(args.output_path)
    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created output directory: {output_path}")

    try:
        download_channel(args.url, args.output_path)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Backup process completed.")
        logging.info(f"Summary: {downloaded_videos} videos downloaded successfully, {errors} errors encountered.")

if __name__ == '__main__':
    main()

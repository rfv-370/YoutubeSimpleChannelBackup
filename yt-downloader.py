import yt_dlp
import sys, os

# Define download rate limit in byte
ratelimit = 5000000

# Define download format
format = 'best[ext=mp4]'

# Get url as argument
try:
    url = sys.argv[1]
    path = sys.argv[2]
except:
    sys.exit('Usage: python3 yt_dowmloader.py URL folder_destination')

# Download all videos of a channel
if url.startswith((
    'https://www.youtube.com/c/', 
    'https://www.youtube.com/channel/',
    'https://www.youtube.com/@', 
    'https://www.youtube.com/user/')):
    ydl_opts = {
        'ignoreerrors': True,
        'abort_on_unavailable_fragments': True,
        'format': format,
        'outtmpl': path + '%(title)s.%(ext)s',
        'ratelimit': ratelimit,
    }

# Download all videos in a playlist
elif url.startswith('https://www.youtube.com/playlist'):
    ydl_opts = {
        'ignoreerrors': True,
        'abort_on_unavailable_fragments': True,
        'format': format,
        'outtmpl': path + '%(title)s.%(ext)s',
        'ratelimit': ratelimit,
    }

# Download single video from url
elif url.startswith((
    'https://www.youtube.com/watch', 
    'https://www.twitch.tv/', 
    'https://clips.twitch.tv/')):
    ydl_opts = {
        'ignoreerrors': True,
        'abort_on_unavailable_fragments': True,
        'format': format,
        'outtmpl': path + '%(title)s.%(ext)s',
        'ratelimit': ratelimit,
    }

# Downloads depending on the options set above
if ydl_opts is not None:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
print("Fixing characters...")
os.system("sudo python3 "+os.path.dirname(__file__) + "/fixChar.py " + path)

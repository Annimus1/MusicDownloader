from pytubefix import YouTube
from pytubefix.cli import on_progress

# Source
# pytubefix = https://github.com/JuanBindez/pytubefix

def getUrlFromFile(path, output_dir):
    with open(path, "r") as file:
        for url in file:
            DownloadAudio(url, output_dir)

def DownloadAudio(url, output_dir):
    YouTubeAudio = YouTube(url, use_oauth=True, on_progress_callback = on_progress)
    audio = YouTubeAudio.streams.get_audio_only()
    audio.download(output_path=output_dir, mp3=True)

def DownloadPlaylist(url, output_dir):
    playlist = Playlist(url)

    for video in pl.videos:
        audio = video.streams.get_audio_only()
        audio.download(output_path=output_dir, mp3=True)   

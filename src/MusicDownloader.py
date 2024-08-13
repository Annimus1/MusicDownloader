#!/usr/bin/python3

from os import path 
import platform
import getpass
import click
from Functions import getUrlFromFile, DownloadAudio, DownloadPlaylist

# Source 
# clcik = https://pywombat.com/articles/CLI-python


@click.command()
@click.option('--file', '-f', type=str, required=True, help="Text file or String with data source URL to download from YouTube.")
@click.option('--playlist', '-p', is_flag=True, show_default=True, default=False, help="String with data source URL to download a Playlist from YouTube.")
@click.option('--output', default="" , help='Output directory to dump the data.')
def main(file, output, playlist):
    
    os = platform.system()
    username = getpass.getuser()
    
    # Set the output directory depending on the operative system.
    if(os == "Linux" and not output):
        output = path.join("/", "home", username, "Music")

    if(os == "Windows" and not output):
        output = path.join("C", "Users", username, "Music")

    # Download audio from file
    if(path.isfile(file)):
        getUrlFromFile(file, output)

    # Download audio from url
    if(file.startswith("https://www.youtube.com/watch?")):
        if(playlist):
            DownloadPlaylist(file, output)
        else:
            DownloadAudio(file, output)


if __name__ == '__main__':
    main()

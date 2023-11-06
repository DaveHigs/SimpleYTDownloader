import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError, PytubeError
from folder_chooser import webview_file_dialog

def download_mp4(video_url):
    '''
    Download a video in MP4 format.

    This function takes a video URL and attempts to download the video in MP4
    format.

    Args:
        video_url (str): The URL of the video to be downloaded.

    Returns:
        str or bool: If the download is successful, it returns True. If an error
        occurs, it returns a string containing an informative error message.

    Raises:
        - VideoUnavailable: If the video is unavailable or has been deleted.
        - RegexMatchError: If the video URL format is not supported.
        - PytubeError: If a PyTube-specific error occurs.
        - Exception: If an unexpected error occurs during the download.
    '''
    try:
        yt = YouTube(video_url)
        
        path = webview_file_dialog(yt.title, '.mp4')
        download_path, filename = os.path.split(path)

        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=download_path, filename=filename)
        return True
    
    except VideoUnavailable:
        return 'Video is unavailable or deleted.'
    except RegexMatchError:
        return 'Video URL format is not supported.'
    except PytubeError as e:
        return f'PyTube error: {str(e)}'
    except Exception as e:
        return f'An unexpected error occurred: {str(e)}'

        
def download_mp3(video_url):
    '''
    Download a video in MP3 format.

    This function takes a video URL and attempts to download the audio in MP3
    format.

    Args:
        video_url (str): The URL of the video from where the audio is to be downloaded.

    Returns:
        str or bool: If the download is successful, it returns True. If an error
        occurs, it returns a string containing an informative error message.

    Raises:
        - VideoUnavailable: If the video is unavailable or has been deleted.
        - RegexMatchError: If the video URL format is not supported.
        - PytubeError: If a PyTube-specific error occurs.
        - Exception: If an unexpected error occurs during the download.
    '''
    try:
        yt = YouTube(video_url)

        path = webview_file_dialog(yt.title, '.mp3')
        download_path, filename = os.path.split(path)

        stream = yt.streams.filter(only_audio=True, subtype='webm').first()
        stream.download(output_path=download_path, filename=filename)
        return True
    
    except VideoUnavailable:
        return 'Video is unavailable or deleted.'
    except RegexMatchError:
        return 'Video URL format is not supported.'
    except PytubeError as e:
        return f'PyTube error: {str(e)}'
    except Exception as e:
        return f'An unexpected error occurred: {str(e)}'
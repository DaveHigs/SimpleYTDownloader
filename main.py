import os
import sys
import customtkinter as tk
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError, PytubeError

# This variable will serve to check if a status window exists
status_window = None

def download_video():
    '''
    Download a video from a given URL.

    This function downloads a video from the URL provided by the user. 
    It supports downloading videos in both MP4 and MP3. If the selected format
    is MP4, the function attempts to download the video in the highest available
    resolution. For MP3, it downloads the audio content in the WebM format and
    saves it as an MP3 file with the same title as the video.

    Args:
        None (The function retrieves input from global variables, url_entry, and formatmenu).

    Returns:
        None

    Note:
        - The downloaded video is saved in the current working directory.
        - In case of a successful download, the status message is updated to 
          'Download successful!' for a few seconds and then automatically cleared.
        - If the provided URL is incorrect or the download encounters an error,
          the status message will display the proper error.
    '''
    global status_window

    # Check if status_window is already open, if so, close it
    if status_window:
        status_window.destroy()

    video_url = url_entry.get()
    format_choice = formatmenu.get()

    if format_choice == 'MP4':
        result = download_mp4(video_url)
    else:
        result = download_mp3(video_url)

    if result is True:
        show_status_message('Download successful!')
    else:
        show_status_message(f'Error: {result}')

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
        stream = yt.streams.get_highest_resolution()
        # download_path = os.path.expanduser('~')  # Change this to your desired download path
        download_path = os.getcwd() # Uses CWD
        stream.download(output_path=download_path)
        return True
    
    except VideoUnavailable:
        return "Video is unavailable or deleted."
    except RegexMatchError:
        return "Video URL format is not supported."
    except PytubeError as e:
        return f"PyTube error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

        
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
        stream = yt.streams.filter(only_audio=True, subtype='webm').first()
        download_path = os.getcwd() # Uses CWD
        stream.download(output_path=download_path, filename=f'{yt.title}.mp3')
        return True
    
    except VideoUnavailable:
        return "Video is unavailable or deleted."
    except RegexMatchError:
        return "Video URL format is not supported."
    except PytubeError as e:
        return f"PyTube error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

    
def show_status_message(message):
    '''
    Displays a status message in a separate Toplevel window.

    This function takes a message to be displayed after the execution of the
    proper download function.

    Args:
        message (str): The message to be displayed in the window.

    Returns:
        None.
    '''
    global status_window

    status_window = tk.CTkToplevel()
    status_window.geometry('400x150')
    status_window.title('Status')

    status_label = tk.CTkLabel(status_window, text=message, font=('Roboto', 18))
    status_label.pack(pady=20, padx=20)

    close_button = tk.CTkButton(status_window, text='Close', command=status_window.destroy)
    close_button.pack(pady=10, padx=10)

# Create the main window
tk.set_appearance_mode('system')

root = tk.CTk()
root.geometry('500x300')
root.title('YouTube Downloader')
root.minsize(350, 350)

# Create the main frame
frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill='both', expand=True, side='bottom')

# Title
label = tk.CTkLabel(master=frame, text='Simple YouTube Downloader', font=('Roboto', 24))
label.pack(pady=12, padx=10)

# Youtube URL
url_label = tk.CTkLabel(frame, text='Enter YouTube URL:')
url_label.pack()

url_entry = tk.CTkEntry(frame, width=400)
url_entry.pack(padx=10)

# Format Selector
format_label = tk.CTkLabel(frame, text='Choose Download Format:')
format_label.pack(pady=5)

formatmenu = tk.CTkOptionMenu(frame, values=['MP4', 'MP3'], anchor='center')
formatmenu.pack(padx=10)

# Download Button
download_button = tk.CTkButton(frame, text='Download', command=download_video)
download_button.pack(pady=30, padx=10)

# Start the GUI main loop
root.mainloop()
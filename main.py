import os
import sys
import customtkinter as tk
from pytube import YouTube

# This variable will serve to check if a status window exists
status_window = None

# Function to download as mp4
def download_video():
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
        show_status_message('Error: Incorrect URL')

def download_mp4(video_url):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        # download_path = os.path.expanduser('~')  # Change this to your desired download path
        download_path = os.getcwd() # Uses CWD
        stream.download(output_path=download_path)
        return True
    except:
        return False
        
def download_mp3(video_url):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True, subtype='webm').first()
        download_path = os.getcwd() # Uses CWD
        stream.download(output_path=download_path, filename=f'{yt.title}.mp3')
        return True
    except:
        return False
    
def show_status_message(message):
    global status_window

    status_window = tk.CTkToplevel()
    status_window.geometry('300x150')
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
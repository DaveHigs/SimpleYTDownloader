import os
import sys
import customtkinter as tk
from pytube import YouTube

# Function to download the video
def download_video():
    video_url = url_entry.get()

    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        # download_path = os.path.expanduser("~")  # Change this to your desired download path
        download_path = os.getcwd() # Uses CWD
        stream.download(output_path=download_path)
        status_label.configure(text="Download successful!")
    except Exception as e:
        status_label.configure(text="Error: " + str(e))

# Create the main window
root = tk.CTk()
root.title("YouTube Downloader")

# Create a label
url_label = tk.CTkLabel(root, text="Enter YouTube URL:")
url_label.pack()

# Create an entry field to input the URL
url_entry = tk.CTkEntry(root, width=400)
url_entry.pack()

# Create a download button
download_button = tk.CTkButton(root, text="Download", command=download_video)
download_button.pack()

# Create a status label
status_label = tk.CTkLabel(root, text="")
status_label.pack()

# Start the GUI main loop
root.mainloop()


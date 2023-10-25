import os
import sys
import customtkinter as tk
from pytube import YouTube

# Function to download as mp4
def download_video():
    video_url = url_entry.get()
    if formatmenu.get() == 'MP4':
        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            # download_path = os.path.expanduser("~")  # Change this to your desired download path
            download_path = os.getcwd() # Uses CWD
            stream.download(output_path=download_path)
            status_label.configure(text="Download successful!")
        except Exception as e:
            status_label.configure(text=f"Error: {str(e)}")
    else:
        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(only_audio=True, subtype='webm').first()
            download_path = os.getcwd() # Uses CWD
            stream.download(output_path=download_path, filename=f'{yt.title}.mp3')
            status_label.configure(text="Download successful!")
        except Exception as e:
            status_label.configure(text=f"Error: {str(e)}")

# Create the main window
root = tk.CTk()
root.geometry('500x500')
root.title("YouTube Downloader")
root.minsize(350, 350)

# Create the main frame
frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill='both', expand=True, side='bottom')

# Youtube URL
url_label = tk.CTkLabel(frame, text="Enter YouTube URL:")
url_label.pack()

url_entry = tk.CTkEntry(frame, width=400)
url_entry.pack(padx=10)

# Format Selector
format_label = tk.CTkLabel(frame, text="Choose Download Format:")
format_label.pack(pady=5)

formatmenu = tk.CTkOptionMenu(frame, values=['MP4', 'MP3'], anchor='center')
formatmenu.pack(padx=10)

# Download Button
download_button = tk.CTkButton(frame, text="Download", command=download_video)
download_button.pack(pady=10, padx=10)

# Create a status label
status_label = tk.CTkLabel(frame, text="")
status_label.pack()

# Start the GUI main loop
root.mainloop()
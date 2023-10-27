import customtkinter as tk
from download_functions import download_mp4, download_mp3
from folder_chooser import webview_folder_dialog

# Variable used to check if a status window exists
status_window = None

def download_video():
    '''
    Download a video from a given URL.

    This function downloads a video from the URL provided by the user. 
    It supports downloading videos in both MP4 and MP3, and it will call the
    appropriate function depending on the format chosen by the user.

    Args:
        None (The function retrieves input from global variables, url_entry, 
        and formatmenu).

    Returns:
        None

    Note:
        - The function will create a dialog window to choose folder download path.
        - In case of a successful download, the status message is updated to 
          'Download successful!' for a few seconds and then automatically cleared.
        - If the provided URL is incorrect or the download encounters an error,
          the status message will display the proper error.
    '''
    global status_window

    # Check if status_window is already open, if so, close it
    if status_window:
        status_window.destroy()
    
    download_path = webview_folder_dialog()

    video_url = url_entry.get()
    format_choice = formatmenu.get()
    
    if format_choice == 'MP4':
        result = download_mp4(video_url, download_path)
    else:
        result = download_mp3(video_url, download_path)

    if result is True:
        show_status_message('Download successful!')
    else:
        show_status_message(f'Error: {result}')

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
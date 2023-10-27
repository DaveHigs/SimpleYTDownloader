import os
import webview

def webview_folder_dialog():
    '''
    Creates a dialog window that allows the user to pick a folder path.

    Args:
        None
    
    Returns:
        file (str) or None: A string with the choosen folder path, or None if 
        the user closes the window.

    Raises:
        TypeError: If user exits the folder dialog without picking a location.
    '''
    file = None
    def choose_folder_dialog(w):
        nonlocal file
        try:
            default_dir = os.path.expanduser("~/Downloads")
            file = w.create_file_dialog(webview.FOLDER_DIALOG, directory=default_dir)[0]
        except TypeError:
            pass
        finally:
            w.destroy()
    window = webview.create_window('', hidden=True)
    webview.start(choose_folder_dialog, window)

    return file

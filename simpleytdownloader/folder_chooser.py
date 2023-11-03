import os
import webview

def webview_file_dialog(filename, format):
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
    def save_file_dialog(w):
        nonlocal file
        nonlocal filename
        nonlocal format

        filename += format

        try:
            default_dir = os.path.expanduser("~/Downloads")
            file = w.create_file_dialog(webview.SAVE_DIALOG, directory=default_dir,
                                        save_filename=filename)
        except TypeError:
            pass
        finally:
            w.destroy()
    window = webview.create_window('', hidden=True)
    webview.start(save_file_dialog, window)

    return file

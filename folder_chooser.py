import os
import webview

def webview_folder_dialog():
    file = None
    def choose_folder_dialog(w):
        nonlocal file
        try:
            default_dir = os.path.expanduser("~/Downloads")
            file = w.create_file_dialog(webview.FOLDER_DIALOG, directory=default_dir)[0]
        except TypeError:
            pass  # user exited file dialog without picking
        finally:
            w.destroy()
    window = webview.create_window('', hidden=True)
    webview.start(choose_folder_dialog, window)
    # file will either be a string or None
    return file

print(webview_folder_dialog())

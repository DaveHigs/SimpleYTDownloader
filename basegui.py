import customtkinter

customtkinter.set_appearance_mode('system')
#customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.geometry('500x500')
root.title('Youtube Downloader')

def test():
    print('Test')

def choose_resolution(choice):
    print(choice)

def access_resolution():
    button.configure(state='disabled')

    labelres = customtkinter.CTkLabel(master=frame, text='Choose Resolution', font=('Roboto', 12))
    labelres.pack(pady=3, padx=10)

    optionmenu = customtkinter.CTkOptionMenu(master=frame, values=['360p', '720p', '1080p'], command=choose_resolution)
    optionmenu.pack(pady=12, padx=10)



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = customtkinter.CTkLabel(master=frame, text='Simple Youtube Downloader', font=('Roboto', 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Insert Link', width=350)
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='Start Download', command=access_resolution)
button.pack(pady=12, padx=10)

root.mainloop()
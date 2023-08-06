import pipje
def showpip():
    from PIL import Image, ImageTk
    from urllib.request import urlopen
    import tkinter as tk
    root = tk.Tk()
    root.title("Pip")
    URL = "https://i.imgur.com/1sfOxTw_d.webp?maxwidth=760&fidelity=grand"
    u = urlopen(URL)
    raw_data = u.read()
    u.close()
    photo = ImageTk.PhotoImage(data=raw_data) # <-----
    label = tk.Label(image=photo)
    label.image = photo
    label.pack()
    root.mainloop()
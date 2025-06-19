import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Entry, Label, Radiobutton, Progressbar
from PIL import Image, ImageTk
from yt_dlp import YoutubeDL
import re

# ========= YouTube URL validation =========
def is_valid_url():
    url = url_entry.get().strip()
    youtube_regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+'  # Regular expression to match YouTube URLs
    if not url or not re.match(youtube_regex, url):
        messagebox.showerror("Invalid URL", "Please enter a valid YouTube URL.")
        return False  # Return False if URL is invalid
    return True  # Return True if URL is valid

# ========= Function to Handle Progress =========
def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            percent = downloaded / total * 100
            progress_bar['value'] = percent
            root.update_idletasks()  # Update the progress bar

# ========= Video/Audio Download Function =========
def download_video():
    if not is_valid_url():  # Check if URL is valid before proceeding
        return  # If invalid, stop execution here
    
    url = url_entry.get().strip()  # Get the URL from the text box

    save_path = filedialog.askdirectory()  # Ask for the directory to save the file
    if not save_path:
        return  # If the user cancels, stop the function

    format_choice = "bestaudio/best" if choice.get() == "audio" else "bestvideo+bestaudio"

    ydl_opts = {
        'format': format_choice,
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'noplaylist': True,
        'quiet': True,
        'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe'
    }

    def run_download():
        try:
            status_label.config(text="Downloading...", foreground="blue")
            progress_bar["value"] = 0
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])  # Start the download
            status_label.config(text="Download Completed", foreground="green")
            messagebox.showinfo("Success", "Download finished successfully.")
        except Exception as e:
            status_label.config(text="Download Failed", foreground="red")
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    threading.Thread(target=run_download).start()  # Run the download in a separate thread

# ========= Clear Entry Field =========
def clear_url():
    url_entry.delete(0, tk.END)  # Clear the URL text box
    progress_bar['value'] = 0  # Reset the progress bar
    status_label.config(text="")  # Reset status label

# ========= Right-Click Paste =========
def paste_from_clipboard(event=None):
    url_entry.delete(0, tk.END)  # Clear existing URL
    url_entry.insert(0, root.clipboard_get())  # Insert clipboard content into the URL entry

def show_context_menu(event):
    menu.tk_popup(event.x_root, event.y_root)  # Show the right-click context menu

# ========== GUI SETUP ==========
style = Style("flatly")
root = style.master
root.title("YouTube Downloader by Anjali")
root.geometry("600x400")
root.resizable(False, False)

# ======= Background Image Setup =======
bg_image_path = "background.jpg"
if os.path.exists(bg_image_path):
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((600, 400))  # Resize image to match window size
    bg_photo = ImageTk.PhotoImage(bg_image)   
    root.bg_photo = bg_photo  # Store a reference to prevent garbage collection
    bg_label = tk.Label(root, image=root.bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place it behind the frame

# ======= Content Frame =======
frame = tk.Frame(root, bg='white', bd=3, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor='center')  # Center the frame in the window
frame.lift()  # Make sure the frame is above the background image

Label(frame, text="Enter YouTube URL", font=("Segoe UI", 12, "bold"), background="white").grid(row=0, column=0, padx=10, pady=(10, 5), columnspan=2)

url_entry = Entry(frame, width=50)
url_entry.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

# Right-click context menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Paste", command=paste_from_clipboard)
url_entry.bind("<Button-3>", show_context_menu)  # Bind right-click event to the paste functionality

# Radio buttons for video/audio selection
choice = tk.StringVar(value="video")
Radiobutton(frame, text="Video & Audio", variable=choice, value="video", bootstyle="primary").grid(row=2, column=0, pady=10, padx=10)
Radiobutton(frame, text="Audio Only", variable=choice, value="audio", bootstyle="info").grid(row=2, column=1, pady=10, padx=10)

# Buttons for download and clear
Button(frame, text="Download", command=download_video, bootstyle="success outline").grid(row=3, column=0, columnspan=2, pady=(0, 5))
Button(frame, text="Clear", command=clear_url, bootstyle="warning outline").grid(row=4, column=0, columnspan=2, pady=5)

# Progress bar for download
progress_bar = Progressbar(frame, length=350, mode='determinate')
progress_bar.grid(row=5, column=0, columnspan=2, pady=10)

# Status label to show download status
status_label = Label(frame, text="", font=("Segoe UI", 10), foreground="green", background="white")
status_label.grid(row=6, column=0, columnspan=2, pady=(5, 10))

# ========== Start GUI ==========
root.mainloop()
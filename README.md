# YouTube Video & Audio Downloader by Anjali

![image](https://github.com/user-attachments/assets/b4078e95-86e6-491b-9346-1636b5a8e8b1)

A stylish and user-friendly desktop application to download YouTube videos or audio in high quality. Built with Python and Tkinter, the app features real-time progress tracking, clipboard support, and a modern GUI using ttkbootstrap.

---

## Features

- Download **Video & Audio** or **Audio Only**
- **Right-click Paste** from clipboard for faster input
- **URL validation** with error messages
- **Progress bar** to show download status
- Modern GUI with **background image**
- **Multithreading** to keep the UI responsive
- Clear status updates and success/error dialogs

---

## Tech Stack

- `Python 3.7+`
- `Tkinter` & `ttkbootstrap`
- `yt-dlp` (YouTube download library)
- `Pillow` (for handling background images)

---

## Installation

### Prerequisites
- Python 3.7+
- [FFmpeg](https://ffmpeg.org/download.html) (must be installed & path set in environment variables)

### Setup Instructions

```bash
git clone https://github.com/anjalipatel19/youtube-downloader-python.git
cd youtube-downloader-python
pip install -r requirements.txt
python youtube_downloader.py
````

---

## Project Structure

* `youtube_downloader.py` – Main application script
* `background.jpg` – Background image used in the GUI
* `requirements.txt` – List of Python dependencies
* `README.md` – Project overview and usage instructions
* `LICENSE` – MIT License for open-source use

---

## Demo

> Simply run `youtube_downloader.py` and paste a YouTube link to start downloading.
> You can select between **Video & Audio** or **Audio Only** modes.
> Progress bar shows real-time status of the download.

---

##  License

This project is licensed under the **MIT License**. See the `LICENSE` file for more information.

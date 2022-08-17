from os import link
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

# functions


def select_path():
    # allows user to select the path from the file explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget('text')
    screen.title("Downloading video...")
    # Download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete!")


screen = Tk()
title = screen.title('YouTube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# image logo
logo_img = PhotoImage(file='Youtube-Logo.png')
# resize image logo
logo_img = logo_img.subsample(7, 7)
canvas.create_image(250, 80, image=logo_img)

# link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter video URL", font=('Segoe UI', 14))

# select path for downloaded video
path_label = Label(screen, text="Select path for download",
                   font=('Segoe UI', 14))
select_btn = Button(screen, text="Select", command=select_path)

# add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# add widget to window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

# download buttons
download_btn = Button(screen, text="Download video", command=download_file)
# add download button to canvas
canvas.create_window(250, 390, window=download_btn)
screen.mainloop()

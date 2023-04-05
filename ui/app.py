"""Module to run the UI
"""
import sys
import os
import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

sys.path.append(os.path.join(os.getcwd(), 'src'))

from main import main  # NOQA

_APP_TITLE = 'The tool for labeling'


class LabelInterface():
    """Provides UI for labeling process.
    """

    def __init__(self,
                 app_root) -> None:
        """Init
        """
        self.root = app_root
        self.wind_width = self.root.winfo_screenwidth()
        self.win_height = self.root.winfo_screenheight()
        self.root.title(_APP_TITLE)
        self.root.minsize(
            self.wind_width-100,
            self.win_height-150)

        self.image_frame_left = tk.Frame(
            master=self.root,
            width=300,
            height=self.win_height-200,
            bg='blue')

        self.image_frame_left.grid(
            row=0,
            column=0,
            padx=(20, 20),
            pady=(20, 20),
            sticky="nsew")

        self.image_frame_right = tk.Frame(
            master=self.root,
            width=self.wind_width-400,
            height=self.win_height-200,
            bg='red')
        self.image_frame_right.grid(
            row=0,
            column=1,
            padx=(20, 20),
            pady=(20, 20),
            sticky="nsew")
        self.image = tk.PhotoImage(master=self.image_frame_right)

        self.select_folder_lbl = tk.Label(
            master=self.image_frame_left,
            text="Select Folder:",
            font=("Arial", 16, "bold"))
        self.select_folder_lbl.grid(
            row=0,
            column=0,
            padx=(2, 20),
            pady=(10, 5))

        self.select_folder_entry = tk.Entry(
            master=self.image_frame_left,
            width=50,
            state='disabled'
        )
        self.select_folder_entry.grid(
            row=1,
            column=0,
            padx=(2, 20),
            pady=(10, 5))

        self.slect_folder_btn = tk.Button(
            master=self.image_frame_left,
            text='Select folder',
            width=30,
            height=2,
            command=self._select_folder)
        self.slect_folder_btn.grid(
            row=2,
            column=0,
            columnspan=2,
            padx=(20, 20),
            pady=(20, 20))

    def _select_folder(self):
        """Reads the select folder
        """
        self.select_folder_entry.configure(state='normal')
        entry_folder = self.select_folder_entry.get()
        if entry_folder:
            self.select_folder_entry.delete(0, tk.END)
        folder_path = filedialog.askdirectory()
        self.select_folder_entry.insert(0, folder_path)
        self.select_folder_entry.configure(state='disabled')

        self.start_labeling()

    def start_labeling(self):
        """Start labeling
        """
        input_dir_path = self.select_folder_entry.get()
        command = ['-i', input_dir_path, '-o', 'output']
        images_paths, output_dir = main(command)


if __name__ == '__main__':
    app = LabelInterface(app_root=tk.Tk())
    app.root.mainloop()

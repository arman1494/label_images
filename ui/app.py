"""Module to run the UI
"""
import customtkinter as ctk

_APP_TITLE = 'The tool for labeling'


class LabelInterface(ctk.CTk):
    """Provides UI for labeling process.
    """

    def __init__(self) -> None:
        """Init
        """
        super().__init__()
        self.wind_width = self.winfo_screenwidth()
        self.win_height = self.winfo_screenheight()
        self.title(_APP_TITLE)
        self.minsize(
            self.wind_width-50,
            self.win_height-100)

        self.image_frame_left = ctk.CTkFrame(
            master=self,
            width=300,
            height=self.win_height-100,
            fg_color='blue')

        self.image_frame_left.grid(
            row=0,
            column=0,
            padx=(20, 20),
            pady=(20, 20),
            sticky="nsew")

        self.image_frame_right = ctk.CTkFrame(
            master=self,
            width=self.wind_width-300,
            height=self.win_height-100,
            fg_color='red')
        self.image_frame_right.grid(
            row=0,
            column=1,
            padx=(20, 20),
            pady=(20, 20),
            sticky="nsew")


if __name__ == '__main__':
    app = LabelInterface()
    app.mainloop()

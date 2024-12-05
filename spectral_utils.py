import spectral
import matplotlib.pyplot as plt
import numpy as np
import customtkinter as ctk
import os
import tkinter as tk
from tkinter import filedialog as fd


class CustomButton(ctk.CTkFrame):
    def __init__(self, master, text="Click Me", width=150, height=50, command=None, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.grid_propagate(False)
        self.button = ctk.CTkButton(
            self,
            text=text,
            command=command,
            width=width - 10,
            height=height - 10
        )
        self.button.grid(row=0, column=0, padx=5, pady=5, sticky="nswe")

    def set_text(self, text):
        self.button.configure(text=text)

    def get_text(self):
        return self.button.cget("text")

    def set_command(self, command):
        self.button.configure(command=command)


class CustomInputField(ctk.CTkFrame):
    def __init__(self, master, placeholder_text="Enter text...", width=200, height=40, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.grid_propagate(False)
        self.entry = ctk.CTkEntry(self, placeholder_text=placeholder_text, width=width - 10)
        self.entry.grid(row=0, column=0, padx=5, pady=5, sticky="we")

    def get(self):
        return self.entry.get()

    def set(self, text):
        self.entry.delete(0, "end")
        self.entry.insert(0, text)

    def clear(self):
        self.entry.delete(0, "end")


def show_error_popup(message):
    popup = ctk.CTkToplevel()
    popup.geometry("300x150")
    popup.title("Błąd")
    popup.grab_set()

    label = ctk.CTkLabel(popup, text=message, font=("Lato", 14), wraplength=250, justify="center")
    label.pack(pady=20)

    close_button = ctk.CTkButton(popup, text="Zamknij", command=popup.destroy)
    close_button.pack(pady=10)


def spectral_visu(hdr_path, spc_path):
    if not os.path.exists(hdr_path):
        show_error_popup("Błąd: Plik .hdr nie istnieje!")
        return
    if not os.path.exists(spc_path):
        show_error_popup("Błąd: Plik .spc nie istnieje!")
        return

    image = spectral.io.envi.open(hdr_path, image=spc_path)
    print(f"Rozmiar obrazu: {image.shape}")
    print(f"Typ danych obrazu: {image.dtype}")
    plt.imshow(image[:, :, 100])  
    plt.colorbar()
    plt.show()


def convert_to_RGB(hdr_path, spc_path):
    if not os.path.exists(hdr_path):
        show_error_popup("Błąd: Plik .hdr nie istnieje!")
        return
    if not os.path.exists(spc_path):
        show_error_popup("Błąd: Plik .spc nie istnieje!")
        return

    r_band, g_band, b_band = 60, 100, 150
    image = spectral.io.envi.open(hdr_path, image=spc_path)
    r = (image[:, :, r_band] - image[:, :, r_band].min()) / (image[:, :, r_band].max() - image[:, :, r_band].min())
    g = (image[:, :, g_band] - image[:, :, g_band].min()) / (image[:, :, g_band].max() - image[:, :, g_band].min())
    b = (image[:, :, b_band] - image[:, :, b_band].min()) / (image[:, :, b_band].max() - image[:, :, b_band].min())

    rgb_image = np.dstack((r, g, b))

    plt.imshow(rgb_image)
    plt.title("RGB")
    plt.axis("off")
    plt.show()
def get_file():
    file_path = ''
    file_types = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    file_name = fd.askopenfilename(
        title='Open file',
        initialdir='/',
        filetypes= file_types
    )
    file_path  = file_name
    return file_path

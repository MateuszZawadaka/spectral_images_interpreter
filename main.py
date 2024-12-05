from spectral_utils import CustomInputField, CustomButton, spectral_visu, convert_to_RGB, get_file
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog as fd

def select_file_button():
    get_hdr_file_button = CustomButton(
        master=root_tk,
        text='Wybierz plik .hdr',
        command=lambda: hdr_path.set(get_file())
    )
    get_hdr_file_button.place(relx=0.6, rely=0.4, anchor=ctk.CENTER)

    get_spc_file_button = CustomButton(
        master=root_tk,
        text='Wybierz plik .spe',
        command=lambda: spc_path.set(get_file())
    )
    get_spc_file_button.place(relx=0.6, rely=0.8, anchor=ctk.CENTER)

if __name__ == "__main__":
    hdr_path = tk.StringVar()
    spc_path = tk.StringVar()
    root_tk = ctk.CTk()
    root_tk.geometry("1024x700")
    root_tk.title("Spectral file reader")
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    select_file_button()

    button_rgb = CustomButton(
        master=root_tk,
        text="Wizualizacja RGB",
        command=lambda: convert_to_RGB(hdr_path.get(), spc_path.get())
    )
    button_rgb.place(relx=0.8, rely=0.2, anchor=ctk.CENTER)

    button_spectral = CustomButton(
        master=root_tk,
        text="Wizualizacja spektrum",
        command=lambda: spectral_visu(hdr_path.get(), spc_path.get())
    )
    button_spectral.place(relx=0.8, rely=0.4, anchor=ctk.CENTER)
    

    
    root_tk.mainloop()
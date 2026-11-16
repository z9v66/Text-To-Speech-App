import customtkinter as ctk
from voice import speak_text

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Text to Speech Pro")
window.geometry("500x600")

def speak():
    speak_text(entry.get(), slider.get(), volume_slider.get() / 100)

title_label = ctk.CTkLabel(window, text="Text to Speech", font=("Arial", 20, "bold"))
title_label.pack(pady=15)

entry = ctk.CTkEntry(window, width=350, height=38, placeholder_text="Enter your text here...")
entry.pack(pady=8)

speed_label = ctk.CTkLabel(window, text="Speech Speed", font=("Arial", 12))
speed_label.pack(pady=(10, 0))
slider = ctk.CTkSlider(window, from_=100, to=300, width=300)
slider.set(200)
slider.pack(pady=5)

volume_label = ctk.CTkLabel(window, text="Volume Level", font=("Arial", 12))
volume_label.pack(pady=(10, 0))
volume_slider = ctk.CTkSlider(window, from_=0, to=100, width=300)
volume_slider.set(50)
volume_slider.pack(pady=5)

button = ctk.CTkButton(
    window,
    text="Speak",
    command=speak,
    width=200,
    height=40,
    corner_radius=20,
    font=("Arial", 15, "bold")
)
button.pack(pady=20)

window.mainloop()
import tkinter as tk
from tkinter import messagebox
import pygame
from music_generator import analyze_text_simple, generate_music

def generate_music_gui():
    user_input = text_input.get()
    mood = analyze_text_simple(user_input)
    generate_music(mood)
    messagebox.showinfo("Результат", f"Музика збережена як 'generated_music.mid'\nНастрій: {mood}")

def play_music():
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("generated_music.mid")
        pygame.mixer.music.play()
        messagebox.showinfo("Програвання", "Музика відтворюється...")
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося відтворити музику:\n{e}")

root = tk.Tk()
root.title("Генерація музики за текстом")

tk.Label(root, text="Введіть опис музики:").pack(pady=5)
text_input = tk.Entry(root, width=40)
text_input.pack(pady=5)

generate_button = tk.Button(root, text="Генерувати музику", command=generate_music_gui)
generate_button.pack(pady=10)

play_button = tk.Button(root, text="Відтворити музику", command=play_music)
play_button.pack(pady=5)

root.mainloop()

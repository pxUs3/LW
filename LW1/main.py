import tkinter as tk
from tkinter import messagebox
from music21 import stream, note, midi
import random
import pygame

def analyze_text_simple(text):
    happy_keywords = ['щаслива', 'радісна', 'енергійна', 'весела']
    sad_keywords = ['сумна', 'повільна', 'спокійна']
    
    text_lower = text.lower()
    if any(word in text_lower for word in happy_keywords):
        return 'happy'
    elif any(word in text_lower for word in sad_keywords):
        return 'sad'
    else:
        return 'neutral'

def generate_music(mood, filename="generated_music.mid"):
    melody = stream.Stream()

    if mood == 'happy':
        scale = ['C5', 'D5', 'E5', 'G5', 'A5']
        durations = [0.5, 1.0]
    elif mood == 'sad':
        scale = ['A3', 'C4', 'D4', 'E4', 'G4']
        durations = [1.0, 2.0]
    else:
        scale = ['C4', 'D4', 'E4', 'F4', 'G4']
        durations = [0.75, 1.0]

    for _ in range(16):
        pitch = random.choice(scale)
        dur = random.choice(durations)
        n = note.Note(pitch, quarterLength=dur)
        melody.append(n)

    mf = midi.translate.streamToMidiFile(melody)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()

def generate_music_gui():
    user_input = text_input.get()
    print(user_input)
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

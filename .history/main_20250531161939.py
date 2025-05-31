from textblob import TextBlob
from music21 import stream, note, midi
import random

def analyze_text(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0.2:
        mood = 'happy'
    elif sentiment < -0.2:
        mood = 'sad'
    else:
        mood = 'neutral'
    return mood

def generate_music(mood, filename="generated_music.mid"):
    melody = stream.Stream()

    # Налаштування нот залежно від настрою
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
    
    # Збереження у MIDI
    mf = midi.translate.streamToMidiFile(melody)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()
    print(f"Музика збережена як {filename}")

def main():
    print("Введіть опис настрою або музики:")
    user_input = input("> ")
    mood = analyze_text(user_input)
    print(f"Визначено настрій: {mood}")
    generate_music(mood)

if __name__ == "__main__":
    main()
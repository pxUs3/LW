from music21 import stream, note, midi
import random

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

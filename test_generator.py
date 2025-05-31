import os
import unittest
from music_generator import generate_music, analyze_text_simple

class TestMusicGenerator(unittest.TestCase):
    def test_analyze_happy_text(self):
        self.assertEqual(analyze_text_simple("радісна музика"), "happy")

    def test_analyze_sad_text(self):
        self.assertEqual(analyze_text_simple("сумна мелодія"), "sad")

    def test_analyze_neutral_text(self):
        self.assertEqual(analyze_text_simple("музика без настрою"), "neutral")
        
class TestMusicFile(unittest.TestCase):
    def test_generate_music_file(self):
        filename = "test_output.mid"
        generate_music("happy", filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)
import unittest
from poem_generator import load_generator, generate_poem

class TestPoemGenerator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.generator = load_generator("gpt2")

    def test_poem_not_empty(self):
        topic = "sunset"
        poem = generate_poem(topic, self.generator)
        self.assertTrue(len(poem.strip()) > 0)

    def test_poem_styles(self):
        styles = ["romantic", "haiku", "horror", "inspirational", "default"]
        for style in styles:
            with self.subTest(style=style):
                poem = generate_poem("nature", self.generator, style)
                self.assertIn("\n", poem)  # Poem should have line breaks

if __name__ == '__main__':
    unittest.main()

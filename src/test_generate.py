import unittest
from generate import extract_title


class TestGenerate(unittest.TestCase):
    def test_extract_title(self):
        text = "# This is a title and some extra text"
        title = extract_title(text)
        self.assertEqual(title, "This is a title and some extra text")
  
    def test_raises_on_no_title(self):
        text = "This is a block of text with no title header"        
        with self.assertRaises(ValueError):
            extract_title(text)

if __name__== "__main__":
        unittest.main()
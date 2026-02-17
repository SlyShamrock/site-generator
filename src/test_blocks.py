import unittest
from blocks import block_to_block_type, BlockType

class TestBlocks(unittest.TestCase):
    def test_blocks_header(self):
        text = "### this is a header block"
        header = block_to_block_type(text)
        self.assertEqual(header, BlockType.HEADING)
    
    def test_blocks_code(self):
        text = "```\nthis is a code block```"
        code = block_to_block_type(text)
        self.assertEqual(code, BlockType.CODE)
    
    def test_blocks_quote(self):
        text = ">this is a quote block\n>this is the next line\n>and one more line"
        quote = block_to_block_type(text)
        self.assertEqual(quote, BlockType.QUOTE)

    def test_blocks_unordered_list(self):
        text = "- this is an unordered list block\n- this is the next line\n- and one more line"
        unordered = block_to_block_type(text)
        self.assertEqual(unordered, BlockType.UNORDERED_LIST)
    
    def test_blocks_ordered_list(self):
        text = "1. this is an ordered list\n2. This is the next line\n3. and one more line"
        ordered = block_to_block_type(text)
        self.assertEqual(ordered, BlockType.ORDERED_LIST)

    def test_blocks_paragrpah(self):
        text = "1. this is a regular paragraph\n>this is the next line\n- and one more line"
        paragraph = block_to_block_type(text)
        self.assertEqual(paragraph, BlockType.PARAGRAPH)

if __name__== "__main__":
    unittest.main()
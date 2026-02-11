import unittest

from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class TestDelimiter(unittest.TestCase):
    def test_delimiter_code(self):
        node = TextNode("This is a text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0], TextNode("This is a text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))

    def test_delimiter_bold(self):
        node = TextNode("This is a text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0], TextNode("This is a text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold block", TextType.BOLD))

    def test_delimiter_italic(self):
        node = TextNode("This is a text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0], TextNode("This is a text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("italic block", TextType.ITALIC))
    
    def test_no_delimiter(self):
        node = TextNode("This is a regular text node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0], TextNode("This is a regular text node", TextType.TEXT))
        
    def test_multiple_delimiters(self):
        node = TextNode("This has **multiple**_delimiters_`inside`", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(nodes[0], TextNode("This has ", TextType.TEXT))
        self.assertEqual(nodes[1], TextNode("multiple", TextType.BOLD))
        self.assertEqual(nodes[2], TextNode("delimiters", TextType.ITALIC))
        
    def test_raises_error(self):
        node = TextNode("This has an error in it'", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertRaises(ValueError)
    
    def test_empty_delimiter(self):
        node = TextNode("This has an `` empty section", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(nodes[0], TextNode("This has an "), TextType.TEXT)
        self.assertEqual(nodes[1], TextNode(" empty section"), TextType.TEXT)
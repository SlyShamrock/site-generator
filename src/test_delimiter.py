import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

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

    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with an ", TextType.TEXT),
                              TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                              TextNode(" and another ", TextType.TEXT),
                              TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),],new_nodes,)
    
    def test_split_links(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is text with a link ", TextType.TEXT),
                              TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                              TextNode(" and ", TextType.TEXT),
                              TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),],new_nodes,)
        
    def test_split_images_text_after(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and some extra text", TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with an ", TextType.TEXT),
                              TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                              TextNode(" and another ", TextType.TEXT),
                              TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                              TextNode(" and some extra text", TextType.TEXT),],new_nodes,)
    
    def test_no_image(self):
        node = TextNode("This is text with no image", TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("This is text with no image"),], new_nodes,)

    def test_no_link(self):
        node = TextNode("This is text with no link", TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([TextNode("This is text with no link"),], new_nodes,)
    
    def test_image_no_leading_text(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)")
        new_nodes = split_nodes_image([node])
        self.assertListEqual([TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                              TextNode(" and another ", TextType.TEXT),
                              TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),],new_nodes,)
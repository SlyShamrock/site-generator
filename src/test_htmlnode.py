import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://x.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(),' href="https://x.com" target="_blank"')
        
    def test_props_to_html2(self):
        node = HTMLNode(props={"href": "https://x.com", "target": "_blank"})
        node2 = HTMLNode(props={"href": "https://x.com", "target": "_blank", "href": "https://www.boot.dev"})
        self.assertNotEqual(node, node2)

    def test_props_to_html3(self):
        node = HTMLNode(props={"href": "https://x.com", "target": "_blank", "href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")   

    def test_leaf_to_html_p(self):
        node = LeafNode("a", "Hello, world!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")   

    def test_leaf_to_html_raises_on_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
         node.to_html()           

if __name__== "__main__":
    unittest.main()
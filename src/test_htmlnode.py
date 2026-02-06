import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://x.com", "target": "_blank"})
        print(node.props_to_html())

    def test_props_to_html2(self):
        node = HTMLNode(props={"href": "https://x.com", "target": "_blank"})
        node2 = HTMLNode(props={"href": "https://x.com", "target": "_blank", "href": "https://www.boot.dev"})
        self.assertNotEqual(node, node2)

    def test_props_to_html3(self):
        node = HTMLNode(props={"href": "https://x.com", "target": "_blank", "href": "https://www.boot.dev"})
        print(node.props_to_html())     

if __name__== "__main__":
    unittest.main()
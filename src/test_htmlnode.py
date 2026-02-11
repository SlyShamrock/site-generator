import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    #Tests for props_to_html
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

    #Tests for LeafNode
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
   
    ## Tests for ParentNode
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)

    def test_to_html_empty_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_raises_on_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
    
    def test_to_html_raises_on_no_child(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    
if __name__== "__main__":
    unittest.main()
import unittest
from blocks import block_to_block_type, BlockType, markdown_to_html_node

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

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )   

    def test_quoteblock(self):
        md = """
>This is **bolded** paragraph
>text in a p
>tag here
>This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> paragraph text in a p tag here This is another paragraph with <i>italic</i> text and <code>code</code> here</blockquote></div>",
    )
        
    def test_headingblock(self):
        md = "#### This is **bolded** heading text in a h tag here. This is another paragraph with _italic_ text and `code` here"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>This is <b>bolded</b> heading text in a h tag here. This is another paragraph with <i>italic</i> text and <code>code</code> here</h4></div>",
    )
        
    def test_orderedblock(self):
        md = """1. This is **bolded** paragraph
2. text in a p
3. tag here
4. This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is <b>bolded</b> paragraph</li><li>text in a p</li><li>tag here</li><li>This is another paragraph with <i>italic</i> text and <code>code</code> here</li></ol></div>",
    )
        
    def test_unorderedblock(self):
        md = """
- This is **bolded** paragraph
- text in a p
- tag here
- This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is <b>bolded</b> paragraph</li><li>text in a p</li><li>tag here</li><li>This is another paragraph with <i>italic</i> text and <code>code</code> here</li></ul></div>",
    )

if __name__== "__main__":
    unittest.main()
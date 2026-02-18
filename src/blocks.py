import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from enum import Enum
from split_nodes import markdown_to_blocks, text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(markdown_block):
    if markdown_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    s = markdown_block.strip()
    if s.startswith("```\n") and s.endswith("```"):
        return BlockType.CODE
    quote_tracker = True
    for line in markdown_block.splitlines():
        if not line.startswith(">"):
            quote_tracker = False
            break               
    if quote_tracker:
        return BlockType.QUOTE
    unord_tracker = True
    for line in markdown_block.splitlines():
        if not line.startswith("- "):
            unord_tracker = False
            break               
    if unord_tracker:
        return BlockType.UNORDERED_LIST
    ord_tracker = True
    numbered_line = 1
    for line in markdown_block.splitlines():
        if not line.startswith(f"{numbered_line}. "):
            ord_tracker = False
            break     
        numbered_line += 1          
    if ord_tracker:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            node = assign_heading_block(block)
        elif block_type == BlockType.CODE:
            node = assign_code_block(block)
        elif block_type == BlockType.QUOTE:
            node = assign_quote_block(block)
        elif block_type == BlockType.UNORDERED_LIST:
            node = assign_unordered_block(block)
        elif block_type == BlockType.ORDERED_LIST:
            node = assign_ordered_block(block)
        else:
            node = assign_paragraph_block(block)   
        children.append(node) 
    final_node = ParentNode("div", children)
    return final_node
                    
def assign_heading_block(block):
    count = 0
    for character in block:
        if character != "#":
            break
        count += 1
    heading_text = block[count+1:]
    children = text_to_children(heading_text)
    heading_node = ParentNode(f"h{count}", children)
    return heading_node  

def assign_code_block(block):
    code_text = block[4:-3]
    code_textnode = TextNode(code_text, TextType.TEXT)
    converted = text_node_to_html_node(code_textnode)
    inner_node = ParentNode("code", [converted])        
    code_node = ParentNode("pre", [inner_node])
    return code_node                             

def assign_quote_block(block):
    lines = []
    for line in block.splitlines():
        removed = line.lstrip(">").strip()
        lines.append(removed)
    joined = " ".join(lines)
    children = text_to_children(joined)   
    quote_node = ParentNode("blockquote", children)
    return quote_node

def assign_unordered_block(block):
    lines = []         
    for line in block.splitlines():
        removed = line[2:]                       
        line_children = text_to_children(removed)
        line_node = ParentNode("li", line_children)
        lines.append(line_node)          
    unordered_list_node = ParentNode("ul", lines)
    return unordered_list_node

def assign_ordered_block(block):
    lines = []
    for line in block.split("\n"):
        if not line.strip():
            continue
        prefix, line_text = line.split(". ", 1)
        line_children = text_to_children(line_text)
        line_node = ParentNode("li", line_children)
        lines.append(line_node)               
    ordered_list_node = ParentNode("ol", lines)
    return ordered_list_node

def assign_paragraph_block(block):
    lines = []
    for line in block.splitlines():
        lines.append(line)
    joined = " ".join(lines)
    children = text_to_children(joined)
    paragraph_node = ParentNode("p", children)
    return paragraph_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    child_node = []
    for tn in text_nodes:
        child_node.append(text_node_to_html_node(tn))    
    return child_node


    
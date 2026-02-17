import re

from enum import Enum

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
    if markdown_block.startswith("```\n") and markdown_block.endswith("```"):
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
    
    
 
from textnode import TextNode
from textnode import TextType
from static import copy_content
from generate import generate_pages_recursive
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_content("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)
    
    
main()


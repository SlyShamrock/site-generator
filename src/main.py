from textnode import TextNode
from textnode import TextType
from static import copy_content
from generate import generate_pages_recursive

def main():
    copy_content("static", "public")
    generate_pages_recursive("content", "template.html", "public")
    
main()


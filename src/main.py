from textnode import TextNode
from textnode import TextType

def main():
    node = TextNode("some text here", TextType.LINK, "https://www.bootdev.com")
    print(node)

main()


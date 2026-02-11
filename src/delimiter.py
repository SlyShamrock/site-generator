from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Syntax")
        holder = []
        for i in range(0,len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                even_node = TextNode(sections[i], TextType.TEXT)
                holder.append(even_node)
            else:
                odd_node = TextNode(sections[i], text_type)
                holder.append(odd_node)
        new_nodes.extend(holder)
    return new_nodes

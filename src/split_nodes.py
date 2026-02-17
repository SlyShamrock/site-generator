from textnode import TextNode, TextType, extract_markdown_images, extract_markdown_links

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extract = extract_markdown_images(node.text)
        remaining_text = node.text
        for pair in extract:
            image_alt = pair[0]
            image_link = pair[1]
            sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            before = sections[0]
            after = sections[1]
            if before != "":
                new_text = TextNode(before, TextType.TEXT)
                new_nodes.append(new_text)
            new_image = TextNode(image_alt, TextType.IMAGE, image_link)            
            new_nodes.append(new_image)
            remaining_text = after
        if remaining_text != "":
            leftover = TextNode(remaining_text, TextType.TEXT)    
            new_nodes.append(leftover)       
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extract = extract_markdown_links(node.text)
        remaining_text = node.text
        for pair in extract:
            link_alt = pair[0]
            link_url = pair[1]
            sections = remaining_text.split(f"[{link_alt}]({link_url})", 1)
            before = sections[0]
            after = sections[1]
            if before != "":
                new_text = TextNode(before, TextType.TEXT)
                new_nodes.append(new_text)
            new_link = TextNode(link_alt, TextType.LINK, link_url)            
            new_nodes.append(new_link)
            remaining_text = after
        if remaining_text != "":
            leftover = TextNode(remaining_text, TextType.TEXT)    
            new_nodes.append(leftover)       
    return new_nodes

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    node = split_nodes_image(node)
    node = split_nodes_link(node)
    node = split_nodes_delimiter(node, "**", TextType.BOLD)
    node = split_nodes_delimiter(node, "_", TextType.ITALIC)
    node = split_nodes_delimiter(node, "`", TextType.CODE)
    return node

def markdown_to_blocks(markdown):
    blocks = []
    newline_split = markdown.split("\n\n")
    for block in newline_split:
        no_whitespace = block.strip()
        if no_whitespace != "":
            blocks.append(no_whitespace)
    return blocks
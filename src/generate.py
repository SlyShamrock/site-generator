import os
from blocks import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from static import copy_content
from pathlib import Path

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No title found")                          
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_markdown = open(from_path, "r")
    from_contents = from_markdown.read() 
    from_markdown.close()   
    template_markdown = open(template_path, "r")    
    template_contents = template_markdown.read()
    template_markdown.close()
    source_html = markdown_to_html_node(from_contents)
    html_string = source_html.to_html()
    title = extract_title(from_contents)
    replace_placeholders = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    exists = os.path.dirname(dest_path)
    if exists != "":
        os.makedirs(exists, exist_ok=True)
    final_contents = open(dest_path, "w")
    final_contents.write(replace_placeholders)
    final_contents.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    directory_list = os.listdir(dir_path_content)
    for path in directory_list:
        source_path = os.path.join(dir_path_content, path)
        destination_path = os.path.join(dest_dir_path, path)
        if os.path.isdir(source_path):
            os.makedirs(destination_path, exist_ok=True)
            generate_pages_recursive(source_path, template_path, destination_path)
        elif os.path.isfile(source_path) and source_path.endswith(".md"):
            dest_filename = str(Path(destination_path).with_suffix(".html"))            
            generate_page(source_path, template_path, dest_filename)
        else:
            continue


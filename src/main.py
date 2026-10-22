from textnode import TextNode, TextType
from copystatic import copy_static_to_public
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main() -> None:
    copy_static_to_public()
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

from textnode import TextNode, TextType
from copystatic import copy_static_to_public
from gencontent import generate_pages_recursive
import sys

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main() -> None:
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    copy_static_to_public()
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

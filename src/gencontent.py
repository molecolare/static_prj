from markdown_to_html_node import markdown_to_html_node
from pathlib import Path
import os

def extract_title(markdown):
	righe = markdown.split("\n")
	for row in righe:
		if row.startswith("#") and not row.startswith("##"):
			return row[1:].strip()

	raise Exception("Nessun titolo trovato")
def generate_page(from_path, template_path, dest_path):
	with open(from_path, "r") as file:
		mark = file.read()
	with open(template_path, "r") as file:
		temp = file.read()
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	html = markdown_to_html_node(mark).to_html()
	titolo = extract_title(mark)
	temp = temp.replace("{{ Title }}", titolo)
	temp = temp.replace("{{ Content }}", html)
	cart = os.path.dirname(dest_path)
	os.makedirs(cart, exist_ok=True)
	with open(dest_path, "w") as file:
		writ = file.write(temp)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	for p in os.listdir(dir_path_content):
		from_path = os.path.join(dir_path_content, p)
		dest_path = os.path.join(dest_dir_path, p)
		if os.path.isfile(from_path):
			generate_page(from_path, template_path, Path(dest_path).with_suffix(".html"))
		else:
			generate_pages_recursive(from_path, template_path, dest_path)

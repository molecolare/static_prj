import unittest
from textnode import TextNode, TextType
from text_to_text_nodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(expected, nodes)

    def test_text_to_textnodes_empty(self):
        nodes = text_to_textnodes("")
        expected = [TextNode("", TextType.TEXT)]
        self.assertListEqual(expected, nodes)

    def test_text_to_textnodes_only_text(self):
        text = "This is just plain text."
        nodes = text_to_textnodes(text)
        expected = [TextNode("This is just plain text.", TextType.TEXT)]
        self.assertListEqual(expected, nodes)

    def test_text_to_textnodes_only_bold(self):
        text = "**bold text**"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode("", TextType.TEXT),
        ]
        self.assertListEqual(expected, nodes)

    def test_text_to_textnodes_only_italic(self):
        text = "_italic text_"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode("", TextType.TEXT),
        ]
        self.assertListEqual(expected, nodes)

    def test_text_to_textnodes_only_code(self):
        text = "`code text`"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("", TextType.TEXT),
            TextNode("code text", TextType.CODE),
            TextNode("", TextType.TEXT),
        ]
        self.assertListEqual(expected, nodes)

    def test_text_to_textnodes_only_image(self):
        text = "![alt text](https://example.com/image.png)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
        ]
        self.assertListEqual(expected, nodes)

    def test_text_to_textnodes_only_link(self):
        text = "[link text](https://example.com)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("link text", TextType.LINK, "https://example.com"),
        ]
        self.assertListEqual(expected, nodes)

if __name__ == "__main__":
    unittest.main()

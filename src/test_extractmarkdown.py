import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertListEqual(expected, matches)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(expected, matches)

    def test_extract_markdown_links_no_images(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and ![not a link](https://example.com/image.png)"
        matches = extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev")]
        self.assertListEqual(expected, matches)

    def test_extract_markdown_images_no_matches(self):
        matches = extract_markdown_images("This is text without images.")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_no_matches(self):
        matches = extract_markdown_links("This is text without links.")
        self.assertListEqual([], matches)

if __name__ == "__main__":
    unittest.main()

import unittest
from blocktype import BlockType
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_multiple_levels(self):
        for i in range(1, 7):
            block = f"{'#' * i} Heading {i}"
            self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block(self):
        block = "```\nprint('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = "> This is a quote\n> Another line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_without_space(self):
        block = "#Heading without space"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block_single_line(self):
        block = "``` print('Hello, world!') ```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_without_leading_gt(self):
        block = "This is not a quote\n> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list_without_space(self):
        block = "-Item without space"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_non_consecutive(self):
        block = "1. Item 1\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()

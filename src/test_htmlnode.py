from htmlnode import HTMLNode

def test_htmlnode_with_props():
    node = HTMLNode(
        tag="a",
        value="Google",
        props={"href": "https://www.google.com", "target": "_blank"}
    )
    props_html = node.props_to_html()
    expected = ' href="https://www.google.com" target="_blank"'
    assert props_html == expected, f"Expected: {expected}, Got: {props_html}"
    print("Test props_to_html with props passed!")

def test_htmlnode_without_props():
    node = HTMLNode(tag="p", value="Hello, world!")
    props_html = node.props_to_html()
    assert props_html == "", f"Expected empty string, Got: {props_html}"
    print("Test props_to_html without props passed!")

def test_htmlnode_repr():
    node = HTMLNode(tag="h1", value="Title", children=[], props={"class": "main"})
    repr_str = repr(node)
    expected = "HTMLNode(tag=h1, value=Title, children=[], props={'class': 'main'})"
    assert repr_str == expected, f"Expected: {expected}, Got: {repr_str}"
    print("Test __repr__ passed!")

if __name__ == "__main__":
    test_htmlnode_with_props()
    test_htmlnode_without_props()
    test_htmlnode_repr()

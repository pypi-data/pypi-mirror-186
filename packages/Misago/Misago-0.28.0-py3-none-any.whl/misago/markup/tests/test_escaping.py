# Bunch of tests for unsafe/malicious contents escaping
from ..parser import parse


def test_text_is_escaped(request_mock, user, snapshot):
    text = '<script>alert("!")</script>'
    result = parse(text, request_mock, user, minify=False)
    snapshot.assert_match(result["parsed_text"])


def test_inline_code_is_escaped(request_mock, user, snapshot):
    text = '`<script>alert("!")</script>`'
    result = parse(text, request_mock, user, minify=False)
    snapshot.assert_match(result["parsed_text"])


def test_code_in_quote_markdown_is_escaped(request_mock, user, snapshot):
    text = '> <script>alert("!")</script>'
    result = parse(text, request_mock, user, minify=False)
    snapshot.assert_match(result["parsed_text"])


def test_code_in_quote_bbcode_is_escaped(request_mock, user, snapshot):
    text = '[quote]<script>alert("!")</script>[/quote]'
    result = parse(text, request_mock, user, minify=False)
    snapshot.assert_match(result["parsed_text"])

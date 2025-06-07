import re

text = """
System: Fairbanks

Interface: This is a test
about email body to extract the content
using python

Filename: Test
"""

match = re.search(r'Interface:\s*(.*?)\s*Filename:', text, re.DOTALL)
if match:
    content = match.group(1).strip()
    print(content)

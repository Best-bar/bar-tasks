import re

with open('index.html', 'r') as f:
    content = f.read()

# Let's check what the API mocked earlier returned for 'user'
print(content[400:800])

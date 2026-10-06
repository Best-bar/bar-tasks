import re

with open('index.html', 'r') as f:
    content = f.read()

# Let's see what roles are defined in the select option
matches = re.findall(r'<option value="([^"]+)">([^<]+)<\/option>', content)
print(matches)

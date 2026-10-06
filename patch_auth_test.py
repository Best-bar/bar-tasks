import re

with open('index.html', 'r') as f:
    content = f.read()

# Let's extract the performLogin function
match = re.search(r"async function performLogin\(\).*?\}", content, re.DOTALL)
if match:
    print(match.group(0))
else:
    print("Not found")

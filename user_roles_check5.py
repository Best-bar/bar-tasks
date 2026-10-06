import re

with open('index.html', 'r') as f:
    content = f.read()

# Let's check the applyUserRoleUI function to see what roles exist
print(re.findall(r"function applyUserRoleUI.*?\}", content, re.DOTALL))

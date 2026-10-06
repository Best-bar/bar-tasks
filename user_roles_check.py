import re

with open('index.html', 'r') as f:
    content = f.read()

print(re.findall(r"if \(currentUserRole === '[^']+'\)", content))

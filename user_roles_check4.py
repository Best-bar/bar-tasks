import re

with open('index.html', 'r') as f:
    content = f.read()

# Let's see what roles are set for the select option. Is the value 'user' mapping to 'requester' role?
# We need to know what role the API assigns. We previously saw:
# const USERS_DB = {
#  "admin": { pass: "admin77", role: "admin", name: "Администратор" },
#  "user":  { pass: "user2026", role: "requester", name: "Подающий заявку" },
#  "exec":  { pass: "0", role: "executor", name: "Исполнитель" }
# };
# So the role is INDEED "requester"! But the backend is not in index.html, it's just the login input value that is 'user'.
# When login='user', API returns role='requester'.

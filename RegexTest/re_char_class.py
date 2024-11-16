import re

pattern = r"[1-9a-z]"
string = "Hello, world!0123456789"
ms = re.findall(pattern, string)
print(ms)
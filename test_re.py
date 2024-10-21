import re

text = "Here are some strings: xxxc-123, yyy-456, and zzzz-789."
matches = re.findall(r'\b[a-zA-Z]+-[1-9]+\b', text)
print(matches)  # 输出: ['xxxx-123', 'yyy-456', 'zzzz-789']

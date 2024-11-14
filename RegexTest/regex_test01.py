import re

string = 'Car'
pattern = r'\b[Cc][Aa][Rr]\b'
match = re.fullmatch(pattern, string)
print(match)
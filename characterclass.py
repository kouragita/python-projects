import re

#AA1
pattern = r"[{A-Z}, {A-Z}, {0-9}]"

if re.match(pattern, "AA1"):
    print("match")

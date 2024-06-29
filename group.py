import re

#grp
pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadbread"):
    print("Match Found")

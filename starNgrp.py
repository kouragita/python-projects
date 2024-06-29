import re

#star
pattern = r"eggs(bacon)*"

if re.match(pattern, "eggsbaconbacon"):
    print("Match Found")

import re

#grp
pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadbread"):
    print("Match Found")

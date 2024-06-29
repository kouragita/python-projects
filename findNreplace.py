import re

string = "My name is sensei, Hi i'm sensie"

pattern = r"sensie"

newstring = re.sub(pattern, "chifuu", string)
print(newstring)

import re
pattern = r"gr.y"
if re.match(pattern, "gray"):
    print('Match found')

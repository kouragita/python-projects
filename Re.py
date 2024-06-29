import re

pattern = r"yahoo"

if re.match(pattern, 'yahoogmailgmailyahoo'):
    print('Match found')

else:
    print('No match found')

if re.search(pattern, 'yahoogmailgmailyahoo'):
    print('Match found')

else:
    print('No match found')

print(re.findall(pattern, 'yahoogmailgmailyahoo'))

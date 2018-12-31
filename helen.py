import re
from collections import Counter
paper = open('helen.txt', encoding='utf-8')
data = paper.read()
paper.close()

preps = ['after', 'on', 'in', 'over', 'with', 'of', 'to', 'at', 'from', 'by', 'about', 'as', 'after', 'before', 'between', 'during', 'without']
frmt_str = '[preps[0]preps[1]]'
first_word_prep = re.compile(r'\.\s{{1,2}}(?P<sentence>(?P<prep>{})\s[\w\d,;"\(\)]*[^\.\?\!]+)'.format('|'.join(preps)), re.I)

for match in first_word_prep.finditer(data):
    if match.group('prep'):
        print('I used the preposition "{prep}" in the following sentence: "{sentence}."'.format(**match.groupdict()))

words = re.findall(r'\w+', data, re.I)
print(Counter(words).most_common(10))

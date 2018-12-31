import re

names_file = open('names.txt', encoding='utf-8')
data = names_file.read()
names_file.close()



line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t    # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t     #Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t    #Phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?    # Job and company
    (?P<twitter>@[\w\d]+)?$    # Twitter
''', re.X|re.M)

class Person:
    def __init__(self, last_name, first_name, email, phone, job, twitter):
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone = phone
        self.job = job
        self.twitter = twitter

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

people = []
#import pdb; pdb.set_trace()
for match in line.finditer(data):
    people.append(Person(
                         '{last}'.format(**match.groupdict()),
                         '{first}'.format(**match.groupdict()),
                         '{email}'.format(**match.groupdict()),
                         '{phone}'.format(**match.groupdict()),
                         '{job}'.format(**match.groupdict()),
                         '{twitter}'.format(**match.groupdict())
                         ))






#print(re.match(r'Love', data))
#print(re.search(r'Kenneth', data))
#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

#print(re.findall(r'\w*, \w+', data))

#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))

#new_word = re.findall(r'''
#    \b@[-\w\d.]*
#    [^gov\t]+
#    \b
#''', data, re.VERBOSE|re.I)


#print(re.findall(r'''
#    \b[-\w]*,
#    \s
#    [-\w ]+
#    [^\t\n]
#    ''', data, re.X))

#print(re.findall(r'[a-zA-z]', data))
#print(len(re.findall(r'[a-zA-z]', data)))
#print(re.findall(r'[a-zA-z]*[^l-p]*', data))
#print(len(re.findall(r'[a-zA-z][^l-p]*', data)))



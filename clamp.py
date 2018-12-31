import inflect
p = inflect.engine()

num_str = []
new = []

a = 'abcdefghijklmnopqrstuvwxyz'

for i in range(1000001):
    num_str.append(p.number_to_words(i))

num_str = ''.join(num_str)

for i in num_str:
    if i not in new and i.isalpha():
        new.append(i)

print('the 20th letter is {}!'.format(new[19]))
    






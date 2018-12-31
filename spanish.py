from random import shuffle

vocab = 'alto amable antipatico bajo bonito buen corto delgado este estos feo field gordo grande guapo joven largo listo mal moreno mucho nuevo otro pequeno perezoso pobre rico rubio simpatico todo tonto trabajador viejo'
import pdb; pdb.set_trace()
vocab = vocab.split(' ')
shuffle(vocab)
for word in vocab:
    print(word)

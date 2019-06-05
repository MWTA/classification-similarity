# -*- coding: utf-8 -*-


from nltk.corpus import wordnet as wn

word = 'MISCELLANEOUS'

synset = wn.synsets(word)
print 'Synset:', synset
print '\nHypernym:', synset[0].hypernym_paths()
print '\nDefinition:', synset[0].definition()

print '\n\nDefinition:', wn.synset('feeling.n.01').definition()
#print wn.synset('profession.n.02').examples()

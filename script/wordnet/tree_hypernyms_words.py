# -*- coding: utf-8 -*-
'''
    Description: Generates the hierarchy chart for each word.
                 Gera o gráfico da hierarquia de cada palavra.
    
    Date: 22/11/2018
'''

from graphviz import Digraph
from nltk.corpus import wordnet as wn


def closure_graph(synset, fn):
    seen = set()

    def recurse(s):
        if not s in seen:
            seen.add(s)
            for s1 in fn(s):
                dot.edge(str(s.name().split(".")[0]), str(s1.name().split(".")[0]))
                recurse(s1)

    recurse(synset)


def load_data(path):
    temp_list = []

    with open(path, 'rb') as file:
        for i, line in enumerate(file):
            temp_list.append(line.strip('\n'))

    return temp_list

if __name__ == '__main__':

    path_root = '/home/rodriguesfas/Mestrado/workspace/data_science/classification/similarity/'

    for word in load_data(path_root + 'in/list_words.csv'):

        dot = Digraph('unix', format='svg', filename=path_root+'out/img/tree_words/'+word+'.gv')
        dot.attr(rankdir='BT')
        dot.node_attr.update(color='lightblue2', style='filled')
    
        try:
            synset = wn.synsets(word)[0]
            closure_graph(synset, lambda s: s.hypernyms())
            dot.view()
        except Exception as err:
            print err
            

    
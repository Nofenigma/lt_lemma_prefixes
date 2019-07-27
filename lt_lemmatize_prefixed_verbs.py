'''The program corrects the automatically lemmatized Lithuanian UD-format .conllu files in such a way that all lemmas
with non-derivational prefixes (ne-, be-, te-) are correctly lemmatized.
The potential lemmas are compared to the lemmas from the Lithuanian corpus (frequency) dictionary.
For those lemmas that are obviously reflexive, but are absent in this dictionary, the comparison is done for non-reflexive lemmas;
then the reflexive variant is an updated lemma.
'''
import sys

with open ('dazninis.utf8.txt', 'r', encoding='utf-8') as dic: #creates a dictionary with lemmas from a frequency dictionary
    lt_lemmas = []
    word_0 = ''
    for line in dic:
        line = line.split('\t')
        if line[0] != word_0: #we don't need all the duplicated lemmas - the original file has a 'wordform-per-line' format
            lt_lemmas.append(line[0])
        word_0 = line[0]
        
file = sys.argv[1]
doc = sys.argv[2]
with open (file, 'r', encoding='utf-8') as file:
    with open (doc, 'w', encoding='utf-8') as doc:    
        for line in file:
            line = line.split('\t')
            if len(line) == 10:
                lemma = line[2]
                if line[3] == 'VERB':
                    if lemma.startswith('nebe'): #checks for negated continuative NEBE-
                        print(line)
                        if lemma.startswith('nebesi'): #checks if the verb if reflexive
                            if 'Reflex=Yes' in line[5]:
                                if lemma[6:] + 's' in lt_lemmas:
                                    line[2] = lemma[6:] + 's'
                        elif lemma[4:] in lt_lemmas: #checks for the verb starting with be-, e.g., belsti
                            line[2] = lemma[4:]
                        elif lemma[2:] in lt_lemmas:
                            line[2] = lemma[2:]
                    elif lemma.startswith('ne'): #checks for negated continuative NEBE-                        
                        if 'Reflex=Yes' in line[5]:
                        #if lemma.startswith('nesi'): #checks if the verb if reflexive
                         #   if lemma[4:] + 's' in lt_lemmas:
                            line[2] = lemma[4:] + 's'
                        elif lemma[2:] in lt_lemmas:
                            line[2] = lemma[2:]
                    elif lemma.startswith('tebe'): #checks for the restrictive continuative TEBE-
                        if 'Reflex=Yes' in line[5]:
    #                    if lemma.startswith('tebesi'): #checks if the verb if reflexive
     #                       if lemma[6:] + 's' in lt_lemmas:
                            line[2] = lemma[6:] + 's'
                        elif lemma[2:] in lt_lemmas: #checks for the verb starting with be-, e.g., belsti
                            line[2] = lemma[2:]
                        else:
                            line[2] = lemma[4:]
                    elif lemma.startswith('be'):
                        #if lemma.startswith('besi'): #checks if the verb if reflexive
                        if 'Reflex=Yes' in line[5]:
                            #if lemma[4:] + 's' in lt_lemmas:
                            line[2] = lemma[4:] + 's'
                        elif lemma[2:] in lt_lemmas:
                            line[2] = lemma[2:]                    
                line1= '\t'.join(line)
                doc.write(line1)
            else:
                line1= '\t'.join(line)
                doc.write(line1)

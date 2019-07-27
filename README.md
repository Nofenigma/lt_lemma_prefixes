# lt_lemma_prefixes
This is a short program for improved lemmatization of Lithuanian words with non-derivational prefixes.

At present, only verbs are concerned. The verbs with different combinations of non-derivational (external) prefixes are correctly lemmatized according to their lexical meaning.

# Why use this?
The currently available morphological analyzers for Lithuanian don't lemmatize some prefixed lexemes (mainly verbs) properly. This concerns the prefixes *ne-* (negation), *te-* (permissive or restrictive) and *be-* (continuative), which can also appear in various combinations with each other, e.g., as *tebe-* (continuative) that can be segmented as *te-be-*.

The prefixes in focus are not lexical (don't change the lexical meaning) and can be used with basically any Lithuanian verb, therefore treating such prefixal derivates as separate lemmas seems counterintuitive and just multiplies the number of lemmas in the dictionary, putting obstacles to the generalization between obviously related lexical meanings of their lexical stems.

As concerns the presently available morphological analyzers, the following prefixal derivates of the reflexive verb *rūpintis* 'look after, take care of' are treated as separate lexemes: *tesirūpinti* 'only + V', *nebesirūpinti* 'no more + V', *besirūpinti* 'still + V'.

In addition, not only verbs, but also adjectives and adjectivized participles can be used with such prefixes, e.g., *te-galima* 'RESTR-possible'.

The prefixes *te-* and *be-* and their usage have been considered in the following papers by Peter Arkadiev:

On the aspectual uses of the prefix *be*- in Lithuanian // Baltic Linguistics Vol. 2 (2011), pp. 37–78.

Notes on the Lithuanian restrictive // Baltic Linguistics Vol. 1 (2010), pp. 9—49.

You can also have a look at [this handout](https://inslav.ru/images/stories/people/arkadiev/Arkadiev_2012_te_be_Helsinki.pdf).

# How to use this?

The program takes your UD-style formatted .conllu files (10 columns per non-metadata line) and looks for problematic lexemes. After checking their non-prefixed based verbs, the correct lemma is written in the output file.

Just print this in your command line (don't forget about the dazninis.utf8.txt file, as it is the Lithuanian dictionary used for comparison of lemmas):
`python input_file output_file`


***NB:*** right now there are probably too many commented lines; this is due to the fact that annotation errors are possible, and it's probably not so good to rely on the features 'Neg' and 'Refl' and their values. I have already changed this for negation; for reflexivity the alternative variants are currently commented.

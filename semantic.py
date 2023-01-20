import spacy
nlp = spacy.load('en_core_web_md')

#---------------------------------------------------------------------------------------------------------------------------------------------
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#Write a note about what you found interesting about the similarities 
# between cat, monkey and banana and think of an example of your own.

#Comparing cat and monkey they have more than 50% of similarity because 
#are annimals meanwhile cat and banana have the lowest similarity. banana 
# and monkey have the second highest similarity because they are linked by
# the fact that monkeys eat bananas

word4 = nlp("church")
word5 = nlp("singer")
word6 = nlp("music") 

print("____________________________________________________\n")

print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

print("\n____________________________________________________\n")

#Comparing the wordds church, singer and music, the pair of words with the 
#higests similarity are singer and music, this has sense because both words
#are linked.


#---------------------------------------------------------------------------------------------------------------------------------------------

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#---------------------------------------------------------------------------------------------------------------------------------------------

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp (sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
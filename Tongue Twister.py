
from spacy.lang.te import Telugu
nlp = Telugu()

#from spacy.lang.te.examples import sentences
#docs = nlp.pipe(sentences)

tong = nlp('నీ నాన్న నా నాన్న అని నేనన్ననా? నా నాన్న నీ నాన్న అని నేనన్ననా? నీ నాన్న నీ నాన్నే, నా నాన్న నా నాన్నే అని నేనన్నాను')
text = 'నీ నాన్న నా నాన్న అని నేనన్ననా? నా నాన్న నీ నాన్న అని నేనన్ననా? నీ నాన్న నీ నాన్నే, నా నాన్న నా నాన్నే అని నేనన్నాను'
ind = set(text)
'''
The below results in only two letters as the sentence is written by varying the the two letters 'అ', 'న'
ఏ కింది వాక్యం 'అ', 'న' అనే ఇ రెండు అక్షరాలతో రాయబడింది
'''
print(ind) # {'?', 'ీ', 'అ', 'న', 'ే', ',', '్', ' ', 'ి', 'ా', 'ు'}

words = text.split(' ')
result = {i:words.count(i) for i in set(words)}
# May be the frequent occurence of words was the reason it was a tongue twister
print(result) # {'నా': 4, 'అని': 3, 'నాన్నే': 1, 'నీ': 4, 'నేనన్ననా?': 2, 'నేనన్నాను': 1, 'నాన్నే,': 1, 'నాన్న': 6}

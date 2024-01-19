import pandas as pd

df = pd.read_csv('indic_phonemizer/data/map.csv')


#print(df.head())

t2p = dict(zip(df['character'], df['IPA representation']))

#print(t2p)

def text2phn(text:str):
    phn = ''
    for char in text:
        phn += t2p.get(char.upper(), '').replace('/', '')
    return phn

text = 'dad'

out = text2phn(text)
print('Text: ', text)
print('Phoneme: ', out)
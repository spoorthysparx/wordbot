from nltk.corpus import wordnet as wn

def get_meaning(word):
    synsets=wn.synsets(word)
    if synsets:
        return(synsets[0].definition())
    else:
        return None

def get_synonyms(word):
    synonyms=[]
    synsets=wn.synsets(word)
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma:
                synonyms.append(lemma.name())
    return set(synonyms)

def get_antonyms(word):
    antonyms=[]
    synsets=wn.synsets(word)
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return set(antonyms)

if __name__ == "__main__":
    word="good"
    print(get_meaning(word))
    print(get_synonyms(word))
    print(get_antonyms(word))
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from string import punctuation
from nltk import pos_tag
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
def process_paragraph(paragraph):
    paragraph=paragraph.lower()
    par_tokens=nltk.word_tokenize(paragraph)
    setstopwords=set(stopwords.words("english"))
    lemmatizer=WordNetLemmatizer()
    final_tokens=[]
    for x in par_tokens:
        if x not in setstopwords and x not in punctuation:
            final_tokens.append(x)
    pos_tags=pos_tag(final_tokens)
    output_tokens=[lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags]
    return output_tokens
# main summariser file
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def main(): 
    input_text = """ """
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(input_text)

    freq_table = {}

    rankWords(words, stop_words, freq_table)
    rankSentences(input_text, freq_table)


def rankWords(words, stop_words, freq_table):
    # Rank the number of words in the given input text
    # using a frequency table
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

def rankSentences(text, freq_table):
    # Rank the sentences' relevance
    sentences = sent_tokenize(text)
    sentence_value = {}

    for sentence in sentences:
        for word, freq in freq_table:
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq
                
def defineAverageValue(sen_val):
    sum_values = 0
    for sen in sen_val:
        sum_values += sen_val[sen]

    average = int(sum_values / len(sen_val))
    return average




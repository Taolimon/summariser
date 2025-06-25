# main summariser file
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def main(): 
    input_text = getInputText()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(input_text)

    freq_table = {}

    sentences = sent_tokenize(input_text)

    rankWords(words, stop_words, freq_table)
    
    # Get the value of each sentence using the frequency table
    sentence_value = rankSentences(freq_table, sentences)

    # Use the average frequency as a threshold
    average = defineAverageValue(sentence_value)

    # Generate summary
    summary = getSummary(sentences, sentence_value, average)

    showSummary(summary)

def getInputText():
    text = """ """
    itext = " "
    print("Enter input text: ")
    while True:
        itext = input()
        if itext == "END":
            break
        text += itext
    return text

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

def rankSentences(freq_table=dict, sentences=[str]):
    # Rank the sentences' relevance
    sentence_value = {}

    for sentence in sentences:
        for word in freq_table:
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq_table[word]
                else:
                    sentence_value[sentence] = freq_table[word]
    
    return sentence_value
                
def defineAverageValue(sen_val):
    sum_values = 0
    for sen in sen_val:
        sum_values += sen_val[sen]

    average = int(sum_values / len(sen_val))
    return average

def getSummary(sents, sen_val, avg):
    summary = """"""
 
    for sen in sents:
        if sen in sen_val and sen_val[sen] > (1.2 * avg):
            summary += " " + sen

    return summary

def showSummary(summary):
    print("\nSummary:\n" + summary)

main()
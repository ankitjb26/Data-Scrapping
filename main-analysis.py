import os
import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

stopwords_dir = 'GIVEN-DATA\StopWords'
stopwords = set()

# Define a function to clean the text by removing stop words, punctuation, and converting to lowercase
def clean_text(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Remove stop words
    #stop_words = set(stopwords.words('stopwords'))
    stop_words = set()
    words = text.split()
    words = [word for word in words if word not in stop_words]
    # Join the remaining words into a cleaned text string
    cleaned_text = ' '.join(words)
    return cleaned_text

# Define a function to create dictionaries of positive and negative words
def create_word_dict(filename):
    word_dict = {}
    with open(filename, 'r',encoding="ISO-8859-1") as f:
        for line in f:
            word = line.strip()
            word_dict[word] = 1
    return word_dict

# Define a function to extract derived variables

def extract_variables(text):
    # Calculate average number of words per sentence
    sentences = re.findall(r'[.!?]+', text)
    words = re.findall(r'\w+', text)
    try:
        avg_words_per_sentence = len(words) / len(sentences)
    except ZeroDivisionError:
        avg_words_per_sentence = 0


 # Calculate complex word count
    complex_words = [word for word in words if len(word) > 3 and len(re.findall(r'[aeiouy]+', word, re.IGNORECASE)) >= 3]
    complex_word_count = len(complex_words)

    # Calculate word count
    word_count = len(words)

    # Calculate syllable count per word
    syllables = sum(len(re.findall(r'[aeiouy]+', word, re.IGNORECASE)) for word in words)
    syllable_count_per_word = syllables / word_count

    # Count personal pronouns
    personal_pronouns = ['i', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours']
    personal_pronoun_count = sum(1 for word in words if word.lower() in personal_pronouns)

    # Calculate average word length
    total_word_length = sum(len(word) for word in words)
    avg_word_length = total_word_length / word_count

    return avg_words_per_sentence, complex_word_count, word_count, syllable_count_per_word, personal_pronoun_count, avg_word_length

# Define the folder path
folder_path = 'GIVEN-DATA\MasterDictionary'
text_files_dir = 'data'

# Create dictionaries of positive and negative words
positive_words = create_word_dict('GIVEN-DATA//MasterDictionary//positive-words.txt')
negative_words = create_word_dict('GIVEN-DATA//MasterDictionary//negative-words.txt')

# Loop over all the text files in the folder
for filename in os.listdir(text_files_dir):
    if filename.endswith('.txt'):
        # Load the text file
        with open(os.path.join(text_files_dir, filename), 'r',encoding="ISO-8859-1") as f:
            text = f.read()
        # Clean the text
        cleaned_text = clean_text(text)

        # Analyze the sentiment of the text
        positive_count = sum(1 for word in cleaned_text.split() if word in positive_words)
        negative_count = sum(1 for word in cleaned_text.split() if word in negative_words)
        sentiment_score = (positive_count - negative_count) / (positive_count + negative_count)

        # Extract derived variables
avg_words_per_sentence, complex_word_count, word_count, syllable_count_per_word, personal_pronoun_count, avg_word_length = extract_variables(cleaned_text)

# Print the results
print('Sentiment score:', sentiment_score)
print('Average number of words per sentence:', avg_words_per_sentence)
print('complex_word_count is :',complex_word_count)
print(' word_count is :', word_count)
print('syllable_count_per_word:',syllable_count_per_word)
print('personal_pronoun_count :',personal_pronoun_count )
print('avg_word_length',avg_word_length)
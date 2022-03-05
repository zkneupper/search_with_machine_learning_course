import nltk

nltk.download("averaged_perceptron_tagger")

# POS tagging
str = "Cats eat raw fish."
tokens = nltk.word_tokenize(str)
nltk.pos_tag(tokens)

# NER
nltk.download("words")
nltk.download("maxent_ne_chunker")
str = "Barack Obama served as the 44th President of the United States."
tokens = nltk.word_tokenize(str)
nltk.ne_chunk(nltk.pos_tag(tokens))

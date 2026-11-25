#----------------------------------------
# 1. calculate the number of characters
#----------------------------------------

def char_count(text):
    length = len(text)
    return length

#----------------------------------------
# 2. total number of words
#----------------------------------------

def word_count(text):
    words = text.split()
    word = len(words)
    return word

#---------------------------------------
# 3. total number of sentences
#---------------------------------------

def sentence_count(text):
    sentence = text.count(".") + text.count("!") + text.count("?") 
    return sentence

#---------------------------------------
# 4. Average word length
#---------------------------------------

def avg_count(text):
    total = 0
    for word in text.split():
        total = total + len(word)
    avg_count = total / len(text.split())
    return avg_count

#----------------------------------------------------------
# 5. to check whether the length of text is even or odd
#----------------------------------------------------------

def is_even(text):
    length = len(text)
    if length % 2 == 0:
        return True
    else:
        return False

def main():
    text = input("Enter the text :")

    charCount = char_count(text)
    noWord = word_count(text)
    noSentence = sentence_count(text)
    average = avg_count(text)
    EvenOrOdd = is_even(text)

    print("Total number of characters : ", charCount)
    print("Total number of words : ", noWord)
    print("Total number of sentences : ", noSentence)
    print("Average length of words : ", average)
    print("is the length even or odd : ", EvenOrOdd)

main()


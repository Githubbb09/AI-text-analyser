#----------------------------------------
#getting input from the user
#--------------------------------------

UI = input("Enter the sentence : ")

#----------------------------------------
# 1. calculate the number of characters
#----------------------------------------

char_length = len(UI)
print("Total character length: ",char_length)

#----------------------------------------
# 2. total number of words
#----------------------------------------

words = UI.split(" ")
no_word = len(words)
print(words)
print("Total number of words in this sentence: ",no_word)


#---------------------------------------
# 3. total number of sentences
#---------------------------------------

sentences = UI.count(".") + UI.count("!") + UI.count("?")
print(sentences)

#---------------------------------------
# 4. Average word length
#---------------------------------------

total = 0
for word in words:
    total += len(word)

average = total / no_word
print(average)
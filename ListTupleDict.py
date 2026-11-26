#---------------------------------------------------------------------------
# Creating a COUNTER function that counts how many times a word is repeatedWdzzx
#---------------------------------------------------------------------------

def words_counter(text):
    abc = text.lower().replace(".", "")
    words = abc.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1

    return freq

user_input = input("Enter the sentence: ")
result = words_counter(user_input)

for word, count in result.items():
    print(word +":", count)
#----------------------------------------------------------------------
# Same frequency function in unique way
#----------------------------------------------------------------------

def unique_counter(text):
    feelter = text.lower().replace(".","")
    words = feelter.split()
    frequency = {}

    for w in words:
        frequency[w] = frequency.get(w, 0) + 1

    return frequency

#----------------------------------------------------------------------
# Unique word extractor from the sentence
#----------------------------------------------------------------------

def unique_extractor(text):
    abc = text.lower().replace(".","")
    words = abc.split()
    extractor = set(words)

    return extractor

user_input = input("Enter the sentence : ")
result = unique_counter(user_input)
result1 = unique_extractor(user_input)

print(result)
print(result1)



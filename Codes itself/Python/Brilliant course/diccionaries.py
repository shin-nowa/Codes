# Tentando entender como funciona essa porra de dicionário.
# Using a diccionary to count the times that a word appears and how many times uniques words appeared.
reader = open('C:\Twice\Momo\Worships\Momo1.txt') # Reading a text file to analyse.

punctuation = '.;,-“’”:?—‘!()_' # Defining the punctuation.

freq_dict = {} # A place to store the counting thing.

for line in reader: # Go through each word in the reader.
    for word in line.split():
        cleaned_word = word.lower().strip(punctuation) # Lower thing is to get the characters in lower case and strip one is to remove whatever you want that is attached to the words.
        if cleaned_word in freq_dict: # In case that a new word isn't on the frequency dict.
            freq_dict[cleaned_word] += 1
        else:
            freq_dict[cleaned_word] = 1 # And here is for when a word is already in the frequency dict, but we want to count it anyways.
print(freq_dict)
print(len(freq_dict))



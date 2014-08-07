from sys import argv

script, filename = argv

def get_list_from_line(line, my_file):
    #for line in my_file:
    line = line.rstrip().lower()
    words = line.rsplit(' ')
    return words

# def remove_punctuation(words):
#     for word in words:
#         while ord(word[-1]) < 97:
#             word = word[0:-1] 
#     return words

# def replace_puncuation_with_space(my_file):
#     for character in my_file:
#         character = character.lower
#         if ord(character) < 97 or ord(character) > 122:
#             character = " "
#     return my_file
    

def update_dictionary(words, word_count):
    for word in words:
        #word = word.strip(';:,.-"!?_)')#dict.setdefault will set dict[key] = default if key is not in dictionary
        # it will insert the key into the dictionary if not there

        # if word.isalpha():
        word_count[word] = word_count.setdefault(word, 0) + 1
        #elif "'" in word:
            #word_count[word] = word_count.setdefault(word, 0) + 1
        # if "--" in word:
        #     separate_hyphens = word.rsplit("--")
        #     for separate_words in separate_hyphens:
        #          word_count[separate_words] = word_count.setdefault(separate_words, 0) + 1

    return word_count

def print_counts(word_count):
      # In Python, you don't have to define variables before using them. key, value
    for key, value in sorted(word_count.items()):
        print key, value


def main():
    my_file = open(filename)

    #my_file = replace_puncuation_with_space(my_file)

    word_count = {}

    for line in my_file:
        update_dictionary(get_list_from_line(line, my_file),word_count)
        
    print_counts(word_count)

  

if __name__ == '__main__':
     main() 


'''
# read every line, split by space
# uses the get function to see if the key already exists
# if the key exists, up the counter by one
# if the key doesn't yet exist, create it and increment by one
# for each key, print its value i.e. for key, value in dictionary_name,
# print key, value

def main():
    # open the text file
    text = open("twain.txt")
    word_list = [] # this will contain all of the words in twain.txt
    count_list = [] # this will contain a list of integers for the wordcounts
    word_dict = {} # this will contain key-value pairs representing asdffff
    wordcount_dict = {} # this will contain key-value pairs representing adfff

    # iterate through each line in twain.txt and do the following
    for line in text:
        line = line.rstrip() # takes off the pesky \n characters
        line = line.lower() # converts everything to lowercase
        cleaned_line = "" # initialize empty string variable for cleaned-up text
        
        # go through each character in the line and do the following
        for char in line:
            # if the character has an ascii value in this range, it's a letter
            if ord(str(char)) >= 97 and ord(str(char)) <= 122:
                pass
            # if its ascii value is outside 97-122, it's not a letter
            else:
                char = " " # so we convert it to a space
            cleaned_line += char # put the resulting char back in the cleaned-up line
        # split the line up by spaces and add each segment to word_list
        word_list += cleaned_line.split(" ")

    # go through each word in the word list and
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1 # if the word is already a key, increment value by 1
        else:
            word_dict[word] = 1 # if the word isn't a key yet, create it and assign value of 1

    # go through each key/value pair in the word dictionary
    for key, value in word_dict.iteritems():
        # if the value (the count) is already in the wordcount dictionary
        if value in wordcount_dict.keys():
            # append the key (the word) to the value, which is a list of the words that appear key times
            wordcount_dict[value].append(key)
        else:
            # otherwise, assign a new key-value pair, and start the word list (the value)
            wordcount_dict[value] = [key]

    # go through each key/value pair in the wordcount dictionary
    for key, value in wordcount_dict.iteritems():
        value.sort() # alphabetize value, which is a list of words
        count_list.append(key) # appending the count (a number) to the count list, because it would be inefficient to go in sequence

    count_list.sort() # put the count_list (integers) in ascending order
    count_list.reverse() # put the count_list in descending order, per the extra credit

    # go through each count in the count_list
    for count in count_list:
        # in turn, go through each word in the wordcount dictionary
        for word in wordcount_dict[count]:
            # print the count, followed by the word in alphabetical order
            print count, word

if __name__ == "__main__":
    main()
'''

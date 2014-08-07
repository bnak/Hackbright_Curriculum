#!/usr/bin/env python

from sys import argv
import re
import random
#script, filename = argv




def make_chains(my_file):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    f = open(my_file)
    filetext = f.read()
    filetext = re.sub('[,)(_]', "", filetext)
            
    f.close()
    
    words = filetext.split()

    bigrams_dict = {}


    for i in range(len(words)-2):
        key = (words[i], words [i+1])
        value = words[i+2]
        if key in bigrams_dict:
            bigrams_dict[key] = bigrams_dict.setdefault(key, [value]) + [value]

        else: 
            bigrams_dict[key] = [value]




    return bigrams_dict

def make_text(bigrams_dict, length):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""


    key = random.choice(bigrams_dict.keys())

    #print key

    random_text_list = [key[0].title(), key[1]]
    #print random_text_list

    for i in range(0,length*10):
        new_word = random.choice(bigrams_dict[key])
        #print new_word
        random_text_list.append(new_word)
        #print random_text_list
        key = (key[1], new_word) 
        #print key


    return random_text_list

def print_list_as_string(random_text_list, length):
    #length = int(raw_input("How many characters should the output be?"))

    space = ' '
    text_string = space.join(random_text_list)
    text_string = text_string[0:length]
    position_of_period = text_string.rfind(".")
    text_string = text_string[0:position_of_period+1]
    print position_of_period
    print text_string

def combine_dicts(dict1, dict2):

    for key in dict2:
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else: 
            dict1[key] = dict2[key]

    combined_dict = dict1

    
    return combined_dict

def main():

    #script, filename = argv

    script, file1, file2 = argv
    

    dict1 =  make_chains(file1)
   
    dict2 = make_chains(file2)
  

    combined_dict = combine_dicts(dict1, dict2)



    length = int(raw_input("How many characters should the output be?"))

    print_list_as_string(make_text(combined_dict, length), length)

    #print_list_as_string(make_text(make_chains(filename), length), length)

    #random_text = make_text(chain_dict)
    #print my_text

if __name__ == "__main__":
    main()
#Michael Hart

"""
This program opens a text document and get information about it.
"""

def remove_characters(full_str, remove_chars):
    'Returns version of string full_str without remove_chars characters.'

    # Make remove_chars into a list.
    remove_char_list = []
    remove_char_list += remove_chars

    # Set up string to return that will eventually not have the remove_chars.
    clean_str = full_str

    # Go through each of the characters in remove_char_list and remove them from clean_str.
    for no_char in remove_char_list:
        clean_str = clean_str.replace(no_char, '')

    return clean_str
    

def remove_stop_words(word_list, stop_words):
    'Returns a version of word_list without words in stop_words.'

    # Make a copy of word_list so we don't modify the original.
    clean_list = word_list.copy()

    # Go through each stop word.
    for stop_word in stop_words:
        # Remove the stop word from list.
        words_left_to_remove = True
        while words_left_to_remove:
            try:
                clean_list.remove(stop_word)
            except:
                words_left_to_remove = False

    # Return the word_list without the stop_words.
    return clean_list


# Open file for reading.
text_file = open("text_files/usdeclar.txt")

# Read content from text file (content variable is a string).
content = text_file.read()

#
# Get number of characters and inform user.
#
num_characters = len(content)
print("This file has " + str(num_characters) + " characters")

#
# Get the number of words.
#
content_no_punctuation = remove_characters(content, '.,;!?:-\'"$0987654321()')
content_no_punctuation = content_no_punctuation.lower()
word_list = content_no_punctuation.split()
num_words = len(word_list)
print("This file has " + str(num_words) + " words")

#
# Get word frequency.
#
import collections

word_counter = collections.Counter(word_list)
top_20_words = word_counter.most_common(20)
print("The 20 most common words are " + str(top_20_words))


#
# Get rid of stop words.
#

# Get list of stop words.
stop_words_file = open("text_files/stop_words.txt")
stop_words_content = stop_words_file.read()
stop_words = stop_words_content.split()

# Get the word counts without the stop words.
clean_word_list = remove_stop_words(word_list, stop_words)
word_counter = collections.Counter(clean_word_list)
top_20_words = word_counter.most_common(20)
print("The 20 most common words are " + str(top_20_words))


# Close the file.
text_file.close()

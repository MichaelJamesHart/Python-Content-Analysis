#Michael Hart

"""
This program opens a text document and provides the following information:
1) The total character count.
2) The total word count.
3) The 20 most common words, *including* stop words.
4) The 20 most common words, *excluding* stop words.

This program can be used as part of a large project to quantitatively analyze the topic or sentiment of a document,
or for something simpler such as making sure you don't overuse a particular adjective in a cover letter, research paper,
or any other important body of text.
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


# Open the file for reading; rewrite what is inside the *open("")* double quotes to analyze a different file.
text_file = open("text_files/cover_letter.txt")

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
print("The 20 most common words (*including* stop word) are " + str(top_20_words))


#
# Get rid of stop words.
#

# Get list of stop words. Feel free to add or remove stop words from the stop_words.txt file as necessary.
stop_words_file = open("text_files/stop_words.txt")
stop_words_content = stop_words_file.read()
stop_words = stop_words_content.split()

# Get the word counts without the stop words.
clean_word_list = remove_stop_words(word_list, stop_words)
word_counter = collections.Counter(clean_word_list)
top_20_words = word_counter.most_common(20)
print("The 20 most common words (*excluding* stop words) are " + str(top_20_words))


# Close the file.
text_file.close()

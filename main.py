# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from string import punctuation


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as file:
        file_content = file.read()
        file.close()
        return file_content

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    for i in punctuation:
        text = text.replace(i, "")
    # create a dictionary to store the count
    count_dict = {}
    text = text.lower()
    # split the text into words
    words = text.split()

    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    print(count_dict)
    return count_dict

count_words()

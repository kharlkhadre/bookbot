def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
# get the count of the words
        count = word_count(file_contents)
# get the dictionary of character counts
        ch_count = char_count(file_contents)
# sort the dictionary by counts
        ch_list = list(ch_count.items())
        ch_list.sort(reverse=True, key=lambda chars: chars[1])

        print("--- Begin report of books/frankenstein.txt ---")
        print(count, " words found in the document")
        for i in ch_list:
            print(f"The '{i[0]}' was found {i[1]} times")


def sort_on(dict):
    return dict[1]
    
def word_count(filetext):
    file_split = filetext.split()
    return len(file_split)

def char_count(filetext):
    char_dict = {}
    ltxt = filetext.lower()
    for i in ltxt:
        if i.isalpha():
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
    return char_dict

main()


 #2 assignement count words:
def num_words(book_text):
    text = book_text.split() #Return a list of the words in the string
    num_words = len(text)
 
    #print(f"{num_words} words found in the document")
    return num_words

def num_char(book_text):   
    lower_strings = book_text.lower() #only lower string

    #print(lower_strings)
    chars = [char for char in lower_strings] #Split String into List of characters in Python
    #print(chars)

    char_dic = {}
    for char in chars:
        if char in char_dic:
            char_dic[char] +=1
        else:
            char_dic[char] =1
    return char_dic

def sort_on(items):
    return items["num"]

#Report
def sort(char_counts):
    list_dicts = []
    # small_dict = {}
        
# iteracja po slowniku i wyswietlenie go jako char: num:
    for char in char_counts:
        num = char_counts[char]
        #print(f"char: {char}, num: {num}")
        if char.isalpha() == True: #tylko charackters beda zwrocone w nowym small dict
            small_dict = {
                # tutaj
                "char": char,
                "num": num
            }
            
    # add to the list: 
            list_dicts.append(small_dict)
    #print(list_dicts)


    list_dicts.sort(reverse=True, key=sort_on)
    return list_dicts
    #print(list_dicts)


# test 1
#sort_dicts({"a": 10, "b": 15})
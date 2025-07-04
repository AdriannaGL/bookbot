#import from stats
from stats import num_words, num_char, sort, sort_on 
#1 assignement read file: 
def get_book_text(path_to_the_file):
    with open(path_to_the_file) as f:
        file_contents = f.read() #read the contents of a file into a string:
        return file_contents
    
def main():   
    book_text = get_book_text('/Users/adrianna/dev/bookbot/books/Frankenstein.txt')
    print(f"Analyzing book found at books/frankenstein.txt...")
    num_w = num_words(book_text)
    print(f"Found {num_w} total words")
    char_counts = num_char(book_text)
    
    #print(char_counts)
    result = sort(char_counts)
    
    for small_dict in result:
        final_char = small_dict["char"]
        final_num = small_dict["num"]
        #print(small_dict)
        print(f"{final_char}: {final_num}")
        
    #print(result)
    

main()
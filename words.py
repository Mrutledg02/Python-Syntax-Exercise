def print_upper_words(words):
    '''Print each word in all uppercase on a separate line.
    
    Parameters:
    -words (list): A list of words.

    Example:
    words_list = ["apple", "banana", "cherry", "date"]
    print_upper_words(words_list)
    APPLE
    BANANA
    CHERRY
    DATE
    '''
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """ Print each word in all uppercase on a separate line if it starts with 'e' (either upper or lowercase).

    Parameters:
    - words (list): A list of words.

    Example:
    words_list = ["apple", "banana", "cherry", "date", "elderberry", "eggplant"]
    print_upper_words2(words_list)
    ELDERBERRY
    EGGPLANT
    """

    for word in words:
        if word.lower().startswith('e') or word.startswith("E"):
            print(word.upper())

    # for word in words:
    #     if word.startswith("e") or word.startswith("E"):
    #         print(word.upper())

def print_upper_words(words, must_start_with):
    """
    Print each word in all uppercase on a separate line if it starts with any of the specified letters.

    Parameters:
    - words (list):  A list of words.
    - must_start_with (set): A set of letters to filter words that must start with.

    Example:
    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                    must_start_with={"h","y"})
    HELLO
    HEY
    YO
    YES
    """

    for word in words:
        if any(word.lower().startswith(letter) for letter in must_start_with):
            print(word.upper())

    # for word in words:
    #     for letter in must_start_with:
    #         if word.startswith(letter):
    #             print(word.upper())
    #             break
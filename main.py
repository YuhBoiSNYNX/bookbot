
def main():
    """
    The main function of the script

    This function is responsible for calling all other functions and
    printing the report.
    """
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    wordcount = word_count(file_contents)
    # The letter count is a dictionary where the keys are the letters and
    # the values are the counts of each letter
    lettercount = letter_count(file_contents)
    # The print_report function takes the word count, letter count and the
    # path to the book and prints a report
    print_report(wordcount, lettercount, book_path)

def word_count(file_contents: str):
    words = file_contents.split()
    return len(words)

def letter_count(file_contents: str):
    """
    Count the frequency of each letter in the given text.

    Args:
        file_contents (str): The content of the file as a string

    Returns:
        dict: A dictionary with letters as keys and their frequencies as values
    """
    char_count = {}
    # Convert the text to lowercase to ensure case-insensitivity
    file_contents = file_contents.lower()
    # Iterate over each character in the text
    for char in file_contents:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # If the letter is already in the dictionary, increment its count
            if char in char_count:
                char_count[char] += 1
            else:
                # If the letter is not in the dictionary, add it with a count of 1
                char_count[char] = 1
    return char_count

def print_report(word_count: int, letter_count: dict, book_path: str):
    """
    Print a report of the word count and letter frequency in the document

    Args:
        word_count (int): The number of words in the document
        letter_count (dict): A dictionary containing the letters and their counts
        book_path (str): The path to the document
    """
    # Print the header of the report
    print(f"--- Begin report for {book_path} ---")
    print(f"{word_count} words found in the document \n")

    # Sort the letters by count in descending order
    letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    # Print the counts of each letter
    for letter, count in letter_count:
        print(f"The \'{letter}\' character was found {count} times")


    # Print the footer of the report
    print(f"--- End report for {book_path} ---")



main()
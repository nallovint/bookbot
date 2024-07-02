from string import ascii_lowercase

with open("books/frakenstein.txt") as f:
    file_contents = f.read()
    # print(len(file_contents.split()))
    letters_dict = {k: v for k, v in sorted({letter: file_contents.count(letter) for letter in ascii_lowercase}.items(), key=lambda item: item[1], reverse=True)}
    # print(letters_dict)
    print('--- Begin report of books/frakenstein.txt ---')
    print('\n'.join(map(lambda x: f"The letter '{x[0]}' was found {x[1]} times", letters_dict.items())))
    print('--- End report ---') 
with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    print(file_contents)

    counter = 0
    words = file_contents.split()
    for word in words:
        counter += 1;
    print(counter)
    
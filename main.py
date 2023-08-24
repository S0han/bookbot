with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    # print(file_contents)

    counter = 0
    words = file_contents.split()
    for word in words:
        counter += 1;
    # print(counter)

    dict = {}
    string_content = ''.join(words).lower()
    for chr in string_content:
        if chr not in dict:
            dict[chr] = 0
            dict[chr] += 1
        else:
            dict[chr] += 1 
    print(dict)
    
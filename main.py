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
    # print(dict)

    report_list = list(dict)
    header = "--- Begin report of books/frankenstein.txt ---"
    count_string = (f"{counter} words found in the document\n")
    end_string = "--- End report ---"
    
    # report
    print(header)
    print(count_string)

    for item in report_list:
        if item.isalpha():
            print(f"The {item} character was found {dict[item]} times")

    print("\n")
    print(end_string)

    
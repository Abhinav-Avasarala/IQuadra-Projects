def make_logo(string):
    count_dictionary = {}
    for i in range(len(string)):
        count = 1
        current_letter = string[i].lower()
        for j in string[i + 1:]:
            if j == current_letter:
                count += 1

        if current_letter not in count_dictionary:
            count_dictionary[current_letter] = count

    trans_dictionary = count_dictionary.copy()

    final_word = ""

    while len(final_word) != 3:
        count = 0
        list = []

        for key in count_dictionary:
            if count_dictionary[key] >= count:
                count = count_dictionary[key]

        for key in count_dictionary:
            if count_dictionary[key] == count:
                list.append(key)

        if len(list) == 1:
            current_letter = list[0]
            final_word += current_letter
            del count_dictionary[current_letter]

        else:
            current_letter = "z"
            for i in range(len(list)):
                if list[i] < current_letter:
                    current_letter = list[i]

            final_word += current_letter
            del count_dictionary[current_letter]

    print(f"{final_word[0]} {trans_dictionary[final_word[0]]}")
    print(f"{final_word[1]} {trans_dictionary[final_word[1]]}")
    print(f"{final_word[2]} {trans_dictionary[final_word[2]]}")

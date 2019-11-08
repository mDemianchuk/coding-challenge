def words_exist(words):
    return len(words) != 0


def is_source_shorter_than_concatenation(source, word_length):
    return len(source) < word_length


def find_indices(source, words):
    indices = []
    try:
        if not words_exist(words):
            raise Exception("The word list is empty")

        word_dict = dict()
        for word in words:
            number_of_occurrences = word_dict.get(word)
            if number_of_occurrences is None:
                number_of_occurrences = 0
            word_dict.update({word: number_of_occurrences + 1})

        # assuming that all words are the same length
        concatenation_length = len(words[0]) * len(words)

        if is_source_shorter_than_concatenation(source, concatenation_length):
            raise Exception("The source is shorter than the word concatenation")

        max_index = len(source) - (concatenation_length - 1)
        for i in range(max_index):
            source_slice = source[i:concatenation_length + i]
            index = 0
            found = False
            word_dict_copy = word_dict.copy()
            for word in words:
                word_slice = source_slice[index:len(words[0]) + index]
                index = index + len(words[0])
                expected_number_of_occurrences = word_dict_copy.get(word_slice)
                if expected_number_of_occurrences is None or expected_number_of_occurrences == 0:
                    found = False
                    break
                else:
                    word_dict_copy.update({word_slice: expected_number_of_occurrences - 1})
                    found = True
            if found:
                indices.append(i)

    except Exception as e:
        print("An error occurred " + repr(e))

    return indices


print(find_indices("barfoothefoobarman", ["foo", "bar"]))

def frequent_words_finder_json(json_filepath, encoding_format, top_number):

    import json
    from pprint import pprint

    with open('newsfiles/newsafr.json', encoding = encoding_format) as f:
        news_data = json.load(f)
        # pprint(news_data)
        news_list = news_data['rss']['channel']['items']

        word_array = []

    for record in news_list:

        split_title = record['title'].split()
        for word in split_title:
            if len(word) > 6:
                word_array.append(word)

        split_description = record['description'].split()
        for word in split_description:
            if len(word) > 6:
                word_array.append(word)


    top_frequent_words = {}
    word_array_set = set(word_array)

    for number in range(top_number):
        max_frequency = 0
        for word in word_array_set:
            if word_array.count(word) > max_frequency:
                max_frequency = word_array.count(word)
                frequent_word = word
        top_frequent_words[frequent_word] = max_frequency
        word_array_set.remove(frequent_word)

    print(top_frequent_words)
    return top_frequent_words


frequent_words_finder_json('newsfiles/newsafr.json', 'utf-8', 10)
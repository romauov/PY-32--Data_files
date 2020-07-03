def frequent_words_finder_json(json_filepath, encoding_format, top_number):

    import json
    from pprint import pprint

    with open(json_filepath, encoding = encoding_format) as f:
        news_data = json.load(f)
        # pprint(news_data)
        news_list = news_data['rss']['channel']['items']

    word_array = []

    for record in news_list:

        split_title = record['title'].split()
        for word in split_title:
            if len(word) > 6:
                word_array.append(word.lower())

        split_description = record['description'].split()
        for word in split_description:
            if len(word) > 6:
                word_array.append(word.lower())


    return top_words_counter(word_array, top_number)
    # frequent_words = {}
    # top_frequent_words = {}
    #
    # for word in word_array:
    #     frequent_words[word]=frequent_words.get(word, 0) + 1
    #
    #
    # number = 0
    # for item in sorted(frequent_words.items(), reverse=True, key=lambda couple: couple[1]):
    #     if number == top_number:
    #         break
    #     else:
    #         top_frequent_words[item[0]] = item[1]
    #         number += 1
    #
    # return top_frequent_words




    # # for word in word_array_set:
    # #     frequency = word_array.count(word)
    # #     top_frequent_words[word] = frequency
    # # for word, frequency in sorted(top_frequent_words.items()):
    # #     print(word, frequency)
    #
    # for number in range(top_number):
    #     max_frequency = 0
    #     for word in word_array_set:
    #         if word_array.count(word) > max_frequency:
    #             max_frequency = word_array.count(word)
    #             frequent_word = word
    #     top_frequent_words[frequent_word] = max_frequency
    #     word_array_set.remove(frequent_word)
    #
    # print(top_frequent_words)
    # return top_frequent_words

def frequent_words_finder_xml(xml_filepath, encoding_format, top_number):

    import xml.etree.ElementTree as ET
    from pprint import pprint

    parser = ET.XMLParser(encoding = encoding_format)
    tree = ET.parse(xml_filepath, parser)
    root = tree.getroot()

    xml_news_titles = root.findall("channel/item/title")
    news_list = []
    for xml_title in xml_news_titles:
        title = xml_title.text
        news_list.append(title)


    xml_news_descriptions = root.findall("channel/item/description")
    news_descriptions = []
    for xml_news_descriptions in xml_news_descriptions:
        description = xml_news_descriptions.text
        news_descriptions.append(description)


    word_array = []

    for record in news_list:
        split_title = record.split()
        for word in split_title:
            if len(word) > 6:
                word_array.append(word.lower())

    for record in news_descriptions:
        split_description = record.split()
        for word in split_description:
            if len(word) > 6:
                word_array.append(word.lower())


    # top_frequent_words = {}
    # word_array_set = set(word_array)
    #
    # for number in range(top_number):
    #     max_frequency = 0
    #     for word in word_array_set:
    #         if word_array.count(word) > max_frequency:
    #             max_frequency = word_array.count(word)
    #             frequent_word = word
    #     top_frequent_words[frequent_word] = max_frequency
    #     word_array_set.remove(frequent_word)
    #
    # print(top_frequent_words)
    return top_words_counter(word_array, top_number)

def top_words_counter(words_list, top_number):
    frequent_words = {}
    top_frequent_words = {}

    for word in words_list:
        frequent_words[word]=frequent_words.get(word, 0) + 1


    number = 0
    for item in sorted(frequent_words.items(), reverse=True, key=lambda couple: couple[1]):
        if number == top_number:
            break
        else:
            top_frequent_words[item[0]] = item[1]
            number += 1

    return top_frequent_words



print(frequent_words_finder_json('newsfiles/newsafr.json', 'utf-8', 10))
print(frequent_words_finder_xml('newsfiles/newsafr.xml', 'utf-8', 10))
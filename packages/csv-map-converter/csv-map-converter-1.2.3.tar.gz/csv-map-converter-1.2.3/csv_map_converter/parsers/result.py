# -*- coding: utf-8 -*- 

class CsvMapResult(object):
    """
    It is csv result which call csv map parser.
    """

    def __init__(self, titles, data, title_mapping):
        self.__titles = titles
        self.__data = data
        self.__title_mapping = title_mapping

    def get_titles(self):
        """
        Get titles.
        """
        return self.__titles

    def get_title_by_index(self, index):
        """
        Get title by original csv index.
        """
        return self.__title_mapping.get(index)

    def get_indexes_by_title(self, title):
        indexes = []

        title_mapping_items = self.__title_mapping.items()
        for key, val in title_mapping_items:
            if val == title: indexes.append(key)

        return indexes

    def get_content(self):
        """
        Get a dict array from title mapping.
        """
        return self.__data


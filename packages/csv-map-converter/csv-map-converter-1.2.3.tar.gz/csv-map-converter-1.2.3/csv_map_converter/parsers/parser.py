# -*- coding: utf-8 -*- 

from .result import CsvMapResult

class CsvMapParser(object):
    """
    It is a csv parser which is able to convert csv lines to map of titles and values.
    """

    def __init__(self): pass

    def __build_title_mapping(self, row):
        mapping = dict()
        current_idx = None

        for idx, cell in enumerate(row):
            is_title_name = False

            if cell:
                title_name = cell.strip()
                if title_name:
                    mapping[idx] = title_name
                    current_idx = idx
                    is_title_name = True

            if is_title_name and current_idx:
                mapping[current_idx] = mapping.get(idx)
            elif current_idx:
                mapping[idx] = mapping.get(current_idx)

        return mapping

    def __get_titles(self, line):
        titles = []
        for cell in line:
            if cell:
                normal_cell = cell.strip()
                if normal_cell: titles.append(normal_cell)

        return titles
                
    def __push_cell(self, title_name, row_data, cell_str):
        current_cell_data = row_data.get(title_name)

        if current_cell_data:
            current_cell_data.append(cell_str)
        else:
            current_cell_data = [cell_str]
            row_data[title_name] = current_cell_data

    def parse(self, lines, start_row = 1, title_row = 0):
        """
        Parse csv lines.
        It will return title mapping result.
        """

        result = list()
        row_count = len(lines)
        title_line = lines[title_row]
        title_mapping = self.__build_title_mapping(title_line)
        titles = self.__get_titles(title_line)
        rows = lines[start_row:]

        for row in rows:
            row_data = dict()

            for idx, cell in enumerate(row):
                title_name = title_mapping.get(idx)

                if title_name and cell:
                    cell_str = cell.strip()
                    if cell_str: self.__push_cell(title_name, row_data, cell_str)

            result.append(row_data)

        return CsvMapResult(titles, result, title_mapping)



# -*- coding: utf-8 -*- 

from .parsers.parser import CsvMapParser
from .models.fields.base import ListField
from .models.fields import ModelDescriptor

class ConvertResult(object):

    def __init__(self, map_result, models = None):
        self.__map_result = map_result
        self.__models = models

    @property
    def models(self):
        return self.__models

    @property
    def map_result(self):
        return self.__map_result
    

class Converter(object):
    """
    This is csv converter.
    """

    def __init__(self):
        self.__csv_map_parser = CsvMapParser()

    def __convert_parsing_result_to_models(self, csv_map_result, Model):
        titles = csv_map_result.get_titles()
        data_rows = csv_map_result.get_content()
        model_descriptor = ModelDescriptor(Model)
        models = []

        for data_row in data_rows:
            model = Model()
            for title in titles:
                field = model_descriptor.get(title)
                if field:
                    cell_data = data_row.get(title)

                    if not(isinstance(field, ListField)) and cell_data and len(cell_data): cell_data = cell_data[0]
                    
                    if not(cell_data) and field.default: field_value = field.default
                    else: field_value = field.to_python(cell_data)

                    #setattr(model, title, field_value)
                    model_descriptor.set(model, title, field_value)

            models.append(model)

        return models

    def convert(self, lines, Model = None, start_row = 1, title_row = 0):
        """
        Parse lines of titles and data to array map.

        :Args
        - lines - two dimensional array of string.
        - start_row - start parsing data row index.
        - title_row - title row index.
        """

        csv_map_result = self.__csv_map_parser.parse(lines, start_row = start_row, title_row = title_row)
        if Model:
            models = self.__convert_parsing_result_to_models(csv_map_result, Model)
        else:
            models = None

        return ConvertResult(csv_map_result, models)

        


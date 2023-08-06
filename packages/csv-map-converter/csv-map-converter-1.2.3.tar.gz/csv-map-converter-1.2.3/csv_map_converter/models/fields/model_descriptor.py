
from .base import FIELD_LIST

class ModelDescriptor():

    def __init__(self, Model):
        self.__init_all_dict_of_model_field(Model)

    def get(self, name):
        return self.__field_dict.get(name)

    def set(self, model, csv_field_name, value):
        model_attr_names = self.__original_mapping_dict.get(csv_field_name) or []
        for model_attr_name in model_attr_names:
            setattr(model, model_attr_name, value)
        

    def __init_all_dict_of_model_field(self, Model):
        self.__field_dict = field_dict = dict()
        self.__original_mapping_dict = original_mapping_dict = dict()
            
        for attr_name in dir(Model):
            field = getattr(Model, attr_name)
            if field.__class__ in FIELD_LIST:
                if field.name:
                    field_dict[field.name] = field
                    csv_field_name = field.name
                else:
                    field_dict[attr_name] = field
                    csv_field_name = attr_name

                if original_mapping_dict.get(csv_field_name) == None:
                    original_mapping_dict[csv_field_name] = []

                original_mapping_dict[csv_field_name].append(attr_name)



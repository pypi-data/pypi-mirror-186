from distutils.util import strtobool
from datetime import datetime
from types import FunctionType
from dataclasses import fields
from typing import Dict
# Key points:
# 0) For get_instance_from_dict or get_dict_from_instance to work, the obj MUST be a dataclass!
# 1) conversion_fxn_map is a map from the STRING name of a data_type (e.g. 'int', not int)
#       to a function that converts an input value to that data_type.
# 2) The input values for get_instance_from_dict are currently all strings because they are
#       just payloads from http responses, but you can support any input data_type with this
#       framework. You simply have to define the conversion fxns to support the desired
#       input/output types.
# 3) Currently, get_dict_from_instance does not perform any type conversions. I may choose
#       to add that capability in the future, but it currently only converts the object to a
#       dict in the form {field_name_1 : field_val_1, ...}
class DataConverter:
    conversion_fxn_map : dict #[str : FunctionType]

    def __init__(self,extended_conversion_fxn_map=None):
        self.conversion_fxn_map = {cls.__name__: cls for cls in [str, int, float, bool, dict]}
        self.conversion_fxn_map['bool']=strtobool #allows us to convert the string input to a bool in a more intuitive way
        self.conversion_fxn_map['datetime']=lambda x : datetime.fromisoformat(x)

        if extended_conversion_fxn_map is not None:
            self.conversion_fxn_map.update(extended_conversion_fxn_map)
    # convert a single value to the specified data_type_str by using the appropriate conversion_fxn
    # e.g. convert_from('123','int') returns the integer-type 123. Note: 'int', not int.
    def convert_from(self,val,date_type_str):
        return self.conversion_fxn_map[date_type_str](val)

    # Converts a dict in the form {field_name_1 : field_val_1, ...} to an instance of a dataclass.
    # The dict may contain "extra" field_names not defined in the dataclass. Only the fields that
    # exist in the dataclass will be copied into the new instance object.
    def get_instance_from_dict(self,some_dict : dict, cls):
        converted_dict = {}
        for field in fields(cls):
            val, type_name=None, None
            if field.name in some_dict:
                val = some_dict[field.name]

                type_name=field.type

                # for some odd reason, type_name is sometimes a string literal and sometimes a class object
                # (e.g. sometimes the string 'int' and sometimes the class int)
                if not isinstance(type_name,str):
                    type_name = type_name.__name__

            if val is not None:
                converted_dict[field.name]=self.conversion_fxn_map[type_name](val)
            else:
                converted_dict[field.name]=None
        return cls(**converted_dict)

    def get_instances_from_arr_of_dicts(self,arr_of_dicts : list[dict],cls):
        return [self.get_instance_from_dict(d,cls) for d in arr_of_dicts]
    # Convert a dataclass instance to a dict in the form {field_name_1 : field_val_1, ...}.
    # No type conversions are currently performed, but they can be added as needed.
    # Specify an "only_include" array to specify a subset of field_names to copy into the new dict
    def get_dict_from_instance(self,obj,only_include=None):
        if only_include is None:
            only_include = [f.name for f in fields(obj)]
        return {field_name : getattr(obj,field_name) for field_name in only_include}
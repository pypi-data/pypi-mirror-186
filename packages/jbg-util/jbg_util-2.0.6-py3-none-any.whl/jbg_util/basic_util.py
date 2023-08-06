from datetime import datetime,timedelta
from tabulate import tabulate
from traceback import print_exc
from distutils.util import strtobool
TYPES = {cls.__name__: cls for cls in [str, int, float, bool, dict]}
TYPES['bool']=strtobool #allows us to convert the string input to a bool in a more intuitive way

def add_to_dte(dte,days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    return dte + timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks)

def dte_to_str(dte):
    if dte is None:
        return None
    return dte.strftime("%Y-%m-%d")

def now():
    return datetime.utcnow()

def first(lst,matching_fxn):
    try:
        return next(item for item in lst if matching_fxn(item))
    except StopIteration as e:
        return None

# A decorator that catches exceptions and logs them.
# Requires that the function be an instance method and the instance has a self.logger.error() function
def catches_exceptions(fxn):
    def wrapper(self,*args,**kwargs):
        try:
            fxn(self,*args,**kwargs)
        except Exception as e:
            self.logger.error(f'Exception occurred during {fxn.__qualname__}: {str(e)}')
            print_exc()
    return wrapper

def print_table(rows,col_headers):
    rows = [col_headers, *rows]
    print(tabulate(rows, headers='firstrow', tablefmt='fancy_grid'))

def get_mapped_val(map,key):
    if key not in map:
        raise ValueError(f'unrecognized key: {key}')
    return map[key]
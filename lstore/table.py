from lstore.index import Index
from time import time
from lstore.page_range import PageRange

INDIRECTION_COLUMN = 0
RID_COLUMN = 1
TIMESTAMP_COLUMN = 2
SCHEMA_ENCODING_COLUMN = 3


class Record:

    def __init__(self, rid, key, columns):
        self.rid = rid
        self.key = key
        self.columns = columns

class Table:

    """
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """
    def __init__(self, name, num_columns, key):
        self.name = name
        self.key = key
        self.num_columns = num_columns
        self.page_directory = {}
        self.page_range = [PageRange(num_columns)] # Stores all page ranges
        self.index = Index(self)
        self.merge_threshold_pages = 50  # The threshold to trigger a merge
        self.base_rid_count = 1 # RID counter

    def __merge(self):
        print("merge is happening")
        pass
 
    # Note: RID -> (page_range, page #, offset)
    # Output: Location of the record as a tuple
    def find_record(self, rid):
        location = self.page_directory[rid]
        return location

    # Note: RID -> (page_range, page #, offset)
    # Output: The items in the record as a tuple
    def get_record(self, rid):
        location = self.page_directory[rid]
        record = self.page_range[location[0]].base_pages[location[1]].get_record(location[2])
        return record

    def get_rid(self):
        rid = self.base_rid_count
        self.base_rid_count += 1
        return rid

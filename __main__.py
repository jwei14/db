from lstore.db import Database
from lstore.query import Query
from time import process_time
from random import choice, randrange

# Student Id and 4 grades
db = Database()
grades_table = db.create_table('Grades', 2, 0)
query = Query(grades_table)
keys = []

#query.insert(906659671, 93)

#print(int.from_bytes(db.tables[0].page_range[0].base_pages[0].rid.data[0:8], byteorder = 'big'))
#print(int.from_bytes(db.tables[0].page_range[0].base_pages[0].indirection.data[0:8], byteorder = 'big'))
#print(int.from_bytes(db.tables[0].page_range[0].base_pages[0].time.data[0:8], byteorder = 'big'))
#print(int.from_bytes(db.tables[0].page_range[0].base_pages[0].schema_encoding.data[0:8], byteorder = 'big'))
#print(int.from_bytes(db.tables[0].page_range[0].base_pages[0].pages[0].data[0:8], byteorder = 'big'))
#print(int.from_bytes(db.tables[0].page_range[0].base_pages[0].pages[1].data[0:8], byteorder = 'big'))

insert_time_0 = process_time()
for i in range(0, 511):
    query.insert(906659671 + i, 93)
    keys.append(906659671 + i)
insert_time_1 = process_time()

print("Inserting 512 records took:  \t\t\t", insert_time_1 - insert_time_0)
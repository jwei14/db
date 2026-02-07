from lstore.page import Page, BasePage, TailPage

class PageRange:
    def __init__(self, num_columns):
        self.base_pages = [BasePage(num_columns)]
        self.tail_pages = [TailPage(num_columns)]
        self.current_base_index = 0
        self.current_tail_index = 0
    
    # Adds user info into columns inside base page (for INSERT)
    def append_base(self, rid, indirection, time, se, col_info):
        if len(self.base_pages) == 16:
            col = len(col_info) + 4
            p = PageRange(col) # create a new page range
            p.base_pages[p.current_base_index].append_record(rid, indirection, time, se, col_info)
        else:
            self.base_pages[self.current_base_index].append_record(rid, indirection, time, se, *col_info) 

    # Adds user info into columns inside tail page (for UPDATE)
    def append_tail(self, col_info):
        if len(self.base_pages) == 16:
            return False # create a new page range
        else:
            self.tail_pages[self.current_tail_index].append_record(rid, indirection, time, se, col_info)

    # Used when previous base page is full
    def add_base_page(self):
        if len(self.base_pages) == 16: 
            return False # Tell table to create a new Page Range
        else:
            b = BasePage()
            self.base_pages.append(b)
            self.current_base_index += 1
        return b

    # Used when previous tail page is full
    def add_tail_page(self):
        t = TailPage()
        self.tail_pages.append(t)
        self.current_tail_index += 1
        return t

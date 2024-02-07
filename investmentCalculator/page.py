class Page():
    def __init__(self, page_number=1, page_size=30):
        self.page_number = page_number
        self.page_size = page_size

    def set_page(self, page):
        self.page_number = page

    def set_page_size(self, page_size):
        self.page_size = page_size
        self.set_page(1)

    def get_page_data(self, data):
        pages = [data[x:x+int(self.page_size)] for x in range(0, len(data), int(self.page_size))]

        if int(self.page_number) > len(pages):
            self.set_page(1)

        return pages[int(self.page_number)-1]

    def get_number_of_pages(self, data):
        if data is None: return 0
        
        pages = [data[x:x+int(self.page_size)] for x in range(0, len(data), int(self.page_size))]

        return len(pages)


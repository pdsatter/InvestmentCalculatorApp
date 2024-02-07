class CanvasDrawer():
    def __init__(self, canvas, width, height):
        self.canvas = canvas

        self.height = height
        self.width = width
    
    def clear(self):
        self.canvas.delete("all")

    def draw_years(self, years_data):
        self.clear()

        for year in years_data:
            self.draw_year(year, years_data)    

    def draw_year(self, year_data, years_data):
        height1 = year_data.finalContributedFunds
        height2 = year_data.finalInterestFunds

        y_max = self.calc_max_height(years_data)

        y1 = self.height - (self.calc_normalized_height(y_max, height1))
        y2 = self.height - (self.calc_normalized_height(y_max, height2) + self.calc_normalized_height(y_max, height1))

        width = self.calc_normalized_width(len(years_data))

        x1 = width * (year_data.year - 1)
        x2 = width * (year_data.year)

        self.draw_rectangle(x1,self.height,x2,y1)
        self.draw_rectangle(x1,y1,x2,y2, fill="green")
    
    def calc_normalized_width(self, number_of_rectangles, margin_right=0):
        rect_width = (self.width - margin_right) / (number_of_rectangles)
        return rect_width
    
    def calc_normalized_height(self, y_max, y, margin_top=10):
        if y_max == 0: return 0
        
        max_height = (y/y_max) * (self.height - margin_top)

        return max_height

    def calc_max_height(self, years_data):
        return years_data[-1].finalTotalFunds

    def draw_rectangle(self, x1, y1, x2, y2, outline="black", fill="blue"):
        return self.canvas.create_rectangle(x1, y1, x2, y2,
                                            outline = outline, fill = fill,
                                            width = 2)
                                            
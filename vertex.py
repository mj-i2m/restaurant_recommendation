class Restaurant:

    def __init__(self, name:str, location, cuisine: str, price_segment, rating: int, open=True):
        self.name = name
        self.location = location
        self.cuisine = cuisine
        self.price_segment = price_segment
        self.rating = rating
        self.open = open

    def get_distance(self, my_location):

        x1 = my_location[0]
        y1 = my_location[1]

        x2 = self.location[0]
        y2 = self.location[1]

        return abs(x1 - x2) + abs(y1 - y2) # manhattan distance because of grid-stlye map

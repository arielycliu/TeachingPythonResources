# Create your own Class
# For cards
# Attributes: Value (1-13), House(Clubs, Heart, Diamond, Spades)

# Use try and except to make sure that only valid values and houses are accepted
# when your creating your object
# Take up at 5:53

class cards(object):
    def __init__(self, value, house):
        # Make sure value is a number
        # Make sure value is 1-13
        try:
            v = int(value)
            if v < 1 or v > 13:
                raise ValueError
        except:
            print("Invalid value")
        else:
            self.value = value

        # Make sure house is clubs, diamonds, hearts, spade
        if house == "spades" or house == "diamonds" or house == "hearts" or house == "spades":
            self.house = house
        else:
            print("Invalid house")

cardN = cards(2, "not a house")




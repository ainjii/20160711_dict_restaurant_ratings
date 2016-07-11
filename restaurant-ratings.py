# your code goes here
import sys
from collections import OrderedDict

def rate_restaurants(filename):
    """Lists restaurant ratings.

    For example:
        >>> rate_restaurants("scores.txt")
        Andalu is rated at 3.
        Arinell's is rated at 4.
        Bay Blend Coffee and Tea is rated at 3.
        Casa Thai is rated at 2.
        Charanga is rated at 3.
        El Toro is rated at 5.
        Giordano Bros is rated at 2.
        Irma's Pampanga is rated at 5.
        Little Baobab is rated at 1.
        Pancho Villa is rated at 3.
        Taqueria Cancun is rated at 2.
        Urbun Burger is rated at 1.

    Prints restaurant data, alphabetically by name.
    """

    restaurant_dict = {}

    restaurant_file = open(filename)
    for line in restaurant_file:
        line = line.rstrip()
        restaurant_data = line.split(":")

        name = restaurant_data[0]
        rating = int(restaurant_data[1])
        restaurant_dict[name] = rating

    sorted_ratings = OrderedDict(sorted(restaurant_dict.items(), key=lambda restaurant: restaurant[0]))

    for restaurant, rating in sorted_ratings.iteritems():
        print "%s is rated at %d." % (restaurant, rating)

filename = sys.argv[1]
rate_restaurants(filename)

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"

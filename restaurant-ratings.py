# your code goes here
import sys
from collections import OrderedDict
from random import randint

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

    user_name = raw_input("Hello! What is your name? ")
    refresh_random = True

    while True:
        if refresh_random:
            random_number = randint(0,len(restaurant_dict.keys())-1)
            random_name = restaurant_dict.keys()[random_number]
            random_rating = restaurant_dict[random_name]

        print "The rating for the restaurant %s is %d." % (random_name, random_rating)
        
        try:
            new_rating = raw_input("%s, what should the restaurant's rating be? " % user_name)
            new_rating = int(new_rating)
            refresh_random = True
        except ValueError:
            if new_rating == "q":
                break
            else:
                print "You must enter a valid integer."
                refresh_random = False
                continue

        restaurant_dict[random_name] = new_rating

        sorted_ratings = OrderedDict(sorted(restaurant_dict.items(), key=lambda restaurant: restaurant[0]))

        for restaurant, rating in sorted_ratings.iteritems():
            print "%s is rated at %d." % (restaurant, rating)
    

filename = sys.argv[1]
rate_restaurants(filename)

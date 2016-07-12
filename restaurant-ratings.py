# your code goes here
import sys
from random import choice

def rate_restaurants(filename):
    """Lists restaurant ratings.

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
            random_name = choice(restaurant_dict.keys())
            random_rating = restaurant_dict[random_name]

        print "The rating for the restaurant %s is %d." % (random_name, random_rating)
        
        try:
            new_rating = raw_input("\n%s, what should the restaurant's rating be? (1-5) " % user_name)
            new_rating = int(new_rating)

        except ValueError:
            if new_rating == "q":
                break
            else:
                print "You must enter a valid integer."
                refresh_random = False
                continue

        if new_rating <= 5 and new_rating >=1:
            print "You have changed the restaurant's rating to %d." % new_rating
            refresh_random = True
        else:
            refresh_random = False
            print "The rating must be between 1 and 5."
            continue

        restaurant_dict[random_name] = new_rating

        sorted_ratings = sorted(restaurant_dict.items())

        for restaurant, rating in sorted_ratings:
            print "%s is rated at %d." % (restaurant, rating)
    

filename = sys.argv[1]
rate_restaurants(filename)

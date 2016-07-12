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

    refresh_random = True

    while True:
        if refresh_random:
            random_name = choice(restaurant_dict.keys())
            random_rating = restaurant_dict[random_name]


        new_rating = raw_input("What should the restaurant's rating be? (1-5) ")
        refresh_random = is_input_valid(new_rating)

        if is_input_valid(random_rating):
            new_rating = convert_to_int(new_rating)
            print "You have changed the restaurant's rating to %d." % new_rating
        else:
            continue


        print "The rating for the restaurant %s is %d." % (random_name, random_rating)
        
        restaurant_dict[random_name] = new_rating

        sorted_ratings = sorted(restaurant_dict.items())

        for restaurant, rating in sorted_ratings:
            print "%s is rated at %d." % (restaurant, rating)
    

def is_input_valid(new_rating):
    try:
        convert_to_int(new_rating)

    except ValueError:
        if new_rating == "q":
            break
        else:
            print "You must enter a valid integer."
            return False

    if not (new_rating <= 5 and new_rating >=1):
        print "The rating must be between 1 and 5."
        return False


def convert_to_int(new_rating):
    return int(new_rating)

filename = sys.argv[1]
rate_restaurants(filename)

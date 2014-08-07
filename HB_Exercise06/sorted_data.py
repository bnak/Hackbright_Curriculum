from sys import argv

script, filename = argv

def main():
    my_file = open(filename)

    ratings = {}
    
    for line in my_file:
        line = line.rstrip()
        key_value = line.split(':')

        key = key_value[0]
        value = key_value[1]
        ratings[key] = value

        print key_value, key, value

    print ratings
    print sorted(ratings.iteritems())

    # must make dictionary into iterable list of tuples in order to alphabetize key-value pairs
    for key,value in sorted(ratings.iteritems()):
        print "Resturant %s is rated at %s." % (key, value) 


if __name__ == '__main__':
    main()



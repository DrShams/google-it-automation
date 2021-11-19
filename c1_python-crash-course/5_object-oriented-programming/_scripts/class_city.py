# define a basic city class
class City:
    name = ""
    country = ""
    elevation = 0
    population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    highest_elevation = 0
    return_city = ""

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population > min_population:
        if highest_elevation < city1.elevation:
            highest_elevation = city1.elevation
            return_city = ("{}, {}".format(city1.name,city1.country))
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city2.population > min_population:
        if highest_elevation < city2.elevation:
            highest_elevation = city2.elevation
            return_city = ("{}, {}".format(city2.name,city2.country))
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population > min_population:
        if highest_elevation < city3.elevation:
            highest_elevation = city3.elevation
            return_city = ("{}, {}".format(city3.name,city3.country))

    #Format the return string
    if return_city != "":
        return return_city
    else:
        return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

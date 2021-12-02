'''

A country can be said as being big if it is:

Big in terms of population.
Big in terms of area.
Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

Population is greater than 250 million.
Area is larger than 3 million square km.
Also, create a method which compares a country's population density to another country object. Return a string in the following format:

{country} has a {smaller / larger} population density than {other_country}
Examples
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

australia.is_big ➞ True
andorra.is_big ➞ False
andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"
Notes
Population density is calculated by dividing the population by the area.
Area is given in square km.
The input will be in the format (name_of_country, population, size_in_km2), where name_of_country is a string and the other two inputs are integers.
'''

# class Country:
#     def __init__(self,name,population,area):
#         self.name = name
#         self.population = population
#         self.area = area
#         self.density = self.population/self.area
#         self.isBig = population>250*10**6 or area > 3 * 10**6
        

#     def c_pd(self,c_obj):
#         if




# obj1 = Country("India",168432,604651)
# obj2 = Country("Pakistan",58464365,245)


# obj1.c_pd(obj2)


class country:
    def __init__(self,name,population,area):
        self.name = name
        self.population = population
        self.area = area
        self.pd = self.population/self.area
        self.is_big = self.population > 3*10**6 or self.area > 250*10**6
       

    def compare(self,obj):
        if (self.pd > obj.pd):
            print(self.name+" has larger population density than "+obj.name)
        else:
            print(self.name+" has smaller population density than "+obj.name)

obj1 = country("India",12345678,12345)
ogj2 = country("pakistan",123456, 12345)

obj1.compare(ogj2)


'''
oops.py

'''

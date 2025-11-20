#{Key:Value}
#{Bug:"Definition"}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you casn easily call over and over again.",
    #"Loop": "The action of doing something over and over again."
}

#Retrieving items from dictionary
#print(programming_dictionary["Bug"])

#Adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Wipe an existing dictionary
#programming_dictionary = {}

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
#print(programming_dictionary)

#Loop
#for x in programming_dictionary:
    #print(x)
    #print(programming_dictionary[x])

#Nesting
capitals = {
    "Germany": "Berlin",
    "France": "Paris",
}

#Nesting a List in a dictionary & Dictionary in Dictionary
travel_log = {
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Munich"], "total_visits": 35},
    "France": {"cities_visited": ["Paris", "Strasbourg", "Dijon"], "total_visits": 12}
}

#["A", "B", ["C", "D"]]


#Nesting a distionary in a list
dictionaries = [
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Munich"], 
        "total_visits": 35
        },
    {
        "country": "France", 
        "cities_visited": ["Paris", "Strasbourg", "Dijon"], 
        "total_visits": 12
        }
]

#Similiar in Java to Local and Global Variable
#Scope: Metaphor: Apple-tree in your own Garde is only accesible through you & your family. Apple-tree out of your property is accesible to everyone walking past this tree.

#Local Scope: When creating a Variable/Function in another Function you can only access it inside this function
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#print(potion_strength) --> will give you an error

#Global Scope --> Difference to Local Scope is where you define your Variable/Function. In the following example the Variable is defined outside of the Function and therefore always accesible
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
#print(player_health) --> won't give you an error

#Block-Scope: There is no such thing in Python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) #possible --> when you create a function around this if statement, the print-statement wouldn't be valid any more

#Change of a Global Variable:
enemies = 1

def increase_enemies():
    global enemies #this allows the function to change a global variable -->it's taht complicated, bc you usually don't want to change a global variable
    enemies += 1 #won't be possible on it's own, while this creates a new variable inside the function
    print(f"enemies insiode function: {enemies}")

increase_enemies()
print(f"enemies outside function : {enemies}")

#Global Constants: Change naming convention and make global variables in Upper-Case and therefore you can avoid mistakes
PI = 3.14159
GOOGLE_URL = "https://www..."

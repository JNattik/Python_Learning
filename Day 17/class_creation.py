class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0 # -->all objects from this class have in terms of their followers, the value "0"
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1

    #pass #--> this keywoard skips the indention error

user_1 = User("001", "Justin")
user_2 = User("002", "Olivia")
#user_1.id = "001" --> that would be an attribute from an object of the class "User"

user_1.follow(user_2)
print(user_2.follower)
print(user_1.following)
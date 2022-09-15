class CD:

    def __init__(self, songwriter, tittle, songs):
        self.songwriter = songwriter
        self.tittle = tittle
        self.songs = songs

    def __str__(self):  #This special method helps us as class creators to devise the way in which we want our clustering to be displayed every time a method requires it.                                                          
        return f"Album: {self.tittle} by {self.songwriter}"

    def __len__(self):
        return self.songs

    def __del__(self):
        print ("CD has been deleted")


my_cd = CD("Pink Floyd", "The Wall", 24 )

print (my_cd)
print (len(my_cd))

del my_cd

# https://www.udemy.com/course/total-python/learn/lecture/32472402#learning-tools
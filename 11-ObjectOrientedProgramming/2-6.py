#Create a class that represents pieces of music. Define a class constructor that allows you to set the initial values of the music piece (artist, track title, album, year)
#  when the object is created. Complete the class with the __str__ method returning the song data as a string, in the format as below (4 lines).
#  Then, create two objects that represent two pieces of music and print their data. Sample result:

#Performer: Ed Sheeran
#Title:     Hearts Don't Break Around Here
#Album:     Divide
#Year:      2017

#Performer: Queen
#Title:     Bohemian Rhapsody
#Album:     A Night at the Opera
#Year:      1975


# class definition
class Song:
   def __init___(self,performer,title,album,year):
      self.performer = performer 
      self.title = title
      self.album = album
      self.year = year
   def __str__ (self):
      return f'Performer is {self.performer}\n Title is {self.title}\n Album is {self.album}\n Year is {self.year}'
      

# object creation
song1 = Song ('Ed Sheeran','Hearts Don\'t Break Around Here','Divide','2017')
song2 = Song ('Queen','Bohemian Rhapsody',' A Night at the Opera','1975')

## object usage
print(song1)
print(song2)
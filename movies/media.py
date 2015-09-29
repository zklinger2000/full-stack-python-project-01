import urllib
import webbrowser
import json

# Movie
class Movie():
    """ This class provides a way to store movie related information """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #def show_trailer(self):
        #webbrowser.open(self.trailer_youtube_url)

    def get_movie_info(self, movie_title):
        connection = urllib.urlopen("http://www.omdbapi.com/?t=" + movie_title +
                                    "&y=&plot=short&r=json")
        outputA = connection.read()
        #print(outputA)

        movie_info = json.loads(outputA)
        outputB = "Title: " + movie_info["Title"] + "\nYear: " + movie_info["Year"]
        connection.close()

        print(outputB)

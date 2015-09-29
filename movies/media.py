# preprocessor directives
import urllib
import json

#===============================================================================
# Movie
#-------------------------------------------------------------------------------
class Movie():
#===============================================================================
    """ This class provides a way to store movie related information """

    #===========================================================================
    # Constructor
    #---------------------------------------------------------------------------
    # movie_title     : The title of the movie to search for
    # trailer_youtube : URL to the trailer for the movie on Youtube
    #---------------------------------------------------------------------------
    def __init__(self, movie_title, trailer_youtube):
    #===========================================================================
        # Title passed in to constructor
        self.title = movie_title
        # Storyline recieved from OMDB
        self.storyline = self.get_movie_info(movie_title)["Plot"]
        # Poster recieved from OMDB
        self.poster_image_url = self.get_movie_info(movie_title)["Poster"]
        # Year recieved from OMDB
        self.year = self.get_movie_info(movie_title)["Year"]
        # Youtube URL passed in to constructor
        self.trailer_youtube_url = trailer_youtube

    #===========================================================================
    # Get Movie information from www.omdbapi.com
    #---------------------------------------------------------------------------
    # movie_title : The title of the movie to search for
    #---------------------------------------------------------------------------
    def get_movie_info(self, movie_title):
    #===========================================================================
        # request JSON data for Movie
        connection = urllib.urlopen("http://www.omdbapi.com/?t=" + movie_title +
                                    "&y=&plot=short&r=json")
        # saving the response
        jsonData = connection.read()
        # parsing JSON data
        movie_info = json.loads(jsonData)
        # closing connection stream
        connection.close()
        # returning Movie data
        return movie_info

# preprocessor directives
import fresh_tomatoes
import media

# Movie objects
bladerunner = media.Movie("Blade Runner", "https://www.youtube.com/watch?v=4lW0F1sccqk")
mad_max = media.Movie("Mad Max: Fury Road", "https://www.youtube.com/watch?v=hEJnMQG9ev8")
point_break = media.Movie("Point Break", "https://www.youtube.com/watch?v=0hd49bnStgU")
brazil = media.Movie("Brazil", "https://www.youtube.com/watch?v=4Wh2b1eZFUM")
isteve = media.Movie("iSteve", "https://www.youtube.com/watch?v=0FChm-Ayj7g")

# an array of Movie objects
movies = [bladerunner, point_break, mad_max, brazil, isteve]

# calling fresh_tomatoes() to create page
fresh_tomatoes.open_movies_page(movies)

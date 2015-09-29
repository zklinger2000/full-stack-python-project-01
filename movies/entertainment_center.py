import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story about toys",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

#toy_story.show_trailer()

#movies = [toy_story]

#fresh_tomatoes.open_movies_page(movies)

toy_story.get_movie_info("School of Rock")

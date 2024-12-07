import imdb
from TTS.fast_df import speak

def fetch_movie_data(movie_name):
    try:
        # Initialize IMDb instance
        movies_db = imdb.IMDb()

        # Search for the movie
        speak(f"Searching for the movie: {movie_name}")
        movies = movies_db.search_movie(movie_name)

        # Check if any movies were found
        if not movies:
            speak(f"Sorry, I couldn't find any movies with the title '{movie_name}'.")
            return

        # Display all details for the first search result
        movie = movies[0]
        movie_id = movie.movieID
        movie_info = movies_db.get_movie(movie_id)

        # Retrieve and display available data
        title = movie_info.get('title', 'Unknown Title')
        year = movie_info.get('year', 'Unknown Year')
        rating = movie_info.get('rating', 'Rating not available')
        genres = ', '.join(movie_info.get('genres', []))
        directors = ', '.join(str(director) for director in movie_info.get('directors', []))
        cast = ', '.join(str(actor) for actor in movie_info.get('cast', [])[:10])
        plot = movie_info.get('plot outline', 'Plot summary not available')
        runtime = movie_info.get('runtimes', ['Unknown runtime'])[0]

        # Speak and print the data
        speak(f"Here is the information about {title}:")
        speak(f"Title: {title}")
        speak(f"Year: {year}")
        speak(f"IMDb Rating: {rating}")
        speak(f"Genres: {genres}")
        speak(f"Directed by: {directors}")
        speak(f"The main cast includes: {cast}")
        speak(f"Runtime is {runtime} minutes")
        speak(f"The plot summary is: {plot}")

    except Exception as e:
        print(f"An error occurred while fetching movie data: {e}")
        speak("I encountered an error while fetching the movie details.")

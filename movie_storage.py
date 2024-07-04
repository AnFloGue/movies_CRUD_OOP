import json


def load_data():
    """ loads the movie data from the 'data.json' movie_data_file.

    Returns:
        A dictionary containing movie data, and if the movie data is not
        found or is empty an empty dictionary.
    """
    
    try:
        with open('data.json', 'r') as movie_data_file:
            return json.load(movie_data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Could not load data. We default to an empty list.")
        return {}


def save_data(movies):
    """Saves movie data changes (add_movie, delete_movie_by_name, update_movie...), back to the 'data.json' file.

    Args:
        movies a dictionary containing movie data to save.
    """
    
    with open('data.json', 'w') as file:
        json.dump(movies, file, indent=4)


def movies_list_empty(movies):
    """Checks if the movie list is empty.

    Args:
        The dictionary containing movie data.

    Returns:
        A boolean value, True if the movie list is empty, False otherwise.
    """
    
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")
        return True
    return False


def add_movie(movies):
    """Adds a new movie with a rating, release year, and genre.

    Args:
        The dictionary containing movie data.

    Returns:
        The updated dictionary with the new movie added.
    """
    name = input("\nNew movie to add: ")
    if name.lower() == 'q':
        return movies
    
    while True:
        try:
            year = int(input("\nPlease, enter the release year as integers (e.g., 2022): "))
            break
        except ValueError:
            print("Invalid input. Please enter a year as an integer  (e.g., 2022): ")
    
    while True:
        try:
            rating = float(input("\nPlease, enter a value between 0-10: "))
            if 0 <= rating <= 10:
                break
            else:
                print("Invalid input. Please enter a value between 0 and 10: ")
        except ValueError:
            print("Invalid input. Please enter a numeric value: ")
    
    # we check the movie does not exist already in my data.json
    while name.lower() in movies.keys():
        print(f"\nMovie '{name}' already exists. ")
        name = input("Please enter a unique name: ")
    
    genre = input("\nEnter the movie genre (e.g., Comedy, Sci-Fi): ")
    
    # The new movie will be added as a new key-value pair to the movies dictionary
    movies[name] = {'rating': rating, 'year': year, 'genre': genre}
    
    save_data(movies)  # execute the save_data() to save data to the data.json file
    return movies


def delete_movie_by_name(movies):
    """Deletes a movie by substring.

    Args:
        The dictionary containing movie data.

    Returns:
        The updated dictionary once the movie is deleted.
    """
    
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")
        return movies
    
    name = input("\nPlease, enter name of the movie to delete: ").lower()
    
    for movie in movies.keys():
        if movie.lower() == name:
            del movies[movie]
            save_data(movies)
            print(f"\nMovie '{movie}' has been deleted.")
            return movies
    
    print(f"\nMovie not in the list")
    return movies


def update_movie(movies):
    """Updates the rating, release year, and genre (as an option) of a movie

    Args:
        The dictionary containing movie data.

    Returns:
         The updated dictionary once the movie updated .
    """
    
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")
        return movies
    
    name = input("\nEnter name of the movie to update: ")
    
    if name in movies:
        while True:
            try:
                rating = float(input("\nPlease, enter a rating value between 0-10: "))
                if 0 <= rating <= 10:
                    movies[name]['rating'] = rating
                    break
                else:
                    print("Invalid input. Please enter a value between 0 and 10: ")
            except ValueError:
                print("Invalid input. Please enter a numeric value: ")
        
        while True:
            try:
                year = int(input("Enter new year of release (e.g., 2022): "))
                movies[name]['year'] = year
                break
            except ValueError:
                print("Invalid input. Please enter a year as an integer (e.g., 2022): ")
        
        # we offer the option to update the genre if the user wants
        update_genre = input("\nWould you like to update the genre (y/n)? ").lower()
        if update_genre == 'y':
            genre = input("Enter the new genre: ")
            movies[name]['genre'] = genre
        
        save_data(movies)
        return movies
    
    print(f"\nMovie not in the list")
    return movies

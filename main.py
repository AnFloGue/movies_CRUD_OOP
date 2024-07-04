from random import choice
from movie_storage import load_data, save_data, add_movie, delete_movie_by_name, update_movie , movies_list_empty


def print_menu():
    print("\n")
    print("-------------------------")
    print(" MY MOVIES DATABASE")
    print("-------------------------")
    print(" MENU:")
    print("-------------------------")
    print("0. Exit")
    print("1. List movies")
    print("2. Add movie")
    print("3. Delete movie")
    print("4. Update movie")
    print("5. Stats")
    print("6. Random movie")
    print("7. Search movie")
    print("8. Movies sorted by rating")


def list_movies(movies):
    """Prints all movies: name rating and release year"""

    print("\n")
    
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")

    else:
        counter = 0
        for key, value in movies.items():
            counter += 1
            print(f"{counter} {key}, Rating: {value['rating']}, Year: {value['year']}")


def stats_movies(movies):
    """Calculates and displays the average, lowest, and highest movie ratings"""
    print("\n")
    
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")
    
    else:
        movies_values_list = []
        for movie in movies.values():
            movies_values_list.append(float(movie['rating']))
        
        best_rating = max(movies_values_list)
        worst_rating = min(movies_values_list)
        average = round(sum(movies_values_list) / len(movies_values_list), 2)
        
        print(f"Average rating: {average}\n")
        print(f"Lowest Rating: {worst_rating}\n")
        print(f"Best Rating: {best_rating}\n")


def random_movie(movies):
    """Picks a random movie and displays its name and rating"""
    print("\n")
    
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")
    
    else:
        
        random_movies = choice(list(movies.keys()))
        rating_random_movie = movies[random_movies]['rating']
        print(f"Random Movie: {random_movies}: {rating_random_movie}\n")


def search_movie_by_name(movies):
    """ The user searches for movies in the dict movies by name as a substring"""
    
    print("\n")
    
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")
    
    else:
        
        searched_movie = input(f"Please, enter at least part of the movie name to search: ").lower()
        
        found = False
        for key, value in movies.items():
            if searched_movie in key.lower():
                print(f"\n{key}, Rating: {value['rating']}, Year: {value['year']}")
                found = True
        
        if not found:
            print("That movie is not in the list.")


def sorted_movies_by_rating(movies):
    """Sorts movies in the dict movies by rating (highest to lowest)."""
    print("\n")
    
    if len(movies) == 0:
        print("----------------------")
        print("No movies in the list.")
        print("----------------------")
    
    else:
        
        movie_list_tuples = movies.items()
        
        def get_value(item):
            return float(item[1]['rating'])
        
        sorted_pairs = dict(sorted(movie_list_tuples, key=get_value, reverse=True))
        for k, v in sorted_pairs.items():
            print(f"{k}: {v['rating']}")


def menu(movies):
    """
    this is the menu for the user
    """
    
    menu_choice = -1  # so is not 0
    
    while menu_choice != 0:
        
        print_menu()
        
        menu_choice = int(input("\nEnter choice (0-8): "))
        
        if menu_choice == 1:
            list_movies(movies)
        
        elif menu_choice == 2:
            add_movie(movies)
        
        elif menu_choice == 3:
            delete_movie_by_name(movies)
        
        elif menu_choice == 4:
            update_movie(movies)
        
        elif menu_choice == 5:
            stats_movies(movies)
        
        elif menu_choice == 6:
            random_movie(movies)
        
        elif menu_choice == 7:
            search_movie_by_name(movies)
        
        elif menu_choice == 8:
            sorted_movies_by_rating(movies)
        
        elif menu_choice == 0:
            print("\nBye!")
            break


def main():
    movies = load_data()
    menu(movies)
    save_data(movies)


if __name__ == "__main__":
    main()

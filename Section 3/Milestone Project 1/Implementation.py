movies = []
movies.append({"title": "Heat", "director": "Dick Richardson", "year": "1986"})
movies.append({"title": "Heat", "director": "Michale Mann", "year": "1995"})
movies.append({"title": "Pulp Fiction", "director": "Quentin Tarantino", "year": "1994"})
movies.append({"title": "Leon: The Professional", "director": "Luc Besson", "year": "1994"})
movies.append({"title": "The Fifth Element", "director": "Luc Besson", "year": "1997"})

def add_movies():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie's year of release: ")
    
    movies.append({'title': title, 'director': director, 'year': year})
    cont = input("Add another? ('y' or 'n'): ")
    while cont != 'n':
        if cont == 'y':
            add_movies()
        else:
            print("Unknown command. Returning to main menu.")
    User_Menu() 

def list_movies():
    for movie in movies:
        print(f"{movie["title"]}, by {movie["director"]} in {movie["year"]}")
    User_Menu()

def print_movie(movie):
    print(f"'{movie["title"]}', directed by: {movie["director"]}, and released in {movie["year"]}")

def find_movies():
    choice = input("Please choose a property to search for, 't' for title, 'd' for director, 'y' for year of release, 'c' to cancel and return to main menu: ")
    while choice != 'c':
        if choice == 't':
            value = input("What title are you looking for?: ")
            count = 0
            for movie in movies:
                if movie["title"] == value:
                    count = count + 1
                    print_movie(movie)
            if count == 0:
                print("No movies with that title were found")
                User_Menu()
            User_Menu()
        elif choice == 'd':
            value = input("What director are you looking for?: ")
            count = 0
            for movie in movies:
                if movie["director"] == value:
                    count = count + 1
                    print_movie(movie)
            if count == 0:
                 print("No movies with that director were found")
                 User_Menu()
            User_Menu()
        elif choice == 'y':
            value = input("What year of release were you looking for?: ")
            count = 0
            for movie in movies:
                if movie["year"] == value:
                    count = count + 1 
                    print_movie(movie)
            if count == 0:
                print("No movies with that year of release were found")
                User_Menu()
            User_Menu()
        else:
            print("Unknown Command: Please try again")          
    User_Menu()

def User_Menu():
    MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movies()
            User_Menu()
        elif selection == "l":
            list_movies()
        elif selection == "f":
            find_movies()
        else:
            print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)

User_Menu()
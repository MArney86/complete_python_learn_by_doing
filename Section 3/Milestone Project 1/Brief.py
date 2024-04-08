'''add new movies to my collection so i can keep track of all my movies
   list all the movies in my collection so i can see what movies i already have
   find a movie by using the movie title so i can locate a specific movie easily when the collection grows
   implemention:
   decide where to store movies in code
      store in list
   decide what data we want to store for each movie
      store as dictionary with movie title, director, and release year
   show the user a menu and let them pick an option
   implement each requirement in tur each as a seperate function
   stop running the program when they type 'q' in the menu
'''
movies = []

title = input("Enter the movie title: ")
director = input("Enter the movie director: ")
year = input("Enter the movie release year")

movies.append({'title': title, 'director': director, 'year': year
})

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == 'a':
        pass
    elif selection == "l":
        pass
    elif selection == "f":
        pass
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)

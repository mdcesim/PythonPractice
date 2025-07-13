# MUHAMMED CESİM

def user_input():
    # Ask the user to input the movie name and validate it
    movie_name = input("Enter the movie name (Jurassic Park) or (The Lord Of The Rings): ")
    while movie_name not in movies:
        print(f"The movie name is wrong.. Try again: ")
        movie_name = input("Enter Movie Name: ")
    
    # Ask for the season choice and validate it
    season = input("Choose Season (Season 1) or (Season 2) or (Season 3): ")
    while season not in movies[movie_name]:
        print(f"Wrong season input.. Try again")
        season = input("Choose Season (Season 1) or (Season 2) or (Season 3): ")
        
    # Ask for the starting seat position (row and column)
    start_row = int(input("Enter row number (1-5): ")) -1
    start_col = int(input("Enter column number (1-5): ")) -1
    ticket_count = int(input("Enter the number of tickets you want to book: "))
    
    # Check for valid input range for rows, columns, and ticket count
    if start_row < 0 or start_row > 4 or start_col < 0 or start_col > 4 or ticket_count < 1:
        print(f"Invalid input. Please make sure row and column are between 1 and 5")
    else:
        # Proceed to book tickets and display seats
        multiple_tickets(movie_name, season, start_row, start_col, ticket_count)
        display_seats(movie_name, season)

# Define a dictionary to store seat availability for each movie and season
movies = {
    "Jurassic Park": {
        "Season 1" : [[0]*5 for _ in range(5)],
        "Season 2" : [[0]*5 for _ in range(5)],
        "Season 3" : [[0]*5 for _ in range(5)],
    },
    "The Lord Of The Rings": {
        "Season 1" : [[0]*5 for _ in range(5)],
        "Season 2" : [[0]*5 for _ in range(5)],
        "Season 3" : [[0]*5 for _ in range(5)],
    }
}

def display_seats(movie_name, season):
    # Print the seating arrangement for the chosen movie and season
    seats = movies[movie_name][season]
    print(f"seats for {movie_name} - {season} :")
    for row in seats:
        print("\n")
        print(" ".join(str(seat) for seat in row))
        print("\n")

def book_seat(movie_name, season, row, col):
    # Book a single seat for the given movie, season, row, and column
    seats = movies[movie_name][season]
    if seats[row][col] == 0:
        seats[row][col] = 1
        print(f"Row {row+1} Column {col+1} was booked successfully")
    else:
        print(f"The seat {row+1} - {col+1} is not available. \nFinding nearest seat...")
        nearest_seat = def_nearest_seat(seats, row, col)
        if nearest_seat:
            print(f"The nearest seat is {nearest_seat[0]+1} - {nearest_seat[1]+1}")
        else:
            print(f"Unfortunately, all seats are not available now..")

def def_nearest_seat(seats, row, col):
    # Search for the nearest available seat
    for r in range(len(seats)):
        for c in range(len(seats[r])):
            if seats[r][c] == 0:
                return(r,c)
    return None

def multiple_tickets(movie_name, season, start_row, start_col, ticket_count):
    # Try to book multiple tickets starting from the given row and column
    seats = movies[movie_name][season]
    available_seats = []

    for i in range(ticket_count):
        col = start_col + i
        if col < 5 and seats[start_row][col] == 0:
            available_seats.append((start_row, col))
        else:
            print(f"Some of chosen seats are not available..")
            suggust_seat(seats, ticket_count)
            return
    for row, col in available_seats:
        seats[row][col] = 1
    print(f"{ticket_count} tickets have successfully been booked.")

def suggust_seat(seats, ticket_count):
    # Suggest alternative seats if some of the chosen ones are not available
    print(f"Finding Alternative Seats..")
    alternative_seats = []
    for r in range(len(seats)):
        for c in range(len(seats[r])):
            if seats[r][c] == 0:
                alternative_seats.append(r,c)
                if len(alternative_seats) == ticket_count:
                    print(f"Available seats: ")
                    for row, col in alternative_seats:
                        print(f" Row {row+1} - Column {col+1}")
                    return
    print(f"No enough seats available.")

def main():
    # Main function that controls the booking process and repeats until user opts out
    while True:
        print(f"Welcome to the Movie Booking System ")
        user_input()
        another_booking = input("Do you want to do another booking? yes or no ").lower
        if another_booking != "yes":
            print(f"Thank you for using the Movie Booking System. GoodBye!")
            break
main()

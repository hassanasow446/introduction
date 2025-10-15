#Ask user to enter a username and how many books to borrow.
username = input("enter a username: ")
num_books = int(input("how many books to borrow? "))

fees = {
    "Novel": (2, 0.50),
    "Textbook": (4, 1),
    "Magazine": (1, 0.25),
    "Comic Book": (1.50, 0.75)
}


total_late_fees = 0
books_processed = 0
total_rental_cost = 0

#For each book, ask the user to enter the book title, book type (Novel, Textbook, Magazine or Comic Book), and the number of days they want to rent it.
for i in range(num_books):
    print(f"{i+1}. book")
    book_title = input("Enter the book title: ")
    book_type = input("Enter the book type (Novel, Textbook, Magazine, Comic Book): ")
    days_rented = int(input("Enter the number of days to rent the book: "))


    rental_fee, late_fee = fees[book_type]
    rental_cost = rental_fee * days_rented
    late_cost = 0

#Each book can be rented for a maximum of 14 days. If a book is kept beyond the due date, apply the appropriate late fee based on its type.
    if days_rented > 14:
        late_days = days_rented - 14
        late_cost = late_fee * late_days

# Calculate rental and late fees

    total_rental_cost += rental_cost
    total_late_fees += late_cost
    books_processed += 1

#After processing all rentals, display the username, the total rental cost, and the total late fees incurred.
    print(f"Book Title: {book_title}, Rental Cost: ${rental_cost:.2f}, Late Fee: ${late_cost:.2f}")

print(f"\nUsername: {username}")
print(f"Total Rental Cost: ${total_rental_cost:.2f}")
print(f"Total Late Fees: ${total_late_fees:.2f}")

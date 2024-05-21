# Question 2 Task 1

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

# Book a room 
def book_room(room_number, customer_name):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} has been booked by {customer_name}.")
        else:
            print(f"Room {room_number} is not available.")
    else:
        print(f"Room {room_number} does not exist.")

# Check-out a customer
def check_out_room(room_number):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "booked":
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(f"Room {room_number} is now available.")
        else:
            print(f"Room {room_number} is already available.")
    else:
        print(f"Room {room_number} does not exist.")

# Display the status of all rooms
def display_status():
    print("Hotel Room Status:")
    for room_number, details in hotel_rooms.items():
        status = details["status"]
        customer = details["customer"]
        print(f"Room {room_number}: Status: {status}, Customer: {customer}")

# Main function to interact with the system
def main():
    while True:
        print("\nHotel Room Booking Tracker")
        print("1. Book a room")
        print("2. Check-out a room")
        print("3. Display room status")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            room_number = input("Enter room number to book: ")
            customer_name = input("Enter customer name: ")
            book_room(room_number, customer_name)
        elif choice == "2":
            room_number = input("Enter room number to check-out: ")
            check_out_room(room_number)
        elif choice == "3":
            display_status()
        elif choice == "4":
            print("Thank you for using the Hotel Room Booking Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
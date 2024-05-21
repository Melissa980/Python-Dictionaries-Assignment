# Question 3 Task 1

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Open a new service ticket

def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {
            "Customer": customer_name,
            "Issue": issue_description,
            "Status": "open"
        }
        print(f"Ticket {ticket_id} has been opened for {customer_name}.")
    else:
        print(f"Ticket ID {ticket_id} already exists.")


# Update the status of an existing ticket

def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        if status in ["open", "closed"]:
            service_tickets[ticket_id]["Status"] = status
            print(f"Ticket {ticket_id} status has been updated to {status}.")
        else:
            print("Invalid status. Please enter 'open' or 'closed'.")
    else:
        print(f"Ticket ID {ticket_id} does not exist.")

# Display all tickets or filter by status

def display_tickets(filter_status=None):
    print("Customer Service Tickets:")
    for ticket_id, details in service_tickets.items():
        if filter_status is None or details["Status"] == filter_status:
            customer = details["Customer"]
            issue = details["Issue"]
            status = details["Status"]
            print(f"{ticket_id}: Customer: {customer}, Issue: {issue}, Status: {status}")

# Main function

def main():
    while True:
        print("\nCustomer Service Ticket Tracker")
        print("1. Open a new ticket")
        print("2. Update ticket status")
        print("3. Display all tickets")
        print("4. Display tickets by status")
        print("5. Quit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            ticket_id = input("Enter ticket ID: ")
            customer_name = input("Enter customer name: ")
            issue_description = input("Enter issue description: ")
            open_ticket(ticket_id, customer_name, issue_description)
        elif choice == "2":
            ticket_id = input("Enter ticket ID: ")
            status = input("Enter new status (open/closed): ")
            update_ticket_status(ticket_id, status)
        elif choice == "3":
            display_tickets()
        elif choice == "4":
            status = input("Enter status to filter by (open/closed): ")
            if status in ["open", "closed"]:
                display_tickets(filter_status=status)
            else:
                print("Invalid status. Please enter 'open' or 'closed'.")
        elif choice == "5":
            print("Thank you for using the Customer Service Ticket Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

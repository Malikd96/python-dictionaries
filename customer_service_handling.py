#Task 1: Customer Service Ticket Tracker - Demonstrate your ability to use nested collections and loops by 
# creating a system to track customer service tickets.
#Problem Statement: Develop a program that:

#Tracks customer service tickets, each with a unique ID, customer name, issue description, 
# and status (open/closed).
#Implement functions to:
# - Open a new service ticket.
# - Update the status of an existing ticket.
# - Display all tickets or filter by status.

# Initialize with some sample tickets and include functionality for additional ticket entry.

def add_ticket(tickets, ticket_id,customer,issue ):
    if ticket_id not in tickets:
        tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": []}
        print(f"Customer '{customer}' added with ID: {ticket_id} ")
    else:
        print(f"Customer with ID: {ticket_id} already exists. ")

def ticket_status(tickets, ticket_id, status):
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = status
        print(f"Customer ticket ID: {ticket_id} status updated to {status}. ")
    else:
        print(f"Customer Ticket ID {ticket_id} not found.")

def display_tickets(tickets):
    for ticket_id, customer in tickets.items():
        print(f"Ticket ID: '{ticket_id}', Customer: {customer['Customer']}, Issue: {customer['Issue']}', Status: '{customer['Status']}'")

# Example Ticket Structure
service_tickets = {
"Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
"Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

while True:
    print("\nCustomer Service Ticket System")
    print("1: Add service ticket\n2: Ticket Status Update\n3: Display Ticket\n4. Quit:")
    option = input("Choose option: ")
    if option == "1":
        ticket_id = input("Enter ticket ID: ")
        customer = input("Enter name: ")
        issue = input("Enter customer's issue: ")
        add_ticket(service_tickets, ticket_id, customer, issue)
    elif option == "2":
        ticket_id = input("Enter Ticket ID: ")
        status = input("Enter status. (open/closed): ")
        ticket_status(service_tickets, ticket_id, status)
    elif option == "3":
        display_tickets(service_tickets)
    elif option == "4":
        break
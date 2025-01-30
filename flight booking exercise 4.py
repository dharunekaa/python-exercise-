# Define a tuple with available flights (Flight Number, Destination, Price)
flights = (
    ("AI101", "New York", 450),
    ("BA202", "London", 350),
    ("CA303", "Paris", 300),
    ("DA404", "Tokyo", 600),
    ("EA505", "Sydney", 700),
)

# Display available flights
print("Available Flights:")
print("-" * 40)
for i, flight in enumerate(flights, start=1):
    print(f"{i}. Flight Number: {flight[0]}, Destination: {flight[1]}, Price: ${flight[2]}")

# Let the user book a flight
cart = []
while True:
    choice = input("\nEnter the flight number to book (or type 'done' to finish): ")
    flight_found = False
    for flight in flights:
        if choice.upper() == flight[0]:
            cart.append(flight)
            print(f"Flight to {flight[1]} has been booked.")
            flight_found = True
            break
    if choice.lower() == "done":
        break
    elif not flight_found:
        print("Invalid flight number. Please try again.")

# Display the booking summary
if cart:
    print("\nBooking Summary:")
    print("-" * 40)
    total_cost = 0
    for flight in cart:
        print(f"Flight Number: {flight[0]}, Destination: {flight[1]}, Price: ${flight[2]}")
        total_cost += flight[2]
    print("-" * 40)
    print(f"Total Price: ${total_cost}")
else:
    print("\nNo flights were booked.")

# Thank the user
print("\nThank you for using the Flight Booking System!")

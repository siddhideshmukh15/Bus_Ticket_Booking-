Seats= {}

while True:
    print("\n==== Bus Ticket Booking System ===")
    print("1.'Book Ticket' \n 2.'View Bookings' \n 3. 'Cancel Ticket'\n 4.'Available Seats'\n 5. 'Eit'")

    choice =input("Enter your choice:")

    if choice=="1":
        seat =input("Enter seat number:")
        if seat in Seats:
            print("Seat already booked!")
        else:
             name =input("Enter passenger name:")
             destination=input("Enter destination:")

             Seats[seat]=(name,destination)
             print("Ticket booked successfully!")

    elif choice=="2":
        if not Seats:
            print("No bookings found.")
        else:
            print("\n---Bookings---")
            for seat, details in Seats.items():
                print("Seat:",seat,
                      "passenger:",details[0],
                      "destination:",details[1])

    elif choice=="3":
        seat =input("Enter seat number to cancel:")

        if seat in Seats:
            del Seats[seat]
            print("Ticket cancelled!")

        else:
            print("Booking not found!")
    elif choice=="4":
        total_seats =20
        available =total_seats-len(Seats)
        print("Total seats:",total_seats)
        print("Available seats:",available)

    elif choice=="5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice!")
        
    
            
            
        

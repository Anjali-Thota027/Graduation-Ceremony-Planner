from planner import user  

def main():
    print("\nHello Welcome!")

    
    User = user("2025-26 Graduation", "Auditorium", "08 March", "\n ECE:10:00 AM\n CSE:11:00 AM\n MECH:12:00 PM\n EEE:2:00 PM", "XXX",
                 "1:00 PM at Dinning Hall", 25,"XYZ Catering", 450000)

    while True:
        user_type = int(input("\nAre you a student or a planner?\nIf student enter 1\nIf planner enter 2:\nPlease enter your choice: "))

        if user_type == 1:
            student_choice = input("Do you have a registration? (yes/no): ").lower()
            if student_choice == "yes":
                usn = input("Enter your USN: ")
                if User.is_registered(usn):
                    User.display_details()
                else:
                    print("USN not found. Please register.")
                    name = input("Enter your Name: ")
                    User.register_student(usn, name)
                    User.display_details()
            else:
                print("Please request you to register .")
                name = input("Enter your Name: ")
                usn = input("Enter your USN: ")
                User.register_student(usn, name)
                User.display_details()
                
        elif user_type == 2:
            User.display_details1()
            changes=int(input("\nSelect option\n1.Modify Details\n2.Delete Details\n3.None\nEnter the option:"))
            
            if changes==1:
                
                Password = 1234
                password = input("Enter password:")
                if password == Password:
                        while True:
                            update_detail(User)
                            more_updates = input("\nDo you want to update more details? (yes/no):\n ").lower()
                            if more_updates != 'yes':
                                break
                            

                        print("\nUpdated  Details Successfully:")
                        User.display_details1()
                        
                else:
                    print("Access denied")
               
            elif changes==2:
                delete=int(input("\nDo you want to delete any details? \nIf yes enter 1\nIf no enter 2:\n "))
                if delete==1:
                    lock=1234
                    Lock=input("Enter password:")
                    if Lock==lock:
                        while True:
                            delete_details(User)
                            more_deletes=input("\nDo you want to delete more details? (yes/no):\n").lower()
                            if more_deletes=="yes":
                                continue
                            print("\n Entered Details are deleted successfully.")
                            User.display_details1()
                            break
  
                    else:
                        print("Wrong password")
                else:
                   print("Thank you")
            elif changes==3:
                print("\nOK.Thank you.")
            else:
                print("\nNot found.")
        else:
            print("Invalid User")

        exit_option = int(input("\nEnter 0 to quit or press 1 to continue: "))
        if exit_option == 0:
            print("Thank you")
            break

def update_detail(user_details):
    print("\nUpdate event Details:")
    choice = input("Which detail would you like to modify? (Event_name/venue/Date/guest/time/vendor/budget):\n ").lower()
    if choice == 'name':
        user_details.set_name(input("Enter new Event name: "))
    elif choice == 'venue':
        user_details.set_venue(input("Enter new venue: "))
    elif choice == 'date':
        user_details.set_date(input("Enter new date: "))
    elif choice == 'time':
        user_details.set_timings(int(input("Enter new timings: ")))
    elif choice == 'vendor':
        user_details.set_vendor(input("Enter new vendor details: "))
    elif choice == 'budget':
        user_details.set_budget(int(input("Enter new budget: ")))
    elif choice == 'guest':
        user_details.set_guest(int(input("Enter new Guest name: ")))
    else:
        print("\nInvalid choice!")
        
def delete_details(user_details):
    print("\nDelete details")
    delete=input("Which detail would you like to delete?\n(Event_name/venue/Date/time/guest/vendor/budget):\n ").lower()
    if delete=="name":
        user_details.set_name(" ")
        print("\nDeleted successfully.")
    elif delete=="venue":
        user_details.set_venue(" ")
        print("\nvenue deleted successfully.")
    elif delete=="date":
        user_details.set_date(" ")
        print("\ndate deleted successfully")
    elif delete=="time":
        user_details.set_timings(" ")
        print("\nTimings deleted successfully.")
    elif delete=="guest":
        user_details.set_guest(" ")
        print("\nGuest details deleted successfully.")
    elif delete=="vendor":
        user_details.set_vendor(" ")
        print("\n vendor deleted successfully.")
    elif delete=="budget":
        user_details.set_budget(0)
        print("\nBudget deleted successfully.")
    else:
        print("\nNo such detail")
    
    
if __name__ == "__main__":
    main()
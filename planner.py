from  AbstractPlanner import AbstractPlanner

class user(AbstractPlanner):
    
    def display_details1(self):
        print("\nGraduation Details:")
        print(self.name)
        print("\nVenue:",self.venue)
        print("Date:",self.date)
        print("Timings:",self.timings)
        print("Cheif Guest:",self.guest)
        print("Lunch:",self.lunch)
        print("\nEvent details")
        
        print("\nVendor:",self.vendor)
        print("Attendees:",self.attendees)
        print("Budget:",self.budget)
        
        if self.attendees > 0:
           print("\nRegistered Students:")
           for usn, name in self.students_data.items():
               print(f"USN: {usn}, Name: {name}")
        else:
           print("\nNo students registered yet.")
           
    

            
    def display_details(self):
        print("\nGraduation Details:")
        print(self.name)
        print("Venue:",self.venue)
        print("Date:",self.date)
        print("Timings:",self.timings)
        print("Chief Guest:",self.guest)
        print("Lunch:",self.lunch)
        
        
    def register_student(self, usn, name):
        if usn in self.students_data:
            print("\nStudent already registered.")   
        else:
            self.students_data[usn] = name
            self.attendees += 1
            print(f"\nStudent {name} with USN {usn} has been successfully registered.")   
        
    def is_registered(self, usn):
        return usn in self.students_data

    def set_name(self,new_name):
        self.name=new_name
        
    def set_venue(self,new_venue):
        self.venue=new_venue
        
    def set_date(self,new_date):
        self.date=new_date
        
    def set_timings(self,new_time):
        self.timings=new_time
        
    def set_guest(self,new_guest):
        self.guest=new_guest
        
    def set_lunch(self,new_lunch):
        self.lunch=new_lunch
        
    def set_vendor(self,new_vendor):
        self.vendor=new_vendor
        
    def set_attendees(self,new_attendees):
        self.attendees=new_attendees
        
    def set_budget(self,new_budget):
        self.budget=new_budget
        
    def add_students(self,students):
         self.new_students.append(students)
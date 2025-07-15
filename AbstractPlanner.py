from abc import ABC, abstractmethod

class AbstractPlanner(ABC):
    def __init__(self,event_name,venue,date,timings,guest,lunch,attendees,vendor,budget):
        self.name=event_name
        self.venue=venue
        self.date=date
        self.timings=timings
        self.guest=guest
        self.lunch=lunch
        self.attendees=attendees
        self.vendor=vendor
        self.budget=budget
        self.students_data={}
        
      

    @abstractmethod
    def display_details(self):
        pass
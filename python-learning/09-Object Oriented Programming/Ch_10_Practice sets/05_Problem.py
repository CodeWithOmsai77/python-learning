# Write a Class 'Train' which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(f"Ticket is booled in train No: {self.trainNo} from {fro} to {to}")
        
    def getstatus(self,):
        print(f"train No: {self.trainNo} is running on time")
        
    def getfare(self,  fro, to):
        print(f"Ticket fare in train No: {self.trainNo} from {fro} to {to} is {randint(252, 7848)}")
        
t = train (55542)
t.book("mumbai", "Delhi")
t.getstatus()
t.getfare("mumbai", "Delhi")
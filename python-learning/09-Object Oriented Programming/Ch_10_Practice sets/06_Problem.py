# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

#        -> No, the output doesnot change if you change the self from slf

from random import randint

class train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        
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
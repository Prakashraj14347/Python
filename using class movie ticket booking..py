import sys

class ParentClass:
    def __init__(self,username,password):
       self.username = username
       self.password = password 
    
    def loginCheck(self):
        if (self.username=="HAPPY" and self.password=="12345"):
            print("Login Successfull")
        else:
            print("Invalid Login")
            sys.exit()
            
class Childclass(ParentClass):
    def __init__(self, username, password):
        ParentClass.__init__(self,username, password)
        
    def movieSelection(self):
        print("\nWelcome to Movie Ticket Booking website")
        print("\nSelect an movie")
        movieList =	{
            "1":"SPIDERMAN",
            "2":"HULK",
            "3":"AVENGERS",
            "4":"IRONMAN"
            }
        for i in movieList:
            print(i,"-",movieList[i])
        self.movieNum = input()
        self.selectedMovie = movieList[self.movieNum]
        
        screenList =	{
            "1":"Screen 1",
            "2":"Screen 2",
            "3":"Screen 3",
            "4":"Screen 4"
            }
        self.selectedScreen = screenList[self.movieNum]
        
        return self.selectedMovie,self.selectedScreen
        
        
        
    def DisplayshowTimeSelection(self):
        
        print("\nSelect a show timing (1-4)\n")
        if (self.movieNum == "1" or self.movieNum == "3"):
            slotTime = {
                "1":"10:00 ",
                "2":"13:00 ",
                "3":"16:00 ",
                "4":"21:00 ",
                }
            for i in slotTime:
                print(i,"-",slotTime[i])
            
        else:
            slotTime = {
                "1":"11:00 ",
                "2":"14:00 ",
                "3":"17:00 ",
                "4":"22:00 ",
                }
            for i in slotTime:
                print(i,"-",slotTime[i])

        self.slotSelection = input()
        self.selectedSlot = slotTime[self.slotSelection]
        return self.selectedSlot
        
    def DisplayTicketSelection(self):
        print("\n Enter the number of tickets to be booked")
        self.ticketSelection = int(input())
        if (self.ticketSelection > 15):
            print("BOOK UPTO 15/LOGIN")
        else:
            return self.ticketSelection
        
print("\nEnter the username")
username = input()
print("\nEnter the password")
password = input()

c1 = Childclass(username, password)  
c1.loginCheck()
c1.movieSelection()
c1.DisplayshowTimeSelection()
c1.DisplayTicketSelection()

movie = c1.selectedMovie
screen = c1.selectedScreen
time = c1.selectedSlot
tickets = c1.ticketSelection

print(f"-\nBooking Confirmed\nMovie - {movie}\nScreen - {screen}\nShow Time - {time}\nTickets - {tickets}\n-")
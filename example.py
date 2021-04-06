class Flight:
    Flightid=1
    def __init__(self,source,destination,duration):
        self.source=source
        self.destination=destination
        self.duration=duration
        self.passengers=[]
        self.id=Flightid

    def display(self):
        print(self.source)
        print(self.destination)
        print(self.duration)
        for i in self.passengers:
            print(i.name)

    def delay(self,hours):
        self.duration=self.duration + hours

    def add(self,name):
        self.passengers.append(name)
        name.n=self.Flightid


class Passenger:
    
    def __init__(self,passengers_name):
        self.name=passengers_name
        
    
def main():
    s=Flight("New York","Paris",550)
    s.display()
    s.delay(4)
    s.display()
    g=Passenger("sam")
    h=Passenger("Vishal")
    s.add(g)
    s.add(h)
    s.display()

    

if __name__=="__main__":
    main()
        
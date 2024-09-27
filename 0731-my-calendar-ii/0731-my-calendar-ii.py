class MyCalendarTwo:

    def __init__(self):
        self.allEvents = []
        self.doubleBooked = []

    def book(self, start: int, end: int) -> bool:
        
        for eachEvent in self.doubleBooked:
            prevStart = eachEvent[0]
            prevEnd = eachEvent[1]
            
            if prevEnd < start or prevStart > end - 1:
                continue
            return False
        
        for eachEvent in self.allEvents:
            prevStart = eachEvent[0]
            prevEnd = eachEvent[1]
            
            if prevEnd < start or prevStart > end - 1:
                continue
            self.doubleBooked.append([max(prevStart, start), min(end - 1, prevEnd)])
        
        self.allEvents.append([start, end - 1])
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
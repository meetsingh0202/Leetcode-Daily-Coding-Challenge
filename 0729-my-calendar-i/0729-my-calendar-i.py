class MyCalendar:

    def __init__(self):
        self.allEvents = []
        

    def book(self, start: int, end: int) -> bool:
        for eachEvent in self.allEvents:
            prevStart = eachEvent[0]
            prevEnd = eachEvent[1]
            
            if prevEnd < start or prevStart > end - 1:
                continue
            return False
        
        self.allEvents.append([start, end - 1])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
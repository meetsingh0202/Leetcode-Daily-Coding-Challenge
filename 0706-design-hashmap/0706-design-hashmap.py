class MyHashMap:
    def __init__(self):
        self.MyHashMap=[-1]*10000000
        

    def put(self, key: int, value: int) -> None:
        self.MyHashMap[key]=value
        

    def get(self, key: int) -> int:
        if self.MyHashMap[key]!=-1:
            return self.MyHashMap[key]
        return -1
        

    def remove(self, key: int) -> None:
        self.MyHashMap[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
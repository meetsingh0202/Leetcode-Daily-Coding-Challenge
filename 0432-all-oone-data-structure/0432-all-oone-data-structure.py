class AllOne:

    def __init__(self):
        self.data = {}
        self.head = {'prev': None, 'count': 0}
        self.tail = {'prev': self.head, 'next': None, 'count': float("inf")}
        self.head['next'] = self.tail
        
    def removeNode(self, node):
        node['prev']['next'] = node['next']
        node['next']['prev'] = node['prev']
    
    def insertNode(self, count, key, cur):
        prev = cur['prev']
        while cur and cur['count'] < count:
            prev = cur
            cur = cur['next']
        
        node = {'key': key, 'prev': prev, 'next': cur, 'count': count}
        prev['next'] = node
        cur['prev'] = node
        return node


    def inc(self, key: str) -> None:
        cur = self.head
        if key not in self.data:
            self.data[key] = [1, None]
        else:
            cur = self.data[key][1]['prev']
            self.removeNode(self.data[key][1])

            self.data[key][0] += 1

        node = self.insertNode(self.data[key][0], key, cur)
        self.data[key][1] = node


    def dec(self, key: str) -> None:
        if self.data[key][0] == 1:
            self.removeNode(self.data[key][1])
            del self.data[key]
        else:
            cur = self.data[key][1]['prev']
            self.removeNode(self.data[key][1])

            self.data[key][0] -= 1
            node = self.insertNode(self.data[key][0], key, cur)
            self.data[key][1] = node

    def getMaxKey(self) -> str:
        if 'key' not in self.tail['prev']:
            return ""
        
        return self.tail['prev']['key']
        

    def getMinKey(self) -> str:
        if 'key' not in self.head['next']:
            return ""
        
        return self.head['next']['key']



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
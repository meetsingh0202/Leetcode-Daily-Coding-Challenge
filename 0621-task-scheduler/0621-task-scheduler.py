class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict1={}
        for i in tasks:
            dict1[i]=1+dict1.get(i,0)
        
        heap=[]
        
        for key,value in dict1.items():
            heappush(heap,-value)
        
        time=0
        queue=deque()
        
        while heap or queue:
            time+=1
            
            if heap:
                temp=heappop(heap)
                temp+=1
                if temp:
                    queue.append((temp,time+n))
            
            if queue and queue[0][1]==time:
                temp=queue.popleft()[0]
                heappush(heap,temp)
        
        return time
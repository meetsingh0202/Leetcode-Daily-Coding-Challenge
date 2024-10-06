class Solution:
    def areSentencesSimilar(self, sentence1, sentence2):
        
        lst1 = sentence1.split()
        lst2 = sentence2.split()

        while(lst1 and lst2 and lst1[0]==lst2[0]):
            lst1.pop(0)
            lst2.pop(0)
        
        while(lst1 and lst2 and lst1[-1]==lst2[-1]):
            lst1.pop()
            lst2.pop()
        
        return not lst1 or not lst2

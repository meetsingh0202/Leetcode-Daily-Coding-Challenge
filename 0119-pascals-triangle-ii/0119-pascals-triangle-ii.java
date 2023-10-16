class Solution {
    public List<Integer> getRow(int rowIndex) {
        
        List<List<Integer>> result=new ArrayList();
        List<Integer> r1=new ArrayList<>();
        r1.add(1);
        result.add(r1);
        
        for(int i=1;i<rowIndex+1;i++)
        {
            List<Integer> prev=result.get(i-1);
            List<Integer> currentrow=new ArrayList<>();
            
            currentrow.add(1);
            for(int j=1;j<i;j++)
            {
                currentrow.add(prev.get(j-1)+prev.get(j));
            }
            currentrow.add(1);
            result.add(currentrow);
        }
        
        return result.get(rowIndex);        
        
    }
}
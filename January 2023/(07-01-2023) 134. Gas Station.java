class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        long fuel = 0; 
        int pos = 0;        
        long fuelSum = 0;
        long gasSum = 0;
        for (int i = 0; i < gas.length; i++)
        {
            fuelSum += cost[i];
            gasSum += gas[i];
            int currentFuel = gas[i];
            int distance = cost[i];
            int difference = currentFuel - distance;
            fuel = fuel + difference;
            if(fuel < 0)
            {
                pos = i + 1;
                fuel = 0;
            }         
            // System.out.println(fuel);
        }
        if (gasSum - fuelSum < 0){
            return -1;
        }
        return pos;
    }
}

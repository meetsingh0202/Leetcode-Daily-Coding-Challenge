class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.foodRating = dict()
        self.foodCuisine = dict()
        self.HashMap = defaultdict(list)
        
        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.foodRating[food] = rating
            self.foodCuisine[food] = cuisine
            heappush(self.HashMap[cuisine], (-rating, food))
        
        # print(self.HashMap)
        
    def changeRating(self, food: str, newRating: int) -> None:
        self.foodRating[food] = newRating
        tempCuisine = self.foodCuisine[food]
        heappush(self.HashMap[tempCuisine], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        
        while self.HashMap[cuisine] and self.HashMap[cuisine][0][0] != -1 * self.foodRating[self.HashMap[cuisine][0][1]]:
            heappop(self.HashMap[cuisine])
        
        return self.HashMap[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
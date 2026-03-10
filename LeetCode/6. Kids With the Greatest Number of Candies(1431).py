class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new=[]
        max_=candies[0]
        for i in candies:
            if i>max_:
                max_=i
        
        for i in candies:
            if i+extraCandies>=max_:
                new.append(True)
            else:
                new.append(False)
        return new

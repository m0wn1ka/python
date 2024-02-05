class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #go over a for loop
        #add extra candies to loop var
        #find the max value out of rest of the candies arrya
        #if both are equal set it to ture
        result=[]
        for i in candies:
            x=i+extraCandies
            temp=candies.copy()
            temp.remove(i)
            y=max(temp)
            print("x==y",x,y)
            if (y<=x):
                result.append(True)
            else:
                result.append(False)
        return result

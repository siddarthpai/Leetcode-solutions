class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() #to keep 2 pointers, one at lightest and one at heaviest
        boats = 0 #no of boats
        left =0 #left pointer(smallest values)
        right = len(people)-1 # right pointer (largest values)

        while(left<=right) :
            remain  = limit - people[right]
            right -=1 
            boats +=1
            if left<=right and remain >= people[left]:
                left +=1
        return boats

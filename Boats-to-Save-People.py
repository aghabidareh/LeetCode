class Solution:
    def numRescueBoats(self , people , limit):
        people.sort()
        smallest = 0
        biggest = len(people)-1
        boats = 0
        while biggest >= smallest:
            if people[biggest] + people[smallest] <= limit:
                biggest -= 1
                smallest += 1
            else:
                biggest -= 1
            boats += 1
        return boats
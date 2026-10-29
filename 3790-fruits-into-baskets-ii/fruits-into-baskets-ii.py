class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        k=len(fruits)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    k=k-1
                    baskets[j]=0
                    break
        return k
                      

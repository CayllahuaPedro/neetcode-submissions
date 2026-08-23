class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        scand = sorted(candidates)
        n = len(scand)
        def findCombinations(start: int, total: int, curr: List[int]):
            if total == target:
                res.append(curr)
                return
            if start >= n:
                return
            print("start ", scand[start], total)
            for j in range(start,n):
                newSum = total + scand[j]
                if newSum > target:
                    continue
                if j > start and scand[j] == scand[j-1]:
                    continue 
                newCurr = [*curr, scand[j]]
                findCombinations(j +1,newSum, newCurr)
            print("fin, suma: ", total)
            return 
        findCombinations(0, 0, [])
        return res
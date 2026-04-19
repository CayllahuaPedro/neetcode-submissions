class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_waiting = []
        n = len(temperatures)
        results= [0]* n;
        for i in range(n):
            current_temp = temperatures[i]
            # el stack representa los indices que estan pendiente, sus valores estan 
            # ordenados de menor a mayor , con el top siendo el mayor
            while days_waiting and current_temp > temperatures[days_waiting[-1]]:
                idx = days_waiting.pop()
                results[idx] = i - idx;
            days_waiting.append(i)
        return results;
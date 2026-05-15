from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        items = self.store[key]
        l, r = 0, len(items) -1
        found = -1
        while l <= r:
            mid = (l+r) // 2
            if items[mid][1] <= timestamp:
                #mid es un candidate valido entonces busco
                #candidate mas grandes a la derecha
                found = mid 
                l = mid +1
            else: 
                r = mid -1
        return "" if found == -1 else items[found][0]
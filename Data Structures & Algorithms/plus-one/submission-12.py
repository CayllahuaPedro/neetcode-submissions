class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index= len(digits)-1
        while index >= 0:
            if digits[index] == 9:
                digits[index]=0
            else:
                digits[index]+= 1
                break;
            index -=1
        if digits[0] == 0:
            return [1] + digits
        else:
            return digits


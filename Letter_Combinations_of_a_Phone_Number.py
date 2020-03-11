class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combine(pres, dict, digit):
            result = []
            for pre in pres:
                for letter in mapping_digit[digit]:
                    result.append(pre+letter)
            
            return result
    
        if digits is "":
            return []
        
        mapping_digit = {'2': ["a", "b", "c"], '3': ["d", "e", "f"], '4': ["g", "h", "i"], '5': ["j", "k", "l"], '6':["m", "n", "o"], '7': ["p", "q", "r", "s"], '8': ["t", "u", "v"], '9': ["w", "x", "y", "z"]}
        
        answer=['']
        
        for digit in digits:
            answer = combine(answer, mapping_digit, digit)
            
        return answer
        

            
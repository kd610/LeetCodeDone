class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return False
        
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for b in s:
            if b in mapping: #Find value in the key og hashmap
                top_element = stack.pop() if stack else "#"
            
                if mapping[b] != top_element:
                    return False
            else:
                stack.append(b)
                
        
        return not stack #If stack is empty, return true. Otherwise, return false

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().isValid(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
#Solution function is written by kd610
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        val = x
        reverse = 0
        if x < 0:
            return False
        else:
            while val > 0:
                reminder = val % 10
                reverse = (reverse*10) + reminder
                val //= 10
            
            if x == reverse:
                return True
            else:
                return False

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
            x = int(line);
            
            ret = Solution().isPalindrome(x)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
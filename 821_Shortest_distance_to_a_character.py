class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        result = [0] * n

        last_include = - 4 ** 10 + 1 

        for i in range(n):
            if s[i] == c:
                last_include = i
            result[i] = i - last_include


        last_include =  4 ** 10 + 1 

        for i in range(n-1, -1, -1):
            if s[i] == c:
                last_include = i
            result[i] = min(last_include - i, result[i])

        return result



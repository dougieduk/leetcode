class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([(n,0)])

        while q: 
            num, count = q.popleft() 
            
            for num_to_subt in range(floor(sqrt(num)), -1, -1):
                new_num = num - num_to_subt*num_to_subt 
                if new_num == 0 : 
                    return count+1
                elif new_num < 0 : 
                    continue 
                else: 
                    q.append((new_num, count+1))
        
                
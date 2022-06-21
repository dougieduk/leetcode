class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadset = set(deadends)
        q = deque([('0000',0)])
        v = set('0000') 

        while q: 
            curr_num, count = q.popleft() 
            if curr_num in deadset: 
                continue
            elif curr_num == target : 
                return count 
            for digit in range(4):
                for plusminus in [-1,1]:
                    new_digit = (int(curr_num[digit]) + plusminus)%10
                    new_num = curr_num[:digit] + str(new_digit) + curr_num[digit+1:]
                    if new_num not in v: 
                        q.append((new_num,count+1))
                        v.add(new_num)
        return -1 
                
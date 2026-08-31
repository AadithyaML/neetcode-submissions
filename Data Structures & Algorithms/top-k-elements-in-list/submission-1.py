class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        un = defaultdict(int)
        for i in nums :
            un[i]+=1
        key = list(un.keys())
        v = list(un.values())
        fin = []
        while len(fin)<k :
            maxim = v[0]
            index = 0
            for i in range(len(v)):

                if maxim < v[i]:
                    maxim = v[i]
                    index = i 
            v.pop(index)
            fin.append(key.pop(index))
        return fin


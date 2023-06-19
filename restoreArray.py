# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        restore_dict = {}
        res = []
        s = set(element for item in adjacentPairs for element in item)
        for u,v in adjacentPairs:
            if u in restore_dict:
                restore_dict[u].add(v)
                s.remove(u)
            else:
                restore_dict[u] = {v}

            if v in restore_dict:
                restore_dict[v].add(u)
                s.remove(v)
            else:
                restore_dict[v] = {u}
        
        item = s.pop()
        while len(restore_dict) > 0:
            res.append(item)
            temp = item
            if len(restore_dict[item]) > 0:
                item = restore_dict[item].pop()
                restore_dict[item].remove(temp)
            restore_dict.pop(temp)


        return res

//https://leetcode.com/problems/brick-wall/submissions/
// Easy solution using hash-map

class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        map <int,int> m;
        map <int,int>::iterator itr;
        int minBricks = wall.size();
        int sumSoFar = 0;
        int sumOfRow = 0;
        for (vector<int> v : wall){
           for (int x: v) {
               sumSoFar += x;
               m[sumSoFar] += 1;
           }
            sumOfRow  = sumSoFar;
            sumSoFar = 0;
        }
        m[sumOfRow] = 0;
        for (itr = m.begin(); itr != m.end(); itr++) {
            if ((wall.size() - itr->second) < minBricks) {
                minBricks = (wall.size() - itr->second);
            }
        }
        return minBricks;
    }
};

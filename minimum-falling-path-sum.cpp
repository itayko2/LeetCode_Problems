//https://leetcode.com/problems/minimum-falling-path-sum/submissions/
//Solution using dynnamic programming
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int result = INT_MAX;
        vector<vector<int>> table(m, vector<int> (n, 0));
        table[0] = matrix[0];
        for (int i = 1; i < m ; i++){
            for (int j = 0; j < n ; j++){
                if (j == 0){
                    table[i][j] = min(table[i - 1][0],table[i - 1][1]) + matrix[i][j];
                }
                else if(j == n - 1){
                    table[i][j] = min(table[i - 1][n - 1],table[i - 1][n - 2]) + matrix[i][j];
                }
                else{
                    table[i][j] = min(min(table[i - 1][j - 1],table[i - 1][j]),table[i - 1][j + 1]) + matrix[i][j];
                }
            }
        }
        for (int x: table[m - 1]){
            result = min(x,result);
        }
        return result;
    }
};

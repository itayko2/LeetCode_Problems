//https://leetcode.com/problems/arithmetic-slices/submissions/
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int result = 0;
        int c = 0;
        if (nums.size() < 3) {
            return 0;
            }
        for (int i = 0; i < nums.size() - 2; i++) {
            if((nums[i+2] - nums[i+1]) == (nums[i+1]-nums[i])){
                c++;
            }
            else{
                result += c * (c + 1) / 2;
                c = 0;
            }
        }
        result += c * (c + 1) / 2;
        return result;
    }
};

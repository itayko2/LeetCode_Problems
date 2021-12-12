https://leetcode.com/problems/remove-element/solution/
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int result = nums.size();
        int c = nums.size() - 1;
        for (int i = 0 ; i < nums.size() ; i++) {
            if (nums[i] == val){
                nums[i] = -1;
                swap(nums[i],nums[c]);
                c--;
                i--;
            }
        }
        return c + 1;
    }
};

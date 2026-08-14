class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i1 , j1;
        for(int i=0 ; i < nums.size() ; i++){
            for(int j = i+1 ; j< nums.size() ; j++){
                if(nums[i]+nums[j] == target){
                   i1 =i;
                   j1 =j;
                   return {i1, j1};
                }
            }
        }
    }
};

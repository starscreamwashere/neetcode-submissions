class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int complement;
        int i,j;
        for(i=0;i<nums.size();i++){
            complement=target-nums[i];
            for(j=i+1;j<nums.size();j++){
                if (nums[j]==complement){
                    return {i,j};
                }
            }
        }
        return {};
    }
};

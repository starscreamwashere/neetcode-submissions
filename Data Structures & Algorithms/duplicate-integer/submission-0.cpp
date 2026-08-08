class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> countMap;
        int flag=0;
        for(int& num:nums){
            if(countMap.count(num)==0){
                countMap[num]=1;
            }
            else{
                countMap[num]++;
            }
        }
        for(int& num:nums){
            if(countMap[num]>1){
                flag++;
            }
        }
        if(flag>0){
            return true;
        }
        else{
            return false;
        }

        
    }
};
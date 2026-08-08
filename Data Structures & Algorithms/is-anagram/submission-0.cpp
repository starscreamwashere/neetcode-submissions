class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> smap;
        unordered_map<char,int> tmap;
        if(s.size()!=t.size()){
            return false;
        }
        for(char st1:s){
            if(smap.count(st1)==0){
                smap[st1]=1;
            }
            else{
                smap[st1]++;
            }
        }
        for(char st2:t){
            if(tmap.count(st2)==0){
                tmap[st2]=1;
            }
            else{
                tmap[st2]++;
            }
    }
    if(smap==tmap){
            return true;
        }
        else{
            return false;
        }
    }
};

class Solution {
public:
    bool isAnagram(string s, string t) {
       if(s.length() != t.length()) {
            return false;
       } 

       unordered_map<char,int> charS;
       unordered_map<char,int> charT;
        int i = 0;
       while(i < s.length()) {
        charS[s[i]]++;
        charT[t[i]]++;
        i++;
       }

       return charS == charT;
    }
};

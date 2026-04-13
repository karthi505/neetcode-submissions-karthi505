class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        int range = 0;
        int compliment;

        while (range < nums.size()) {
            compliment = target - nums[range];

            for (int i = 0; i < nums.size(); i++) {
                if (compliment == nums[i] && i != range) {
                    result.push_back(range);
                    result.push_back(i);
                    return result;
                }
            }

            range++;
        }

        return result; // return empty if no match found
    }
};

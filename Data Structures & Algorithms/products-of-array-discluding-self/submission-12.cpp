class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1);
        int leftAcc = 1;
        for (int i = 0; i < n ; i++){
            result[i]= leftAcc;
            leftAcc *= nums[i];
        }
        int rightAcc= 1;
        for (int i = n - 1; i >= 0 ; i--){
            result[i] *= rightAcc;
            rightAcc *= nums[i];
        }
        return result;
    }
};

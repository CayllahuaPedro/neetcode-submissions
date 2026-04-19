class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
         int n = nums.size();
        vector<int> result(n); // Sin inicializar a 1, ahorra un pase
        
        result[0] = 1;
        // Prefijos: calculamos directamente en el vector
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }
        
        int rightAcc = 1;
        // Sufijos: multiplicamos sobre el valor existente
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= rightAcc;
            rightAcc *= nums[i];
        }
        
        return result;
    }
};

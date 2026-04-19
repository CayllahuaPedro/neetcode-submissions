class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // 1. Aceleración de I/O
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int n = nums.size();
        vector<int> res(n);
        
        // 2. Primer pase: Prefijos
        // Evitamos variables extra usando directamente el vector de salida
        res[0] = 1;
        for (int i = 1; i < n; ++i) {
            res[i] = res[i - 1] * nums[i - 1];
        }

        // 3. Segundo pase: Sufijos (Optimizado)
        int suffix = 1;
        for (int i = n - 1; i >= 0; --i) {
            res[i] *= suffix;
            suffix *= nums[i];
        }

        return res;
    }
};


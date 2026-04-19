class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n, 0);
        stack<int> daysWaiting;
        for (int i = 0 ; i < n ; i++){
            while (!daysWaiting.empty() && temperatures[i] > temperatures[daysWaiting.top()]){
                int idx = daysWaiting.top();
                daysWaiting.pop();
                result[idx] = i -idx;
            }
            daysWaiting.push(i);
        }
        return result;
    }
};

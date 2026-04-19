#include <vector>
#include <string>
class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for (const string& s : strs) {
            encoded += to_string(s.length()) + "#" + s;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> result; 
        int i = 0;

        while (i < s.length()){
            size_t j = s.find('#', i);
            if (j == string::npos) break;
            int length = stoi(s.substr(i, j - i));
            int start = j + 1;
            string word = s.substr(start, length);
            result.push_back(word);
            i = start + length;
        }
        return result;
    }
};

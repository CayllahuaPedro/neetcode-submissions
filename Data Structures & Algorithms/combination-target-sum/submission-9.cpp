#include <vector>

using namespace std;

class Solution {
public:
    void backtracking(int index, vector<int>& nums, int target, vector<int>& path, vector<vector<int>>& soluciones) {
        // Caso base: si el target llega a 0, encontramos una combinación válida
        if (target == 0) {
            soluciones.push_back(path);
            return;
        }
        
        // Si el target es negativo, nos pasamos de la suma; paramos de buscar por esta rama
        if (target < 0) {
            return;
        }

        for (int i = index; i < nums.size(); i++) {
            // Decisión: incluir el número actual
            path.push_back(nums[i]);
            
            // Pasamos 'i' en lugar de 'i + 1' porque se permite reutilizar el mismo número
            backtracking(i, nums, target - nums[i], path, soluciones);
            
            // Backtrack: remover el último número para probar otras combinaciones
            path.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> soluciones;
        vector<int> path; // Corrección de la declaración
        
        // Iniciamos la búsqueda desde el índice 0
        backtracking(0, nums, target, path, soluciones);
        
        return soluciones;
    }
};

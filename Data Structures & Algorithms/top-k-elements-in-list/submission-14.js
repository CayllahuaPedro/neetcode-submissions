class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
    const freq = new Map();
    
    // 1. Contar frecuencias
    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    // 2. Convertir llaves a array, ordenar por valor y cortar
    return [...freq.keys()]
        .sort((a, b) => freq.get(b) - freq.get(a)) // Orden descendente por frecuencia
        .slice(0, k); // Tomar los primeros k
}
}

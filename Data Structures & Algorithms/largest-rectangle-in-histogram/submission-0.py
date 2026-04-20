class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # guarda ÍNDICES, no alturas
        max_area = 0
        
        # truco: agregamos 0 al final para forzar el vaciado del stack
        heights.append(0)
        
        for i in range(len(heights)):
            # mientras la barra actual sea menor que el tope del stack,
            # popeamos y calculamos el área del popeado
            while stack and heights[i] < heights[stack[-1]]:
                altura = heights[stack.pop()]
                
                # barrera izquierda: nuevo tope del stack (o -1 si está vacío)
                izq = stack[-1] if stack else -1
                
                # barrera derecha: i (la barra actual que forzó el popeo)
                ancho = i - izq - 1
                
                max_area = max(max_area, altura * ancho)
            
            stack.append(i)
        
        heights.pop()  # restauramos el array (opcional)
        return max_area


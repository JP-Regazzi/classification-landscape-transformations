import numpy as np
from sklearn.linear_model import LinearRegression

# Criar matrizes X e Y (valores de exemplo)
X = np.random.rand(300, 5, 2)  # Matriz X com 300 linhas, 5 colunas e 2 valores em cada posição
Y = np.random.rand(300, 5)      # Matriz Y com 300 linhas e 5 colunas

# Redimensionar a matriz X para que seja uma matriz bidimensional (300x10)
X_reshaped = X.reshape(-1, 10)  

# Inicializar um modelo de regressão linear
model = LinearRegression()

# Ajustar o modelo aos dados
model.fit(X_reshaped, Y.reshape(-1,))

# Obter os coeficientes (parâmetros) da regressão
params = model.coef_.reshape(300, 2)

print("Parâmetros da regressão para cada linha:")
print(params)
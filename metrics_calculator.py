import pandas as pd

def calculate_metrics(vp, vn, fp, fn):
    """
    Calcula as principais métricas de avaliação de modelos de classificação.
    VP: Verdadeiro Positivo, VN: Verdadeiro Negativo, 
    FP: Falso Positivo, FN: Falso Negativo
    """
    total = vp + vn + fp + fn
    
    # Fórmulas
    accuracy = (vp + vn) / total
    precision = vp / (vp + fp) if (vp + fp) > 0 else 0
    sensitivity = vp / (vp + fn) if (vp + fn) > 0 else 0 # Recall
    specificity = vn / (vn + fp) if (vn + fp) > 0 else 0
    f_score = 2 * (precision * sensitivity) / (precision + sensitivity) if (precision + sensitivity) > 0 else 0
    
    return {
        "Acurácia": round(accuracy, 4),
        "Precisão": round(precision, 4),
        "Sensibilidade (Recall)": round(sensitivity, 4),
        "Especificidade": round(specificity, 4),
        "F-Score": round(f_score, 4)
    }

# Matriz de Confusão Arbitrária (Exemplo: Diagnóstico de Pragas no Agro ou Invasão de Rede)
# Altere os valores abaixo conforme desejar para o seu desafio
matriz = {
    "vp": 85,
    "vn": 95,
    "fp": 5,
    "fn": 15
}

results = calculate_metrics(**matriz)

# Exibição dos Resultados
print("=== Relatório de Métricas de Avaliação ===")
for metrica, valor in results.items():
    print(f"{metrica}: {valor * 100:.2f}%")
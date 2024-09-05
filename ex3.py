# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, 
# na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

# Abrindo e lendo o arquivo JSON
with open('dados.json', 'r') as meu_json:
    faturamento_json = json.load(meu_json)


# Filtrando apenas os dias com faturamento maior que zero
faturamento_valido = [dia["valor"] for dia in faturamento_json if dia["valor"] > 0]

# Calculando o menor e maior faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# Calculando a média mensal
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Contando os dias com faturamento acima da média
dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

# Exibindo os resultados
print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
#from → importar coisas prontas.
#def → criar funções.
#datetime.strptime → transformar texto em data.
#timedelta → somar/subtrair tempo em datas.
#return → devolver o resultado de uma função.



from datetime import datetime, timedelta

def ler_data(data_str):
    formatos = ["%d/%m/%Y", "%d%m%Y"]  # aceita com barra e sem barra
    for formato in formatos:
        try:
            return datetime.strptime(data_str, formato)
        except ValueError:
            continue
    raise ValueError("Formato de data inválido. Use dd/mm/aaaa ou ddmmaaaa.")

def calcular_periodo_fertil(data_ultima_menstruacao, ciclo=28):
    # Aqui usamos a função adaptada
    data_inicio = ler_data(data_ultima_menstruacao)

    # Dia fértil estimado: ciclo - 14
    dia_fertil = data_inicio + timedelta(days=ciclo - 14)

    # Janela fértil: 3 dias antes e 3 dias depois
    inicio = dia_fertil - timedelta(days=3)
    fim = dia_fertil + timedelta(days=3)

    return inicio, fim

# Programa principal
print("=== Calculadora de Período Fértil (estimativa) ===")
data = input("Digite a data da última menstruação (dd/mm/aaaa ou ddmmaaaa): ")
ciclo = int(input("Digite a duração média do seu ciclo em dias (padrão 28): ") or 28)

inicio, fim = calcular_periodo_fertil(data, ciclo)

print(f"Seu período fértil estimado é de {inicio.strftime('%d/%m/%Y')} até {fim.strftime('%d/%m/%Y')}")
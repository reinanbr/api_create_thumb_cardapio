import datetime

def get_date_info():
    # Obtém a data atual
    data_atual = datetime.datetime.now()

    # Obtém o dia da semana como um número (0 = segunda-feira, 6 = domingo)
    dia_da_semana = data_atual.weekday()

    # Nomes abreviados dos meses
    nomes_mes_abreviados = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    month_name = nomes_mes_abreviados[data_atual.month - 1]

    # Nomes dos dias da semana
    nomes_dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
    dia_semana = nomes_dias_semana[dia_da_semana]

    # Cria um dicionário com as informações
    informacoes = {
        'date': data_atual.strftime(f'%d {month_name} %Y'),
        'hour': data_atual.strftime('%H:%M'),
        'day_week': dia_semana,
        'month': month_name
    }

    return informacoes


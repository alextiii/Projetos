import requests
import pyodbc
from dateutil import parser

def get_new_token():
    url = ""
    payload = {
        "login": "alex.s",
        "senha": "1234567"
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        token = response.json().get("token")
        return token
    else:
        raise Exception("Não foi possível obter um novo token.")

def fetch_data(token, dt_inicio):
    url = ""
    params = {
        "DtInicio": dt_inicio,
        "codTipoFicha": 1
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json().get("result")
        return data
    else:
        raise Exception("Erro ao obter dados da API.")

def convert_datetime(datetime_str):
    if datetime_str:
        datetime_obj = parser.parse(datetime_str)
        return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    return None

def insert_data(data):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=;"
        "DATABASE=;"
        "UID=;"
        "PWD=;"
    )
    cursor = conn.cursor()

    for item in data:
        codigo_avaliacao = item.get("CODIGO_AVALIACAO")

        query = "SELECT COUNT(*) FROM ofensoresviavarejo2clixapi WHERE CODIGO_AVALIACAO = ?"
        cursor.execute(query, codigo_avaliacao)
        result = cursor.fetchone()
        count = result[0]

        try:
            insert_query = """
            INSERT INTO ofensoresviavarejo2clixapi(
                CODIGO_AVALIACAO,
                DATA_CONTATO,
                DATA_AVALIACAO,
                AVALIADO,
                SUPERIOR,
                NEGOCIO,
                CAMPANHA,
                DEPARTAMENTO,
                AVALIADOR,
                TIPO_AVALIACAO,
                CODIGO_GRAVACAO,
                FORMULARIO,
                SECAO,
                CRITERIO,
                PESO,
                RESPOSTA,
                DETALHE_RESPOSTA,
                STATUS_AVALIACAO,
                DATA_INICIO_SETOR,
                OBS_AVALIADOR,
                PROCESSO,
                NOTA,
                NOTA_SEM_NCG,
                TIPO_RESPOSTA,
                CODIGO_CRITERIO,
                PERIODO,
                MATRICULA,
                TIPO_CALCULO,
                UNIDADE,
                DATA_FEEDBACK,
                TEMPO_FEEDBACK_ABERTO,
                PESO_CALCULADO,
                CODIGO_TICKE,
                DATA_PRAZO_FEEDBACK,
                EMAIL_AVALIADO,
                PENDENTE_DE_ASSINATURA,
                DIAS_ATE_ASSINATURA,
                DIAS_PENDENTES_ATE_ASSINATURA
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            values = (
                item.get("CODIGO_AVALIACAO"),
                convert_datetime(item.get("DATA_CONTATO")),
                convert_datetime(item.get("DATA_AVALIACAO")),
                item.get("AVALIADO"),
                item.get("SUPERIOR"),
                item.get("NEGOCIO"),
                item.get("CAMPANHA"),
                item.get("DEPARTAMENTO"),
                item.get("AVALIADOR"),
                item.get("TIPO_AVALIACAO"),
                item.get("CODIGO_GRAVACAO"),
                item.get("FORMULARIO"),
                item.get("SECAO"),
                item.get("CRITERIO"),
                item.get("PESO"),
                item.get("RESPOSTA"),
                item.get("DETALHE_RESPOSTA"),
                item.get("STATUS_AVALIACAO"),
                convert_datetime(item.get("DATA_INICIO_SETOR")),
                item.get("OBS_AVALIADOR"),
                item.get("PROCESSO"),
                item.get("NOTA"),
                item.get("NOTA_SEM_NCG"),
                item.get("TIPO_RESPOSTA"),
                item.get("CODIGO_CRITERIO"),
                item.get("PERIODO"),
                item.get("MATRICULA"),
                item.get("TIPO_CALCULO"),
                item.get("UNIDADE"),
                convert_datetime(item.get("DATA_FEEDBACK")),
                item.get("TEMPO_FEEDBACK_ABERTO"),
                item.get("PESO_CALCULADO"),
                item.get("CODIGO_TICKE"),
                item.get("DATA_PRAZO_FEEDBACK"),
                item.get("EMAIL_AVALIADO"),
                item.get("PENDENTE_DE_ASSINATURA"),
                item.get("DIAS_ATE_ASSINATURA"),
                item.get("DIAS_PENDENTES_ATE_ASSINATURA"),
            )

            cursor.execute(insert_query, values)
            conn.commit()
            print(f"Dados inseridos com sucesso: {values}")
        except Exception as e:
            print(f"Erro ao inserir os dados: {e}")

    cursor.close()
    conn.close()

def remove_duplicates():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=;"
        "DATABASE=;"
        "UID=;"
        "PWD=;"
    )
    cursor = conn.cursor()

    try:
        cursor.execute("exec duplicadasofensoresviavarejo2clix")
        conn.commit()
        print("Registros duplicados removidos com sucesso!")
    except Exception as e:
        print(f"Erro ao remover registros duplicados: {e}")

        cursor.close()
        conn.close()

def main():
    try:
        token = get_new_token()
        dt_inicio = "2024-01-01" 
        data = fetch_data(token, dt_inicio)
        insert_data(data)

        remove_duplicates()

        print("Dados inseridos com sucesso e registros duplicados removidos!")
    except Exception as e:
        print(f"Erro ao importar os dados: {e}")

if __name__ == "__main__":
    main()

import requests
import pyodbc
from dateutil import parser
import sys

def get_new_token():
    url = "https://api.2clix.com.br/v3/Usuario/login"
    payload = {
        "login": "rafaela.andrade",
        "senha": "Rafaelakk92"
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


def fetch_data():
 
    token = get_new_token()


    params = {
        "DtInicio": "2024-01-01",
        "codTipoFicha": 1
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }


    url = "https://api.2clix.com.br/v3/Reports/ResumoAvaliacoes"
    response = requests.get(url, params=params, headers=headers)

   
    if response.status_code == 200:
        data = response.json()
        return data["result"]
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
        "SERVER=192.168.100.28;"
        "DATABASE=HEADSET_AFFIX;"
        "UID=51543445888;"
        "PWD=T123456;"
    )

    cursor = conn.cursor()

  
    for item in data:
        cod_monitoria = str(item.get("COD_MONITORIA"))
        query = f"SELECT COUNT(*) FROM Monitoria2clix WHERE COD_MONITORIA = '{cod_monitoria}'"
        cursor.execute(query)
        result = cursor.fetchone()
        count = result[0]

        if count == 0:
          
            data_avaliacao = convert_datetime(item.get("data_avaliacao"))
            data_ligacao = convert_datetime(item.get("DATA_LIGACAO"))
            data_feedback = convert_datetime(item.get("data_feedback"))

            insert_query = """
                INSERT INTO Monitoria2clix (
                    COD_MONITORIA,
                    data_avaliacao,
                    cliente,
                    campanha,
                    Superior,
                    Avaliado,
                    Avaliador,
                    Nota,
                    NOTA_SEM_NCG,
                    Processo,
                    DATA_LIGACAO,
                    data_feedback,
                    TIPO_FEEDBACK,
                    CODIGO_GRAVACAO
                )
                VALUES (?, CONVERT(datetime2, ?, 126), ?, ?, ?, ?, ?, ?, ?, ?, CONVERT(datetime2, ?, 126), ?, ?, ?)
            """

            values = (
                cod_monitoria,
                data_avaliacao,
                item.get("cliente"),
                item.get("campanha"),
                item.get("Superior"),
                item.get("Avaliado"),
                item.get("Avaliador"),
                str(item.get("Nota")),
                str(item.get("NOTA_SEM_NCG")),
                item.get("Processo"),
                data_ligacao,
                data_feedback,
                item.get("TIPO_FEEDBACK"),
                item.get("CODIGO_GRAVACAO")
            )
            cursor.execute(insert_query, values)
        else:
            print(f"inserindo: COD_MONITORIA = {cod_monitoria}")

   
    conn.commit()

    conn.close()

    print("DADOS INSERIDOS")


data = fetch_data()
insert_data(data)
sys.exit()
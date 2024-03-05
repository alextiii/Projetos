import requests
import pyodbc
from datetime import datetime
import urllib3
import time



# Desativa os avisos de certificado SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

db_connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=192.168.100.28;"
    "DATABASE=HEADSET_AFFIX;"
    "UID=51543445888;"
    "PWD=T123456;"
)

db_conn = pyodbc.connect(db_connection_string)
db_cursor = db_conn.cursor()

api_base_url = 'https://onlinesaude_proa.vollsc.com/api/agent_sessions'
api_key = '5435e5a127810527319801067d61bb98'

today = datetime.now().strftime('%Y-%m-%d')

api_headers = {
    'voll-api-key': api_key
}

try:
    for page in range(1, 50):
        api_params = {
            'per': 998,
            'page': page,
            'start_date': '2024-01-01' 
        }

        # Adicione verify=False ao fazer a solicitação para desativar a verificação do certificado SSL
        response = requests.get(api_base_url, headers=api_headers, params=api_params, verify=False)
        response.raise_for_status()

        data = response.json().get("items", [])

        for item in data:
            id_value = item.get("id")

            db_cursor.execute("SELECT COUNT(*) FROM Pbi_voll WHERE id = ?", id_value)
            if db_cursor.fetchone()[0] > 0:
                print(f"ID {id_value} já existe no banco de dados. Ignorando inserção.")
                continue

            customer_started_at_str = item.get("customer_started_at")
            agent_started_at_str = item.get("agent_started_at")
            
            started_at = None
            agent_started_at = None
            customer_started_at = None
            
            if customer_started_at_str:
                customer_started_at = datetime.strptime(customer_started_at_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            
            if agent_started_at_str:
                agent_started_at = datetime.strptime(agent_started_at_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            
            ended_at_str = item.get("ended_at")
            ended_at = datetime.strptime(ended_at_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            
            if "started_at" in item and item["started_at"]:
                started_at_str = item.get("started_at")
                started_at = datetime.strptime(started_at_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            
            time_exceeded = item.get("time_exceeded")
            formatted_time_exceeded = item.get("formatted_time_exceeded")
            customer_name = item.get("customer_name")
            cpf = item.get("cpf")
            campaign_name = item.get("campaign_name")
            tabulation_name = item.get("tabulation_name")
            tabulation_group_name = item.get("tabulation_group_name")
            hook_id = item.get("hook_id")
            obs = item.get("obs")
            received_message_count = item.get("received_message_count")
            sent_message_count = item.get("sent_message_count")
            total_messages = item.get("total_messages")
            total_time = item.get("total_time")
            customer_tmr = item.get("customer_tmr")
            agent_tmr = item.get("agent_tmr")
            origin = item.get("origin")
            agent_name = item.get("agent_name")
            system = item.get("system")
            number = item.get("number")
            
           
            insert_query = """
                INSERT INTO Pbi_voll (
                    id, started_at, agent_started_at, customer_started_at, ended_at, time_exceeded, formatted_time_exceeded,
                    customer_name, cpf, campaign_name, tabulation_name, tabulation_group_name, hook_id, obs,
                    received_message_count, sent_message_count, total_messages, total_time, customer_tmr,
                    agent_tmr, origin, agent_name, system, number
                ) VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
            """
            
            db_cursor.execute(insert_query, id_value, started_at, agent_started_at, customer_started_at, ended_at,
                              time_exceeded, formatted_time_exceeded, customer_name, cpf, campaign_name,
                              tabulation_name, tabulation_group_name, hook_id, obs, received_message_count,
                              sent_message_count, total_messages, total_time, customer_tmr, agent_tmr, origin,
                              agent_name, system, number)
            
            db_conn.commit()
            print(f"Inserindo id {id_value} (página {page})")

    print("Dados inseridos com sucesso no banco.")

except requests.exceptions.RequestException as e:
    print("Erro durante a solicitação da API:", e)

except pyodbc.Error as e:
    print("Erro ao inserir dados no banco de dados:", e)

finally:
    db_cursor.close()
    db_conn.close()
time.sleep(5)    

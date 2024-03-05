import pyodbc
import requests
from datetime import datetime
import sys

def insert_data_to_db(data):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=;"
        "DATABASE=;"
        "UID=;"
        "PWD=;"
    )
    cursor = conn.cursor()

    for item in data:
        protocol = item.get("protocol")

        query = "SELECT COUNT(*) FROM atendimentosakiva WHERE protocol = ?"
        cursor.execute(query, protocol)
        result = cursor.fetchone()
        count = result[0]

        try:
            if count == 0:
                date_value = datetime.strptime(item.get("date"), "%d/%m/%Y %H:%M:%S")

                duration_parts = item.get("duration").split(":")
                duration_seconds = int(duration_parts[0]) * 3600 + int(duration_parts[1]) * 60 + int(duration_parts[2])

                insert_query = """
                    INSERT INTO atendimentosakiva (
                      agent ,channel,client ,client_contact ,date,duration_seconds,finished_by,hour,protocol,queue_name,
                      tabulation,type_attendance
                    ) VALUES (
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    )
                """
                cursor.execute(
                    insert_query,
                    item.get("agent"),
                    item.get("channel"),
                    item.get("client"),
                    item.get("client_contact"),
                    date_value,
                    duration_seconds,
                    item.get("finished_by"),
                    item.get("hour"),
                    item.get("protocol"),
                    item.get("queue_name"),
                    item.get("tabulation"),
                    item.get("type_attendance"),
                )
                conn.commit()

                print(f'Dados {protocol} inseridos no banco')

        except Exception as e:
            print("Error inserting data:", e)

api_url = "https://omni-backend.trafficmanager.net/back/api/v1/reports/reportsconsolidate"
request_params = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb21wYW55X2lkIjoiNDgifQ.riCLA02ppksWepyB7a72GiHwYzK8H_HmAPTJRJlfW9Y",
    "date_start": "2024-02-01 00:00",
    "date_end": "2024-09-01 00:00"
}

try:
    response = requests.get(api_url, params=request_params)
    response.raise_for_status()  

    data_from_api = response.json().get("data")
    insert_data_to_db(data_from_api)
    print('Não há mais dados Alex, todos os dados foram inseridos com sucesso')

except requests.exceptions.RequestException as e:
    print("Error during API request:", e)
    sys.exit()

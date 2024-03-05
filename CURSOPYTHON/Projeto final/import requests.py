import requests

def consultar_cep(cep):
    url = f"https://h-apigateway.conectagov.estaleiro.serpro.gov.br/api-cep/v1/consulta/cep/{cep}"

    headers = {
        'Chave-Acesso-API': 'SUA_CHAVE_AQUI'  # Substitua pela sua chave de API, se aplicável
    }

    try:
        # Faz a requisição à API dos Correios com os headers
        response = requests.get(url, headers=headers)

        # Verifica se a requisição foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Converte a resposta para o formato JSON
            resultado = response.json()

            # Exibe as informações obtidas
            print("CEP:", resultado["cep"])
            print("Tipo de CEP:", resultado["tipoCep"])
            print("Subtipo de CEP:", resultado["subTipoCep"])
            print("UF:", resultado["uf"])
            print("Cidade:", resultado["cidade"])
            print("Bairro:", resultado["bairro"])
            print("Endereço:", resultado["endereco"])
            print("Complemento:", resultado["complemento"])
            print("Código IBGE:", resultado["codigoIBGE"])
        else:
            print(f"Erro na requisição. Código de status: {response.status_code}")

    except Exception as e:
        print(f"Erro na requisição: {e}")

# Consultando o CEP: 02203100
consultar_cep("02203100")

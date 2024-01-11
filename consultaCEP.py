import requests


def consult_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        return {}
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return {}
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return {}
    except requests.exceptions.RequestException as err:
        print("Something wrong.", err)
        return {}

    return response.json()

if __name__ == "__main__":
    cep = input("Digite o CEP para consulta: ")
    dados_cep = consult_cep(cep)

    if dados_cep:
        print("Logradouro:", dados_cep.get("logradouro"))
        print("Bairro:", dados_cep.get("bairro"))
        print("Cidade:", dados_cep.get("localidade"))
        print("Estado:", dados_cep.get("uf"))
    else:
        print("CEP não encontrado.")
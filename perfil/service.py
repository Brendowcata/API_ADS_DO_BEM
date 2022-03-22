import requests

def busca_cep(cep:str):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if not response.ok:
        return None
    return response.json()
from typing import Dict
import requests

class PerfilService():

    def busca_cep(cep:str) -> Dict:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if not response.ok:
            return None
        return response.json()
    
    def create_to_save(self, data_response:dict, data_resquest:dict) -> Dict:
        return {
            "nome_instituicao": data_resquest.get("nome_instituicao"),
            "cnpj": data_resquest.get("cnpj"),
            "cep": data_resquest.get("cep"),
            "logradouro": data_resquest.get("logradouro"),
            "bairro": data_resquest.get("bairro"),
            "cidade": data_resquest.get("localidade"),
            "complemento": data_resquest.get("complemento"),
            "uf": data_resquest.get("uf"),
        }

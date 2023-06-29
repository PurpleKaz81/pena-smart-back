from flask import jsonify
from .calculate_qualifier_years import calculate_qualifier_years_total


def get_qualifiers():
    qualifiers = [
        { "id": "qualifier-1", "label": "inciso I", "value": "mediante paga ou promessa de recompensa, ou por outro motivo torpe", "years": 0 },
        { "id": "qualifier-2", "label": "inciso II", "value": "por motivo fútil", "years": 0 },
        { "id": "qualifier-3", "label": "inciso III", "value": "com emprego de veneno, fogo, explosivo, asfixia, tortura ou outro meio insidioso ou cruel, ou de que possa resultar perigo comum", "years": 0 },
        { "id": "qualifier-4", "label": "inciso IV", "value": "à traição, de emboscada, ou mediante dissimulação ou outro recurso que dificulte ou torne impossível a defesa do ofendido", "years": 0 },
        { "id": "qualifier-5", "label": "inciso V", "value": "para assegurar a execução, a ocultação, a impunidade ou vantagem de outro crime", "years": 0 },
        { "id": "qualifier-6", "label": "inciso VI", "value": "contra a mulher por razões da condição de sexo feminino", "years": 0 },
        { "id": "qualifier-7", "label": "inciso VII", "value": "contra autoridade ou agente descrito nos arts. 142 e 144 da Constituição Federal, integrantes do sistema prisional e da Força Nacional de Segurança Pública, no exercício da função ou em decorrência dela, ou contra seu cônjuge, companheiro ou parente consanguíneo até terceiro grau, em razão dessa condição", "years": 0 },
        { "id": "qualifier-8", "label": "inciso VIII", "value": "com emprego de arma de fogo de uso restrito ou proibido", "years": 0 },
        { "id": "qualifier-9", "label": "inciso IX", "value": "contra menor de 14 (quatorze) anos", "years": 0 },
    ]

    return jsonify(qualifiers)

def calculate_qualifier_years_for_request(qualifiers):
    return calculate_qualifier_years_total(qualifiers)

class WineFoodRecommendationSystem:
    def __init__(self):
        # Base de Conhecimento (Ontologia)
        self.database = {
            "Vinho": {
                "Sauvignon Blanc": {
                    "Tipo de Comida": ["peixes grelhados", "saladas", "massa ao molho branco", "frango grelhado"],
                    "Motivo": "O Sauvignon Blanc é conhecido por sua acidez e frescor, o que combina bem com pratos leves e grelhados, como peixes e saladas."
                },
                "Cabernet Sauvignon": {
                    "Tipo de Comida": ["carnes grelhadas", "queijos fortes", "carne vermelha assada ou cozida", "bacalhau"],
                    "Motivo": "O Cabernet Sauvignon é um vinho encorpado e tânico, ideal para acompanhar pratos de carne grelhada ou assada, queijos fortes e bacalhau."
                },
                "Chardonnay": {
                    "Tipo de Comida": ["frango assado", "frutos do mar"],
                    "Motivo": "O Chardonnay é um vinho branco encorpado com sabores de frutas tropicais e notas de carvalho, excelente para acompanhar pratos de frango assado e frutos do mar."
                },
                "Merlot": {
                    "Tipo de Comida": ["massas  com molho vermelho", "queijos leves", "salmão"],
                    "Motivo": "O Merlot é um vinho tinto macio e frutado, perfeito para acompanhar massas com molho vermelho, queijos leves e salmão."
                },
                "Pinot Noir": {
                    "Tipo de Comida": ["salmão assado", "cogumelos", "fondue de queijo"],
                    "Motivo": "O Pinot Noir é um vinho tinto leve e elegante, que combina bem com salmão assado, pratos à base de cogumelos e fondue de queijo."
                },
                "Vinho tinto suave Seleção Pérgola": {
                    "Tipo de Comida": ["salmão"],
                    "Motivo": "Este vinho tinto suave é ideal para acompanhar pratos leves, como salmão, devido ao seu sabor suave e frutado."
                },
                "RSV espumante Prosecco": {
                    "Tipo de Comida": ["comida japonesa"],
                    "Motivo": "O RSV espumante Prosecco é uma excelente escolha para acompanhar comida japonesa devido à sua acidez refrescante e efervescência."
                },
                "Tomero Torrontés, safra 2014": {
                    "Tipo de Comida": ["risoto de aspargos"],
                    "Motivo": "O Tomero Torrontés é um vinho branco aromático com notas florais e cítricas, perfeito para acompanhar risoto de aspargos."
                },
                "Leopoldina Terroir Merlot Rosé, safra 2015": {
                    "Tipo de Comida": ["frutos do mar"],
                    "Motivo": "Este vinho rosé é leve e refrescante, ideal para acompanhar frutos do mar devido à sua acidez equilibrada e sabores frutados."
                },
                "Maquis Rosé, safra 2016": {
                    "Tipo de Comida": ["yakisoba"],
                    "Motivo": "O Maquis Rosé é um vinho rosé com notas de frutas vermelhas e boa acidez, que harmoniza perfeitamente com o saboroso yakisoba."
                },
                "Casa Del Bosque Reserva Sauvignon Blanc, safra 2015": {
                    "Tipo de Comida": ["frango grelhado"],
                    "Motivo": "Este Sauvignon Blanc é um vinho fresco e aromático, excelente para acompanhar pratos de frango grelhado."
                },
                "Vinho nacional San Martin Cabernet Sauvignon tinto seco": {
                    "Tipo de Comida": ["bacalhau"],
                    "Motivo": "Este Cabernet Sauvignon nacional é encorpado e apresenta taninos macios, combinando bem com o sabor forte e a textura do bacalhau."
                }
            }
        }

    def recommend_wine(self, food):
        # Convertendo a entrada do usuário para minúsculas
        food = food.lower()

        # Engenho de Inferência
        recommended_wines = []
        for wine, details in self.database["Vinho"].items():
            if food in details["Tipo de Comida"]:
                recommended_wines.append((wine, details["Motivo"]))
        return recommended_wines

# Exemplo de Uso
system = WineFoodRecommendationSystem()

# Usuário informa o tipo de comida
food_type = input("Informe o tipo de comida (ex: Peixes grelhados): ")

# Recomendar vinho baseado no tipo de comida informado
recommended_wines = system.recommend_wine(food_type)

if recommended_wines:
    print("Recomendamos os seguintes vinhos para acompanhar {}:".format(food_type))
    for wine, motivo in recommended_wines:
        print("- {}: {}".format(wine, motivo))
else:
    print("Desculpe, não temos recomendações para esse tipo de comida.")

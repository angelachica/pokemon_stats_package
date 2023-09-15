import pandas as pd
from pokemon_stats.pokemon_stats import PokemonDataAnalyzer

if __name__ == "__main__":
    csv_file = "C:/Users/angel/OneDrive/Escritorio/Curso Python/Ejercicios/Tema 16/pokemon/pokemon_api_package/pokemon_api/estadisticas_grupo.csv"  # Replace with the actual path to your CSV file
    analyzer = PokemonDataAnalyzer(csv_file)

    grupos_pokemon = analyzer.get_grupos_pokemon()
    print("All Pokemon Groups:")
    print(grupos_pokemon)

    grupo_name = "Dragon"
    altura_media_result = analyzer.get_altura_media_grupo(grupo_name)
    if altura_media_result is not None and not altura_media_result.empty:
        print(f"Average Height for the {grupo_name} Group:")
        print(altura_media_result)
    else:
        print(f"No data found for the {grupo_name} Group.")

    peso_medio_result = analyzer.get_peso_medio_grupo(grupo_name)
    if peso_medio_result is not None and not peso_medio_result.empty:
        print(f"Average Weight for the {grupo_name} Group:")
        print(peso_medio_result)
    else:
        print(f"No data found for the {grupo_name} Group.")

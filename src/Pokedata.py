import requests
import argparse
from math import floor

def get_pokemon_data(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_id = str(pokemon_data['id']).zfill(3)
        name = pokemon_data['name']
        type1 = pokemon_data['types'][0]['type']['name']
        type2 = pokemon_data['types'][1]['type']['name'] if len(pokemon_data['types']) > 1 else None
        height = pokemon_data['height']
        weight = pokemon_data['weight']

        moves = [move['move']['name'] for move in pokemon_data['moves']]
        
        species_url = pokemon_data['species']['url']
        species_response = requests.get(species_url)

        if species_response.status_code == 200:
            species_data = species_response.json()
            description = species_data['flavor_text_entries'][0]['flavor_text']
            description = ' '.join(description.split())
            description = description.replace("POKéMON", "Pokémon")
            
            line1 = description[:44]
            line2 = description[44:100]
            
            max_length=41
            attacks = ''
            for move in moves:
                if len(attacks) + len(move) + 2 <= max_length:
                    attacks += f"{move}, "
            
            title = f"#{pokemon_id} {name.upper()} : {type1.upper()}"
            if type2:
                title = title+f" / {type2.upper()}"
            print(title)
            print(f"HEIGHT: {round(height/10, 1)}m WEIGHT: {floor(weight/10)}kg")
            print(f"ATTACKS: {attacks}etc.")
            print(f"{line1.strip()}-")
            print(line2.strip())
            
        else:
            print(f"Error: Unable to fetch species data for Pokemon with ID {pokemon_id}")
    else:
        print(f"Error: Unable to fetch data for Pokemon with ID {pokemon_id}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--id', type=int, help='Pokemon ID (e.g., 6)')
    group.add_argument('--range', type=str, help='Range of Pokemon IDs (e.g., 1-45)')
    args = parser.parse_args()
    if args.id:
        get_pokemon_data(args.id)
    else:
        ends = args.range.split("-")
        for id in range(int(ends[0]), int(ends[1])+1):
            get_pokemon_data(id)
            print("="*30)

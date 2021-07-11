def pokemon():
    pokemon_list = ['audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary', 'bronzor', 'carracosta', 'charmeleon',
                    'cresselia', 'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite', 'girafarig',
                    'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan', 'kricketune',
                    'landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone', 'mamoswine',
                    'nosepass', 'petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena', 'porygon2', 'porygonz',
                    'registeel', 'relicanth', 'remoraid', 'ruﬄet', 'sableye', 'scolipede', 'scrafty', 'seaking', 'sealeo', 'silcoon',
                    'simisear', 'snivy', 'snorlax', 'spoink', 'starly', 'tirtouga', 'trapinch', 'treecko', 'tyrogue', 'vigoroth', 'vulpix',
                    'wailord', 'wartortle', 'whismur', 'wingull', 'yamask']

    longest_sequence, current_sequence = [], []

    for pokemon in pokemon_list:
        current_pokemon = pokemon
        current_sequence.append(current_pokemon)

        copy_pokemon_list = pokemon_list[:]
        copy_pokemon_list.pop(copy_pokemon_list.index(current_pokemon))

        index = name_start(copy_pokemon_list, current_pokemon[-1])

        while index is not False:
            current_pokemon = copy_pokemon_list[index]
            current_sequence.append(current_pokemon)
            copy_pokemon_list.pop(index)
            index = name_start(copy_pokemon_list, current_pokemon[-1])

        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence

        current_sequence = []

    print(longest_sequence)


def name_start(list, last_letter):
    for index, name in enumerate(list):
        if name.startswith(last_letter):
            return index
    return False


if __name__ == "__main__":
    pokemon()

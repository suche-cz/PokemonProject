from pokemon.models import Pokemon


def create_pokemons():
    for n in range(1000, 2000):
        Pokemon.objects.create(
            number=n,
            name='Pokemon ' + str(n),
            slug='pokemon-' + str(n),
        )

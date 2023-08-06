import click
from .generate_routers import router


@click.command()
@click.option('--name', prompt='Ingresa el nombre de la ruta')

def main( name ):
    router( name )

if __name__ == '__main__':
    main()
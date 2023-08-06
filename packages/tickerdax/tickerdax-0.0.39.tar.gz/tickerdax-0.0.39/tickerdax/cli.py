import os
import typer
import shutil
import pkg_resources
import tickerdax
import tomlkit
import art
from pathlib import Path
from rich import print
from rich.text import Text
from typing import Optional
from tickerdax import formatting
from tickerdax.constants import Envs
from tickerdax.client import TickerDax
from tickerdax.streamer import Streamer
from tickerdax.downloader import Downloader
from typer import rich_utils
from dotenv import load_dotenv

# load in the env file if there is one
load_dotenv()

# monkey patch this function, so we can add in header ascii art
rich_format_help = rich_utils.rich_format_help


def override_help(*args, **kwargs):
    text = Text(art.text2art('TICKERDAX'))
    text.stylize("bold blue")
    print(text)
    rich_format_help(*args, **kwargs)


rich_utils.rich_format_help = override_help

# create cli app
app = typer.Typer(
    pretty_exceptions_show_locals=False
)


def validate_callback(value):
    if not value:
        raise typer.BadParameter('This must be set')


config_argument = typer.Argument(
    'config.yaml',
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=False,
    readable=True,
    resolve_path=True,
    show_default=False,
    help=Envs.CONFIG.description,
    envvar=Envs.CONFIG.value
)
rest_api_key_argument = typer.Argument(
    None,
    callback=validate_callback,
    show_default=False,
    help=Envs.REST_API_KEY.description,
    envvar=Envs.REST_API_KEY.value
)

websocket_api_key_argument = typer.Argument(
    None,
    callback=validate_callback,
    show_default=False,
    help=Envs.WEBSOCKET_API_KEY.description,
    envvar=Envs.WEBSOCKET_API_KEY.value
)

force_argument = typer.Option(
    False,
    help="Forces new REST requests for all missing data, even if that data has already been marked as missing"
)

debug_argument = typer.Option(
    False,
    help="Displays debug logs during execution"
)


def get_version():
    """
    Gets the package version.
    """
    project_file_path = os.path.join(os.path.dirname(__file__), os.path.pardir, 'pyproject.toml')
    if os.path.exists(project_file_path):
        with open(project_file_path, "rb") as project_file:
            data = tomlkit.load(project_file)
            return data.get('tool', {}).get('poetry', {}).get('version', '0.0.1')
    return pkg_resources.get_distribution(tickerdax.__name__).version


def version_callback(value: bool):
    """
    Shows the current cli version

    :param bool value: Whether the version flag was passed.
    """
    if value:
        print(f"TickerDax CLI Version: {get_version()}")
        raise typer.Exit()


@app.callback(no_args_is_help=True)
def callback(version: Optional[bool] = typer.Option(None, "--version", callback=version_callback)):
    """
    The TickerDax CLI tool interfaces with the tickerdax.com REST and websockets APIs. It
    handles common data operations like batch downloading, streaming, and caching data
    locally to minimize network requests.
    """


@app.command()
def create_config(debug: bool = debug_argument):
    """
    Creates a new tickerdax config.
    """
    file_formats = ['json', 'yaml']
    extension = typer.prompt(
        'What file format do you want to use? (json or yaml)',
        default='yaml'
    )
    if extension not in file_formats:
        raise typer.BadParameter(f'Your choice {extension} is not one of the valid formats {file_formats}')

    # copy the example config to the current working directory
    shutil.copyfile(
        os.path.join(os.path.dirname(__file__), 'example_configs', f'config.{extension}'),
        os.path.join(os.getcwd(), f'config.{extension}')
    )


@app.command()
def list_routes(debug: bool = debug_argument):
    """
    Lists all routes available to download or stream.
    """
    tickerdax_client = TickerDax(connect=False, debug=debug)
    routes = tickerdax_client.get_available_routes()
    formatting.show_routes(routes)


@app.command()
def download(
        config: Optional[Path] = config_argument,
        rest_api_key: str = rest_api_key_argument,
        force: bool = force_argument,
        debug: bool = debug_argument
):
    """
    Downloads data from the routes with the time interval specified in your config.
    """
    Downloader(
        config=config,
        client_kwargs={
            'rest_api_key': rest_api_key,
            'force': force,
            'debug': debug
        }
    )


@app.command()
def stream(
        config: Optional[Path] = config_argument,
        rest_api_key: str = rest_api_key_argument,
        websocket_api_key: str = websocket_api_key_argument,
        force: bool = force_argument,
        debug: bool = debug_argument
):
    """
    Streams data from the routes specified in your config.
    """
    Streamer(
        config=config,
        client_kwargs={
            'rest_api_key': rest_api_key,
            'websocket_api_key': websocket_api_key,
            'force': force,
            'debug': debug
        }
    )

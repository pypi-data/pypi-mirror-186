import click
from pathlib import Path


@click.group(help="CLI tool to manage web app.")
def web():
    pass


@web.command(help="Start the web.")
@click.option("--debug", is_flag=True, default=False, help="Use debug mode")
@click.option("--port", help="port.", type=int, default=5000)
def start(debug, port):
    from scinode_app.app import app
    import webbrowser

    kwargs = {}
    kwargs["debug"] = debug
    kwargs["port"] = port
    # webbrowser.open_new('http://127.0.0.1:{}/'.format(port))
    app.run(**kwargs)

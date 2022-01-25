import click
import whitehat

@click.command()
@click.option('--ip', '-i', help="Set IP to scan (Default : 127.0.0.1 or localhost)", required=False)
@click.option('--port', '-p', help="Set Port to scan", required=True)
def cli(ip, port):
    """Port scanner function"""
    if ip == None:
        ip = "127.0.0.1"
    ip = str(ip)
    port = int(port)
    port = whitehat.Port(ip, port)
    click.echo(port.scan())

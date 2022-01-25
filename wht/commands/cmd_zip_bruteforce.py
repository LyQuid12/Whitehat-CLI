import click
import whitehat

@click.command()
@click.option('--wordlist', '-wl', help="Set wordlist to Bruteforce", required=True)
@click.option('--zip_path', '-zp', help="Set zip path to Bruteforce", required=True)
def cli(wordlist, zip_path):
    """Bruteforce function for zip"""
    bf = whitehat.BruteForce(wordlist=wordlist)
    click.echo(bf.zip(zip_path=zip_path))

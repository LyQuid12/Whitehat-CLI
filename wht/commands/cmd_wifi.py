import click
import whitehat

opt = ["get_all_saved_pw", "GASP", "gasp",]

@click.command()
@click.argument("option")
def cli(option):
    if any(v in option for v in opt):
        click.echo(whitehat.Wifi.get_all_saved_pw())
        click.echo(click.style("If Password : None, you need to run cmd as administrator", bg="red"))

    else:
        error = click.style("Error :\n", bg="red")
        available = click.style(f"Available option : {opt} (Windows only)", fg="green")
        click.echo(error + f"Invalid option. " + available)

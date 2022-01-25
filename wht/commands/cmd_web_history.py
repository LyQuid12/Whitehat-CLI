import click
import whitehat

@click.command()
@click.argument('browser', required=True)
@click.option('--show', '-s', help="How much history should be displayed (Default : 100 | Max : all)", required=False, default=100)
def cli(browser, show):
    """
    Get Browser history\n
    Supported browser : Chrome
    """
    chrome = whitehat.Browser(browser_name=browser)
    chrome.get_history(show)

import click
import whitehat

caesar = ["caesar", "Caesar", "caesar_cipher", 'caesar cipher']
morse = ["morse", "Morse", "morse_code", "morse code", "morse_cipher", "morse cipher"]
binary = ["binary", "Binary"]
vigenere = ["vigenere", "Vigenere", "vigenere_cipher", "vigenere cipher"]


@click.command()
@click.argument('cipher_type', required=True)
@click.option('--encrypt', '-e', help="Encrypt string")
@click.option('--decrypt', '-d', help="Decrypt")
@click.option('--shift', '-s', help="Set Caesar cipher shift", required=False)
@click.option('--key', '-k', help="Set vigenere cipher key")
def cli(cipher_type, encrypt, decrypt, shift, key):
    """Cryptography function"""
    if any(v in cipher_type for v in caesar):
        shift = int(shift)
        if encrypt:
            encrypted = whitehat.Cryptography.CaesarCipher.encrypt(text=encrypt, shift=shift)
            click.echo(encrypted)

        if decrypt:
            decrypted = whitehat.Cryptography.CaesarCipher.decrypt(cipher=decrypt, shift=shift)
            click.echo(decrypted)



    if any(v in cipher_type for v in morse):
        if encrypt:
            encrypted = whitehat.Cryptography.Morse.encrypt(encrypt)
            click.echo(encrypted)

        if decrypt:
            decrypted = whitehat.Cryptography.Morse.decrypt(decrypt)
            click.echo(decrypted)



    if any(v in cipher_type for v in binary):
        if encrypt:
            encrypted = whitehat.Cryptography.Binary.encrypt(encrypt)
            click.echo(encrypted)

        if decrypt:
            decrypted = whitehat.Cryptography.Binary.decrypt(decrypt)
            click.echo(decrypted)



    if any(v in cipher_type for v in vigenere):
        if encrypt:
            encrypted = whitehat.Cryptography.VigenereCipher.encrypt(encrypt, key)
            click.echo(encrypted)

        if decrypt:
            decrypted = whitehat.Cryptography.VigenereCipher.decrypt(encrypt, key)
            click.echo(decrypted)

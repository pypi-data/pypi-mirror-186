# This package encrypt and decrypt text files

def encryption(file):
    """ This function encrypts the text file
    """
    content = ""
    # Do text encryption
    try:
        with open(file, "rt") as fd:
            content = fd.read()
    except Exception as e:
        print(e)

    enc_content = ""

    for ch in content:
        if ch != '\n':
            enc_content += (chr(ord(ch) + 3))
        else:
            enc_content += ch

    try:
        with open(file, "wt") as fd:
            fd.write(enc_content)
            print(file, "encrypted successfully")
    except Exception as e:
        print(e)


def decryption(file):
    """ This function decrypts the text file
    """
    content = ""
    # Do text encryption
    try:
        with open(file, "rt") as fd:
            content = fd.read()
    except Exception as e:
        print(e)

    dec_content = ""

    for ch in content:
        if ch != "\n":
            dec_content += (chr(ord(ch) - 3))
        else:
            dec_content += ch

    try:
        with open(file, "wt") as fd:
            fd.write(dec_content)
            print(file, "decrypted successfully")
    except Exception as e:
        print(e)

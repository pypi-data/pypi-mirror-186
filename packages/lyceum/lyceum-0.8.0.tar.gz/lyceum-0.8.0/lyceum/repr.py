""" Module sur le passage entre les diverses représentations de données."""


def dec2bin(n: int, sep="_") -> str:
    # https://docs.python.org/3/library/string.html#format-specification-mini-language

    # on groupe les bits par 4 séparés par des tirets bas par défaut
    b = "{0:_b}".format(n)
    if sep is None:
        return b
    return b.replace("_", sep)


def bin2dec(b: str) -> int:
    # https://stackoverflow.com/a/11029366
    if isinstance(b, str):
        return int(b, 2)
    elif isinstance(b, int):
        return int(str(b), 2)
    else:
        raise Exception("Format d'entrée invalide")


def dec2hex(n: int) -> str:
    # https://stackoverflow.com/a/11029366

    return "{0:_X}".format(n)


def hex2dec(x: str) -> int:
    # https://stackoverflow.com/a/11029366

    return int(x, 16)


def ascii2bin(l: str, replace=False, **kwargs) -> str:
    """Convertir une lettre ASCII en octet"""
    assert len(l) == 1, "Ne convertit qu'une lettre à la fois"
    # if replace:
    #    l = l.encode("ascii", "replace")
    # else:
    #    l = l.encode("ascii")*
    n = ord(l)
    assert n < 2**8, "seuls les lettres ascii sont autorisées"
    if "sep" in kwargs:
        return dec2bin(n, **kwargs).zfill(8 + len(kwargs["sep"]))
    else:
        return dec2bin(n, sep="", **kwargs).zfill(8)


def bin2ascii(bins: str, replace=False, **kwargs) -> str:
    """Convertir un octet en lettre ASCII"""
    assert len(bins) == 8, "Ne convertit qu'une lettre à la fois"
    n = bin2dec(bins)
    assert n < 2**8, "seuls les lettres ascii sont autorisées"
    return chr(n)


def txt2hex(txt: str, enc: str = "utf-8") -> str:
    """Convertir le texte en héxadécimal dans l'encodage souhaité"""
    return txt.encode(enc).hex(sep=" ").upper()


def hex2txt(hex: str, enc: str = "utf-8") -> str:
    """Convertir le code hexadécimal en texte l'encodage souhaité"""
    return bytes.fromhex(hex).decode(enc)


def bin2float(n: str, e: int = None, f: int = None, ieee: bool = False):
    """Décode un binaire flottant en flottant

    Reférences: https://en.wikipedia.org/wiki/Half-precision_floating-point_format

    Les valeurs habituelles de f et e sont utilisées si la norme existe(half,
    single et double).

    Paramètres
    ----------
    n: str
        La représentation binaire à décoder.
    e: int
        Le nombre de bits représentant l'exposant

    f: int
        Le nombre de bits représentant la mantisse
    ieee: bool
        Utilise les valeurs spéciales de la norme ieee754:

        - si l'exposant et la mantisse sont nulles: 0
        - si l'exposant est nul et pas la mantisse nombre dénormalisé
        - si l'exposant est max et mantisse nulle: +/- l'infini
        - si l'exposant est max et mantisse non nulle: nan

    """
    # remove spaces
    n = n.replace(" ", "")
    precision = len(n)
    if precision == 16:
        # https://en.wikipedia.org/wiki/Half-precision_floating-point_format
        e = 5
        f = 10
    elif precision == 32:
        # https://en.wikipedia.org/wiki/Single-precision_floating-point_format
        e = 8
        f = 23
    elif precision == 64:
        # https://en.wikipedia.org/wiki/Double-precision_floating-point_format
        e = 11
        f = 52
    if len(n) != e + f + 1:
        raise Exception("Les nombres de bits ne correspondent pas", precision, e, n)
    est_positif = True if n[0] == "0" else False
    décalage = 2 ** (e - 1) - 1
    exposant = int(n[1 : e + 1], 2)
    mantisse_bin = n[e + 1 :]

    # cas spécial ieee
    if ieee:
        # zéros
        if exposant == 0 and int(mantisse_bin, 2) == 0:
            return 0
        # Nan et infinity
        elif exposant == 2**e - 1:
            if int(mantisse_bin, 2) > 0:
                return float("nan")
            else:
                return float("inf") if est_positif else -float("inf")
    if exposant > 0:
        # nombre normalisé
        m = 1
        exp = exposant - décalage
    else:
        # nombre dénormalisé
        m = 0
        exp = exposant - décalage + 1

    for i, bit in enumerate(mantisse_bin):
        m += int(bit) * 2 ** (-i - 1)
    # print("mantisse", m)
    val = m * 2**exp
    return val if est_positif else -val

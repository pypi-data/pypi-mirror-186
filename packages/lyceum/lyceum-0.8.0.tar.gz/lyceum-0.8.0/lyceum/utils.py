"""Module d'utilitaires

Pas sûr de la garder"""

from functools import partial

PRINT_NORMAL = print


def make_print_compact():
    return partial(PRINT_NORMAL, end="|")


def make_print_normal():
    return partial(PRINT_NORMAL)

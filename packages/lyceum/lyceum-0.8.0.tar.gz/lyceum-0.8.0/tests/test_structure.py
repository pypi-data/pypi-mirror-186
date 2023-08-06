#!/usr/bin/env python

"""Tests for `lyceum` package."""

from lyceum.structure import File, Pile


def test_pile():
    pile = Pile()
    assert pile.est_vide() is True

    pile.empiler(1)
    assert pile.est_vide() is False
    assert pile.sommet() == 1

    pile.empiler(2)
    assert pile.est_vide() is False
    assert pile.sommet() == 2
    assert pile.est_vide() is False

    pile.empiler(3)
    assert (
        pile.__repr__()
        == """\
| 3 | <- Sommet
| 2 |
| 1 |
‾‾‾‾‾
PILE 
"""
    )
    assert pile.sommet() == 3
    assert pile.dépiler() == 3

    while not pile.est_vide():
        pile.dépiler()

    assert pile.est_vide() is True
    assert pile.sommet() is None
    print(pile)
    assert (
        pile.__repr__()
        == """\
|   | <- Sommet
‾‾‾‾‾
PILE 
"""
    )


def test_file():
    file = File()
    assert file.est_vide() is True

    file.enfiler(1)
    assert file.est_vide() is False
    assert file.tête() == 1

    file.enfiler(2)
    assert file.est_vide() is False
    assert file.tête() == 1
    assert file.est_vide() is False

    file.enfiler(3)
    assert file.tête() == 1
    assert file.est_vide() is False
    assert (
        "\n" + file.__repr__()
        == """
         _____________        
Queue -> | 3 | 2 | 1 | -> Tête
         ‾‾‾‾‾‾‾‾‾‾‾‾‾        
             FILE             
"""
    )

    assert file.défiler() == 1
    assert file.défiler() == 2
    assert file.défiler() == 3

    assert file.est_vide() is True
    assert file.tête() is None

# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""References for citing Boulder Opal."""
import datetime
import os


def _dict_to_bib(cite_type: str, name: str, data: dict):
    """
    Converts data dictionary to BibTex format.
    """
    as_list = [f"{key} = {value}" for key, value in data.items()]
    format_string = ",\n  ".join(as_list)
    return f"@{cite_type}{{{name},\n  {format_string}\n}}"


def cite_boulder_opal(path):
    """
    Prints the BibTeX information for citing Boulder Opal,
    with the possibility to save it into a BibTeX file.

    Parameters
    ----------
    path : str, optional
        If passed, the BibTeX information will be saved to the file 'boulder_opal.bib' at the
        given path.
    """
    paper = cite_boulder_opal_paper()
    print(paper, end="\n\n")
    website = cite_boulder_opal_product()
    print(website)

    if path is not None:
        with open(
            os.path.join(path, "boulder_opal.bib"), "w", encoding="utf-8"
        ) as bibtex_file:
            bibtex_file.write(paper + "\n\n")
            bibtex_file.write(website)


def cite_boulder_opal_paper():
    """
    Returns information for citing the Boulder Opal paper.
    """

    data = {
        "doi": "{10.1088/2058-9565/abdca6}",
        "url": "{https://doi.org/10.1088/2058-9565/abdca6}",
        "year": "{2021}",
        "publisher": "{I{OP} Publishing}",
        "volume": "{6}",
        "number": "{4}",
        "pages": "{044011}",
        "author": "{Harrison Ball and Michael J Biercuk and Andre R R Carvalho and Jiayin Chen and "
        "Michael Hush and Leonardo A De Castro and Li Li and Per J Liebermann and Harry "
        "J Slatyer and Claire Edmunds and Virginia Frey and Cornelius Hempel "
        "and Alistair Milne}",
        "title": "{Software tools for quantum control: improving quantum computer performance "
        "through noise and error suppression}",
        "journal": "{Quantum Science and Technology}",
    }
    return _dict_to_bib("article", "boulder_opal1", data)


def cite_boulder_opal_product():
    """
    Return information for citing the Boulder Opal product (website).
    """

    data = {
        "author": "{Q-CTRL}",
        "title": "{Boulder {O}pal}",
        "year": f"{{{datetime.datetime.now().year}}}",
        "howpublished": "{https://q-ctrl.com/boulder-opal}",
        "note": "{[Online]}",
    }
    return _dict_to_bib("misc", "boulder_opal2", data)

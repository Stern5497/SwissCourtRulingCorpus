from pathlib import Path
from pprint import pprint
from typing import Any, Optional
from scrc.enums.citation_type import CitationType
import json
import regex

from root import ROOT_DIR

"""
This file is used to extract citations from decisions sorted by spiders.
The name of the functions should be equal to the spider! Otherwise, they won't be invocated!
Overview of spiders still todo: https://docs.google.com/spreadsheets/d/1FZmeUEW8in4iDxiIgixY4g0_Bbg342w-twqtiIu8eZo/edit#gid=0
"""


def XX_SPIDER(soup: Any, namespace: dict) -> Optional[dict]:
    # This is an example spider. Just copy this method and adjust the method name and the code to add your new spider.
    pass


def CH_BGer(soup: Any, namespace: dict) -> Optional[dict]:
    """
    :param soup:        the soup parsed by bs4
    :param namespace:   the namespace containing some metadata of the court decision
    :return:            the sections dict, None if not in German
    """
    law_key = 'artref'
    bge_key = 'bgeref_id'

    laws, rulings = [], []

    for law in soup.find_all("span", class_=law_key):
        if law.string:  # make sure it is not empty or None
            laws.append({"text": law.string})

    for bge in soup.find_all("a", class_=bge_key):
        if bge.string:  # make sure it is not empty or None
            rulings.append({"type": "bge", "url": bge['href'], "text": bge.string})

    return {CitationType.LAW: laws, CitationType.RULING: rulings}


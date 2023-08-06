import enum
import re
from typing import List, Optional


class Filter(str, enum.Enum):
    EQUALS = 'equals'
    STARTS_WITH = 'starts_with'
    ENDS_WITH = 'ends_with'
    CONTAINS = 'contains'


def filter_items(items: List[str], text: str, regex: Optional[bool] = False,
                 filter_: Filter = Filter.EQUALS) -> List[str]:
    """
    Filter items.

    Args:
        items (list): The items to filter.
        text (str): The element to filter.
        regex (bool, optional): True to enable regex search.
            [See for regex details](https://docs.python.org/3/library/re.html)
        filter_ (Filter, optional): Filter pattern without user using regex.
    """
    if regex:
        return [item for item in items if re.search(text, item)]

    if filter_ == Filter.CONTAINS:
        return [item for item in items if text in item]
    elif filter_ == Filter.STARTS_WITH:
        return [item for item in items if item.startswith(text)]
    elif filter_ == Filter.ENDS_WITH:
        return [item for item in items if item.endswith(text)]
    else:
        return [item for item in items if item == text]

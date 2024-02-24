from __future__ import annotations
from typing import Optional, Any, Tuple
from typing import List

# NodeList is
# None or
# Node(value, rest), where rest is the rest of the NodeList
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value
        self.rest = rest

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value
            and self.rest == other.rest
            )
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist: Optional[Node]) -> Optional[str]:
    if strlist is None or []:
        return None
    min_rest = first_string(strlist.rest)
    print(strlist.value)
    print(f"Rest: {strlist.rest}")
    if min_rest is None or strlist.value < min_rest:
        return strlist.value
    else:
        return min_rest

# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively
def split_list(strlist: Optional[Node]) -> Tuple[Optional[Node], Optional[Node], Optional[Node]]:
    vowelList = ['a', 'e', 'i', 'o', 'u']
    alphabetList = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                    'z']
    if strlist is None:
        return None, None, None
    lists = split_list(strlist.rest)
    if strlist.value != "" and strlist.value[0].lower() in vowelList:
        return Node(strlist.value, lists[0]), lists[1], lists[2]
    elif strlist.value != "" and strlist.value[0].lower() in alphabetList:
        return lists[0], Node(strlist.value, lists[1]), lists[2]
    # elif strlist.value != "" and not strlist.value[0].isalpha():
    else:
        return lists[0], lists[1], Node(strlist.value, lists[2])
    # return lists[0], lists[1], lists[2]

from typing import TypedDict


class Weapon(TypedDict):
    name: str
    category: str
    is_magic: bool
    item_type: str
    req_attunement: bool
    rarity: str
    book_info: str
    requirement: str
    enchant_slots: int
    effect: str

class Shield(TypedDict):
    name: str
    category: str
    is_magic: bool
    item_type: str
    req_attunement: bool
    rarity: str
    book_info: str
    requirement: str
    enchant_slots: int
    effect: str
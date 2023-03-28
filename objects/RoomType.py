from enum import Enum

class RoomType(Enum):
    """
        Seperates the large rooms from the small rooms
    """
    LARGE = (
        "306",
        "311",
        "312",
        "313",
        "329",
        "330",
        "331",
        "504",
        "306A" # Because of this "A" we need all the numbers to be strings
    )
    SMALL = (
        "314",
        "315",
        "316",
        "317",
        "318",
        "319",
        "320",
        "321",
        "322",
        "323"
    )

__all__ = [
    "RoomType"
]
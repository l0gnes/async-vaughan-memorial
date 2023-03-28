from typing import List
from datetime import datetime, date
from .RoomType import RoomType
from .BookedTime import BookedTime

class Room(object):
    """
        Dataclass for room data
    """

    room_number : str
    room_type : RoomType
    booked_times : List[BookedTime]

    def __init__(
        self,
        room_number : str,
        room_type : RoomType,
        booked_times : List[BookedTime]
    ) -> None:
        
        self.room_number = room_number
        self.room_type = room_type
        self.booked_times = booked_times



    @classmethod
    def fromJSON(cls, data : dict) -> "Room":
        """Generates a `Room` object from a JSON response

        :param data: The json response to parse
        :type data: dict
        :return: The `Room` object for the corresponding data
        :rtype: Room
        """
        room_number = list(data.keys())[0]
        room_type = RoomType.LARGE if room_number in RoomType.LARGE.value else RoomType.SMALL
        booked_times = [BookedTime.fromJSON(d) for d in data[room_number]]

        return cls(
            room_number = room_number,
            room_type = room_type,
            booked_times = booked_times
        )



    def is_booked_at(
        self,
        t : datetime 
    ) -> bool:
        """Returns `True` if the room is booked at time `t`.

        :param t: The time `t` to check
        :type t: datetime.datetime
        :return: `True` if the room is booked at time `t`, otherwise, returns `False`
        :rtype: bool
        """
        return any([booking.overlap_checker(t) for booking in self.booked_times])

__all__ = [
    "Room"
]
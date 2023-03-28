from datetime import datetime, timedelta
from typing import Optional

class BookedTime(object):
    """
        Contains the data for a time where the study room is booked.
    """

    start : datetime
    end : datetime
    reason : Optional[str]

    def __init__(
        self,
        start : datetime,
        end : datetime,
        reason : Optional[str]
    ) -> None:
        
        self.start = start
        self.end = end
        self.reason = reason



    @classmethod
    def fromJSON(cls, data : dict) -> "BookedTime":
        """Generates a `BookedTime` from a JSON response

        :param data: The json response to parse
        :type data: dict
        :return: The `BookedTime` that correlates to the parsed JSON
        :rtype: BookedTime
        """
        return cls(
            start = datetime.fromisoformat(data['from'][:-1]),
            end = datetime.fromisoformat(data['to'][:-1]),
            reason = data.get("reason", None)
        )



    @property
    def duration(self) -> timedelta:
        """Returns the duration that the room is booked for

        :return: A timedelta containing the duration the room is booked for
        :rtype: datetime.timedelta
        """
        return (self.end - self.start)
    


    def overlap_checker(
        self,
        t : datetime
    ) -> bool:
        """Returns whether or not `t` is within the booked time

        :param t: The time to check
        :type t: datetime.datetime
        :return: Returns `True` if `t` is in the booked time, otherwise, returns `False`
        :rtype: bool
        """

        if t >= self.start and t < self.end: return True # There is an overlap
        return False                                    # There is no overlap
    

__all__ = [
    "BookedTime"
]
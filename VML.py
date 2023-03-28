from typing import List
from objects import Room, RoomType
from aiohttp import ClientSession

class VaughanMemorialLibrary(object):

    LIBRARY_ENDPOINT = "https://auls.acadiau.ca/booking/API/unavailable-times.php"


    async def fetch_room(self, room_number : str) -> Room | None:
        """Fetches the room unavailability for a specific room

        :param room_number: The number of the room
        :type room_number: str
        :return: A room object, or None if the room is invalid
        :rtype: Room | None
        """

        if not (room_number in RoomType.LARGE.value or room_number in RoomType.SMALL.value):
            return None # Room entered is an invalid room

        async with ClientSession() as session:
            async with session.get(
                self.LIBRARY_ENDPOINT,
                params = dict( item = room_number )
            ) as resp:
                js_resp = await resp.json()

        return Room.fromJSON(js_resp)
    


    async def fetch_rooms_by_type(self, type : RoomType) -> List[Room]:
        """Fetches all rooms of a specific type

        :param type: They type of room to query for
        :type type: RoomType
        :return: A list of `Room` objects, containing the booking data for each room.
        :rtype: List[Room]
        """
        rooms = []

        for room_number in type.value:
            r = await self.fetch_room(room_number)
            rooms.append(r)

        return rooms
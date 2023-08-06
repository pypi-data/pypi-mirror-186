from json_cpp import JsonObject, JsonList
from .location import *


class Frame(JsonObject):

    def __init__(self,
                 frame_number: int = 0,
                 time_stamp: float = 0.0,
                 prey_detection: bool = False,
                 predator_detection: bool = False,
                 prey_location: Location = None,
                 predator_location: Location = None,
                 prey_rotation: float = 0.0,
                 predator_rotation: float = 0.0,
                 prey_data: float = "",
                 predator_data: float = ""):
        self.frame_number = frame_number
        self.time_stamp = time_stamp
        self.prey_detection = prey_detection
        self.predator_detection = predator_detection

        if prey_location is None:
            self.prey_location = Location(0, 0)
        else:
            self.prey_location = prey_location

        if predator_location is None:
            self.predator_location = Location(0, 0)
        else:
            self.predator_location = predator_location

        self.prey_rotation = prey_rotation
        self.predator_rotation = predator_rotation
        self.prey_data = prey_data
        self.predator_data = predator_data
        JsonObject.__init__(self)


class Frame_list(JsonList):

    def __init__(self):
        JsonList.__init__(self, list_type=Frame)

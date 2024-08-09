"""your favorite İD class(right?)"""
from typing import Callable


class ID:

    def __init__(self):
        self.global_id_list = []  # we'll use db instead
        # self.__numerical_id_list: list[dict[int, bool]] = []
        # self.__alphabetical_id_list: list[dict[str, bool]] = []
        # self.__numerical_id_catolog: list[dict[int, list[bool, int]]] = []  # have 10x numbers and put how much free space there if non then false
        # self.__alphabetical_id_catolog: list[dict[str, list[bool, int]]] = []  # sort alphabetically then put the free ones
        # self.__numerical_id_database_scale: int = 10                           # FİXME: implement an id

    def check_id(self,
                 id: int | str) -> bool:  # "developers gettin stuff done stuff" -Luke Muscat (in his video about game dev crimes, at 12:50)
        """check if an id is already in use"""
        return id in self.global_id_list

    def default_id_chooser(self, caller: str) -> str:
        id = caller
        if not self.check_id(id):
            i = 0
            while not self.check_id(id):
                id = f"{caller}-{i}"
                i += 1
        return id

        # ILL ADD AN ACTUAL DATABASE JUST WAIT FOR IT

    # def numerical_id_chooser(self) -> int:
    #     i = 0
    #     for key, value in self.__numerical_id_list:
    #         if not value:
    #             self.__numerical_id_list[i] = {key: True}
    #             return key
    #         i += 1

    def get_global_id_list(self):
        """returns a copy of global_id_list"""
        return self.global_id_list

    def assign_id(self, item: str, caller: str, id_chooser: Callable = default_id_chooser, *args):
        """1) if you specified an id_chooser function input the arguments to the *args section
		 2) if you made an id_chooser don't forget to check if the id is already in use or else bugs"""
        if id_chooser == self.default_id_chooser:
            id = self.default_id_chooser(caller=caller)
        else:
            id = id_chooser(args)
        self.global_id_list.append(id)
        return {id: item}

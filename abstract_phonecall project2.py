from abc import ABC, abstractmethod
from datetime import date
from typing import final


class AbstractPhoneCall(ABC):

    @abstractmethod
    def get_caller(self) -> str:

        pass


    def get_callee(self) -> str:


        pass

    def get_starttime(self) -> date:

        pass



    def get_starttime_string(self) -> str:

        pass


    def get_endtime(self)-> date:

        pass


    def get_endtime_string(self)-> str:

        pass



    @final
    def __str__(self)-> str:

        return \
            "Incoming call from " + self.get_caller() +\
            " to " + self.get_callee() +\
            " from " + self.get_starttime_string() +\
            " to " + self.get_endtime_string();
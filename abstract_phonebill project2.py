from abc import abstractmethod
from typing import TypeVar, List, final

from cis301.phonebill.abstract_phonecall import AbstractPhoneCall


class AbstractPhoneBill:

    @abstractmethod
    def get_customer(self) -> str:

        pass

    @abstractmethod
    def add_phonecall(self, phonecall):

        pass

    T = TypeVar(AbstractPhoneCall)
    @abstractmethod
    def get_phonecalls(self) -> List[T]:


    @final
    def __str__(self) -> str:

        return self.get_customer() + "'s phone bill with " + len(self.get_phonecalls()) + " phone calls"
from abc import ABC, abstractmethod
from typing import Union
from .WorldView import WorldView


class Statistic(ABC):
    __currentValue: Union[str, int, bool, float]

    def updateCurrentValue(self, worldView: WorldView):
        self.__currentValue = self.__calcValue(worldView)

    def getCurrentValue(self):
        return self.__currentValue

    @abstractmethod
    def __calcValue(self, worldView: WorldView) -> Union[str, int, bool, float]:
        pass

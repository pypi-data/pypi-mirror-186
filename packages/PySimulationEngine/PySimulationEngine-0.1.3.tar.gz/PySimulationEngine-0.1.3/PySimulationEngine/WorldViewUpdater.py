from abc import ABC, abstractmethod
from .WorldView import WorldView


class WorldViewUpdater(ABC):
    @abstractmethod
    def update(self, worldView: WorldView):
        pass
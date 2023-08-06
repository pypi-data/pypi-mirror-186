from .Agent import Agent


class WorldView():
    def __init__(self, envWidth: int = 60, envHeight: int = 40) -> None:
        self.__objects = set()
        self.__agents = set()
        self.__env = [[None for i in range(envWidth+1)] for j in range(envHeight+1)]
        self.__currentMoment = 0

    # Set/Add methods

    def addAgent(self, agent: Agent) -> None:
        self.__agents.add(agent)

    def addObject(self, object) -> None:
        self.__objects.add(object)
    
    def setEnv(self, newEnv: list[list]) -> None:
        self.__env = newEnv

    # Get Methods

    def getObjects(self) -> set:
        return self.__objects
    
    def getAgents(self) -> set:
        return self.__agents
    
    def getCurrentMoment(self):
        return self.__currentMoment
    
    def getEnv(self):
        return self.__env
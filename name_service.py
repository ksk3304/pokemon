from abc import ABC, abstractmethod

class NameService(ABC):
    @abstractmethod
    def change_name(self, new_name):
        pass
    
    @abstractmethod
    def get_name(self):
        pass
    
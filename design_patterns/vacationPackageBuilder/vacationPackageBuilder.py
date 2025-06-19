from abc import ABC, abstractmethod

class VacationPackageBuilder(ABC):
    @abstractmethod
    def add_destination(self, destination: str):
        """Add a destination to the vacation package."""
        pass

    @abstractmethod
    def add_transportation(self, transportation: str):
        """Add transportation to the vacation package."""
        pass

    @abstractmethod
    def add_accommodation(self, accommodation: str):
        """Add accommodation to the vacation package."""
        pass

    @abstractmethod
    def set_duration(self, days: int):
        """Set the duration of the vacation package in days."""
        pass

    @abstractmethod
    def set_budget(self, budget: float):
        """Set the budget for the vacation package."""
        pass

    @abstractmethod
    def set_num_travelers(self, num_travelers: int):
        """Set the number of travelers for the vacation package."""
        pass

    @abstractmethod
    def set_vacation_type(self, vacation_type: str):
        """Set the type of vacation (e.g., adventure, relaxation, cultural)."""
        pass

    @abstractmethod
    def set_activity(self, activity: str):
        """Add an activity to the vacation package."""
        pass

    @abstractmethod
    def build(self):
        """Build and return the final vacation package."""
        pass


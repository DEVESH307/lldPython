from vacationPackage import VacationPackage
from vacationPackageBuilder import VacationPackageBuilder

class CustomVacationPackageBuilder(VacationPackageBuilder):
    # def __init__(self):
    #     self._destination = None
    #     self._transportation = None
    #     self._accommodation = None
    #     self._duration = None
    #     self._budget = None
    #     self._num_travelers = None
    #     self._vacation_type = None
    #     self._activities = []

    # def add_destination(self, destination: str):
    #     """Add a destination to the vacation package."""
    #     self._vacation_package.set_destination(destination)
    # def add_transportation(self, transportation: str):
    #     """Add transportation to the vacation package."""
    #     self._vacation_package.set_transportation(transportation)
    # def add_accommodation(self, accommodation: str):
    #     """Add accommodation to the vacation package."""
    #     self._vacation_package.set_accommodation(accommodation)
    # def set_duration(self, days: int):
    #     """Set the duration of the vacation package in days."""
    #     self._vacation_package.set_duration(days)
    # def set_budget(self, budget: float):
    #     """Set the budget for the vacation package."""
    #     self._vacation_package.set_budget(budget)
    # def set_num_travelers(self, num_travelers: int):
    #     """Set the number of travelers for the vacation package."""
    #     self._vacation_package.set_num_travelers(num_travelers)
    # def set_vacation_type(self, vacation_type: str):
    #     """Set the type of vacation (e.g., adventure, relaxation, cultural)."""
    #     self._vacation_package.set_vacation_type(vacation_type)
    # def set_activity(self, activity: str):
    #     """Add an activity to the vacation package."""
    #     self._vacation_package.add_activity(activity)

    def __init__(self):
        self._vacation_package = VacationPackage()

    def add_destination(self, destination: str):
        """Add a destination to the vacation package."""
        if not destination or not isinstance(destination, str):
            raise ValueError("Destination must be a non-empty string.")
        self._vacation_package.set_destination(destination)

    def add_transportation(self, transportation: str):
        """Add transportation to the vacation package."""
        if not transportation or not isinstance(transportation, str):
            raise ValueError("Transportation must be a non-empty string.")
        self._vacation_package.set_transportation(transportation)

    def add_accommodation(self, accommodation: str):
        """Add accommodation to the vacation package."""
        if not accommodation or not isinstance(accommodation, str):
            raise ValueError("Accommodation must be a non-empty string.")
        self._vacation_package.set_accommodation(accommodation)

    def set_duration(self, days: int):
        """Set the duration of the vacation package in days."""
        if not isinstance(days, int) or days <= 0:
            raise ValueError("Duration must be a positive integer.")
        self._vacation_package.set_duration(days)

    def set_budget(self, budget: float):
        """Set the budget for the vacation package."""
        if not isinstance(budget, (int, float)) or budget < 0:
            raise ValueError("Budget must be a non-negative number.")
        self._vacation_package.set_budget(budget)

    def set_num_travelers(self, num_travelers: int):
        """Set the number of travelers for the vacation package."""
        if not isinstance(num_travelers, int) or num_travelers <= 0:
            raise ValueError("Number of travelers must be a positive integer.")
        self._vacation_package.set_num_travelers(num_travelers)

    def set_vacation_type(self, vacation_type: str):
        """
        Set the type of vacation.
        Options: adventure, relaxation, cultural, family, romantic, wildlife, cruise, wellness, sports, luxury, eco-tour, road trip, beach, city, ski, backpacking, pilgrimage, culinary, festival, shopping.
        """
        valid_types = {
            "adventure", "relaxation", "cultural", "family", "romantic", "wildlife", "cruise", "wellness",
            "sports", "luxury", "eco-tour", "road trip", "beach", "city", "ski", "backpacking",
            "pilgrimage", "culinary", "festival", "shopping"
        }
        if not vacation_type or not isinstance(vacation_type, str):
            raise ValueError("Vacation type must be a non-empty string.")
        vacation_type_lower = vacation_type.lower()
        if vacation_type_lower not in valid_types:
            raise ValueError(f"Vacation type must be one of: {', '.join(valid_types)}.")
        self._vacation_package.set_vacation_type(vacation_type_lower)

    def set_activity(self, activity: str):
        """Add an activity to the vacation package."""
        if not activity or not isinstance(activity, str):
            raise ValueError("Activity must be a non-empty string.")
        self._vacation_package.set_activity(activity)

    def build(self):
        """Finalize and return the constructed VacationPackage object."""
        return self._vacation_package
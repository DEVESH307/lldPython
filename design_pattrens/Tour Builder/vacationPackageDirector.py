from vacationPackageBuilder import VacationPackageBuilder
from vacationPackage import VacationPackage

class VacationPackageBuilderDirector:
    def __init__(self, builder: VacationPackageBuilder):
        self._tour_builder = builder

    def construct_vacation_package(self):
        """Construct the vacation package using the provided builder."""
        self._tour_builder.add_destination("Paris")
        self._tour_builder.add_transportation("Flight")
        self._tour_builder.add_accommodation("Hotel")
        self._tour_builder.set_duration(7)
        self._tour_builder.set_budget(2000.0)
        self._tour_builder.set_num_travelers(2)
        self._tour_builder.set_vacation_type("Cultural")
        self._tour_builder.add_activity("Eiffel Tower Visit")
        self._tour_builder.add_activity("Louvre Museum Tour")

    def get_vacation_package(self) -> VacationPackage:
        """Get the constructed vacation package."""
        return self._tour_builder.build()
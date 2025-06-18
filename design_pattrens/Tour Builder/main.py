from customVacationPackageBuilder import CustomVacationPackageBuilder
from vacationPackageDirector import VacationPackageDirector

if __name__ == '__main__':
    # Create a custom vacation package builder
    cvp = CustomVacationPackageBuilder()
    # Create a director to manage the vacation package construction
    director = VacationPackageDirector(cvp)
    # Construct the vacation package
    director.construct_vacation_package()
    # Get the constructed vacation package
    vacation_package = director.get_vacation_package()
    # Print the details of the vacation package
    print(f"Vacation Package Object: {vacation_package}")
    print("Vacation Package Details:")
    print(f"Destination: {vacation_package.get_destination()}")
    print(f"Transportation: {vacation_package.get_transportation()}")
    print(f"Accommodation: {vacation_package.get_accommodation()}")
    print(f"Duration: {vacation_package.get_duration()} days")
    print(f"Budget: ${vacation_package.get_budget()}")
    print(f"Number of Travelers: {vacation_package.get_num_travelers()}")
    print(f"Vacation Type: {vacation_package.get_vacation_type()}")
    print(f"Activities: {', '.join(vacation_package.get_activities())}")


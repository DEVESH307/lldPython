class VacationPackage:
    def __init__(self):
        self._destination = None
        self._transportation = None
        self._accommodation = None
        self._duration = None
        self._budget = None
        self._num_travelers = None
        self._vacation_type = None
        self._activities = []

    def set_destination(self, destination):
        self._destination = destination

    def set_transportation(self, transportation):
        self._transportation = transportation

    def set_accommodation(self, accommodation):
        self._accommodation = accommodation

    def set_duration(self, duration):
        self._duration = duration

    def set_budget(self, budget):
        self._budget = budget

    def set_num_travelers(self, num_travelers):
        self._num_travelers = num_travelers

    def set_vacation_type(self, vacation_type):
        self._vacation_type = vacation_type

    def set_activity(self, activity):
        self._activities.append(activity)


    def get_destination(self):
        return self._destination

    def get_transportation(self):
        return self._transportation

    def get_accommodation(self):
        return self._accommodation

    def get_duration(self):
        return self._duration

    def get_budget(self):
        return self._budget

    def get_num_travelers(self):
        return self._num_travelers

    def get_vacation_type(self):
        return self._vacation_type

    def get_activities(self):
        return self._activities
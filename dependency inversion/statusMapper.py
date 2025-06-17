# # 0. Define an interface for status mappers(original code)
# from abc import ABC, abstractmethod
# class StatusMapper(ABC):

#     @abstractmethod
#     def status_mapper(self, status):
#         pass
# class databrick(StatusMapper):

#     def get_status(self):
#         return "SUCCESS"
#     def status_mapper(self,status):

#         if status == "SUCCESS":
#             return "DONE"

#         else:
#             raise Exception(status)
# class SnowFlake(StatusMapper):
#     def get_status(self,status):
#         return "SUCCESSFUL"
#     def status_mapper(self,status):
#         if status == "SUCCESSFUL":
#                 return "DONE"

# def mycode():
#     api = SnowFlake()
#     if api.status_mapper(api.get_status()) == "DONE":
#         print("Databrick is on")
        
from abc import ABC, abstractmethod

class StatusMapper(ABC):
    @abstractmethod
    def status_mapper(self, status):
        pass

class Databrick(StatusMapper):
    def get_status(self):
        return "SUCCESS"

    def status_mapper(self, status):
        if status == "SUCCESS":
            return "DONE"
        else:
            raise Exception(status)

class SnowFlake(StatusMapper):
    def get_status(self):
        return "SUCCESSFUL"

    def status_mapper(self, status):
        if status == "SUCCESSFUL":
            return "DONE"
        else:
            raise Exception(status)

def mycode():
    api = SnowFlake()
    if api.status_mapper(api.get_status()) == "DONE":
        print("SnowFlake is on")

    db = Databrick()
    if db.status_mapper(db.get_status()) == "DONE":
        print("Databrick is on")

if __name__ == "__main__":
    mycode()
    
db = Databrick()
sf = SnowFlake()
# # 0. Exception handling (original code)
# def write_to_db():
#     raise FileExistsError("File error occured")
#
#
# def create_user(password):
#     try:
#         print()
#         write_to_db()
#     except FileExistsError:
#         print()
#
#
# def divide10By(num):
#         return 10 / num
#
#
#
# def debitAmount(amount):
#     try:
#         raise RuntimeError
#         print("amount debited")
#     except RuntimeError:
#         print("amount not debited")
#
# def credit_amount(amount):
#     print("amount credited")
# def start():
#     print("diving number by...")
#     debitAmount(1)
#     credit_amount(1)
#     # print("payment debited")
#     # print("payment credited...")
#
# start()
#
# try:
#     raise RuntimeError
#     print("try something")
# finally:
#     print("finally....")
#
#
# print("release lock..")

# class TransactionFailed(Exception):
#     pass


# try:
#     print("try something")
#     raise TransactionFailed

# except RuntimeError:
#     print("RuntimeError")
# else:
#     print("opps...")
# finally:
#     print("finally...")



# # 1. Exception handling (modified code)
# print(10/0)
# # output: ZeroDivisionError: division by zero

# try:
#     print(10/0)
#     raise IndexError
# except:
#     print("Division by zeo")
    
# def write_to_db():
#     raise FileExistsError("File error occured")

# def create_user():
#     try:
#         print(10/0)
#         write_to_db()
#     except Exception as e:
#         print(str(e))
# create_user()


# def create_user(password):
#     try:
#         print()
#         write_to_db()
#     except FileExistsError as e:
#         print(str(e))
# create_user(1234)

# def divide10By(num):
#     try:
#         return 10/num
#     except Exception as e:
#         print(e)
        
# def debit_amount(amount):
#     try:
#         raise RuntimeError
#         print("amount debited")
#     except RuntimeError:
#         print("amount not debited")

# def credit_amount(amount):
#    print("amount credited") 
   
# def start():
#     print("dividing number by.....")
#     divide10By(0)
#     debit_amount(1)
#     credit_amount(1)
#     # print("payment debited...")
#     # print("payment credited...")
# start()


# # db handling use finally  
# try:
#     raise RuntimeError
#     print("try something")
# except RuntimeError:
#     print("handling runtime exception")
#     # raise RuntimeError
#     # print("go to market..")
# finally:
#     print("finally....")
      
# try:
#     print("try something")
# finally:
#     print("finally....")


# try:
#     print("try something")
    
# # kind of if (except block)    
# except RuntimeError:
#     print("RuntimeError")
# else:
#     print("opps....")
    
    
class TransactionFailed(Exception):
    def __init__(self, message):
        self.message = message

try:
    print("try something")
    raise TransactionFailed("Failed Transection")

except RuntimeError:
    print("RuntimeError")
else:
    print("opps...")
finally:
    print("finally...")

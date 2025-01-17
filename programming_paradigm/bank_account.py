class BankAccount :


      def __init__(self, initial_account = 0):
           
           self.__account_balance = initial_account




      def deposit(self, amount):
          
          if amount > 0:
               self.__account_balance += amount

          else :
               print("the amount should be positive")


      def withdraw(self, amount):
          
          if amount > self.__account_balance:
               
               return False
          elif amount > 0:
               
               self.__account_balance -= amount
               return True
          else:
               print("Withdraw should always positive")

               return False
          
      def display_balance(self):
          
          print(f" Your balance is : ${self.__account_balance: .2f}")
          

               

class Calculator:
    # Addition Function

    def add(self,num_1,num_2):
        return (num_1 + num_2)

    # Subtraction Function

    def subtract(self,num_1,num_2):
        return (num_1 - num_2)

    #Multiplication Function

    def multiply(self,num_1,num_2):
        return (num_1 * num_2)

    # Division Function

    def divide(self,num_1,num_2):
        if num_2 == 0:
            return "Error : Division By Zero is Not Allowed !"
        return (num_1 / num_2 )

    # Menu Function 

    def show_Menu(self):
        print("\n" + "=" * 40)
        print("******".center(40,"="))
        print("Welcome To Basic Calculator".center(40))
        print("******".center(40, "="))
        print("=" * 40)
        print("Enter 1. Addition")
        print("Enter 2. Subtraction")
        print("Enter 3. Multiplication")
        print("Enter 4. Division")
        print("Enter 5. Exit")
        print( "=" * 40 + "\n")

    #Taking User Input
    
    def get_numbers(self,prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            
            except ValueError:
                print("Only Numbers Are Allowed ! Please Enter A Number")
                continue
        
            except Exception:
                print("Only Numbers Are Allowed ! Please Enter A Number")
                continue 
    
    #Function To Run The Whole Calculator 
            
    def run(self):
        while True:
            #Showing Menu
            
            self.show_Menu()
            
            #Choosing and Validating Menu option
            
            choice = input("Select Your Preferred Option (1-5) : ").strip()
            
            if choice not in ["1","2","3","4","5"]:
                print("Invalid Selection ! Enter A Number Between 1 To 5 ")
                continue
            
            #loop Terminator
            
            if choice == "5":
                print("Thank You for Using The Basic Calculator ❤ . GoodBye !")
                break
            
            #Taking and Validating User Input
            
            num_1 = self.get_numbers("Enter Your First Number  : ")
            num_2 = self.get_numbers("Enter Your Second Number : ")
            
            #operations
            
            if choice == "1" or choice.capitalize() == "Addition":
                result = self.add(num_1,num_2)
                operation = "Addition"
                operator = "+"            
            if choice == "2" or choice.capitalize() == "Subtraction":
                result = self.subtract(num_1,num_2)
                operation = "Subtraction"                
                operator = "-"            
            if choice == "3" or choice.capitalize() == "Multiplication":
                result = self.multiply(num_1,num_2)
                operation = "Multiplication"
                operator = "*"
            if choice == "4" or choice.capitalize() == "Division":
                result = self.divide(num_1,num_2)
                operation = "Division"
                operator = "/"  
            
            #Showing operation Result
            
            print("\n" + "-"*40 +"\n"+ f"\n{operation} Result : ")            
            print(f"{num_1} {operator} {num_2} = {result}")
            print("\n" + "-"*40)
            
#Creating Calculator Object
calc1= Calculator()
calc1.run()
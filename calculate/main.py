

# function to calcuate the  average of given number 
def calculate_average(*args):
     
     # check if the args is empty or not 
     # if args is empty then the return will print 0.0 
     # if there are any strings then also it will return  that the value is invalid as the try except is used to catch the error occured
     # while enterning the wrong value
     # the return function then sums the args number and divided by the length of the args  to get the average number  beetween 
     # the given number to meet the requirment of the task by pytech solution

     if not args:
          return 0.0
     return sum(args) / len(args)


# function to concatenate the strings with keyword arguments 
def concat_strings(**kwargs):
     
    # this function is used to concatenate the given strings with the keyword arguments 
    # the function will be empty if there is no keyword arguments as emepty 
    # the function then return the values 
    # if there are keywords then the funcation will return the string concatenated with other values as one sentence.
    # as the kwargs takes the values that ar passed to the function as a dictionary.

     if not kwargs:
         return ""
     return "".join(kwargs.values(  ))


"""
 - this is the main fucntion to execute every things in the program 
 - every logic are written within this function as it makes the code mroe readable and easy to understand as code should be written
   in such a way that each and every one can understand the code and the logic.
 - the function will be called  at the end to execute the logic.

"""

def main_fun():
     

     """
     this function runs when the program is true as the main progrm is itself true it is automatically executed.
     when the program is executed first it shows the user 

         wellcome to pytech solution choose the task you want to perform.
         type 1:  Calculate the average of given number
         type 2: Concatenate the given String

        After that the program will ask the user to enter the number and strip will remove space from the input. 
        if the number is not 1 or 2 then it will print invalid value and ask the user the re-enter the value.
     """

     while True:
          print('\n Wellcome to Pytech Solution. \n  Choose the task you want to perform!')
          print(' type 1:  Calculate the average of given number')
          print(' type 2: Concatenate the given String')

          selected_Number = input(' Enter the number 1 or 2 to select task').strip()

        
        # if the selected value is one the it will enter into the first task 
          if selected_Number == '1':

            # here try and except is used to catch the error that may occur during the exexcction of program
            # the entered value are sepreated by , and it not the value is not loped as they are striped and stroed in the list
            # for loops every number and generates a len of the numbers 
            try:
                numbers_Entered = input('Enter number using comma to separete one with another. Eg:( 2, 3, 4, 5 ) \n')
                number_Listed = [ 
                    float(num.strip()) 
                    for num in numbers_Entered.split(',') 
                    if num.strip()
                    ]
                
                # here the function calcualte_average uses an argumnet to take the number and calculate the average of the number 
                average = calculate_average(*number_Listed)
                
                # the average is then printed with the number entered by the user
                print(f'\n Your Entered Number is :{ number_Listed}')
                # the average is then printed with the number entered by the user
                print(f'Average of number is:{average}')

            # any error that occurs in the program will be catched by except.
            except ValueError:
                print('Invalid input Enter the number  with valid foramt')


           #if selected number is 2 then it will enter into the second task that concatenate the given strings
          elif selected_Number == '2':
                #   as soon as the user enters the number 2 it will ask the user to entern the strings one after another
                # when the user is done the user will type okay to end the input process
                # initially the stringss are empty and the count is one 
                 print('Enter strings One after Another. Type Okay When You entered Enough string ')
                 strings = {}
                 count = 1

                 while True:
                      user_Strings = input(f'Enter strings are {count}: ')

                      # the strings are then converted into lower case and check if the user has enterd okay or not
                      # if the user has enterd okay then the loop will  break and the program will end.
                      if user_Strings.lower() == "okay":
                          break
                      
                      # the stings are stored in dictionary with the key and the count value keep increasing by one
                      strings[f'part{count}'] = user_Strings
                      count += 1

                 # result is where the value of the strings are stored and the function concat_stings is used to concatenate stings     
                 result = concat_strings(**strings)
                 # the result is the printed.
                 print(f'\n Concatenated Strings are: {result}')
          
          else:
            print('invalid Entered Value. please Enter 1 or 2.')

            # after the process is ended then the user is again asked if the user wants to keep using the program or not.
            # if it is not yes thent the program ends and shows user thank you for using the program. and the program ends.
          execute_Again = input( '\n Do You want to execute the program again? ( type yes or no ):').strip().lower()
          if execute_Again != 'yes':
               print('Thank for Using Pytech Solution Program.')
               break
              

# this condtion is used to check if the program is directly executed or not.
if __name__ == "__main__":
    
    main_fun()



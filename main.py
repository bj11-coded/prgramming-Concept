def calculate_average(*args):
     if not args:
          return 0.0
     return sum(args) / len(args)

def concat_strings(**kwargs):
     

     if not kwargs:
         return ""
     return "".join(kwargs.values())


def main_fun():
     
     while True:
          print('\n Wellcome to Pytech Solution. \n  Choose the task you want to perform!')
          print(' type 1:  Calculate the average of given number')
          print(' type 2: Concatenate the given String')

          selected_Number = input(' Enter the number 1 or 2 to select task').strip()

        
        # if the selected value is one the it will enter into the first task 
          if selected_Number == '1':
            try:
                numbers_Entered = input('Enter number using comma to separete one with another. Eg:( 2, 3, 4, 5 ) \n')
                number_Listed = [ 
                    float(num.strip()) 
                    for num in numbers_Entered.split(',') 
                    if num.strip()
                    ]
                
                average = calculate_average(*number_Listed)
                
                print(f'\n Your Entered Number is :{ number_Listed}')
                print(f'Average of number is:{average}')

            except ValueError:
                print('Invalid input Enter the number  with valid foramt')


          elif selected_Number == '2':
               
                 print('Enter strings One after Another. Type Okay When You entered Enough string ')
                 strings = {}
                 count = 1

                 while True:
                      user_Strings = input(f'Enter strings are {count}: ')

                      if user_Strings.lower() == "okay":
                          break
                      
                      strings[f'part{count}'] = user_Strings
                      count += 1

                 result = concat_strings(**strings)
                 print(f'\n Concatenated Strings are: {result}')
          
          else:
            print('invalid Entered Value. please Enter 1 or 2.')

          execute_Again = input( '\n Do You want to execute the program again? ( type yes or no ):').strip().lower()
          if execute_Again != 'yes':
               print('Thank for Using Pytech Solution Program.')
               break
              

if __name__ == "__main__":
    main_fun()



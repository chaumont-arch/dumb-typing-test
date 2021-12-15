#run this from the command line only
import msvcrt
import time
import multiprocessing
from os import system, name

#do something about the global variables - options file?
time_limit = 60
print_width = 50

# https://www.geeksforgeeks.org/clear-screen-python/
# define our clear function
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')    
    
def test_user_on_character(goal_char):
    input_char = ''
    while input_char != goal_char:
        input_char = msvcrt.getch().decode()
    # and then return and reset timer, restart forcibly
    # make sure it all gets printed nice
    # and display wpm when its done
    
def test_user_on_string(text):
    clear()
    for index in range(len(text)):
        final_index = min(len(text),index+print_width)
        print(text[index:final_index])
        goal_char = text[index]
        test_user_on_character(goal_char)
        clear()
    print("END OF STRING REACHED") #is there a way to kill the sleep?
        
def run_function_with_timer(function,*args):  
    p = multiprocessing.Process(target=function, name="function", args=(*args,)) #messy *args handling
    p.start()   
    time.sleep(time_limit) 
    p.terminate()  
    p.join()
        
if __name__ == '__main__':
    message = "That way, Python will recognise it as a tuple with a single element, as intended. Currently, Python is interpreting your code as just a string. However, it's failing in this particular way because a string is effectively list of characters."
    run_function_with_timer(test_user_on_string,message)

#Plan:
#3 strikes out
#60 second time limit
#display active 50 characters
#option to get text from wikipedia
#or just random words from common word dictionary

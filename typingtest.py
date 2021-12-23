#run this from the command line only
import msvcrt
import time
import multiprocessing
import random
from os import system, name

#do something about the global variables - options file?
time_limit = 60
print_width = 50

# https://www.geeksforgeeks.org/clear-screen-python/
def clear_screen():
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
    clear_screen()
    for index in range(len(text)):
        final_index = min(len(text),index+print_width)
        print(text[index:final_index])
        goal_char = text[index]
        test_user_on_character(goal_char)
        clear_screen()
    print("END OF STRING REACHED") #is there a way to kill the sleep?
        
def run_function_with_timer(function,*args):  
    p = multiprocessing.Process(target=function, name="function", args=(*args,)) #messy *args handling
    p.start()   
    time.sleep(time_limit) 
    p.terminate()  
    p.join()

def create_word_list():
    f = open("resources/1-1000.txt", "r")
    wordlist = []
    for line in f:
        wordlist.append(line.strip()+" ")
    f.close()
    random.shuffle(wordlist)

    #Once again, not a great way to do this
    textline = ""
    for word in wordlist:
        textline += word

    return textline

def get_value(message):
    value = ""
    while not isinstance(value,int):
        value = input(message)
        try:
            value = int(value)
        except:
            value = ""
    return value

def get_string():
    print("1. Fixed string")
    print("2. 1000 common words")
    index = get_value("Input mode:")
    #I know there's a better way to do this but I don't care.
    if index == 1:
        message = "That way, Python will recognise it as a tuple with a single element, as intended. Currently, Python is interpreting your code as just a string. However, it's failing in this particular way because a string is effectively a list of characters."
    if index == 2:
            message = create_word_list()
    return message
        
if __name__ == '__main__':
    message = get_string()
    run_function_with_timer(test_user_on_string,message)


#Plan:
#3 strikes out
#60 second time limit
#display active 50 characters
#option to get text from wikipedia
#or just random words from common word dictionary

#TODO:
#fix flickering text
#display stats
#get text databases
#have modes

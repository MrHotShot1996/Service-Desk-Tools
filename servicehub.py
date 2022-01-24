import pyperclip as pc

def servicehub_response():
    '''Main Application'''
    gender = gender_choice()
    name = input("Enter the name:\n")

    choice = input(
        "Enter the response reason:\n"
        "1 - No answer\n"
        "2 - Make a Request\n"
        )
    if choice == "1":
        no_response(gender, name)
    elif choice == "2":
        make_request(gender, name)

def gender_choice():
    '''To make the response more formal'''
    gender = input("1 - [mr] \n2 - [ms]?\n")
    if gender == '1':
        return 'Mr. '
    elif gender == '2':
        return 'Ms. '




# Responses List

def no_response(gender, name):
    '''No answer'''
    msg = (f"Greetings dear {gender}{name}, "
        "I have called but no one seems to be around, "
        "kindly re-open the ticket once you're ready "
        "so that I can further assist you.\n\n"
        "Thank you for your understanding and have a wonderful day."
        )
    pc.copy(msg)
    print(msg)

def make_request(gender, name):
    '''When you cancel and make a request'''
    msg = (f"Greetings dear {gender}{name}, "
        "kindly make a request for this by going to "
        "the service hub and entering the following:\n"
        "- Request a service\n"
        )
    thank = "Thank you for your understanding and have a wonderful day."
    path_ = ""
    while True:
        list_ = "- "
        category = input("Enter the request path: \n")
        seperator = "\n"
        if category == "":
            break
        path = list_ + category + seperator
        path_ += path
        print(path_)

    # Post loop 
    msg += path_ + thank
    pc.copy(msg)
    print(msg)






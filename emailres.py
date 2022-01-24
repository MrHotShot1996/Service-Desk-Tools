import pyperclip as pc

def email_response():
    '''Responses related to email'''
    gender = gender_choice()
    name = input("Enter the name:\n")

    choice = input(
        "Enter the response reason:\n"
        "1 - Phone secure apps\n"
        "2 - Ipac guide\n"
        )
    if choice == "1":
        secure_app(gender, name)
    elif choice == "2":
        ipac(gender, name)


def gender_choice():
    '''To make the response more formal'''
    gender = input("1 - [mr] \n2 - [ms]?\n")
    if gender == '1':
        return 'Mr. '
    elif gender == '2':
        return 'Ms. '


# Responses
def secure_app(gender, name):
    '''Secure application response'''

    msg = (f"Greetings dear {gender}{name},"
        "\n\nIn the attachments, you will find the guide on how "
        "to configure secure apps, if you were to still have any "
        "questions afterwards, feel more than free to ask us for assistance.\n"
        "\nThank you and have a wonderful day."
        )
    print(msg)
    pc.copy(msg)

def ipac(gender, name):
    '''ipac response'''

    msg = (f"Greetings dear {gender}{name},"
        "\n\nIn the attachments, you will find the guide on how "
        "to configure remote access (ipac), if you were to still have any "
        "questions afterwards, feel more than free to ask us for assistance.\n"
        "\nThank you and have a wonderful day."
        )
    print(msg)
    pc.copy(msg)
#Health managemet System
print("Welcome to Health management System\n")
def Client_Name():
    """

    :return: it returns Client Name
    """
    name = input("Enter Which person health Management System you wanna access\n 1. 'Avii' 2. 'Mehul' 3. 'Kartik' \n")
    return name

def take():
    """

    :return: returns user want to lock or retrive
    """
    inp = int(input(" '1' for lock and '2' for retrive\n"))
    return inp

def getdate():
    """

    :return: it returns date and time
    """
    import datetime
    return datetime.datetime.now()

date = str(getdate())

def HMsystem():
    """
    it gives user to wite and read their diet and exercise plan
    :return:
    """
    take_op = take()

    cli_name = Client_Name()

    def diet_exe():
        """

        :return: diet or exercise choosen by user
        """
        inp = input("Enter what you wanna edit \n 1. 'Diet' 2. 'Exercise' \n")
        return inp
    diet_exe1 = diet_exe()
    if take_op == 1:

        if cli_name == "Avii":

            if diet_exe1 == "Diet":
                with open("Avii_diet.txt","a") as f:
                    eat = input("Enter what you ate today\n")
                    f.write(eat)
                    f.write(date)

            elif diet_exe1 == "Exercise":
                with open("Avii_exercise.txt","a") as f:
                    exe = input("Enter exercises you did today\n")
                    f.write(exe)
                    f.write(date)

            else:
                print("Enter option wisely and correctly\n")

        elif cli_name == "Mehul":

            if diet_exe1 == "Diet":
                with open("Mehul_diet.txt","a") as f:
                    eat = input("Enter what you ate today\n")
                    f.write(eat)
                    f.write(date)

            elif diet_exe1 == "Exercise":
                with open("Mehul_exercise.txt","a") as f:
                    exe = input("Enter exercises you did today\n")
                    f.write(exe)
                    f.write(date)

            else:
                print("Enter option wisely and correctly\n")

        elif cli_name == "Kartik":

            if diet_exe1 == "Diet":
                with open("Kartik_diet.txt","a") as f:
                    eat = input("Enter what you ate today\n")
                    f.write(eat)
                    f.write(date)

            elif diet_exe1 == "Exercise":
                with open("Kartik_exercise.txt","a") as f:
                    exe = input("Enter exercises you did today\n")
                    f.write(exe)
                    f.write(date)

            else:
                print("Enter option wisely and correctly\n")

        else:
            print("Enter Client Names Properly\n")


    elif take_op == 2:

        if cli_name == "Avii":

            if diet_exe1 == "Diet":
                with open("Avii_diet.txt", "r") as f:
                   for line in f:
                       print(line,end=" ")

            elif diet_exe1 == "Exercise":
                with open("Avii_exercise.txt", "a") as f:
                    for line in f:
                        print(line, end=" ")

            else:
                print("Enter option wisely and correctly\n")

        elif cli_name == "Mehul":

            if diet_exe1 == "Diet":
                with open("Mehul_diet.txt", "a") as f:
                    for line in f:
                        print(line, end=" ")

            elif diet_exe1 == "Exercise":
                with open("Mehul_exercise.txt", "a") as f:
                    for line in f:
                        print(line, end=" ")

            else:
                print("Enter option wisely and correctly\n")

        elif cli_name == "Kartik":

            if diet_exe1 == "Diet":
                with open("Kartik_diet.txt", "a") as f:
                    for line in f:
                        print(line, end=" ")

            elif diet_exe1 == "Exercise":
                with open("Kartik_exercise.txt", "a") as f:
                    for line in f:
                        print(line, end=" ")

            else:
                print("Enter option wisely and correctly\n")

        else:
            print("Enter Client Names Properly\n")
    else:
        print("write '1' and '2' correctly \n")


HMsystem()
print("Thanks for using\n")

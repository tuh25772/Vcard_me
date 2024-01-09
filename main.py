from helper_functions import *
import read_write_into_file


def main():
    '''
        Main function which is responsible for menu and
        taking actions as per user choice
    '''
    while True:
        num = show_menu()
        if num == 1:
            details = get_Details()
            read_write_into_file.write_vcard(details)

        elif num == 2:
            key = input('Enter the fullname or email or phone number : ')
            ret = find_Card(key)
            if ret != -1:
                while True:
                    choice = input("Do you want to edit this contact information[y/n]: ")
                    if choice.upper() == "Y":
                        edit_info(key)
                        break
                    elif choice.upper() not in ["Y", "N"]:
                        print("Please select valid choice as y/n only!!!")
                        continue
                    else:
                        break
        elif num == 3:
            print_all()

        elif num == 4:
            key = input('Enter the fullname or email or phone number to delete : ')
            delete_info(key)

        elif num == 5:
            print("Good Bye!!!")
            break


if __name__ == '__main__':
    main()
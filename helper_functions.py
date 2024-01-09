import read_write_into_file

def show_menu():
    '''Function to show the menu options'''
    print()
    print("**************************")
    print(
         ' 1. Enter new vcard \n 2. Search Vcard \n 3. Print all the cards \n 4. Delete card \n 5. End Program')
    while True:
        print()
        num = input('Please select your choice: ')
        try:
            num = int(num)
        except Exception:
            print("Please enter integer values only from 1-6 and Try again !!!")
            continue
        if num >= 1 and num <= 6:
            break
        else:
            print("Please enter number from 1-6 only. Try again !!!")
    return num

def get_Details():
    '''
        Allowing the user to enter the vcard details
        All the possbile exceptions are handled in this
    '''
    print('Please enter the contact details  '.center(60, '='))
    details = {}
    details['first_name'] = input(' - First name            : ')
    while details['first_name'].isdigit():
        print('Please enter only characters for first name')
        details['first_name'] = input(' - First name          : ')
    details['last_name'] = input(' - Last name             : ')
    while details['last_name'].isdigit():
        print('Please enter only characters for last name')
        details['last_name'] = input(' - First name          : ')
    details['full_name'] = details['first_name'] + ' ' + details['last_name']
    details['email'] = input(' - E-mail address        : ')
    while "@" not in details['email']:
        print('Please enter valid email')
        details['email'] = input(' - E-mail address        : ')

    while True:
        try:
            details['phone_number'] = input(' - Phone number          : ')
            int(details['phone_number'])
            break
        except Exception:
            print('please enter only digits in phone number')
            continue
    details['vcard'] = make_vcard(**details)
    print(details['vcard'])
    return details

def make_vcard(
        first_name,
        last_name,
        full_name,
        email,
        phone_number,
        ):
    '''Function to convert the information in vcard format specified.'''
    return f"""
        BEGIN:vcard
        FN:{full_name}
        N:{last_name};{first_name}
        EMAIL;INTERNET:{email}
        TEL;WORK:{phone_number}
        VERSION: 2.1
        END:VCARD
    """


def find_index_opti(key):
    '''
        Function to get the index for the given key
        Returns -1 incase key not found
    '''
    vcard = read_write_into_file.read_vcard()
    index = -1
    for i, v in enumerate(vcard):
        if v != '':
            key = key.lower()
            vc = vcard_to_dict(v)
            print(vc)
            if (key == vc['full_name'].lower()) or\
                    (key == vc['email'].lower()) or\
                    (key == vc['phone_number']):
                index = i
                break
    return vcard, index


def find_Card(key):
    '''Function to find card for the given key.'''
    vcard, found = find_index_opti(key)
    if found != -1:
        print("Below details are found in the database")
        print(vcard[found], end='\n')
    else:
        print(f'Record not found for key {key}')
    return found



def vcard_to_dict(vcard):
    '''
        Convert the vcard that is read from the text file to dict
        This make the search operation easy
    '''
    vcard_dict = {}
    vcard_list = []
    for i in vcard.split('\n'):
        if i.strip() != '':
            vcard_list.append(i)
    name = vcard_list[1].strip().replace('FN:', '').split()
    vcard_dict['first_name'] = name[0]
    vcard_dict['last_name'] = name[1]
    vcard_dict['full_name'] = name[0] + ' ' + name[1]
    vcard_dict['email'] = vcard_list[3].strip().replace('EMAIL;INTERNET:', '')
    vcard_dict['phone_number'] = vcard_list[4].strip().replace('TEL;WORK:', '')
    return vcard_dict


def params():
    cols = ['first_name', 'last_name', 'email', 'phone_number']
    for ind, col in enumerate(cols):
        print(f'{ind + 1} : {col}')
    number = int(input('Choose the number you want to edit : ')) - 1
    while number < 0 or number >= len(cols):
        number = int(input('Choose the number you want to edit : ')) - 1
    return cols[number]


def edit_info(key):
    '''Function responsible to make changes in the given vcard.'''
    vcard, found = find_index_opti(key)
    if found != -1:
        print(vcard[found], end='\n')
        From = params()
        To = input('Enter new information: ')
        vc = vcard_to_dict(vcard[found])
        vc[From] = To
        vc['full_name'] = vc['first_name'] + ' ' + vc['last_name']
        vc['vcard'] = make_vcard(**vc)
        vcard[found] = vc['vcard']
        read_write_into_file.delete_db()
        for v in vcard:
            if v != '':
                details = {'vcard': v}
                read_write_into_file.write_vcard(details)
    else:
        print('Record not found')


def print_all():
    '''Priting all the vcard information.'''
    vcard = read_write_into_file.read_vcard()
    for vc in vcard:
        if vc == "":
            continue
        print(vc, end='\n')
        print('--------------')
        print()


def delete_info(key):
    '''Deleting the given vcard.'''
    vcard, found = find_index_opti(key)
    if found != -1:
        read_write_into_file.delete_db()
        vcard[found] = ''

        for v in vcard:
            if v != '':
                details = {'vcard': v}
                read_write_into_file.write_vcard(details)

        print('Record has been deleted')

    return f'Record Not Found for given key {key}'

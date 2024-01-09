import os


def read_vcard(fname='vcf_database.txt'):
    '''Function to read vcard information.'''
    delimiter = '\n' + '*' * 10
    with open(fname, 'r') as f:
        vcard = f.read().split(delimiter)
    return vcard

def delete_db(fname='vcf_database.txt'):
    '''Function to delete vcard information from txt file.'''
    try:
        os.unlink(fname)
    except Exception as e:
        print('database already deleted')
        print(e)


def write_vcard(details, fname='vcf_database.txt'):
    '''Function to write information in txt file'''
    with open(fname, 'a') as f:
        f.write(str(details['vcard']))
        f.write('\n')
        f.write('*' * 10)

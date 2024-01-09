import unittest
import helper_functions
import read_write_into_file
import os


class Testing(unittest.TestCase):

    def test_make_vcard(self):
        ret = helper_functions.make_vcard("First", "Last", "First Last", "email", 123)
        exp_ret = f'''
        BEGIN:vcard
        FN:{"First Last"}
        N:{"Last"};{"First"}
        EMAIL;INTERNET:{"email"}
        TEL;WORK:{123}
        VERSION: 2.1
        END:VCARD
    '''
        self.assertEqual(ret, exp_ret)

    def test_write_vcard(self):
        ret = helper_functions.make_vcard("First", "Last", "First Last", "email", 123)
        temp_dict = {}
        temp_dict['vcard'] = ret
        read_write_into_file.write_vcard(temp_dict, "test.txt")
        self.assertEqual(os.path.exists("test.txt"), True)

    def test_delete_db(self, fname="test.txt"):
        with open(fname, 'w') as fp:
            pass
        read_write_into_file.delete_db(fname)
        self.assertEqual(os.path.exists("test.txt"), False)

    def test_vcard_to_dict(self):
        vcard = '''BEGIN:vcard
        FN:{"First Last"}
        N:{"Last"};{"First"}
        EMAIL;INTERNET:{"email"}
        TEL;WORK:{123}
        VERSION: 2.1
        END:VCARD'''
        ret_dict = helper_functions.vcard_to_dict(vcard)
        self.assertEqual(len(ret_dict), 5)

    def test_vcard_to_dict_2(self):
        vcard = f'''BEGIN:vcard
        FN:{"First Last"}
        N:{"Last"};{"First"}
        EMAIL;INTERNET:{"email"}
        TEL;WORK:{123}
        VERSION: 2.1
        END:VCARD'''
        ret_dict = helper_functions.vcard_to_dict(vcard)
        self.assertEqual(ret_dict['first_name'], "First")
        self.assertEqual(ret_dict['last_name'], "Last")


if __name__ == "__main__":
    unittest.main()

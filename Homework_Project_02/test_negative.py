'''
Автотест архиватора 7z
Файл с негативными тестами (проверками)
'''

from checkers import checkout_negative

folder_in = "/home/user/test_folder" # куда распаковываем архив
folder_neg = "/home/user/folder_neg" # откуда берем поврежденный архив

def test_nstep1():
    #test neg 1
    assert checkout_negative("cd {}; 7z e arh3.7z -o{} -y".format(folder_neg, folder_in),
                             "ERROR"), "test negative 1 FAIL"

def test_nstep2():
    #test neg 2
    assert checkout_negative("cd {}; 7z t arh.7z".format(folder_neg), "ERROR"), \
        "test negative 2 FAIL"
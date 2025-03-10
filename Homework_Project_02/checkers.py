'''
Файл с функциями для позитивных и негативных тестов (проверок)
'''
import subprocess

# для позитивныз проверок
def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

# для негативных проверок
def checkout_negative(cmd, text):
    result = subprocess.run(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode == 0:
        return True
    else:
        return False
import re

string = "nrobo -a nRoBo -l https://www.saucedemo.com/ -u standard_user -p secret_sauc -n 4 -r 0 -b safari  -t allure"

rex = "(-n[ \d]+)"

print(re.sub(rex, "-n 1 ", string))
import sys
import requests
from bs4 import BeautifulSoup

import tkinter
from tkinter import filedialog
root=tkinter.Tk()
root.withdraw()

def zippy_parser(url):
    url_content = requests.get(url).content
    soup = BeautifulSoup(url_content,'html.parser')

    x = list(soup.find_all('script',type='text/javascript'))
    xx = []
        
    for i in x:
        xx.append(str(i))

    for j in xx:
        if 'var a' and 'var b' in j:
            thing = j
            break
        else:
            pass

    line_list = []

    for l in j.splitlines():
        line_list.append(l)

    a = eval(line_list[5].strip('varb= ;'))
    forb = (line_list[6].split('= '))
    web = eval(forb[1].strip('varb= ;'))
    b = (web * ((a+3)%3))

    url_initial = url.split('/')[2]

    file_code = url.split('/')[4]

    #unique_code = (a//3) + (a%b)
    #unique_code = b+18
    unique_code = (b+18)
    #if unique_code == 0: unique_code = 18

    file_name0 = line_list[-5]
    file_name1 = file_name0.split('/')[-1]
    file_name2 = file_name1.strip('";')

    final_url = f'https://{url_initial}/d/{file_code}/{unique_code}/{file_name2}'

    print(final_url)
    return final_url

print('Press any key to select the txt file with the zippyshare links')
input()

file_path_open = filedialog.askopenfilename(
    initialdir='./',
    title='Please select the txt file with the ZippyShare links',
    filetypes=(('Text file','*.txt'),)
)

opened_file = open(file_path_open,'r')

file_path_closed = filedialog.asksaveasfilename(
    initialdir='./',
    title='Save file',
    filetypes=(('Text file','*.txt'),)
)

closed_file = open(file_path_closed+'.txt','a')

for line in opened_file:
    url = line.strip()
    res = zippy_parser(url)
    closed_file.write(res+'\n')

opened_file.close()
closed_file.close()

print('Press any key to exit')
input()
sys.exit()
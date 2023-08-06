"""
 [*]Wuddz-Password-Generator
    
    Password Types:
        d = Digits
        s = Special Characters
        l = Upper & Lower Case Letters
    
    Usage:
        wudz-pwd passwordlength passwordtype  (Default Password Type = Letters+Digits)
        
    Examples:
        wudz-pwd           =>    Prints Help Document
        wudz-pwd 24        =>    Prints 24 Character Password Consisting Of Letters+Digits
        wudz-pwd 40 d      =>    Prints 40 Character Password Consisting Of Digits
        wudz-pwd 32 ls     =>    Prints 32 Character Password Consisting Of Letters+Special Characters
        wudz-pwd 18 lds    =>    Prints 18 Character Password Consisting Of Letters+Digits+Special Characters
"""
import secrets, sys, platform
from os import system
system('')

def clear_screen(name,c=None):
    if c:input('\n\033[1;32;40m...Hit Enter|Return Key To Clear Screen....\033[0m\n')
    cd={'Linux':'clear','Windows':'clear','Darwin':'printf "\\33c\\e[3J"'}
    if cd.get(name):system(cd[name])

def wudz_pwd():
    pwc=''
    pt='ld'
    name=platform.system()
    clear_screen(name)
    wd={'d':'0123456789','s':'!#$%&()*+,-.:;<=>?@[]^_`{|}~',
        'l':'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    if len(sys.argv)==1 or len(sys.argv)>3:print(f'\033[1;32;40m{__doc__}\033[0m')
    else:
        try:
            pl=int(sys.argv[1])
            if len(sys.argv)==3:pt=sys.argv[2]
            for p in pt:
                pwc+=wd[p]
            print("\n\033[1;32;40mPassword => \033[0m"+''.join(secrets.choice(pwc.strip()) for i in range(pl)))
            clear_screen(name,'c')
        except:print(f'\033[1;32;40m{__doc__}\033[0m')

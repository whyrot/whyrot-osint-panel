import os
import requests


def sherlock():
    username = input('username: ')
    
    os.chdir("/home/whyrot/sherlock")
    os.system(f'python3 sherlock_project {username} --print-found')
    input('\npress enter to return to menu')
    return
def ping():
    print('press ctrl + c to stop ping the ip')
    ip = input("enter ip: ")
    os.system(f'ping {ip}')
    return

def phone():
    API_KEY = "API KEY HERE"
    number = input(f'enter phone number (include the + followed by your country code\nno spaces or dashes)\n: ')
    phone_number = f"{number}"
    url = f'http://apilayer.net/api/validate?access_key={API_KEY}&number={phone_number}&format=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  
 
        if data.get('valid', False):
       
            print(f"Phone Number: {data['number']}")
            print(f"Local Format: {data['local_format']}")
            print(f"International Format: {data['international_format']}")
            print(f"Country: {data['country_name']}")
            print(f"Location: {data['location']}")
            print(f"Carrier: {data['carrier']}")
            print(f"Line Type: {data['line_type']}")
        else:
            print(f"The phone number {phone_number} is invalid.")
    else:
        print(f"Error: {response.status_code}, {response.text}")
    input('\npress enter to return to menu')
    return
def nmap():
    nmapip = input("enter ip: ")
    os.system(f'nmap {nmapip}')
    input('\npress enter to return to menu')
    return

foreverloop = "loop"
while foreverloop == "loop":
    os.system('clear')
    choice = input("""
    tarnla osint panel :p

    1. Username Lookup
    2. IP pinger
    3. Phone Lookup
    4. Scan for open ports on an IP (requires ur own api key read the README)

    0. exit
    : """)

    if choice == "1":
        sherlock()

    elif choice == "2":
        ping()

    elif choice == "3":
        phone()

    elif choice == "4":
        nmap()

    elif choice == "0":
        exit

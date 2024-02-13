#!usr/bin/python
import requests

print("""

           _                             _     
          | |                           | |    
 ___ _   _| |__  ___  ___  __ _ _ __ ___| |__  
/ __| | | | '_ \/ __|/ _ \/ _` | '__/ __| '_ \ 
\__ \ |_| | |_) \__ \  __/ (_| | | | (__| | | |
|___/\__,_|_.__/|___/\___|\__,_|_|  \___|_| |_|
                                               
                                               

 """)
target_url=input("Enter hostname: ")
file = input("Enter the path of the file: ")
def send_request(url):
    try:
        get_response = requests.get("http://" + url)
        return get_response
    except requests.exceptions.ConnectionError:
        pass
with open(file, "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        test_url = word + "." + target_url
        response = send_request(test_url)
        response_code = response
        print("Loading. Please wait..")
        if response:
            print("[+] Discovered subdomain: " + test_url + " >> " + str(response_code))

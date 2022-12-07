from send_script import startBomb

def sendSms():
    print("Sms-bomber UZB\n")
    phone = input("Enter number without '+': ")
    print(phone, phone.startswith("+"))
    counter = input("Enter how much u need to send: ")
    
    if(len(phone) != 13 or phone.startswith("+")is not True): 
        print("Incorrect number!")
        return

    startBomb(phone, int(counter))
    
def main():
    sendSms()

if __name__ == "__main__":
    main();


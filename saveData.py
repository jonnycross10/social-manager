import json
import hashlib


def main(username, password, is_signup):
    user_hash = hashlib.md5(str.encode(username)).hexdigest()
    pass_hash = hashlib.md5(str.encode(password)).hexdigest()

    print(user_hash)
    print(pass_hash)

    credentials = {
        user_hash: pass_hash
    }

    def check_account():
        with open('credentials.json') as crd:
            table = json.load(crd)
            if user_hash in table and pass_hash in table[user_hash]:
                return True, table
            return False, table

    def create_account():
        #If the account exists, return nothing
        accounts = None
        with open('credentials.json') as crd:
            accounts = json.load(crd)
            if user_hash in accounts:
                return

        with open('credentials.json', 'w') as crd:
            accounts[user_hash] = credentials[user_hash]
            crd.write(json.dumps(accounts))
            return credentials

    if is_signup:
        if (create_account()):
            print('Account created')
            return username
        else: 
            print('Account already exists')
            return None

    does_exist, _ = check_account()
    if does_exist:
        print('Logged in')
        return username
    else:
        print('Account does not exist')
        return None

if __name__ == '__main__':
    username = "@gmail.com"
    password = "1234567"
    profile_name = main(username,password, is_signup=False)
    if(profile_name):
        print('Hello, ' + str(username))



#read in username✔
#hash username✔
#read in the json file✔
#see if any hashed usernames match✔
#object that contains user info and ability to email
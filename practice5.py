import datetime

def create_membership():
		# 아래 코드는 python에 내장되어 있는 datetime 모듈을 활용하여 오늘 날짜를 입력하는 코드입니다. 
		# stnr_date 코드는 제가 작성했으니, 건드리지 않으셔도 되옵니다 :)
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    users = []
    
    while True:
        user = {}


		# user 딕셔너리에 username, password, email을 아래 주어진 제한 조건에 알맞게 입력받는 코드를 작성하세요.
	  # user 딕셔너리 값에는 username, password, email, stnr_date 총 4가지 값이 저장되어야 합니다.


#아이디
        username = (input("ID: "))
        lst_username = list(username)
        for i in lst_username:
            if not ord('가') <= ord(i) <= ord('힣'):
                print('ID는 한글만 입력 가능합니다')
                exit()

        if len(lst_username) > 4:
            print("ID는 2~4글자만 가능합니다")
            exit()
        elif len(lst_username) < 2:
            print("ID는 2~4글자만 가능합니다")
            exit()
        else:
            user['ID'] = username


#비밀번호
        password = (input("Password: "))
        lst_password = list(password)

        k = 0
        for i in lst_password:
            if i in ['!', '@', '#', '$']:
                k += 1

        if k == 0:
            print('비밀번호에 특수문자를 넣어주세요')
            exit()

        if not ord('A') <= ord(lst_password[0]) <= ord('Z'):
            print('비밀번호의 첫 문자는 영문 대문자로 입력해주세요!')
            exit()
        elif len(password) < 8:
            print('비밀번호는 8자 이상 입력해주세요!')
            exit()
        else:
            user['Password'] = password


#이메일
        email = input("Email: ")
        lst_email = list(email)

        for i in lst_email:
            if ord('a') <= ord(i.lower()) <= ord('z'):
                pass
            elif i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '@']:
                pass
            else:
                print('잘못된 양식입니다')
                exit()

        if lst_email[-1] != 'm':
            print('이메일 주소는 .com으로 끝나야 합니다')
            exit()
        elif lst_email[-2] != 'o':
            print('이메일 주소는 .com으로 끝나야 합니다')
            exit()
        elif lst_email[-3] != 'c':
            print('이메일 주소는 .com으로 끝나야 합니다')
            exit()
        elif lst_email[-4] != '.':
            print('이메일 주소는 .com으로 끝나야 합니다')
            exit()
        elif '@' not in lst_email:
            print('@기호를 넣어주세요')
        else:
            user['Email'] = email

        user['stnr_date'] = stnr_date
        users.append(user)

        print(user)
        print(users)
        add = input("추가 등록을 하시겠습니까?(Y or N)")
        if add.upper() == "Y":
            continue
        else:
            break
    return users


def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    for i in user_list:
        s_txt = i['ID'] + ", " + i['Password'] + ", " + i['Email'] + ", " + i['stnr_date']
        f.write(s_txt + "\n")
    f.close()
    # user_list에 있는 user 3명의 딕셔너리 값을 txt에 작성하세요.
	  # 올바르게 생성된 텍스트 파일i의 예시는 상단에 이미지로 첨부되어 있습니다.

    
def run():
		# 위에서 정의한 create_membership 함수가 실행되어 반환된 결과값을 user_list 객체에 저장합니다.
    user_list = create_membership()
    # 위에 생성된 user_list 객체를 load_to_txt 함수의 입력변수로 활용하여 txt 파일을 생성합니다.
    load_to_txt(user_list)

run()



# 사람 정보를 담는 클레스
class PersonInfo:
    # 맴버변수
    name = ''
    email = ''
    phone = ''
    # 생성자
    def __init__(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phoneNum = phone


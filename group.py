
class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, company, adress,
                 home_phone, mobile_phone, work_phone, fax, email_1, email_2,
                 email_3, homepage, birth_day, birth_month, birth_year, adress_2, phone_2, notes):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
#        self.photo = photo
        self.company = company
        self.adress = adress
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.adress_2 = adress_2
        self.phone_2 = phone_2
        self.notes = notes



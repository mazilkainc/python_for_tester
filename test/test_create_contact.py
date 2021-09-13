# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Jack", middlename="Cristopher", lastname="Depp",
                               nickname="Sparrow", company="Pirates", adress="Black Pearl",
                               home_phone="1234567890", mobile_phone="0987654321", work_phone="0129834765",
                               fax="777777777777", email_1="test1@mail.ru", email_2="test1@gmail.com",
                               email_3="test1@outlook.com", homepage="pirates.com", birth_day="9",
                               birth_month="July", birth_year="1708", adress_2="Caribbean sea",
                               phone_2="Black", notes="bla, bla"))
    app.session.logout()



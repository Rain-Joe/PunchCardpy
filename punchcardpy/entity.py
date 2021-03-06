# -*- coding: UTF-8 -*-

class People:
    """
    学生类
    """
    data = {}
    email = ''
    number = ''
    name = ''
    academy = ''
    clazz = ''
    addressnumber = ''
    address = ''
    status = ''
    code = ''

    def __init__(self, self_information):
        self.data = self_information
        self.email = self_information['email']
        self.number = self_information['number']
        self.name = self_information['name']
        self.academy = self_information['academy']
        self.clazz = self_information['clazz']
        self.addressnumber = self_information['addressnumber']
        self.address = self_information['province'] + self_information['city'] + self_information['country']
        self.status = self_information['status']
        self.code = self_information['code']


class PCRecord:
    """
    日志实体
    """
    date = ''
    pcstatuscode = ''
    pcstatusmsg = ''
    people = any

    def __init__(self, pc_log_dict):
        self.people = People(pc_log_dict)
        self.date = pc_log_dict['pcdate']
        self.pcstatuscode = pc_log_dict['pcstatuscode']
        self.pcstatusmsg = pc_log_dict['pcstatusmsg']

import datetime
class Target:
    def __init__(self, goals, category, status, number, date):
        self.__target3 = ''
        self.__goals = goals
        self.__category = category
        self.__status = status
        self.__number = number
        self.__date = date
    def get_goals(self):
        return self.__goals

    def get_category(self):
        return self.__category

    def get_status(self):
        return self.__status

    def get_number(self):
        return self.__number

    def get_date(self):
        return self.__date

    def set_goals(self, goals):
        self.__goals = goals

    def set_category(self, category):
        self.__category = category

    def set_status(self, status):
        self.__status = status

    def set_number(self, number):
        self.__number = number

    def set_date(self, date):
        self.__date = date

#    def set_enddate(self, enddate):
#        self.__enddate = enddate

    def get_target3(self):
        return self.__target3

    def set_target3(self, target3):
        self.__target3 = target3
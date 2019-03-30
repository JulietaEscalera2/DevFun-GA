from time import strftime
from PyQt5.QtCore import QDateTime, Qt, QDate, QTime
# from src.com.jalasoft.SearchFile.controller.controller import Controller

class ConvertorSize:

    def get_size_value(self, file_size, file_size_unit):
        # file_size =  get_file_size
        # file_size_unit = get_size_combo
        # file_size = parameterSize.__init_search(__file_size)
        # file_size_unit  = parameterSize.__init_search(__file_size_unit)
        if file_size_unit == 'Bytes':
            return file_size
        if file_size_unit == 'Kb':
            return file_size * 1024
        if file_size_unit == 'Mb':
            return file_size * 1024 * 1024
        if file_size_unit == 'Gb':
            return file_size * 1024 * 1024 * 1024

    # March 27 2019 with strftime('%d%b%Y') --> https://www.programiz.com/python-programming/datetime/strftime
    # def get_calendar_value(self, file_date, date):
    #     file_date = Controller.__init_search()
    #     date = strftime('%b%d%Y')


# strftime('%d%b%Y') #March 27 2019
# datetime = QDateTime.currentDateTime()
# print(datetime.toString())
# print(datetime.toString(Qt.ISODate))
# print(datetime.toString(Qt.DefaultLocaleLongDate))
#
# date = QDate.currentDate()
# print(date.toString())
# print(date.toString(Qt.ISODate))
# print(date.toString(Qt.DefaultLocaleLongDate))
#
#
# time = QTime.currentTime()
# print(time.toString())
# print(time.toString(Qt.ISODate))
# print(time.toString(Qt.DefaultLocaleLongDate))
#
# from datetime import datetime
#
# now = datetime.now() # current date and time March 27 2019
# x = now.strftime('%b%d%Y')
# print("format:",x)
# year = now.strftime("%Y")
# print("year:", year)
#
# month = now.strftime("%m")
# print("month:", month)
#
# day = now.strftime("%d")
# print("day:", day)
#
# time = now.strftime("%H:%M:%S")
# print("time:", time)
#
# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)
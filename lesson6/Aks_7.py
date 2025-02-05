"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""



from pyowm import OWM
from pprint import pprint

owm = OWM('87b7c330daf2579649274a648d33f753')
mgr = owm.weather_manager()


city = input('Введите город: ')
obs = mgr.weather_at_place(city)
w = obs.to_dict()



pprint(w['weather'])
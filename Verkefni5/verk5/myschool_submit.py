#!/bin/python
import requests
from bs4 import BeautifulSoup
import getpass
from requests.auth import HTTPBasicAuth
import json


def main():
	URL = 'https://myschool.ru.is/myschool/'
	pword = getpass.getpass()

	#payload = {'File':'Users/BH/Desktop/verk5/ipod.zip'}
	#headers = {'Content-type':'application/json','Accept':'text/plain'}
	fileobj = open('/Users/BH/Desktop/verk5/ipod.zip','rb')
	#files = {''}
	#payload = {'hopmedlimur2':'0509902499'}
	#soup = BeautifulSoup(res.text)
	res = requests.post(URL + '?Page=LMS&ID=16&fagID=27587&View=&ViewMode=2&Tab=&Act=11&verkID=54380',data=payload,auth=HTTPBasicAuth('einarh13',pword))
	print(res)
	#print(res.text)






if __name__ == '__main__':
    main()



































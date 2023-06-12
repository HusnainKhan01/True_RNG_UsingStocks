#!/usr/bin/env python2
"""True Random Number Generator"""

# Write a true random number generator. In order to do so, you have to
# identify a source of true randomness. 
#
# the function shall output 20000 random bits as byte values,
# i.e. it should write a file of 2500 random bytes.

FILENAME='random.dat'
N=2500

import subprocess
import requests
from bs4 import BeautifulSoup

def getStocks():
    url = ('https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD')
    r1 = requests.get(url)
    web_content = BeautifulSoup(r1.text, 'lxml')
    idx = 0
    list = [None] * 400
    j = 0
    for i in range(100):
        j = 0
        for x in range(4):
            web_content1 = web_content.find_all('tr', {"class": 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})[i]
            web_content1 = web_content1.find_all('td', {"class": 'Py(10px) Pstart(10px)'})[j]
            j += 1
            list[idx] = web_content1.text
            idx += 1
    ######
    rn = [None] * 400
    for i in range(400):
        num1 = list[i][8]
        num2 = list[i][7]
        num3 = list[i][5]
        if num1 == '.' or num1 == ',':
            num1 = '0'
        if num2 == '.' or num2 == ',':
            num2 = '0'
        if num3 == '.' or num3 == ',':
            num3 = '0'

        f1 = int(num1)
        f2 = int(num2)
        f3 = int(num3)
        randNum = f1 * 10
        randNum = randNum + f2
        randNum = randNum * 10
        randNum = randNum + f3
        randNum = randNum % 256

        str_val = str(randNum)
        byte_val = str_val.encode()
        rn[i] = byte_val

    return rn

def getUsdEuro():
    url = ('https://finance.yahoo.com/quote/EURUSD%3DX/history?p=EURUSD%3DX')
    r1 = requests.get(url)
    web_content = BeautifulSoup(r1.text, 'lxml')

    # working part #####
    idx = 0
    list = [None] * 400
    j = 0
    for i in range(100):
        j = 0
        for x in range(4):
            web_content1 = web_content.find_all('tr', {"class": 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})[i]
            web_content1 = web_content1.find_all('td', {"class": 'Py(10px) Pstart(10px)'})[j]
            j += 1
            list[idx] = web_content1.text
            idx += 1
    ######
    rn = [None] * 400
    for i in range(400):
        num1 = list[i][5]
        num2 = list[i][4]
        num3 = list[i][3]
        if num1 == '.' or num1 == ',':
            num1 = '0'
        if num2 == '.' or num2 == ',':
            num2 = '0'
        if num3 == '.' or num3 == ',':
            num3 = '0'

        f1 = int(num1)
        f2 = int(num2)
        f3 = int(num3)
        randNum = f1 * 10
        randNum = randNum + f2
        randNum = randNum * 10
        randNum = randNum + f3
        randNum = randNum % 256

        str_val = str(randNum)
        byte_val = str_val.encode()
        rn[i] = byte_val

    return rn

def getGold():
    url = ('https://finance.yahoo.com/quote/GC%3DF/history?p=GC%3DF')
    r1 = requests.get(url)
    web_content = BeautifulSoup(r1.text, 'lxml')
    idx = 0
    list = [None] * 400
    j = 0
    for i in range(100):
        j = 0
        for x in range(4):
            web_content1 = web_content.find_all('tr', {"class": 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})[i]
            web_content1 = web_content1.find_all('td', {"class": 'Py(10px) Pstart(10px)'})[j]
            j += 1
            list[idx] = web_content1.text
            idx += 1
    ######
    rn = [None] * 400
    for i in range(400):
        num1 = list[i][6]
        num2 = list[i][7]
        num3 = list[i][4]
        if num1 == '.' or num1 == ',':
            num1 = '0'
        if num2 == '.' or num2 == ',':
            num2 = '0'
        if num3 == '.' or num3 == ',':
            num3 = '0'

        f1 = int(num1)
        f2 = int(num2)
        f3 = int(num3)
        randNum = f1 * 10
        randNum = randNum + f2
        randNum = randNum * 10
        randNum = randNum + f3
        randNum = randNum % 256

        str_val = str(randNum)
        byte_val = str_val.encode()
        rn[i] = byte_val

    return rn

def getNasdaQ():
    url = ('https://finance.yahoo.com/quote/%5EIXIC/history?p=%5EIXIC')
    r1 = requests.get(url)
    web_content = BeautifulSoup(r1.text, 'lxml')
    idx = 0
    list = [None] * 400
    j = 0
    for i in range(100):
        j = 0
        for x in range(4):
            web_content1 = web_content.find_all('tr', {"class": 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})[i]
            web_content1 = web_content1.find_all('td', {"class": 'Py(10px) Pstart(10px)'})[j]
            j += 1
            list[idx] = web_content1.text
            idx += 1
    ######
    rn = [None] * 400
    for i in range(400):
        num1 = list[i][8]
        num2 = list[i][7]
        num3 = list[i][5]
        if num1 == '.' or num1 == ',':
            num1 = '0'
        if num2 == '.' or num2 == ',':
            num2 = '0'
        if num3 == '.' or num3 == ',':
            num3 = '0'

        f1 = int(num1)
        f2 = int(num2)
        f3 = int(num3)
        randNum = f1 * 10
        randNum = randNum + f2
        randNum = randNum * 10
        randNum = randNum + f3
        randNum = randNum % 256

        str_val = str(randNum)
        byte_val = str_val.encode()
        rn[i] = byte_val

    return rn


def getGbpUsd():
    url = ('https://finance.yahoo.com/quote/GBPUSD%3DX/history?p=GBPUSD%3DX')
    r1 = requests.get(url)
    web_content = BeautifulSoup(r1.text, 'lxml')

    # working part #####
    idx = 0
    list = [None] * 400
    j = 0
    for i in range(100):
        j = 0
        for x in range(4):
            web_content1 = web_content.find_all('tr', {"class": 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})[i]
            web_content1 = web_content1.find_all('td', {"class": 'Py(10px) Pstart(10px)'})[j]
            j += 1
            list[idx] = web_content1.text
            idx += 1
    ######
    rn = [None] * 400
    for i in range(400):
        num1 = list[i][5]
        num2 = list[i][4]
        num3 = list[i][3]
        if num1 == '.' or num1 == ',':
            num1 = '0'
        if num2 == '.' or num2 == ',':
            num2 = '0'
        if num3 == '.' or num3 == ',':
            num3 = '0'

        f1 = int(num1)
        f2 = int(num2)
        f3 = int(num3)
        randNum = f1 * 10
        randNum = randNum + f2
        randNum = randNum * 10
        randNum = randNum + f3
        randNum = randNum % 256

        str_val = str(randNum)
        byte_val = str_val.encode()
        rn[i] = byte_val

    return rn

def getjpyUsd():
    url = ('https://finance.yahoo.com/quote/JPY%3DX/history?p=JPY%3DX')
    r1 = requests.get(url)
    web_content = BeautifulSoup(r1.text, 'lxml')

    # working part #####
    idx = 0
    list = [None] * 400
    j = 0
    for i in range(100):
        j = 0
        for x in range(4):
            web_content1 = web_content.find_all('tr', {"class": 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})[i]
            web_content1 = web_content1.find_all('td', {"class": 'Py(10px) Pstart(10px)'})[j]
            j += 1
            list[idx] = web_content1.text
            idx += 1
    ######
    rn = [None] * 400
    for i in range(400):
        num1 = list[i][5]
        num2 = list[i][4]
        num3 = list[i][6]
        if num1 == '.' or num1 == ',':
            num1 = '0'
        if num2 == '.' or num2 == ',':
            num2 = '0'
        if num3 == '.' or num3 == ',':
            num3 = '0'

        f1 = int(num1)
        f2 = int(num2)
        f3 = int(num3)
        randNum = f1 * 10
        randNum = randNum + f2
        randNum = randNum * 10
        randNum = randNum + f3
        randNum = randNum % 256

        str_val = str(randNum)
        byte_val = str_val.encode()
        rn[i] = byte_val

    return rn

def getDow30():
    url = ('https://finance.yahoo.com/quote/%5EDJI/history?p=%5EDJI')
    r1 = requests.get(url)
    web_content = BeautifulSoup(r1.text, 'lxml')

    # working part #####
    idx = 0
    list = [None] * 100
    j = 0
    for i in range(100):
        web_content1 = web_content.find_all('tr', {"class": 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})[i]
        web_content1 = web_content1.find_all('td', {"class": 'Py(10px) Pstart(10px)'})[4]
        list[idx] = web_content1.text
        idx += 1

    ######
    rn = [None] * 100
    for i in range(100):
        num1 = list[i][8]
        num2 = list[i][7]
        num3 = list[i][4]
        if num1 == '.' or num1 == ',':
            num1 = '0'
        if num2 == '.' or num2 == ',':
            num2 = '0'
        if num3 == '.' or num3 == ',':
            num3 = '0'

        f1 = int(num1)
        f2 = int(num2)
        f3 = int(num3)
        randNum = f1 * 10
        randNum = randNum + f2
        randNum = randNum * 10
        randNum = randNum + f3
        randNum = randNum % 256

        str_val = str(randNum)
        byte_val = str_val.encode()
        rn[i] = byte_val

    return rn


def trng(filename, n):
    rn = []
    list1 = getDow30()
    list2 = getGold()
    list3 = getjpyUsd()
    list4 = getNasdaQ()
    list5 = getGbpUsd()
    list6 = getStocks()
    list7 = getUsdEuro()

    List = [None] * 2500
    for i in range(100):
        List[i] = list1[i]
    j = 100
    for i in range(400):
        List[j + i] = list2[i]
    j = 500
    for i in range(400):
        List[j + i] = list3[i]
    j = 900
    for i in range(400):
        List[j + i] = list4[i]
    j = 1300
    for i in range(400):
        List[j + i] = list5[i]
    j = 1700
    for i in range(400):
        List[j + i] = list6[i]
    j = 2100
    for i in range(400):
        List[j + i] = list7[i]
    rn = List
    ##################
    rnFile = open(filename, 'wb')
    for i in rn:
        rnFile.write(i)
    rnFile.close()


if __name__ == "__main__":
    trng(filename=FILENAME, n=N)




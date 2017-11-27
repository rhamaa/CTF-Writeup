#!/usr/bin/python
# Credit to : https://stackoverflow.com/questions/21079439/implementation-of-luhn-formula
# Credit to : https://github.com/grahamking/darkcoding-credit-card

"""
gencc: A simple program to generate credit card numbers that pass the
MOD 10 check (Luhn formula).
Usefull for testing e-commerce sites during development.
Copyright 2003-2012 Graham King
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

# Flag
# flag{ch3ck-exp3rian-dat3-b3for3-us3}

from pwn import *
import json
from subprocess import check_output
from time import sleep
from random import Random
import copy
import sys

visaPrefixList = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4'],
        ['4', '0'],['4', '1'],['4', '2'],['4', '3'],['4', '4'],['4', '5'],
        ['4', '6'],['4', '7'],['4', '8'],['4', '9']]

mastercardPrefixList = [
        ['5', '1'],
        ['5', '2'],
        ['5', '3'],
        ['5', '4'],
        ['5', '5'],
        ['5', '6'],
        ['5', '7'],
        ['5', '8'],
        ['5', '9'],
        ['5', '0']]
mastercardPrefixList_2 = [
        ['5', '1'],
        ['5', '2'],
        ['5', '3'],
        ['5', '4'],
        ['5', '5'],
        ['2', '2', '2', '1'],
        ['2', '2', '2', '2'],
        ['2', '2', '2', '3'],
        ['2', '2', '2', '4'],
        ['2', '2', '2', '5'],
        ['2', '2', '2', '6'],
        ['2', '2', '2', '7'],
        ['2', '2', '2', '8'],
        ['2', '2', '2', '9'],
        ['2', '2', '3'],
        ['2', '2', '4'],
        ['2', '2', '5'],
        ['2', '2', '6'],
        ['2', '2', '7'],
        ['2', '2', '8'],
        ['2', '2', '9'],
        ['2', '3'],
        ['2', '2'],
        ['2', '4'],
        ['2', '5'],
        ['2', '6'],
        ['2', '7'],
        ['2', '8'],
        ['2', '9'],
        ['2', '7', '0'],
        ['2', '7', '1'],
        ['2', '7', '2', '0']]
amexPrefixList = [['3', '0'], ['3', '1'],['3', '2'], ['3', '3'],['3', '4'], ['3', '5'],['3', '6'], ['3', '7']
,['3', '8'], ['3', '9']]

discoverPrefixList = [['6', '0', '1', '1'],['6', '0'],['6', '1'],['6', '2'],['6', '3'],['6', '4'],['6', '5'],
['6', '6'],['6', '7'],['6', '8'],['6', '9']]

dinersPrefixList = [
        ['3', '0', '0'],
        ['3', '0', '1'],
        ['3', '0', '2'],
        ['3', '0', '3'],
        ['3', '6'],
        ['3', '8']]
unknowPrefixList = [['9','0'],['9','1'],['9','2'],['9','3'],['9','4'],['9','5'],['9','6'],['9','7'],['9','8']
,['9','9'],['8','0'],['8','1'],['8','2'],['8','3'],['8','4'],['8','5'],['8','6'],['8','7'],['8','8']
,['8','9'],['7','0'],['7','1'],['7','2'],['7','3'],['7','4'],['7','5'],['7','6'],['7','7'],['7','8']
,['7','9'],['1','0'],['1','1'],['1','2'],['1','3'],['1','4'],['1','5'],['1','6'],['1','7'],['1','8']
,['1','9']]
unknowPrefixList_2 = [['9'],['8'],['7'],['6'],['5'],['4'],['3'],['2'],['1'],['0']]
enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]

jcbPrefixList = [['3', '5']]

voyagerPrefixList = [['8', '6', '9', '9']]


def completed_number(prefix, length):
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(checkdigit))

    return ''.join(ccnumber)


def credit_card_number(rnd, prefixList, length, howMany):

    result = []

    while len(result) < howMany:

        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))

    return result

def credit_card_number_by_bin(rnd, prefixList, length, howMany,BIN):
    result = ""
    while 1:
        ccnumber = copy.copy(rnd.choice(prefixList))
        result = completed_number(ccnumber, length)
        tmp_res = "".join(result)
        #print tmp_res
        if tmp_res[:4] == BIN:
            return result
        else:
            continue
    return "1337"

def credit_card_number_by_end4(rnd, prefixList, length, howMany,ENDS):
    result = ""
    while 1:
        ccnumber = copy.copy(rnd.choice(prefixList))
        result = completed_number(ccnumber, length)
        tmp_res = "".join(result)
        #print tmp_res
        if tmp_res[-4:] == ENDS:
            return result
        else:
            continue
    return "1337"

def credit_card_number_by_end(rnd, prefixList, length, howMany,ENDS):
    result = ""
    while 1:
        ccnumber = copy.copy(rnd.choice(prefixList))
        result = completed_number(ccnumber, length)
        tmp_res = "".join(result)
        if tmp_res[-1] == ENDS[0]:
            return result
        else:
            continue
    return "1337"

def cc_number_by_bin_result(BIN):
        BIN_PREFIX = list(BIN[0]+BIN[1])
        # print BIN_PREFIX
        if BIN_PREFIX in mastercardPrefixList:
            mastercard = credit_card_number_by_bin(generator, mastercardPrefixList, 16, 1,BIN)
            return mastercard
        elif BIN_PREFIX in mastercardPrefixList_2:
            mastercard = credit_card_number_by_bin(generator, mastercardPrefixList_2, 16, 1,BIN)
            return mastercard
        elif BIN_PREFIX in visaPrefixList:
            visa = credit_card_number_by_bin(generator, visaPrefixList, 16, 1,BIN)
            return visa
        elif BIN_PREFIX in amexPrefixList:
            amex = credit_card_number_by_bin(generator, amexPrefixList, 16, 1,BIN)
            return amex
        elif BIN_PREFIX in discoverPrefixList:
            discover = credit_card_number_by_bin(generator, discoverPrefixList, 16, 1,BIN)
            return discover
        elif BIN_PREFIX in unknowPrefixList:
            unk = credit_card_number_by_bin(generator, unknowPrefixList, 16, 1,BIN)
            return unk
        else:
            unk = credit_card_number_by_bin(generator, unknowPrefixList_2, 16, 1,BIN)
            return unk

def cc_number_by_end_result(ENDS):
        ENDS = list(ENDS)
        # prefix_list = [discoverPrefixList]
        cc_num = credit_card_number_by_end(generator, discoverPrefixList, 16, 1,ENDS)
        return cc_num

def cc_number_by_end_4_result(ENDS):
        prefix_list = [discoverPrefixList,mastercardPrefixList]
        cc_num = credit_card_number_by_end4(generator, random.choice(prefix_list), 16, 1,ENDS)
        return cc_num

def cc_number_by_vendor_result(VENDOR):
    if VENDOR == "MasterCard":
        mastercard = credit_card_number(generator, mastercardPrefixList, 16, 1)
        return mastercard
    elif VENDOR == "Visa":
        visa16 = credit_card_number(generator, visaPrefixList, 16, 1)
        return visa16
    elif VENDOR == "Express":
        amex = credit_card_number(generator, amexPrefixList, 15, 1)
        return amex
    elif VENDOR == "Discover":
        discover = credit_card_number(generator, discoverPrefixList, 16, 1)
        return discover

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


generator = Random()
generator.seed()        # Seed from current time

LEVEL = 3
if LEVEL == 1:
    # VENDOR = sys.argv[1]
    print cc_number_by_vendor_result(VENDOR)
elif LEVEL == 2:
    print cc_number_by_bin_result(BIN)


r = remote("misc.chal.csaw.io", 8308)

x = 0

# Get From Here : http://www.getcreditcardnumbers.com/
discover = json.loads(open("discover.json").read())
visa = json.loads(open("visa.json").read())
mastercard = json.loads(open("mastercard.json").read())
amex = json.loads(open("amex.json").read())
cc=""

soal = r.recv(2048).strip()
while soal:
    try:
        soal = soal.split(" ")
        if "Discover" in soal[4]:
            cc = str(discover[x]['CreditCard']['CardNumber'])
            x += 1
        elif "Visa" in soal[4]:
            cc = str(visa[x]['CreditCard']['CardNumber'])
            x += 1
        elif "MasterCard" in soal[4]:
            cc = str(mastercard[x]['CreditCard']['CardNumber'])
            x += 1
        elif "Amer" in soal[4]:
            cc = str(amex[x]['CreditCard']['CardNumber'])
            x += 1

        #print soal
        if "starts" in soal:
            bin_prefix = soal[-1].replace("!","")
            cc = cc_number_by_bin_result(bin_prefix)
        elif "ends" in soal:
            bin_prefix = soal[-1].replace("!","")
            if len(bin_prefix) == 4:
                cc = cc_number_by_end_4_result(bin_prefix)
            else:
                cc = cc_number_by_end_result(bin_prefix)
        elif "valid!" in soal:
            cc_number = soal[5]
            if len(cc_number) == 16:
                result = is_luhn_valid(int(cc_number))
                if result:
                    cc = "1"
                else:
                    cc = "0"
            else:
                cc = "0"

        print "[Send] : " + cc
        r.send(cc+chr(0x0a))
        soal = r.recv(2048).strip()
    except:
        if "flag{" in soal[0]:
            print "Flag %s " % (soal[0].split("\n")[-1])
            print "Flag %s " % (soal[0].split("\n")[-1])
            print "Flag %s " % (soal[0].split("\n")[-1])
            break

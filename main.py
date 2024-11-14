#!D:\Python\Python39\python.exe
import traceback
import xml.etree.ElementTree as ET
import re
import requests
from log import getLogger

logger = getLogger('crmsmdm', 'logs/crmsmdm')

mdmendpoint = "http://172.25.40.234:8080/eml/services/router";

crmsendpoint= "http://172.25.40.167/crmsapi/ws/crmsapi.php?wsdl";

headers = {'SOAPAction': 'MasterCatalogRecordAction', 'Content-Type': 'text/xml; charset=utf-8'}


def start(crno):
    xmlfile = open('files/Start Point.xml', 'r')
    body = xmlfile.read()

    try:
        response = requests.request("POST", mdmendpoint,headers=headers,
                                    data=body.format(CRNO=crno))
        #print(response.request.body)

        #print(response.text)
        logger.info("Start : =========================================================================")
        logger.info(response.request.body)

        logger.info("Response : =================================")
        print(response.status_code)
        logger.info(response.text)
        logger.info("End : =========================================================================")

        ResultCode = re.findall("<SuccessCount>(.*?)</SuccessCount>", str(response.content))
        #print(ResultCode[0])

        return str(ResultCode[0])
    except Exception as e:
        #print("Exception : %s" % traceback.format_exc())
        return str(e)


def apcsync(crno):
    xmlfile = open('files/APC Sync Point.xml', 'r')
    body = xmlfile.read()

    try:
        response = requests.request("POST", mdmendpoint,headers=headers,
                                    data=body.format(CRNO=crno))
        #print(response.request.body)

        #print(response.text)
        logger.info("Start : =========================================================================")
        logger.info(response.request.body)

        logger.info("Response : =================================")
        #print(response.status_code)
        logger.info(response.text)
        logger.info("End : =========================================================================")

        ResultCode = re.findall("<SuccessCount>(.*?)</SuccessCount>", str(response.content))
        #print(ResultCode[0])

        return str(ResultCode[0])
    except Exception as e:
        #print("Exception : %s" % traceback.format_exc())
        return str(e)


def preuatsucc(crno):
    xmlfile = open('files/Pre UAT Success Point.xml', 'r')
    body = xmlfile.read()

    try:
        response = requests.request("POST", mdmendpoint,headers=headers,
                                    data=body.format(CRNO=crno))
        #print(response.request.body)

        #print(response.text)
        logger.info("Start : =========================================================================")
        logger.info(response.request.body)

        logger.info("Response : =================================")
        #print(response.status_code)
        logger.info(response.text)
        logger.info("End : =========================================================================")

        ResultCode = re.findall("<SuccessCount>(.*?)</SuccessCount>", str(response.content))
        #print(ResultCode[0])

        return str(ResultCode[0])
    except Exception as e:
        #print("Exception : %s" % traceback.format_exc())
        return str(e)


def uatsucc(crno):
    xmlfile = open('files/UAT Success Point.xml', 'r')
    body = xmlfile.read()

    try:
        response = requests.request("POST", mdmendpoint,headers=headers,
                                    data=body.format(CRNO=crno))
        #print(response.request.body)

        #print(response.text)
        logger.info("Start : =========================================================================")
        logger.info(response.request.body)

        logger.info("Response : =================================")
        #print(response.status_code)
        logger.info(response.text)
        logger.info("End : =========================================================================")

        ResultCode = re.findall("<SuccessCount>(.*?)</SuccessCount>", str(response.content))
        #print(ResultCode[0])

        return str(ResultCode[0])
    except Exception as e:
        #print("Exception : %s" % traceback.format_exc())
        return str(e)


def uatfail(crno):

    xmlfile = open('files/UAT Failed Point.xml', 'r')
    body = xmlfile.read()

    try:
        response = requests.request("POST", mdmendpoint,headers=headers,
                                    data=body.format(CRNO=crno))
        #print(response.request.body)

        #print(response.text)
        logger.info("Start : =========================================================================")
        logger.info(response.request.body)

        logger.info("Response : =================================")
        #print(response.status_code)
        logger.info(response.text)
        logger.info("End : =========================================================================")

        ResultCode = re.findall("<SuccessCount>(.*?)</SuccessCount>", str(response.content))
        #print(ResultCode[0])

        return str(ResultCode[0])
    except Exception as e:
        #print("Exception : %s" % traceback.format_exc())
        return str(e)

if __name__ == '__main__':
    start('CR_00515')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
import time


class lightOperation:
    __topic = "switch"
    __broker = "192.168.3.121"
    __mqttCient = mqtt.Client()
    __msg = {
        "target": "switch01",
        "value": "0"
    }

    def __init__(self):
        self.__mqttCient = mqtt.Client()
        self.__mqttCient.connect(self.__broker)

    def setTopic(self, value):
        self.__topic = value

    def setBroker(self, value):
        self.__broker = value

    def __jsonGen(self, value):
        self.__msg["value"] = value
        jsonData = json.dumps(self.__msg)
        # print("print data:")
        # print(jsonData)
        return jsonData

    def setTarget(self, target):
        self.__msg["target"] = target


    def light_on(self):
        self.__mqttCient.reconnect()
        self.__mqttCient.publish(self.__topic, self.__jsonGen("1"))

    def light_off(self):
        self.__mqttCient.reconnect()
        self.__mqttCient.publish(self.__topic, self.__jsonGen("0"))

def main():
    switch = lightOperation()
    switch.light_on()
    time.sleep(5)
    switch.light_off()
    time.sleep(5)

if __name__ == '__main__':
    main()

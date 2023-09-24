def publisher(brokerAdres,userNam,passwor,topic):
    import random
    import time
    import paho.mqtt.client as mqtt
    userName="{}".format(userNam)
    print(userName)
    brokerAdress="{}".format(brokerAdres)
    print(brokerAdress)
    password="{}".format(passwor)
    '''
    wait=int(waitt)
    print(wait)'''

    def on_connnect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected succesfully")
        else:
            print("Connected returned result code:", str(rc))

    def on_message(client, userdata, message):
        print("Received message:" + message.topic + "=>>" + message.payload.decode("utf-8"))


    client = mqtt.Client()
    client.on_connect = on_connnect
    client.on_message = on_message

    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    client.username_pw_set(userName, password)
    client.connect(brokerAdress, 8883)

    min = 10
    max = 100
    while True:
        data = random.randint(min, max)
        client.publish(topic, data)
        print(data)
        time.sleep(1)
        return data


def subscriber(brokerAdres,userNam,passwor,topic):
    import random
    import time
    import paho.mqtt.client as mqtt
    userName="{}".format(userNam)
    brokerAdress="{}".format(brokerAdres)
    password="{}".format(passwor)


    def on_connnect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected succesfully")
        else:
            print("Connected returned result code:", str(rc))

    received_mesage_list = []

    def on_message(client, userdata, message):
        mes=message.decode('utf-8')
        received_mesage_list.append(mes)
        print("Received message:" + message.topic + "=>>" + message.payload.decode("utf-8"))


    client = mqtt.Client()
    client.on_connect = on_connnect
    client.on_message = on_message

    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    client.username_pw_set(userName, password)
    client.connect(brokerAdress, 8883)
    client.subscribe(topic)
    client.loop_forever()
    print(received_mesage_list)


def sub(userNam,brokerAdres,passwor,topi):
    import time
    import paho.mqtt.client as mqtt
    userName="{}".format(userNam)
    brokerAdress="{}".format(brokerAdres)
    password="{}".format(passwor)
    topic = "{}".format(topi)

    def on_connnect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected succesfully")
        else:
            print("Connected returned result code:", str(rc))

    received_mesage_list = []

    def on_message(client, userdata, message):
        received_mesage_list.append(message.payload.decode('utf-8'))
        print("Received message:" + message.topic + "=>>" + message.payload.decode("utf-8"))

    client = mqtt.Client()
    client.on_connect = on_connnect
    client.on_message = on_message

    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    client.username_pw_set(userName, password)
    client.connect(brokerAdress, 8883)

    client.subscribe(topic,1)
    # client.loop_forever()
    #client.loop_forever()
    #print(received_mesage_list)
    count=20
    while count:
        client.loop_start()
        print(received_mesage_list)
        client.loop_stop()
        count=count-1

    print(received_mesage_list)

    return received_mesage_list




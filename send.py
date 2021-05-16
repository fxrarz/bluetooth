from bluetool import Bluetooth
import bluetooth
import subprocess
import time

btool = Bluetooth()
#btool.scan()
#devices = btool.get_available_devices()
#print(devices)

#print(bluetooth.make_discoverable())

def find_devices():
    print("performing inquiry...")
    
    mac_list = [] # find device
    name_list = [] # find device

    host_list = [] # find service host
    description_list = [] # find device description
    provider_list = [] # find device provider
    protocol_list = [] # find device protocol
    port_list = [] # find device port
    service_class_list = [] # find device  service-classes
    profiles_list = [] # find device profiles
    service_list = [] # find device sercvice-id
    
    nearby_devices = bluetooth.discover_devices(lookup_names = True) # returns mac and name
    for mac, name in nearby_devices:
        mac_list.append(mac)
        name_list.append(name)
        
        services = bluetooth.find_service(address=mac) # returns all data about the specific bluetooth
        if len(services) <=0:
            print("no services found in: ",mac)
        else:
            host_list.append(host(services))
            description_list.append(description(services))
            provider_list.append(provider(services))
            protocol_list.append(protocol(services))
            port_list.append(port(services))
            service_class_list.append(service_class(services))
            profiles_list.append(profiles(services))
            service_list.append(service(services))
            
    if len(mac_list) > 0:
        for _ in range(len(mac_list)):
            print("********************************************")
            print("Available device mac address:     ",mac_list[_])
            print("Available device name:            ",name_list[_])
            print("Available device host:            ",host_list[_])
            print("Available device description:     ",description_list[_])
            print("Available device provider:        ",provider_list[_])
            print("Available device protocol:        ",protocol_list[_])
            print("Available device port:            ",port_list[_])
            print("Available device service_classes: ",service_class_list[_])
            print("Available device profiles:        ",profiles_list[_])
            print("Available device service:         ",service_list[_])           
            print("********************************************")
            print("\n")
        #if btool.pair(mac_list[0]) == 0:
        #    btool.pair(mac_list[0])
        #btool.disconnect(mac_list[0])
        time.sleep(3)
        sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect(("B8:27:EB:8C:79:63", 1))
        sock.send("north horn")
        sock.close()
    else:
        print("no near by devce found")
        return()

def host(data):
    data_list = []
    for _ in data:
        data_list.append(_['host'])
    return data_list
    
def description(data):
    data_list = []
    for _ in data:
        data_list.append(_['description'])
    return data_list
    
def provider(data):
    data_list = []
    for _ in data:
        data_list.append(_['provider'])
    return data_list

def protocol(data):
    data_list = []
    for _ in data:
        data_list.append(_['protocol'])
    return data_list

def port(data):
    data_list = []
    for _ in data:
        data_list.append(_['port'])
    return data_list

def service_class(data):
    data_list = []
    for _ in data:
        data_list.append(_['service-classes'])
    return data_list

def profiles(data):
    data_list = []
    for _ in data:
        data_list.append(_['profiles'])
    return data_list

def service(data):
    data_list = []
    for _ in data:
        data_list.append(_['service-id'])
    return data_list


while 1:
    data = input()
    if data == 'horn':
        find_devices()
        print("done")
    else:
        break



print("hai")


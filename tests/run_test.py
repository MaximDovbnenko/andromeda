
CONNECT_ADDR = "opc.tcp://192.168.250.1:4840"
DEBUG        = True
TIME_PERIOD  = 0.1 #s

from opcua import Client
from opcua import ua
import time

opc_ua_client  = None
is_connected   = False



def connect():
    global opc_ua_client, is_connected
    if not DEBUG:
        try:
            print("create coonection on {}".format(CONNECT_ADDR))
            opc_ua_client  = Client(CONNECT_ADDR)
            print("try connect...")
            opc_ua_client.connect()
            is_connected = True
        except Exception as e:
            print("error connect {}".format(e))
    else:
        is_connected = True
        print("emulation coonection on {} {}".format(CONNECT_ADDR, is_connected))

def set_value(node, value):
    if is_connected:
        try:
            tmp = opc_ua_client.get_node(node)
            tmp.set_attribute(ua.AttributeIds.Value, ua.DataValue(value))
        except Exception as e: 
            print(str(e))


def drive_enable():
    if not DEBUG:
        set_value("ns=4;s=Start", True)
    else:
        print("drive sync enabled...")
    pass

def sync_run(vel):
    pass

def sync_stop():
    pass

def main():
    connect()
    drive_enable()


if __name__ == "__main__":
    main()
    pass
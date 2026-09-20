from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)if client.connect():

    client.write_coil(0, True)

    print("Valve changed to ON")

    client.close()

else:
    print("Connection Failed")
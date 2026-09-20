from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)if client.connect():

    client.write_register(200,35)

    print("Temperature changed to 35")

    client.close()

else:
    print("Connection Failed")
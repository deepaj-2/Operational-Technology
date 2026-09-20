from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)if client.connect():

    client.write_registers(201,[110,60])

    print("Pressure and Flow updated")

    client.close()

else:
    print("Connection Failed")
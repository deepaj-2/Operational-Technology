from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=502)if client.connect():

    # Initial Valve State = OFF
    client.write_coil(0, False)

    # Initial Holding Register Values
    client.write_register(200, 25)   # Temperature
    client.write_register(201, 100)  # Pressure
    client.write_register(202, 50)   # Flow Rate

    print("Initial values written successfully.")

    client.close()

else:
    print("Connection Failed")
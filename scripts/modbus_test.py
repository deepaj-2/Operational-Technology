from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=1502)

if client.connect():
    print("Connected to OpenPLC through localhost:1502")
    result = client.read_holding_registers(address=0, count=1, device_id=1)
    print("Result:", result)
    client.close()
else:
    print("Connection failed")

from pymodbus.client import ModbusTcpClient
import time

# Connect to OpenPLC Modbus Server
client = ModbusTcpClient("127.0.0.1", port=502)
if client.connect():
    print("Connected to OpenPLC")

    # -----------------------------
    # Read Coil 0 (Valve Status)
    # -----------------------------
    coil = client.read_coils(0, count=1)

    if coil.isError():
        print("Error reading Coil 0")
    else:
        print("Valve (Coil 0):", coil.bits[0])

    # -----------------------------------------
    # Read Holding Registers 200-202
    # -----------------------------------------
    regs = client.read_holding_registers(address=200, count=3)

    if regs.isError():
        print("Error reading Holding Registers")
    else:
        print("Temperature :", regs.registers[0])
        print("Pressure    :", regs.registers[1])
        print("Flow Rate   :", regs.registers[2])

    print("\nKeeping connection open for 20 seconds...")
    time.sleep(20)

    client.close()
    print("Connection Closed")

else:
    print("Connection Failed")
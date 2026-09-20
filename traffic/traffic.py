from pymodbus.client.sync import ModbusTcpClient
import time
import random

PLC_HOST = "openplc"
PLC_PORT = 502
UNIT_ID = 1

client = ModbusTcpClient(PLC_HOST, port=PLC_PORT)

print("Starting normal OT background traffic...")

if not client.connect():
    print("ERROR: Could not connect to OpenPLC")
    raise SystemExit(1)

print("Connected to OpenPLC.")

try:
    while True:
        coil = client.read_coils(0, 1, unit=UNIT_ID)
        register = client.read_holding_registers(0, 1, unit=UNIT_ID)

        if not coil.isError():
            print("Motor =", coil.bits[0])

        if not register.isError():
            print("Setpoint =", register.registers[0])

        time.sleep(random.randint(2, 4))

except KeyboardInterrupt:
    print("Traffic generator stopped.")

finally:
    client.close()
    print("Disconnected from OpenPLC.")
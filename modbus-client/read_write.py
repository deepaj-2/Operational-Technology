from pymodbus.client.sync import ModbusTcpClient
import time

PLC_HOST = "openplc"
PLC_PORT = 502
UNIT_ID = 1

client = ModbusTcpClient(PLC_HOST, port=PLC_PORT)

print("Connecting to OpenPLC...")

if not client.connect():
    print("ERROR: Could not connect to OpenPLC")
    raise SystemExit(1)

print("Connected to OpenPLC.")

try:
    print("\n--- Initial PLC State ---")

    coil = client.read_coils(0, 1, unit=UNIT_ID)
    register = client.read_holding_registers(0, 1, unit=UNIT_ID)

    if coil.isError():
        print("Error reading coil")
    else:
        print("Motor coil %QX0.0 =", coil.bits[0])

    if register.isError():
        print("Error reading holding register")
    else:
        print("Setpoint %QW0 =", register.registers[0])

    print("\n--- Writing Test Values ---")

    client.write_coil(0, True, unit=UNIT_ID)
    print("Motor coil written: TRUE")

    client.write_register(0, 100, unit=UNIT_ID)
    print("Setpoint register written: 100")

    time.sleep(1)

    print("\n--- PLC State After Write ---")

    coil = client.read_coils(0, 1, unit=UNIT_ID)
    register = client.read_holding_registers(0, 1, unit=UNIT_ID)

    if not coil.isError():
        print("Motor coil %QX0.0 =", coil.bits[0])

    if not register.isError():
        print("Setpoint %QW0 =", register.registers[0])

finally:
    client.close()
    print("\nDisconnected from OpenPLC.")
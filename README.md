# Operational Technology Security Testbed

A Docker-based OT/ICS security testbed for studying industrial control system communication, monitoring, and controlled security testing.

## Components

- OpenPLC - simulated industrial PLC
- ScadaBR - SCADA/HMI interface
- Modbus/TCP - industrial communication protocol
- Modbus client - PLC read/write verification
- OT traffic generator - background normal traffic
- Attacker container - controlled Modbus write tests
- Wireshark - packet capture and protocol analysis

## Objectives

- Build a reproducible OT/ICS laboratory environment.
- Understand PLC and SCADA communication.
- Generate normal Modbus/TCP traffic.
- Perform controlled Modbus write tests.
- Capture and inspect industrial traffic using Wireshark.
- Identify Modbus function codes and packet fields.

## Open-Source Components

This project integrates existing open-source software and libraries, including OpenPLC, ScadaBR, Apache Tomcat, Python, and PyModbus.

The Docker configuration, PLC logic, traffic generator, controlled attack scripts, integration, and experimental workflow were developed specifically for this testbed.

## Project Structure

    Operational-Technology/
    ├── compose.yaml
    ├── attacker/
    ├── docs/
    ├── modbus-client/
    ├── openplc/
    │   └── plc/
    ├── scadabr/
    ├── scripts/
    └── traffic/

## Status

Core OT/ICS cyber-range implementation completed.
Documentation and reproducibility procedures are being finalized.

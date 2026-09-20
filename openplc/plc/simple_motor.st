PROGRAM simple_motor

VAR
    Motor AT %QX0.0 : BOOL;
    Setpoint AT %QW0 : INT;
END_VAR

Motor := Motor;
Setpoint := Setpoint;

END_PROGRAM

CONFIGURATION Config0

RESOURCE Res0 ON PLC

TASK Main(INTERVAL := T#50ms, PRIORITY := 0);

PROGRAM Inst0 WITH Main : simple_motor;

END_RESOURCE

END_CONFIGURATION
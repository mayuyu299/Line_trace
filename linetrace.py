import ev3dev.ev3 as ev3
import time


mr = ev3.LargeMotor('outC')
ml = ev3.LargeMotor('outD')
cs = ev3.ColorSensor('in1')
ts = ev3.TouchSensor('in2')
cs.mode='COL-REFLECT'

while True:
    kp=2.9#1.45
    b=5
    w=90
    target=(b+w)/2
    color = cs.value()
    error=target-color
    print(color)
    pid_value=kp*error
    mr.run_forever(speed_sp=200-pid_value)
    ml.run_forever(speed_sp=200+pid_value) 

    if ts.value()==1:   
        break
    
mr.stop(stop_action='brake')
ml.stop(stop_action='brake')

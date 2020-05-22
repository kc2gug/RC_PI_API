# config.py

PORT=3030
SIMPORT=8000
DPIO=(33,11,13,15)
DRIVE_DIR="REVERSE"
DRIVE_DEFS={
    "FORWARD": [{
        "FWD":[{DPIO[0]: True, DPIO[1]: False,DPIO[2]: True, DPIO[3]: False}],
        "BAK":[{DPIO[0]: False,DPIO[1]: True, DPIO[2]: False,DPIO[3]: True }],
        "SRT":[{DPIO[0]: False,DPIO[1]: True, DPIO[2]: True, DPIO[3]: False}],
        "SLT":[{DPIO[0]: True, DPIO[1]: False,DPIO[2]: False,DPIO[3]: True }],
        "FWL":[{DPIO[0]: True, DPIO[1]: False,DPIO[2]: False,DPIO[3]: False}],
        "BWL":[{DPIO[0]: False,DPIO[1]: False,DPIO[2]: False,DPIO[3]: True }],
        "BWR":[{DPIO[0]: False,DPIO[1]: True, DPIO[2]: False,DPIO[3]: False}],
        "FWR":[{DPIO[0]: False,DPIO[1]: False,DPIO[2]: True, DPIO[3]: False}],
        "STP":[{DPIO[0]: False,DPIO[1]: False,DPIO[2]: False,DPIO[3]: False}]}]
    ,
    "REVERSE": [{
        "BAK":[{DPIO[0]: True, DPIO[1]: False,DPIO[2]: True, DPIO[3]: False}],
        "FWD":[{DPIO[0]: False,DPIO[1]: True, DPIO[2]: False,DPIO[3]: True }],
        "SRT":[{DPIO[0]: False,DPIO[1]: True, DPIO[2]: True, DPIO[3]: False}],
        "SLT":[{DPIO[0]: True, DPIO[1]: False,DPIO[2]: False,DPIO[3]: True }],
        "BWL":[{DPIO[0]: True, DPIO[1]: False,DPIO[2]: False,DPIO[3]: False}],
        "FWL":[{DPIO[0]: False,DPIO[1]: False,DPIO[2]: False,DPIO[3]: True }],
        "FWR":[{DPIO[0]: False,DPIO[1]: True, DPIO[2]: False,DPIO[3]: False}],
        "BWR":[{DPIO[0]: False,DPIO[1]: False,DPIO[2]: True, DPIO[3]: False}],
        "STP":[{DPIO[0]: False,DPIO[1]: False,DPIO[2]: False,DPIO[3]: False}]}]
    }



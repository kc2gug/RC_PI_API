# config.py

PORT=3030
SIMPORT=8000
GPIO_DRIVE_PINS=(33,11,13,15)
DRIVE_DIR="REVERSE"
DRIVE_DEFS={
    "FORWARD": [{
        "FWD":[{"PIN1": True, "PIN2": False,"PIN3": True, "PIN4": False}],
        "BAK":[{"PIN1": False,"PIN2": True, "PIN3": False,"PIN4": True }],
        "SRT":[{"PIN1": False,"PIN2": True, "PIN3": True, "PIN4": False}],
        "SLT":[{"PIN1": True, "PIN2": False,"PIN3": False,"PIN4": True }],
        "FWL":[{"PIN1": True, "PIN2": False,"PIN3": False,"PIN4": False}],
        "BWL":[{"PIN1": False,"PIN2": False,"PIN3": False,"PIN4": True }],
        "BWR":[{"PIN1": False,"PIN2": True, "PIN3": False,"PIN4": False}],
        "FWR":[{"PIN1": False,"PIN2": False,"PIN3": True, "PIN4": False}],
        "STP":[{"PIN1": False,"PIN2": False,"PIN3": False,"PIN4": False}]}]
    ,
    "REVERSE": [{
        "BAK":[{"PIN1": True, "PIN2": False,"PIN3": True, "PIN4": False}],
        "FWD":[{"PIN1": False,"PIN2": True, "PIN3": False,"PIN4": True }],
        "SLT":[{"PIN1": False,"PIN2": True, "PIN3": True, "PIN4": False}],
        "SRT":[{"PIN1": True, "PIN2": False,"PIN3": False,"PIN4": True }],
        "BWR":[{"PIN1": True, "PIN2": False,"PIN3": False,"PIN4": False}],
        "FWR":[{"PIN1": False,"PIN2": False,"PIN3": False,"PIN4": True }],
        "FWL":[{"PIN1": False,"PIN2": True, "PIN3": False,"PIN4": False}],
        "BWL":[{"PIN1": False,"PIN2": False,"PIN3": True, "PIN4": False}],
        "STP":[{"PIN1": False,"PIN2": False,"PIN3": False,"PIN4": False}]}]
    }



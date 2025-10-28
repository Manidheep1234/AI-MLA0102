def water_jug():
    jug4, jug3 = 0, 0
    print(f"Initial State: ({jug4}, {jug3})")
    while jug4 != 2:
        if jug3 == 0:
            jug3 = 3
            print(f"Fill 3-gallon jug: ({jug4}, {jug3})")
        elif jug4 < 4 and jug3 > 0:
            transfer = min(jug3, 4 - jug4)
            jug4 += transfer
            jug3 -= transfer
            print(f"Pour from 3-gallon to 4-gallon jug: ({jug4}, {jug3})")
        if jug4 == 4:
            jug4 = 0
            print(f"Empty 4-gallon jug: ({jug4}, {jug3})")

water_jug()

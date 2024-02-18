import math


#Machine 1

def get_heat1055_1(speed):
    x = (9.8142 * speed) + 35.4848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1055 on machine 2"""

def get_speed1055_1(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 35.4848
    result = heat5 / 9.8142
    print(heat5)
    return result

def get_heat1055t_1(speed):
    temp = 1 + (speed * 1)
    return temp
"""formula for taping one machine 2"""

def get_speed1055t_1(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat1365_1(speed):
    x = (593.806 * speed) + 7504.9
    i = math.log(x)
    n = 1364.18 * i
    result = n - 11950.3
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365_1(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1195030
    heat3 = heat2 / 136418
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 7504.9
    result = heat5 / 593.806
    print(heat5)
    return result

def get_heat1365t_1(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365t_1(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
    print(heat5)
    return result

def get_heat4090_1(speed):
    x = (1395.54 * speed) + 10024.43
    i = math.log(x)
    n = 1231.18 * i
    result = n - 11100.9
    return result


def get_speed4090_1(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1110090
    heat3 = heat2 / 123118
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 10024.43
    result = heat5 / 1395.54
    print(heat5)
    return result

def get_heat4090t_1(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed4090t_1(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat2051_1(speed):
    try:
      x = (520.392 * speed) + 50.7
      i = math.log(x)
      n = 165.926 * i
      result = n - 699.76
      return result
    except ValueError:
        pass

def get_speed2051_1(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 699760
    heat3 = heat2 / 165926
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 50.7
    result = heat5 / 520.392
    print(heat5)
    return result
def get_heat2051t_1(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed2051t_1(heat):
    speed = float((heat - 1) / 1)
    return speed


def get_heatvinyl_1(speed):
    x = (789.232 * speed) + 12522.05
    i = math.log(x)
    n = 1857.22 * i
    result = n - 17307.9
    return result


def get_speedvinyl_1(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1730790
    heat3 = heat2 / 185722
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 12522.05
    result = heat5 / 789.232
    print(heat5)
    return result

def get_heatvinylt_1(speed):
    x = (789.232 * speed) + 12432.3
    i = math.log(x)
    n = 1857.22 * i
    result = n - 17307.9
    return result


def get_speedvinylt_1(heat):
    speed = float((heat - 1) / 1)
    return speed


#machine 2


def get_heat1055_2(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1055 on machine 2"""

def get_speed1055_2(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
    print(heat5)
    return result

def get_heat1055t_2(speed):
    temp = 1 + (speed * 1)
    return temp
"""formula for taping one machine 2"""

def get_speed1055t_2(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat1365_2(speed):
    x = (593.806 * speed) + 7429.65
    i = math.log(x)
    n = 1364.18 * i
    result = n - 11950.3
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365_2(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1195030
    heat3 = heat2 / 136418
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 7429.65
    result = heat5 / 593.806
    print(heat5)
    return result

def get_heat1365t_2(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365t_2(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
    print(heat5)
    return result

def get_heat4090_2(speed):
    x = (1395.54 * speed) + 9901.57
    i = math.log(x)
    n = 1231.18 * i
    result = n - 11100.9
    return result


def get_speed4090_2(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1110090
    heat3 = heat2 / 123118
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9901.57
    result = heat5 / 1395.54
    print(heat5)
    return result

def get_heat4090t_2(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed4090t_2(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat2051_2(speed):
    try:
      x = (520.392 * speed) - 24.6119
      i = math.log(x)
      n = 165.926 * i
      result = n - 699.76
      return result
    except ValueError:
        pass

def get_speed2051_2(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 699760
    heat3 = heat2 / 165926
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 + 24.6119
    result = heat5 / 520.392
    print(heat5)
    return result
def get_heat2051t_2(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed2051t_2(heat):
    speed = float((heat - 1) / 1)
    return speed


def get_heatvinyl_2(speed):
    x = (789.232 * speed) + 12432.3
    i = math.log(x)
    n = 1857.22 * i
    result = n - 17307.9
    return result


def get_speedvinyl_2(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1730790
    heat3 = heat2 / 185722
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 12432.3
    result = heat5 / 789.232
    print(heat5)
    return result

def get_heatvinylt_2(speed):
    x = (789.232 * speed) + 12432.3
    i = math.log(x)
    n = 1857.22 * i
    result = n - 17307.9
    return result


def get_speedvinylt_2(heat):
    speed = float((heat - 1) / 1)
    return speed



#machine 3
def get_heatvinyl_3(speed):
    temp = 480 + (speed * 100)
    return temp


def get_speedvinyl_3(heat):
    speed = float((heat - 480) / 100)
    return speed

def get_heatvinylt_3(speed):
    temp = 520 + (speed * 100)
    return temp


def get_speedvinylt_3(heat):
    speed = float((heat - 520) / 100)
    return speed

def get_heat1055_3(speed):
    temp = 450 + (speed * 100)
    return temp


def get_speed1055_3(heat):
    speed = float((heat - 450) / 100)
    return speed

def get_heat1055t_3(speed):
    temp = 490 + (speed * 100)
    return temp


def get_speed1055t_3(heat):
    speed = float((heat - 490) / 100)
    return speed

def get_heat1365_3(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365_3(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
    print(heat5)
    return result

def get_heat1365t_3(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365t_3(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
    print(heat5)
    return result

def get_heat955t_3(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed955t_3(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat955_3(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed955_3(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat4090_3(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed4090_3(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat4090t_3(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed4090t_3(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat2051_3(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed2051_3(heat):
    speed = float((heat - 1) / 1)
    return speed
def get_heat2051t_3(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed2051t_3(heat):
    speed = float((heat - 1) / 1)
    return speed


#machine 4

def get_heat1055_4(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1055 on machine 2"""

def get_speed1055_4(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
    print(heat5)
    return result

def get_heat1055t_4(speed):
    temp = 1 + (speed * 1)
    return temp
"""formula for taping one machine 2"""

def get_speed1055t_4(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat1365_4(speed):
    x = (593.806 * speed) + 7429.65
    i = math.log(x)
    n = 1364.18 * i
    result = n - 11950.3
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365_4(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1195030
    heat3 = heat2 / 136418
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 7429.65
    result = heat5 / 593.806
    print(heat5)
    return result

def get_heat1365t_4(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365t_4(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
    print(heat5)
    return result

def get_heat4090_4(speed):
    x = (1395.54 * speed) + 9901.57
    i = math.log(x)
    n = 1231.18 * i
    result = n - 11100.9
    return result


def get_speed4090_4(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1110090
    heat3 = heat2 / 123118
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9901.57
    result = heat5 / 1395.54
    print(heat5)
    return result

def get_heat4090t_4(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed4090t_4(heat):
    speed = float((heat - 1) / 1)
    return speed

def get_heat2051_4(speed):
    try:
      x = (520.392 * speed) - 24.6119
      i = math.log(x)
      n = 165.926 * i
      result = n - 699.76
      return result
    except ValueError:
        pass

def get_speed2051_4(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 699760
    heat3 = heat2 / 165926
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 + 24.6119
    result = heat5 / 520.392
    print(heat5)
    return result
def get_heat2051t_4(speed):
    temp = 1 + (speed * 1)
    return temp


def get_speed2051t_4(heat):
    speed = float((heat - 1) / 1)
    return speed


def get_heatvinyl_4(speed):
    x = (789.232 * speed) + 12432.3
    i = math.log(x)
    n = 1857.22 * i
    result = n - 17307.9
    return result


def get_speedvinyl_4(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1730790
    heat3 = heat2 / 185722
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 12432.3
    result = heat5 / 789.232
    print(heat5)
    return result

def get_heatvinylt_4(speed):
    x = (789.232 * speed) + 12432.3
    i = math.log(x)
    n = 1857.22 * i
    result = n - 17307.9
    return result


def get_speedvinylt_4(heat):
    speed = float((heat - 1) / 1)
    return speed


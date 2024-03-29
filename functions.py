import math






#Machine 1

def get_heat1055_1(speed):
    x = (511.41 * speed) + 6579.57
    i = math.log(x)
    n = 1147.41 * i
    result = n - 9875.36
    return result
"""formula for seaming 1055 on machine 1"""

def get_speed1055_1(heat):
    heat1 = heat * 100
    heat2 = heat1 + 987536
    heat3 = heat2 / 114741
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 6579.57
    result = heat5 / 511.41
    return result

def get_heat1055t_1(speed):
    x = (7.75223 * speed) + 17.8386
    i = math.log(x)
    n = 378.092 * i
    result = n - 879.079
    return result
"""formula for taping on machine 1"""

def get_speed1055t_1(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 879079
    heat3 = heat2 / 378092
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 17.8386
    result = heat5 / 7.75223
    return result

def get_heat1365_1(speed):
    """formula for seaming 1365 on machine 1"""
    x = (593.806 * speed) + 7504.9
    i = math.log(x)
    n = 1364.18 * i
    result = n - 11950.3
    return result


def get_speed1365_1(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1195030
    heat3 = heat2 / 136418
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 7504.9
    result = heat5 / 593.806
    return result

def get_heat1365t_1(speed):
    """formula for tapeing 1365 on machine 1"""
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result


def get_speed1365t_1(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
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
    return result

def get_heat4090t_1(speed):
    x = (627.388 * speed) + 6974.79
    i = math.log(x)
    n = 1049.79 * i
    result = n - 9017.08
    return result


def get_speed4090t_1(heat):
    heat1 = heat * 100
    heat2 = heat1 + 901708
    heat3 = heat2 / 104979
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 6974.79
    result = heat5 / 627.388
    return result

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
    return result
def get_heat2051t_1(speed):
    x = (865.785 * speed) + 9290.42
    i = math.log(x)
    n = 1243.27 * i
    result = n - 11122.3
    return result


def get_speed2051t_1(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1112230
    heat3 = heat2 / 124327
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9290.42
    result = heat5 / 865.785
    return result


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
    return result

def get_heatvinylt_1(speed):
    """formula for taping on machine 1"""
    x = (865.785 * speed) + 9290.42
    i = math.log(x)
    n = 1243.27 * i
    result = n - 11122.3
    return result

def get_speedvinylt_1(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1112230
    heat3 = heat2 / 124327
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9290.42
    result = heat5 / 865.785
    return result


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
    return result

def get_heat1055_2_2(speed):
    x = (1107.86 * speed) + 6955.55
    i = math.log(x)
    n = 1023.46 * i
    result = n - 8851.45
    return result
"""formula for seaming 1055 on machine 2"""

def get_speed1055_2_2(heat):
    heat1 = heat * 100
    heat2 = heat1 + 885145
    heat3 = heat2 / 102346
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 6955.55
    result = heat5 / 1107.86
    return result

def get_heat1055t_2(speed):
    x = (7.75223 * speed) + 17.8386
    i = math.log(x)
    n = 378.092 * i
    result = n - 879.079
    return result
"""formula for taping on machine 1"""

def get_speed1055t_2(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 879079
    heat3 = heat2 / 378092
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 17.8386
    result = heat5 / 7.75223
    return result

def get_heat1365_2(speed):
    """formula for seaming 1365 on machine 2"""
    x = (593.806 * speed) + 7429.65
    i = math.log(x)
    n = 1364.18 * i
    result = n - 11950.3
    return result


def get_speed1365_2(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1195030
    heat3 = heat2 / 136418
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 7429.65
    result = heat5 / 593.806
    return result

def get_heat1365_2_2(speed):
    x = (693.569 * speed) + 340.667
    i = math.log(x)
    n = 265.485 * i
    result = n - 1434.61
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365_2_2(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1434610
    heat3 = heat2 / 265485
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 340.667
    result = heat5 / 693.569
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
    return result

def get_heat4090_2_2(speed):
    x = (1395.54 * speed) + 9901.57
    i = math.log(x)
    n = 1231.18 * i
    result = n - 11100.9
    return result


def get_speed4090_2_2(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1110090
    heat3 = heat2 / 123118
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9901.57
    result = heat5 / 1395.54
    return result

def get_heat4090t_2(speed):
    x = (627.388 * speed) + 6974.79
    i = math.log(x)
    n = 1049.79 * i
    result = n - 9017.08
    return result


def get_speed4090t_2(heat):
    heat1 = heat * 100
    heat2 = heat1 + 901708
    heat3 = heat2 / 104979
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 6974.79
    result = heat5 / 627.388
    return result

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
    return result
def get_heat2051t_2(speed):
    x = (865.785 * speed) + 9290.42
    i = math.log(x)
    n = 1243.27 * i
    result = n - 11122.3
    return result


def get_speed2051t_2(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1112230
    heat3 = heat2 / 124327
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9290.42
    result = heat5 / 865.785
    return result


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
    return result

def get_heatvinyl_2_2(speed):
    x = (553.693 * speed) + 221.282
    i = math.log(x)
    n = 212.804 * i
    result = n - 1080.75
    return result


def get_speedvinyl_2_2(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1080750
    heat3 = heat2 / 212804
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 221.282
    result = heat5 / 553.693
    return result

def get_heatvinylt_2(speed):
    x = (789.232 * speed) + 12432.3
    i = math.log(x)
    n = 1857.22 * i
    result = n - 17307.9
    return result


def get_speedvinylt_2(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1730790
    heat3 = heat2 / 185722
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 12522.05
    result = heat5 / 789.232
    return result



#machine 3
def get_heatvinyl_3(speed):
    x = (8.93756 * speed) + 48.4051
    i = math.log(x)
    n = 825.509 * i
    result = n - 2772.52
    return result


def get_speedvinyl_3(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 2772520
    heat3 = heat2 / 825509
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 48.4051
    result = heat5 / 8.93756
    return result

def get_heatvinylt_3(speed):
    x = (0.451196 * speed) + 46.4283
    i = math.log(x)
    n = 11375.5 * i
    result = n - 43100.1
    return result


def get_speedvinylt_3(heat):
    heat1 = heat * 10
    heat2 = heat1 + 431001
    heat3 = heat2 / 113755
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 46.4283
    result = heat5 / 0.451196
    return result

def get_heat1055_3(speed):
    x = (13.2583 * speed) + 111.243
    i = math.log(x)
    n = 1131.88 * i
    result = n - 4935.4
    return result


def get_speed1055_3(heat):
    heat1 = heat * 100
    heat2 = heat1 + 493540
    heat3 = heat2 / 113188
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 111.243
    result = heat5 / 13.2583
    return result

def get_heat1055t_3(speed):
    x = (0.2056 * speed) + 60.1457
    i = math.log(x)
    n = 30224.8 * i
    result = n - 123305
    return result

def get_speed1055t_3(heat):
    heat1 = heat * 10
    heat2 = heat1 + 1233050
    heat3 = heat2 / 302248
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 60.1457
    result = heat5 / 0.2056
    return result

def get_heat1365_3(speed):
    x = (12.9783 * speed) + 38.9918
    i = math.log(x)
    n = 765.11 * i
    result = n - 2493.26
    return result
"""formula for seaming 1365 on machine 3"""

def get_speed1365_3(heat):
    heat1 = heat * 100
    heat2 = heat1 + 249326
    heat3 = heat2 / 76511
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 38.9918
    result = heat5 / 12.9783
    return result

def get_heat1365t_3(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for tapeing 1365 on machine 3"""

def get_speed1365t_3(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
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
    x = (14.5885 * speed) + 5.30373
    i = math.log(x)
    n = 424.062 * i
    result = n - 761.35
    return result


def get_speed4090_3(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 761350
    heat3 = heat2 / 424062
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 5.30373
    result = heat5 / 14.5885
    return result

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
    x = (511.41 * speed) + 6579.57
    i = math.log(x)
    n = 1147.41 * i
    result = n - 9875.36
    return result
"""formula for seaming 1055 on machine 1"""

def get_speed1055_4(heat):
    heat1 = heat * 100
    heat2 = heat1 + 987536
    heat3 = heat2 / 114741
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 6579.57
    result = heat5 / 511.41
    return result

def get_heat1055_4_15(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1055 on machine 2"""

def get_speed1055_4_15(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
    return result

def get_heat1055_4_20(speed):
    x = (9.8142 * speed) + 33.9848
    i = math.log(x)
    n = 494.602 * i
    result = n - 1609.4
    return result
"""formula for seaming 1055 on machine 2"""

def get_speed1055_4_20(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 1609400
    heat3 = heat2 / 494602
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 33.9848
    result = heat5 / 9.8142
    return result

def get_heat1055t_4(speed):
    x = (511.41 * speed) + 6579.57
    i = math.log(x)
    n = 1147.41 * i
    result = n - 9875.36
    return result
"""formula for taping one machine 2"""

def get_speed1055t_4(heat):
    heat1 = heat * 100
    heat2 = heat1 + 987536
    heat3 = heat2 / 114741
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 6579.57
    result = heat5 / 511.41
    return result

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
    return result

def get_heat1365_4_15(speed):
    x = (593.806 * speed) + 7429.65
    i = math.log(x)
    n = 1364.18 * i
    result = n - 11950.3
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365_4_15(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1195030
    heat3 = heat2 / 136418
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 7429.65
    result = heat5 / 593.806
    return result

def get_heat1365_4_20(speed):
    x = (593.806 * speed) + 7429.65
    i = math.log(x)
    n = 1364.18 * i
    result = n - 11950.3
    return result
"""formula for seaming 1365 on machine 2"""

def get_speed1365_4_20(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1195030
    heat3 = heat2 / 136418
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 7429.65
    result = heat5 / 593.806
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
    return result

def get_heat4090_4_15(speed):
    x = (948.23 * speed) + 9105.94
    i = math.log(x)
    n = 1189.59 * i
    result = n - 10587
    return result


def get_speed4090_4_15(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1058700
    heat3 = heat2 / 118959
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9105.94
    result = heat5 / 948.23
    return result

def get_heat4090_4_20(speed):
    x = (1395.54 * speed) + 9901.57
    i = math.log(x)
    n = 1231.18 * i
    result = n - 11100.9
    return result


def get_speed4090_4_20(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1110090
    heat3 = heat2 / 123118
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9901.57
    result = heat5 / 1395.54
    return result

def get_heat4090t_4(speed):
    x = (627.388 * speed) + 6974.79
    i = math.log(x)
    n = 1049.79 * i
    result = n - 9017.08
    return result


def get_speed4090t_4(heat):
    heat1 = heat * 100
    heat2 = heat1 + 901708
    heat3 = heat2 / 104979
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 6974.79
    result = heat5 / 627.388
    return result

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
    return result

def get_heat2051_4_15(speed):
    try:
      x = (520.392 * speed) - 24.6119
      i = math.log(x)
      n = 165.926 * i
      result = n - 699.76
      return result
    except ValueError:
        pass

def get_speed2051_4_15(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 699760
    heat3 = heat2 / 165926
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 + 24.6119
    result = heat5 / 520.392
    return result

def get_heat2051_4_20(speed):
    try:
      x = (520.392 * speed) - 24.6119
      i = math.log(x)
      n = 165.926 * i
      result = n - 699.76
      return result
    except ValueError:
        pass

def get_speed2051_4_20(heat):
    heat1 = heat * 1000
    heat2 = heat1 + 699760
    heat3 = heat2 / 165926
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 + 24.6119
    result = heat5 / 520.392
    return result

def get_heat2051t_4(speed):
    x = (865.785 * speed) + 9290.42
    i = math.log(x)
    n = 1243.27 * i
    result = n - 11122.3
    return result


def get_speed2051t_4(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1112230
    heat3 = heat2 / 124327
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9290.42
    result = heat5 / 865.785
    return result


def get_heatvinyl_4(speed):
    x = (789.232 * speed) + 12522.05
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
    heat5 = heat4 - 12522.05
    result = heat5 / 789.232
    return result

def get_heatvinylt_4(speed):
    x = (865.785 * speed) + 9290.42
    i = math.log(x)
    n = 1243.27 * i
    result = n - 11122.3
    return result


def get_speedvinylt_4(heat):
    heat1 = heat * 100
    heat2 = heat1 + 1112230
    heat3 = heat2 / 124327
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 9290.42
    result = heat5 / 865.785
    return result

# T-100 Tape Machine
def get_speedvinylt_t100tape(heat):
    heat1 = heat * 10
    heat2 = heat1 + 158303
    heat3 = heat2 / 21430
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 2179
    result = heat5 / 3.51168
    return result

def get_heatvinylt_t100tape(speed):
    x = (3.51168 * speed) + 2179
    i = math.log(x)
    n = 2143 * i
    result = n - 15830.3
    return result


def get_speed1055t_t100tape(heat):
    heat1 = heat * 10
    heat2 = heat1 + 158303
    heat3 = heat2 / 21430
    e = 2.7182818284590452353602874713527
    heat4 = math.pow(e, heat3)
    heat5 = heat4 - 2179
    result = heat5 / 3.51168
    return result

def get_heat1055t_t100tape(speed):
    x = (3.51168 * speed) + 2179
    i = math.log(x)
    n = 2143 * i
    result = n - 15830.3
    return result


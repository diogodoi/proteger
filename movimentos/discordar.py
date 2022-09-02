def Discordar():
    names = list()
    times = list()
    keys = list()


    names.append("HeadPitch")
    times.append([0.4, 0.72, 1.04, 1.36, 1.68, 1.96, 2.44, 2.84])
    keys.append([0.0858622, 0.0858622, 0.0873961, 0.0889301, 0.0858622, 0.0858622, 0.0889301, 0.0858622])
    names.append("HeadYaw")
    times.append([0.4, 0.72, 1.04, 1.36, 1.68, 1.96, 2.44, 2.84])
    keys.append([-0.0291878, 0.64884, 0.049046, -0.862151, -0.0291878, 0.64884, -0.862151, -0.0291878])

    return names,times,keys
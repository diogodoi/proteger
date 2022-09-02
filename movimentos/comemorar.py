def Comemorar():
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.266667, 0.533333, 0.666667, 0.8, 0.933333, 1.13333, 1.6, 1.93333, 2.53333, 3, 3.6, 3.8])
    keys.append([-0.368959, -0.272371, -0.185005, -0.0417875, 0.179769, 0.26315, -0.0994838, 0.0724156, -0.121841, -0.426485, -0.191986, -0.0261799])

    names.append("LElbowRoll")
    times.append([0.933333, 1.4, 1.93333, 2.46667])
    keys.append([-0.98262, -1.34414, -1.52156, -1.35727])

    names.append("LHand")
    times.append([1.4, 2.4])
    keys.append([0.06, 0.17])

    names.append("LShoulderPitch")
    times.append([0.333333, 0.666667, 0.933333, 1.2, 1.4, 1.6, 1.93333, 2.2, 2.4, 2.66667, 2.86667, 3.2, 3.4, 3.6, 3.8, 3.93333])
    keys.append([1.73025, 1.07861, 0.631354, 0.0715585, -0.219262, -0.532325, 0.820305, 1.72922, 0.617847, -0.536912, 0.207432, 1.75545, 0.389208, -0.514347, 0.762709, 1.75453])

    names.append("LShoulderRoll")
    times.append([2.2, 2.4])
    keys.append([0.232129, 0.172788])

    names.append("RElbowRoll")
    times.append([0.533333, 0.8, 1.6, 1.93333])
    keys.append([0.699877, 0.459353, 0.333358, 0.34732])

    names.append("RElbowYaw")
    times.append([0.666667])
    keys.append([1.40324])

    names.append("RHand")
    times.append([0.666667, 1.2, 1.6, 2.2])
    keys.append([1, 0.92, 0.96, 0.79])

    names.append("RShoulderPitch")
    times.append([0.333333, 0.666667, 1.6, 1.93333])
    keys.append([0.790634, 0.301942, 0.18675, 0.18675])

    names.append("RShoulderRoll")
    times.append([0.533333, 1, 1.6, 2])
    keys.append([-0.0541052, -0.119408, -0.143117, -0.0249289])

    return names,times,keys
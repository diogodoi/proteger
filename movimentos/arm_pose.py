def arm_pose():
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([-1.06149, -0.957173, -0.883542, -0.866668, -1.00166, -1.4818])

    names.append("LElbowYaw")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([-0.813062, -0.806927, -0.790051, -0.790051, -0.451038, -0.378941])

    names.append("LHand")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([0.022, 0.022, 0.022, 0.022, 0.022, 0.022])

    names.append("LShoulderPitch")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([1.42811, 1.43885, 1.60452, 1.88064, 1.88064, 1.88064])

    names.append("LShoulderRoll")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([0.138018, 0.374254, 0.62583, 0.722472, 0.519984, 0.619695])

    names.append("LWristYaw")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([0.130348, 0.113474, 0.113474, 0.113474, 0.113474, 0.308291])

    names.append("RElbowRoll")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([1.06464, 1.06464, 1.06464, 1.06464, 1.126, 1.49876])

    names.append("RElbowYaw")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([0.83292, 0.825251, 0.774628, 0.76389, 0.628898, 0.613558])

    names.append("RHand")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([0.0244, 0.0244, 0.0244, 0.0244, 0.0244, 0.0244])

    names.append("RShoulderPitch")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([1.41286, 1.53251, 1.6629, 1.91447, 1.93595, 2.0464])

    names.append("RShoulderRoll")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([-0.147306, -0.406552, -0.572224, -0.60904, -0.530805, -0.575292])

    names.append("RWristYaw")
    times.append([0.32, 0.76, 1.16, 1.64, 2.16, 3])
    keys.append([-0.124296, -0.124296, -0.124296, -0.124296, -0.124296, -0.182588])

    return names,times,keys

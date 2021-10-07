def arm_dance():
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1, 2, 2.4, 3, 3.6, 4.2, 4.8, 5.4, 6.32, 7.2, 7.6, 8.2, 8.8, 9.4, 10, 10.6, 11.52, 12.4, 13.48, 13.88, 14.48, 15.08, 15.68, 16.28, 16.88, 17.8, 19.72])
    keys.append([-0.18719, -0.185656, 0.0291041, -0.185656, 0.00149202, -0.185656, 0.0812599, -0.185656, -0.354396, -0.185656, 0.0291041, -0.185656, 0.00149202, -0.185656, 0.0812599, -0.185656, -0.354396, -0.354396, -0.185656, 0.0291041, -0.185656, 0.00149202, -0.185656, 0.0812599, -0.185656, -0.354396, -0.233211])

    names.append("HeadYaw")
    times.append([1, 2, 2.4, 3, 3.6, 4.2, 4.8, 5.4, 6.32, 7.2, 7.6, 8.2, 8.8, 9.4, 10, 10.6, 11.52, 12.4, 13.48, 13.88, 14.48, 15.08, 15.68, 16.28, 16.88, 17.8, 19.72])
    keys.append([-0.00157595, -0.00157595, -0.00157595, 0.00609397, -4.19617e-05, 0.00609397, -4.19617e-05, 0.00609397, 0.431013, 0.00157595, 0.00157595, -0.00609397, 4.19617e-05, -0.00609397, 4.19617e-05, -0.00609397, -0.431013, -0.431013, -0.00157595, -0.00157595, 0.00609397, -4.19617e-05, 0.00609397, -4.19617e-05, 0.00609397, 0.431013, -0.00924586])

    names.append("LAnklePitch")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([0.105804, -0.417291, -0.607505, -0.421891, -0.671934, -0.31136, -0.355846, -0.31136, -0.443284, -0.443284, -0.417291, -0.607505, -0.421891, -0.671934, 0.108872])

    names.append("LAnkleRoll")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([-0.0735901, -0.0858622, -0.125746, -0.0858622, -0.105804, -0.124296, -0.144238, -0.124296, -0.314512, -0.314512, -0.0858622, -0.125746, -0.0858622, -0.105804, -0.113474])

    names.append("LElbowRoll")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([-0.435615, -1.24863, -1.07529, -0.990921, -1.4005, -1.54462, -1.39897, -1.24863, -1.07529, -0.990921, -1.4005, -1.54462, -1.39897, -1.24863, -1.07529, -0.990921, -1.4005, -1.54462, -1.39897, -1.53856, -1.33309, -1.34689, -1.43126, -1.31468, -0.83147, -1.16281, -1.33309, -1.34689, -1.43126, -1.31468, -0.83147, -1.16281, -1.33309, -1.34689, -1.43126, -1.31468, -0.83147, -1.16281, -0.932714, -0.932714, -1.24863, -1.07529, -0.990921, -1.4005, -1.54462, -1.39897, -1.24863, -1.07529, -0.990921, -1.4005, -1.54462, -1.39897, -1.24863, -1.07529, -0.990921, -1.4005, -1.54462, -1.39897, -1.53856, -0.446352])

    names.append("LElbowYaw")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([-1.21344, -0.434165, -0.31758, -0.16418, 0.061318, 0.190241, -0.176453, -0.434165, -0.31758, -0.165714, 0.061318, 0.190241, -0.176453, -0.434165, -0.31758, -0.16418, 0.061318, 0.190241, -0.176453, -1.57086, -0.185572, -0.144154, -0.174835, -0.351244, -0.446352, 0.036858, -0.185572, -0.144154, -0.176367, -0.351244, -0.446352, 0.036858, -0.185572, -0.144154, -0.174835, -0.351244, -0.446352, 0.036858, 0.389678, 0.389678, -0.434165, -0.31758, -0.16418, 0.061318, 0.190241, -0.176453, -0.434165, -0.31758, -0.165714, 0.061318, 0.190241, -0.176453, -0.434165, -0.31758, -0.16418, 0.061318, 0.190241, -0.176453, -1.57086, -1.19503])

    names.append("LHand")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([0.3136, 0, 0.1872, 0.188, 0.184, 0, 0.1908, 0, 0.1872, 0.188, 0.184, 0, 0.1908, 0, 0.1872, 0.188, 0.184, 0, 0.1908, 1, 0, 0.1568, 0.178, 0.1616, 0.1672, 0.1668, 0, 0.1568, 0.178, 0.1616, 0.1672, 0.1668, 0, 0.1568, 0.178, 0.1616, 0.1672, 0.1668, 1, 1, 0, 0.1872, 0.188, 0.184, 0, 0.1908, 0, 0.1872, 0.188, 0.184, 0, 0.1908, 0, 0.1872, 0.188, 0.184, 0, 0.1908, 1, 0.2976])

    names.append("LHipPitch")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([0.131966, -0.052114, -0.33437, -0.052114, -0.406468, -0.0767419, -0.44797, -0.0798099, -0.104354, -0.104354, -0.052114, -0.33437, -0.052114, -0.406468, 0.144238])

    names.append("LHipRoll")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([0.06447, 0.1335, 0.174919, 0.131966, 0.276162, 0.128814, 0.108872, 0.128814, 0.208583, 0.208583, 0.1335, 0.174919, 0.131966, 0.276162, 0.115092])

    names.append("LHipYawPitch")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([-0.170232, -0.36505, -0.378855, -0.36505, -0.371186, -0.36505, -0.378855, -0.36505, -0.371186, -0.371186, -0.36505, -0.378855, -0.36505, -0.371186, -0.171766])

    names.append("LKneePitch")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([-0.0874801, 0.731677, 1.13358, 0.730143, 1.30079, 0.653526, 1.00481, 0.650458, 0.856014, 0.856014, 0.731677, 1.13358, 0.730143, 1.30079, -0.092082])

    names.append("LShoulderPitch")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([1.4818, 0.357381, 0.510779, 0.584411, 0.605888, 0.101229, 0.282215, 0.357381, 0.510779, 0.584411, 0.605888, 0.101229, 0.282215, 0.357381, 0.510779, 0.584411, 0.605888, 0.101229, 0.282215, 0.095066, 0.624379, 0.744032, 0.510865, 0.309909, 0.61671, 0.725624, 0.624379, 0.744032, 0.510865, 0.309909, 0.61671, 0.725624, 0.624379, 0.744032, 0.510865, 0.309909, 0.61671, 0.725624, 0.72409, 0.72409, 0.357381, 0.510779, 0.584411, 0.605888, 0.101229, 0.282215, 0.357381, 0.510779, 0.584411, 0.605888, 0.101229, 0.282215, 0.357381, 0.510779, 0.584411, 0.605888, 0.101229, 0.282215, 0.095066, 1.4726])

    names.append("LShoulderRoll")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([0.0797259, 0.159494, 0.141086, 0.151824, 0.0889301, -0.0907571, -0.066004, 0.159494, 0.141086, 0.151824, 0.0889301, -0.0907571, -0.066004, 0.159494, 0.141086, 0.151824, 0.0889301, -0.0907571, -0.066004, 0.466294, 0.0337899, -0.164096, -0.124212, -0.182504, -0.0843279, -0.052114, 0.0337899, -0.164096, -0.124212, -0.182504, -0.0843279, -0.052114, 0.0337899, -0.164096, -0.124212, -0.182504, -0.0843279, -0.052114, 0.193327, 0.193327, 0.159494, 0.141086, 0.151824, 0.0889301, -0.0907571, -0.066004, 0.159494, 0.141086, 0.151824, 0.0889301, -0.0907571, -0.066004, 0.159494, 0.141086, 0.151824, 0.0889301, -0.0907571, -0.066004, 0.466294, 0.12728])

    names.append("LWristYaw")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([-0.213269, -0.573758, -0.615176, -0.412688, -0.194861, -0.961676, -0.763974, -0.573758, -0.615176, -0.412688, -0.194861, -0.961676, -0.763974, -0.573758, -0.615176, -0.411154, -0.194861, -0.961676, -0.763974, -1.79483, -0.421808, -0.409536, -0.46476, -0.486237, -0.472429, -0.131882, -0.421808, -0.409536, -0.46476, -0.486237, -0.472429, -0.131882, -0.421808, -0.409536, -0.46476, -0.486237, -0.472429, -0.131882, -0.581345, -0.581345, -0.573758, -0.615176, -0.412688, -0.194861, -0.961676, -0.763974, -0.573758, -0.615176, -0.412688, -0.194861, -0.961676, -0.763974, -0.573758, -0.615176, -0.411154, -0.194861, -0.961676, -0.763974, -1.79483, 0.0843279])

    names.append("RAnklePitch")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([0.0951499, -0.31136, -0.355846, -0.31136, -0.443284, -0.417291, -0.607505, -0.421891, -0.671934, -0.671934, -0.31136, -0.355846, -0.31136, -0.443284, 0.105888])

    names.append("RAnkleRoll")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([0.122762, 0.124296, 0.144238, 0.124296, 0.314512, 0.0858622, 0.125746, 0.0858622, 0.105804, 0.105804, 0.124296, 0.144238, 0.124296, 0.314512, 0.073674])

    names.append("RElbowRoll")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([0.385075, 1.33309, 1.34689, 1.43126, 1.31468, 0.83147, 1.16281, 1.33309, 1.34689, 1.43126, 1.31468, 0.83147, 1.16281, 1.33309, 1.34689, 1.43126, 1.31468, 0.83147, 1.16281, 0.932714, 1.24863, 1.07529, 0.990921, 1.4005, 1.54462, 1.39897, 1.24863, 1.07529, 0.990921, 1.4005, 1.54462, 1.39897, 1.24863, 1.07529, 0.990921, 1.4005, 1.54462, 1.39897, 1.53856, 1.53856, 1.33309, 1.34689, 1.43126, 1.31468, 0.83147, 1.16281, 1.33309, 1.34689, 1.43126, 1.31468, 0.83147, 1.16281, 1.33309, 1.34689, 1.43126, 1.31468, 0.83147, 1.16281, 0.932714, 0.428028])

    names.append("RElbowYaw")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([1.23176, 0.185572, 0.144154, 0.174835, 0.351244, 0.446352, -0.036858, 0.185572, 0.144154, 0.176367, 0.351244, 0.446352, -0.036858, 0.185572, 0.144154, 0.174835, 0.351244, 0.446352, -0.036858, -0.389678, 0.434165, 0.31758, 0.16418, -0.061318, -0.190241, 0.176453, 0.434165, 0.31758, 0.165714, -0.061318, -0.190241, 0.176453, 0.434165, 0.31758, 0.16418, -0.061318, -0.190241, 0.176453, 1.57086, 1.57086, 0.185572, 0.144154, 0.174835, 0.351244, 0.446352, -0.036858, 0.185572, 0.144154, 0.176367, 0.351244, 0.446352, -0.036858, 0.185572, 0.144154, 0.174835, 0.351244, 0.446352, -0.036858, -0.389678, 1.17347])

    names.append("RHand")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([0.3112, 0, 0.1568, 0.178, 0.1616, 0.1672, 0.1668, 0, 0.1568, 0.178, 0.1616, 0.1672, 0.1668, 0, 0.1568, 0.178, 0.1616, 0.1672, 0.1668, 1, 0, 0.1872, 0.188, 0.184, 0, 0.1908, 0, 0.1872, 0.188, 0.184, 0, 0.1908, 0, 0.1872, 0.188, 0.184, 0, 0.1908, 1, 1, 0, 0.1568, 0.178, 0.1616, 0.1672, 0.1668, 0, 0.1568, 0.178, 0.1616, 0.1672, 0.1668, 0, 0.1568, 0.178, 0.1616, 0.1672, 0.1668, 1, 0.3044])

    names.append("RHipPitch")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([0.139552, -0.0767419, -0.44797, -0.0798099, -0.104354, -0.052114, -0.33437, -0.052114, -0.406468, -0.406468, -0.0767419, -0.44797, -0.0798099, -0.104354, 0.136484])

    names.append("RHipRoll")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([-0.116542, -0.128814, -0.108872, -0.128814, -0.208583, -0.1335, -0.174919, -0.131966, -0.276162, -0.276162, -0.128814, -0.108872, -0.128814, -0.208583, -0.0628521])

    names.append("RHipYawPitch")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([-0.170232, -0.36505, -0.378855, -0.36505, -0.371186, -0.36505, -0.378855, -0.36505, -0.371186, -0.371186, -0.36505, -0.378855, -0.36505, -0.371186, -0.171766])

    names.append("RKneePitch")
    times.append([1, 2, 3.32, 5.4, 6.32, 7.2, 8.52, 10.6, 11.52, 12.4, 13.48, 14.8, 16.88, 17.8, 19.72])
    keys.append([-0.0858622, 0.653526, 1.00481, 0.650458, 0.856014, 0.731677, 1.13358, 0.730143, 1.30079, 1.30079, 0.653526, 1.00481, 0.650458, 0.856014, -0.091998])

    names.append("RShoulderPitch")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([1.46808, 0.624379, 0.744032, 0.510865, 0.309909, 0.61671, 0.725624, 0.624379, 0.744032, 0.510865, 0.309909, 0.61671, 0.725624, 0.624379, 0.744032, 0.510865, 0.309909, 0.61671, 0.725624, 0.72409, 0.357381, 0.510779, 0.584411, 0.605888, 0.101229, 0.282215, 0.357381, 0.510779, 0.584411, 0.605888, 0.101229, 0.282215, 0.357381, 0.510779, 0.584411, 0.605888, 0.101229, 0.282215, 0.095066, 0.095066, 0.624379, 0.744032, 0.510865, 0.309909, 0.61671, 0.725624, 0.624379, 0.744032, 0.510865, 0.309909, 0.61671, 0.725624, 0.624379, 0.744032, 0.510865, 0.309909, 0.61671, 0.725624, 0.72409, 1.46501])

    names.append("RShoulderRoll")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([-0.067538, -0.0337899, 0.164096, 0.124212, 0.182504, 0.0843279, 0.052114, -0.0337899, 0.164096, 0.124212, 0.182504, 0.0843279, 0.052114, -0.0337899, 0.164096, 0.124212, 0.182504, 0.0843279, 0.052114, -0.193327, -0.159494, -0.141086, -0.151824, -0.0889301, 0.0907571, 0.066004, -0.159494, -0.141086, -0.151824, -0.0889301, 0.0907571, 0.066004, -0.159494, -0.141086, -0.151824, -0.0889301, 0.0907571, 0.066004, -0.466294, -0.466294, -0.0337899, 0.164096, 0.124212, 0.182504, 0.0843279, 0.052114, -0.0337899, 0.164096, 0.124212, 0.182504, 0.0843279, 0.052114, -0.0337899, 0.164096, 0.124212, 0.182504, 0.0843279, 0.052114, -0.193327, -0.0767419])

    names.append("RWristYaw")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4, 6.32, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10, 10.2, 10.4, 10.6, 11.52, 12.4, 13.48, 13.68, 13.88, 14.08, 14.28, 14.48, 14.68, 14.88, 15.08, 15.28, 15.48, 15.68, 15.88, 16.08, 16.28, 16.48, 16.68, 16.88, 17.8, 19.72])
    keys.append([-0.10282, 0.421808, 0.409536, 0.46476, 0.486237, 0.472429, 0.131882, 0.421808, 0.409536, 0.46476, 0.486237, 0.472429, 0.131882, 0.421808, 0.409536, 0.46476, 0.486237, 0.472429, 0.131882, 0.581345, 0.573758, 0.615176, 0.412688, 0.194861, 0.961676, 0.763974, 0.573758, 0.615176, 0.412688, 0.194861, 0.961676, 0.763974, 0.573758, 0.615176, 0.411154, 0.194861, 0.961676, 0.763974, 1.79483, 1.79483, 0.421808, 0.409536, 0.46476, 0.486237, 0.472429, 0.131882, 0.421808, 0.409536, 0.46476, 0.486237, 0.472429, 0.131882, 0.421808, 0.409536, 0.46476, 0.486237, 0.472429, 0.131882, 0.581345, 0.118076])

    return names,times,keys
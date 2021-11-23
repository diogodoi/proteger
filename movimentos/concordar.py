def sim():
      names = list()
      times = list()
      keys = list()

      names.append("HeadPitch")
      times.append([0.4, 0.92, 1.24, 1.66, 2.10, 2.70, 3.40, 4.24])
      keys.append([-0.013848, 0.415673, -0.268493, 0.415673, -0.268493, 0.415673, -0.268493, 0.1733])

      names.append("HeadYaw")
      times.append([0.4, 0.92, 1.24, 1.66, 2.10, 2.70, 3.40, 4.24])
      keys.append([-4.19617e-05, 0.010696, 0.00456004, 0.010696, 0.00456004, 0.010696, 0.00456004, -4.19617e-05])

      return names, times, keys

"""
      #codigo original
      names = list()
      times = list()
      keys = list()

      names.append("HeadPitch")
      times.append([0.64, 0.88, 1.08, 1.32, 1.56, 1.84, 2.12, 2.72])
      keys.append([-0.013848, 0.415673, -0.268493, 0.415673, -0.268493, 0.415673, -0.268493, 0.1733])

      names.append("HeadYaw")
      times.append([0.64, 0.88, 1.08, 1.32, 1.56, 1.84, 2.12, 2.72])
      keys.append([-4.19617e-05, 0.010696, 0.00456004, 0.010696, 0.00456004, 0.010696, 0.00456004, -4.19617e-05])

      names.append("LAnklePitch")
      times.append([1.48])
      keys.append([-0.232481])

      names.append("LAnkleRoll")
      times.append([1.48])
      keys.append([-0.187148])

      names.append("LElbowRoll")
      times.append([0.48, 0.88, 1.52, 2.04])
      keys.append([-0.843657, -1.10137, -1.22102, -0.74088])

      names.append("LElbowYaw")
      times.append([0.48, 0.88, 1.52, 2.04])
      keys.append([-1.3561, -1.10606, -1.26559, -1.25179])

      names.append("LHand")
      times.append([0.96, 2.16])
      keys.append([0.161481, 0.161117])

      names.append("LHipPitch")
      times.append([1.48])
      keys.append([0.502304])

      names.append("LHipRoll")
      times.append([1.48])
      keys.append([0.282256])

      names.append("LHipYawPitch")
      times.append([1.48])
      keys.append([-0.343615])

      names.append("LKneePitch")
      times.append([1.48])
      keys.append([0.109076])

      names.append("LShoulderPitch")
      times.append([0.48, 0.88, 1.52, 2.04])
      keys.append([1.66742, 1.41584, 1.52169, 1.60299])

      names.append("LShoulderRoll")
      times.append([0.48, 0.88, 1.52, 2.04])
      keys.append([0.214717, 0.15796, 0.16563, 0.16563])

      names.append("LWristYaw")
      times.append([0.96, 2.16])
      keys.append([-0.48632, 0.185572])

      names.append("RAnklePitch")
      times.append([1.48])
      keys.append([-0.23555])

      names.append("RAnkleRoll")
      times.append([1.48])
      keys.append([-0.0322141])

      names.append("RElbowRoll")
      times.append([0.48, 0.88, 1.52, 2.04])
      keys.append([1.1981, 1.36837, 1.38678, 1.03089])

      names.append("RElbowYaw")
      times.append([0.48, 0.88, 1.52, 2.04])
      keys.append([0.816046, 0.704064, 1.05995, 1.06149])

      names.append("RHand")
      times.append([0.96, 2.16])
      keys.append([0.280389, 0.280389])

      names.append("RHipPitch")
      times.append([1.48])
      keys.append([0.399527])

      names.append("RHipRoll")
      times.append([1.48])
      keys.append([0.0475539])

      names.append("RKneePitch")
      times.append([1.48])
      keys.append([0.254806])

      names.append("RShoulderPitch")
      times.append([0.48, 0.88, 1.52, 2.04])
      keys.append([1.37451, 1.07691, 1.23798, 1.57393])

      names.append("RShoulderRoll")
      times.append([0.48, 0.88, 1.52, 2.04])
      keys.append([-0.084412, -0.067538, -0.081344, -0.16418])

      names.append("RWristYaw")
      times.append([0.96, 2.16])
      keys.append([0.722472, -0.00157596])
"""

special_table = {"Neck": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25], "Whiplash(1)"),
                 "Mouth": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                                        "Lockjaw(1)"),
                 "Nose": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                                       "Disoriented(2), Nose Broken"),
                 "Ear": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                                      "Tinnitus(1)"),
                 "Eye": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                                      "Vision Loss(3)"),
                 "Forehead": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                            22, 23, 24, 25, 26, 27, 28, 29, 30], "Disoriented(2)"),
                 "Hand": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25], "Flinch(1)"),
                 "Bicep and Forearm": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                     20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "Flinch(1)"),
                 "Elbow and Shoulder": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                      20, 21, 22, 23, 24, 25], "Weakened (1)"),
                 "Foot": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                        23, 24, 25], "Slowed(2)"),
                 "Shin and Thigh": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                  20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "Slowed(1)"),
                 "Knee and Hip": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                                21, 22, 23, 24, 25], "Knockdown"),
                 "Pelvis": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                          21, 22, 23, 24, 25], "Slowed(2)"),
                 "Intestines": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                              21, 22, 23, 24, 25], "Tattered(2)"),
                 "Spine": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                         21, 22, 23, 24, 25], "Flinch(1), Drop, Knockdown"),
                 "Stomach, Kidney, Liver": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                                          21, 22, 23, 24, 25], "Gasping(1)"),
                 "Heart": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                         21, 22, 23, 24, 25], "Winded(5)"),
                 "Lungs": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                         21, 22, 23, 24, 25], "Winded(2), Gasping(2)"),
                 "Ribcage, No Organ": dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                                                     20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                                                    "Winded(1), Gasping(1)")
                 }
special_table["Neck"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], "Whiplash(2)"))
special_table["Neck"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], "Whiplash(3), "
                                                                                                         "Bloodloss(1)")
                             )
special_table["Neck"].update(dict.fromkeys([56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                                           "Whiplash(4), Bloodloss(2), Looming Death(20)"))
special_table["Neck"].update(dict.fromkeys([71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                           "Whiplash(4), Bloodloss(4), Looming Death(1d10)"))

special_table["Mouth"].update(dict.fromkeys([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "Lockjaw(5)"))
special_table["Mouth"].update(dict.fromkeys([31, 32, 33, 34, 35, 36, 37, 38, 39, 40], "Lockjaw(10), Lose 1D5 Teeth"))

special_table["Mouth"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50], "Lockjaw(20), Whiplash(2), "
                                                                                      "Lose 2D5 Teeth"))
special_table["Mouth"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 58, 59, 60, 61,
                                             62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                                             73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], "Lockjaw(Permanent), "
                                                                                              "Whiplash(4), "
                                                                                              "Lose 2D10 Teeth"))

special_table["Nose"].update(dict.fromkeys([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "Disoriented(4), Nose Broken"))
special_table["Nose"].update(dict.fromkeys([31, 32, 33, 34, 35, 36, 37, 38, 39, 40], "Gasping (2), Nose Broken"))
special_table["Nose"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50], "Gasping(3), Nose Broken"))
special_table["Nose"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 58, 59, 60, 61,
                                            62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                                            73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], "Gasping(4), Nose Lost"))


special_table["Ear"].update(dict.fromkeys([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "Tinnitus(3)"))
special_table["Ear"].update(dict.fromkeys([31, 32, 33, 34, 35, 36, 37, 38, 39, 40], "Tinnitus(5), Flinch(1)"))
special_table["Ear"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                                          "Tinnitus(10), Flinch(2), Whiplash(1)"))
special_table["Ear"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 58, 59, 60, 61,
                                           62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                                           73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], "Tinnitus(60), Stunned(3D5)"
                                                                                            ", Ear Lost"))

special_table["Eye"].update(dict.fromkeys([21, 22, 23, 24, 25, 26, 27, 28, 29, 30], "Vision Loss(5)"))
special_table["Eye"].update(dict.fromkeys([31, 32, 33, 34, 35, 36, 37, 38, 39, 40], "Vision Loss(10), Flinch(1)"))
special_table["Eye"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                                          "Vision Loss(10), Flinch(2), Whiplash(1)"))
special_table["Eye"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 58, 59, 60, 61,
                                           62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                                           73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                          "Vision Loss(60), Stunned (3D5), Eye Lost"))

special_table["Forehead"].update(dict.fromkeys([31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
                                                49, 50], "Disoriented(4), Shellshock(1)"))
special_table["Forehead"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65],
                                               "Disoriented(6), Shellshock(2)"))

special_table["Forehead"].update(dict.fromkeys([66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                                               "Disoriented(10), Stunned(3D5), Looming Death(10)"))
special_table["Forehead"].update(dict.fromkeys([81, 82, 83, 84, 86, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95],
                                               "Instant Death, Head Destroyed"))

special_table["Hand"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                           "Flinch(1), Drop"))
special_table["Hand"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55],
                                           "Flinch(3), Drop(5), Bone Broken(Fracture)"))
special_table["Hand"].update(dict.fromkeys([56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                                           "Flinch(3), Drop(10), Bone Broken(Shatter)")
                             )
special_table["Hand"].update(dict.fromkeys([71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                           "Flinch (5), Hand Lost"))

special_table["Bicep and Forearm"].update(dict.fromkeys([31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
                                                         47, 48, 49, 50],
                                                        "Flinch (2), Paralyzed (1)"))
special_table["Bicep and Forearm"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65],
                                                        "Flinch(5), Bone Broken(Fracture)"))
special_table["Bicep and Forearm"].update(dict.fromkeys([66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                                                        "Flinch(6), Bone Broken(Shatter)"))
special_table["Bicep and Forearm"].update(dict.fromkeys([81, 82, 83, 84, 86, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95],
                                                        "Looming Death(10), Arm Lost"))

special_table["Elbow and Shoulder"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                                         "Weakened(2), Drop"))
special_table["Elbow and Shoulder"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55],
                                                         "Weakened(4), Drop(2), Bone Broken(Fractured)"
                                                         ))
special_table["Elbow and Shoulder"].update(dict.fromkeys([56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                                                          67, 68, 69, 70], "Weakened(4), Paralyzed(2), "
                                                                           "Bone Broken(Shatter)"))
special_table["Elbow and Shoulder"].update(dict.fromkeys([71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                                         "Looming Death(9), Arm Lost"))

special_table["Foot"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                           "Slowed(3), Knockdown"))

special_table["Foot"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55],
                                           "Slowed(5), Knockdown(2), Bone Broken(Fracture)"))
special_table["Foot"].update(dict.fromkeys([56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                                            67, 68, 69, 70], "Slowed(6), Knockdown, Prone(2), Bone Broken(Shatter)"))
special_table["Foot"].update(dict.fromkeys([71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                           "Slowed(10, Knockdown, Prone(4), Foot Lost"))

special_table["Shin and Thigh"].update(dict.fromkeys([31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
                                                      47, 48, 49, 50], "Slowed(3)"))
special_table["Shin and Thigh"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65],
                                                     "Slowed(6), Paralyzed(2), Bone Broken(Fracture)"))
special_table["Shin and Thigh"].update(dict.fromkeys([66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                                                     "Slowed(7), Paralyzed(3), Bone Broken(Shatter)"))
special_table["Shin and Thigh"].update(dict.fromkeys([81, 82, 83, 84, 86, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95],
                                                     "Slowed(10), Paralyzed(4), Looming Death(8), Leg Lost"))

special_table["Knee and Hip"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                                   "Knockdown(1)"))
special_table["Knee and Hip"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55],
                                                   "Knockdown(2), Slowed(3), Bone Broken(Fracture)"))
special_table["Knee and Hip"].update(dict.fromkeys([56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                                                    67, 68, 69, 70], "Knockdown(3), Slowed(5), Bone Broken(Shatter)"))
special_table["Knee and Hip"].update(dict.fromkeys([71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                                   "Knockdown(10), Slowed(10), Looming Death(8), Bone Broken(Shatter)"))

special_table["Pelvis"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                             "Slowed(3), Tattered(2)"))
special_table["Pelvis"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55],
                                             "Slowed(4), Tattered(3), Bone Broken(Fracture)"))
special_table["Pelvis"].update(dict.fromkeys([56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                                             "Slowed(4), Tattered(5), Bone Broken(Shatter)"))
special_table["Pelvis"].update(dict.fromkeys([71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], "Slowed(Permanen"
                                                                                                       "t), Tattered(20"
                                                                                                       "), Bone Broken("
                                                                                                       "Shatter)"))

special_table["Intestines"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                                 "Tattered(3), Weakened(2)"))
special_table["Intestines"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50], "Tattered(4), Weakened(4)"))
special_table["Intestines"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 59, 60], "Tattered(5), Weakened(5),"
                                                                                           " Looming Death(15)"))
special_table["Intestines"].update(dict.fromkeys([61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                                                  73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                                 "Tattered(6), Weakened(5), Looming Death(1D10)"))

special_table["Spine"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                            "Flinch(2), Drop(2), Knockdown(1)"))
special_table["Spine"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55],
                                            "Paralyzed(2), Knockdown(3), Bone Broken(Fractured)"))
special_table["Spine"].update(dict.fromkeys([56, 57, 58, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                                            "Paralyzed(5), Knockdown Prone(5), Bone Broken(Shatter)"))
special_table["Spine"].update(dict.fromkeys([71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                            "Spine destroyed, Instant Death"))

special_table["Stomach, Kidney, Liver"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                                             "Gasping(2), Tattered(1)"))
special_table["Stomach, Kidney, Liver"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                                                             "Gasping(3), Tattered(2)"))
special_table["Stomach, Kidney, Liver"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 59, 60], "Gasping(5), "
                                                                                                       "Tattered(5), "
                                                                                                       "Looming Death"
                                                                                                       "(20)"))
special_table["Stomach, Kidney, Liver"].update(dict.fromkeys([61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                                                              73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                                             "Gasping(6), Tattered(6), Looming Death(10)"))

special_table["Heart"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                            "Winded(10), Stunned(2D5), Looming Death(5D10)"))
special_table["Heart"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50], "Winded(10), Stunned(3D5), "
                                                                                      "Looming Death(3D10)"))
special_table["Heart"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 59, 60], "Winded(Permanent), Stunned(3D5),"
                                                                                      " Looming Death(1D10)"))
special_table["Heart"].update(dict.fromkeys([61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                                             73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                            "Heart Destroyed, Instant Death"))

special_table["Lungs"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                            "Winded(3), Gasping(3)"))
special_table["Lungs"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50], "Winded(4), Gasping(5), "
                                                                                      "Looming Death(20)"))
special_table["Lungs"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 59, 60], "Winded(5), Gasping(5), "
                                                                                      "Looming Death(15)"))
special_table["Lungs"].update(dict.fromkeys([61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                                             73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                            "Winded(6), Gasping(5), Suffocation"))

special_table["Ribcage, No Organ"].update(dict.fromkeys([26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                                                        "Winded(2), Gasping(1)"))
special_table["Ribcage, No Organ"].update(dict.fromkeys([41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                                                        "Winded(3), Gasping(2)"))
special_table["Ribcage, No Organ"].update(dict.fromkeys([51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                                                        "Winded(4), Gasping(4), Bone Broken(Fractured)"))
special_table["Ribcage, No Organ"].update(dict.fromkeys([61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                                                         73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
                                                        "Winded(5), Gasping(4), Bone Broken(Shatter)"))


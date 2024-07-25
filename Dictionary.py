body_part = dict.fromkeys([1, 2], "Neck")
body_part.update(dict.fromkeys([3, 4], "Mouth"))
body_part.update(dict.fromkeys([5, 6], "Nose"))
body_part.update(dict.fromkeys([7], "Eye"))
body_part.update(dict.fromkeys([8], "Ear"))
body_part.update(dict.fromkeys([9, 10], "Forehead"))
body_part.update(dict.fromkeys([11, 12], "Hand"))
body_part.update(dict.fromkeys([13, 14, 15], "Forearm"))
body_part.update(dict.fromkeys([16], "Elbow"))
body_part.update(dict.fromkeys([17, 18, 19], "Bicep"))
body_part.update(dict.fromkeys([20], "Shoulder"))
body_part.update(dict.fromkeys([21, 22], "Hand"))
body_part.update(dict.fromkeys([23, 24, 25], "Forearm"))
body_part.update(dict.fromkeys([26], "Elbow"))
body_part.update(dict.fromkeys([27, 28, 29], "Bicep"))
body_part.update(dict.fromkeys([30], "Shoulder"))
body_part.update(dict.fromkeys([31, 32], "Foot"))
body_part.update(dict.fromkeys([33, 34, 35, 36, 37], "Shin"))
body_part.update(dict.fromkeys([38], "Knee"))
body_part.update(dict.fromkeys([39, 40, 41, 42, 43], "Thigh"))
body_part.update(dict.fromkeys([44, 45], "Hip"))
body_part.update(dict.fromkeys([46, 47], "Foot"))
body_part.update(dict.fromkeys([48, 49, 50, 51, 52, 53], "Shin"))
body_part.update(dict.fromkeys([54], "Knee"))
body_part.update(dict.fromkeys([55, 56, 57, 58], "Thigh"))
body_part.update(dict.fromkeys([59, 60], "Hip"))
body_part.update(dict.fromkeys([61, 62, 63, 64, 65], "Pelvis"))
body_part.update(dict.fromkeys([66, 67, 68, 69, 70, 71, 72], "Intestines"))
body_part.update(dict.fromkeys([73, 74, 75, 76, 77, 78], "Spine"))
body_part.update(dict.fromkeys([79, 80, 81, 82, 83, 84], "Stomach, Kidney, Liver"))
body_part.update(dict.fromkeys([85, 86, 87, 88, 89], "Heart"))
body_part.update(dict.fromkeys([90, 91, 92, 93, 94, 95, 96], "Lungs"))
body_part.update(dict.fromkeys([97, 98, 99, 100], "Ribcage, No Organ"))


spc_dmg_description = {
    "Stunned": "Cannot take Actions or Reactions for (X) Half-Actions,\n reduced by Tou Mod. +10 WF Tests made against."
    ,
    "Disoriented": "A Character who has suffered Lost will not be able to tell what direction they are facing, \n"
                   "where they are, or tell allies from enemies. Lost lasts for (X) Half Actions, reduced by Half \n"
                   "the Character’s Toughness Modifier, to a minimum of 1, and ends at the end of the "
                   "Character’s Turn. \n"
                   "Lost Characters can have their Lost reduced by another Character by making an Intellect, Charisma,\n"
                   "or Leadership Test. The Rounds are reduced by 1 if Successful, and an extra +1 for every 2 Degrees of Success.",
    "Lockjaw": "Unable to speak louder than whisper, eat,\n or use mouth for anything for (X) Rounds.",
    "Tinnitus": "-20 Penalty to Hearing-Based Perception Checks.\n Lasts (X) Rounds and until end of Character's turn.",
    "Vision": "-20 Penalty to Sight-Based Perception Checks.\n Lasts (X) Rounds and until end of Character's turn."
    ,
    "Shellshock": "-20 Penalty to all Actions. Will also struggle\n to remember name and other simple pieces of info.\n"
                  "Lasts (X) Rounds and until end of the Character's turn.",
    "Whiplash": "Reactions, including Evasion, are at -30 Penalty.\nLasts (X) Rounds and until end of Character's turn",
    "Winded": "Turns reduced to only being able to take a Half Action.\nLasts for (X) Rounds.",
    "Gasping": "-20 Penalty to any Physical and Warfare tests, including Skills and Attacking.\n"
               "Lasts for (X) Rounds and until end of the Character's turn.",
    "Slowed": "Reduce Movement Speeds, Jump and Leap Distances,\nClimbing, and Swimming speeds by Half.\n"
              "Lasts (X) Rounds.",
    "Suffocation": "Can no longer breathe and will die after\nas many Turns as breath can be held.",
    "Tattered": "Take a level of Fatigue for each Half Action used for\nMovement, Melee Weapons, or Heavy Weapons.\n"
                "Lasts for (X) Half Actions.",
    "Paralyzed": "Limb struck cannot be used and considered useless for (X) rounds.",
    "Bone": "Fractured Limb: Gives 1 Fatigue for each round the limb is used. "
                   "\nShattered Limb: Gives 1 Fatigue and 1 Wound for each round the limb is used.",
    "Weakened": "Reduces amount of their Melee Attacks by half. Lasts for (X) Rounds.",
    "Flinch": "Body swings in a direction that causes their Attacks to have -30 for (X) Half Actions.",
    "Drop": "Drop whatever is in hand and cannot pick up or hold objects for (X) Rounds. "
            "If [TH] weapon is held, make STR test to keep holding with one hand. If [HW], test is at -20.",
    "Bloodloss": "Increases damage taken from any source by (X) amount. Lasts until Extended Medical Test given.",
    "Knockdown": "Moved from Standing to Crouching, or Crouching to Prone. Can also be Standing to Prone if specified. "
                 "Character unable to Stand Up or go from Prone to Crouching for (X) Rounds.",
    "Looming Death": "Character will die regardless of wounds in (X) Rounds, increased by TOU and Mythic TOU. "
                     "Can be stopped by having Biofoam or Sealant Mesh applied to Location struck.",
    "Instant Death": "Character dies regardless of any circumstances. "
                     "Burning luck allows survival and no reduction of wounds beyond the damage of the attack",
    "Eye": "Warfare Characteristic Tests and sight-based Perceptions Tests reduced by -20.",
    "Nose": "-30 penalty to Smell-based Perception tests.",
    "Foot": "Reduce movement by half(round up), -20 to any movement actions, skills, and characteristic tests.",
    "Leg": "Reduce movement by half, -40 to movement actions, skills, characteristic tests. Cannot use Evasion",
    "Ear": "-20 penalty to Hearing-Based Perception Tests.",
    "Hand": "-20 penalty to skills and tests that require two hands. Unable to wield [TH] weapons. "
                 "Equipment can be strapped to arm, however.",
    "Arm": "Same with lost hand, but cannot strap anything to the missing arm.",
    "Lung": "Can only hold breath for half the standard time. Fatigue is doubled. Cannot Run or Charge."
}

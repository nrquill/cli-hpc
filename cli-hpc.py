import argparse
import re

# Body Ratios
MALE_RATIO = {
    "Head_Height": [(6, 5.5), (11, 6), (15, 7), (21, 7.5), (50, 8), (70, 7.5)],
    "Chin_To_S": [(6, 0.2), (11, 0.2), (15, 0.3), (21, 0.3), (50, 0.33), (70, 0.3)],
    "S_Width": [(6, 1.3), (11, 1.3), (15, 1.3), (21, 1.7), (50, 2.0), (70, 1.6)],
    "S_To_Finger": [(6, 2.5), (11, 2.3), (15, 2.7), (21, 3.1), (50, 3.5), (70, 3.1)],
    "S_To_Nipple": [(6, 0.4), (11, 0.4), (15, 0.6), (21, 0.6), (50, 0.66), (70, 0.6)],
    "S_To_C": [(6, 2.0), (11, 2.0), (15, 2.3), (21, 2.4), (50, 2.6), (70, 2.1)],
    "S_To_Navel": [(6, 1.2), (11, 1.3), (15, 1.3), (21, 1.5), (50, 1.65), (70, 1.5)],
    "S_To_Elbow": [(6, 1.1), (11, 1.0), (15, 1.3), (21, 1.4), (50, 1.7), (70, 1.4)],
    "Elbow_To_Finger": [(6, 1.4), (11, 1.1), (15, 1.4), (21, 1.7), (50, 1.8), (70, 1.7)],
    "C_To_F": [(6, 2.3), (11, 2.8), (15, 3.3), (21, 3.7), (50, 4.0), (70, 3.5)],
    "C_To_K": [(6, 1.0), (11, 1.4), (15, 1.5), (21, 1.9), (50, 2.0), (70, 1.8)],
    "K_To_Heel": [(6, 1.3), (11, 1.4), (15, 1.8), (21, 1.8), (50, 2.0), (70, 1.7)]
}

FEMALE_RATIO = {
    "Head_Height": [(6, 5.5), (11, 6), (15, 7), (21, 7.5), (50, 8), (70, 7.5)],
    "Chin_To_S": [(6, 0.2), (11, 0.2), (15, 0.3), (21, 0.3), (50, 0.33), (70, 0.3)],
    "S_Width": [(6, 1.3), (11, 1.4), (15, 1.3), (21, 1.5), (50, 2.0), (70, 1.6)],
    "S_To_Finger": [(6, 2.5), (11, 2.3), (15, 2.7), (21, 3.1), (50, 3.5), (70, 3.1)],
    "S_To_Nipple": [(6, 0.4), (11, 0.4), (15, 0.6), (21, 0.6), (50, 0.8), (70, 0.6)],
    "S_To_C": [(6, 2.0), (11, 2.0), (15, 2.3), (21, 2.7), (50, 3.0), (70, 2.1)],
    "S_To_Navel": [(6, 1.2), (11, 1.3), (15, 1.3), (21, 1.6), (50, 1.8), (70, 1.5)],
    "S_To_Elbow": [(6, 1.1), (11, 1.0), (15, 1.3), (21, 1.4), (50, 1.7), (70, 1.4)],
    "Elbow_To_Finger": [(6, 1.4), (11, 1.1), (15, 1.4), (21, 1.7), (50, 1.8), (70, 1.7)],
    "C_To_F": [(6, 2.3), (11, 2.8), (15, 3.3), (21, 3.5), (50, 3.6), (70, 3.5)],
    "C_To_K": [(6, 1.0), (11, 1.4), (15, 1.5), (21, 1.7), (50, 1.7), (70, 1.8)],
    "K_To_Heel": [(6, 1.3), (11, 1.4), (15, 1.8), (21, 1.8), (50, 2.0), (70, 1.7)]
}

def age_check(age):
    ageString = re.match(r"^(\d+)(m|f)$", age)
    if not ageString:
        raise argparse.ArgumentTypeError(f"Wrong format, <age><gender: 'm|f'")
    if not (6 <= int(ageString.group(1)) <= 70):
        raise argparse.ArgumentTypeError(f"Number out of range: {age}. Expected range: 6-70")
    return ageString


def height_check(height):
    heightString = re.match(r"(^\d+.?\d?)(ft|m|cm|in)", height)
    if not heightString:
        raise argparse.ArgumentTypeError(f"Wrong unit, {height}")
    return heightString


def main():
    # Instances parser
    parser = argparse.ArgumentParser(prog='LerpPropCalc',
                                    description='Calculates the length of human proportions based on a 7.5 Head_Height Ratio') 

    # Add args
    parser.add_argument("age", action='store', type=age_check, metavar="(Age)", help="Whole number age between 6-70")
    parser.add_argument("height", action='store', type=height_check, metavar="(Height)", help="Height Entry")
    parser.add_argument("detail", nargs='?', action='store', type=str, choices=['x'], metavar="x", help="Optional, if you want see the length of each limb")
    
    # Parses args
    args = parser.parse_args()

    # Makes vars
    AGE = int(args.age.group(1))
    HEIGHT = float(args.height.group(1))
    UNIT = args.height.group(2)

    EXTRA = "Detailed" if args.detail else " "


    # Load the appropriate ratio dictionary based on gender
    if args.age.group(2) == 'm':
        GENDER = "Male"
        RATIO = MALE_RATIO
    else:
        GENDER = "Female"
        RATIO = FEMALE_RATIO

    # Call interpolate_ratio function to print interpolated ratios
    C_RATIO = interpolate_ratio(AGE, RATIO, UNIT)
    #print(C_RATIO)
    HU = C_RATIO['Head_Height']
    C_HU = round((HEIGHT / HU), 3)
    TRUE_RATIO = {}
    for key, value in C_RATIO.items():
        if key == 'Head_Height':
            TRUE_RATIO['Total_Height'] = f"{round((value * C_HU), 2)}{UNIT}"
            TRUE_RATIO[key] = f"{round(C_HU, 2)}{UNIT}"
            continue
        TRUE_RATIO[key] = f"{round((value * C_HU), 2)}{UNIT}"
    #print(TRUE_RATIO)
    

    txt = []
    # If they wanted more details
    txt.append(f"\n{EXTRA} {AGE}yr {GENDER} Proportions\n")

    if EXTRA != ' ':
        txt.append("~~~~~~~~~~~~~~~~~~~~~~~")
        txt.append("S: Shoulder, C: Crotch, F: Feet, K: Knee \n")
        txt.append(f"HU's: {HU}\n")

        for measurement, value in TRUE_RATIO.items():
            measurement = measurement.replace("_", " ")
            txt.append(f"{measurement}: {value}")
        txt.append("~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        txt.append("~~~~~~~~~~~~~~~~~~~~~~~")
        txt.append(f"HU's: {HU}\n")
        txt.append(f"Height: {TRUE_RATIO['Total_Height']}")
        txt.append(f"Legs: {TRUE_RATIO['C_To_F']}")
        txt.append(f"Torso: {TRUE_RATIO['S_To_C']}")
        txt.append(f"Neck w/ Head: {TRUE_RATIO['Chin_To_S']}")
        txt.append("~~~~~~~~~~~~~~~~~~~~~~~")


    for line in txt:
        print(line)

def interpolate_ratio(age, ratio_dict, unit):
    # Iterate through each body part and interpolate if possible
    newDict = {}
    for key, value in ratio_dict.items():
        for i in range(len(value)):
            x0, y0 = value[i]
            if age == x0:   # If the age is exactly on the mark
                newDict[key] = round(y0, 3)
                break
            elif i < len(value) - 1:
                x1, y1 = value[i + 1]
                if x0 <= age < x1:  # Check if age is within the range (x0, x1)
                    interpolated_ratio = lerpY(x0, y0, x1, y1, age)
                    newDict[key] = round(interpolated_ratio, 3)
                    break
    return newDict


def lerpY(x0, y0, x1, y1, x):
    """Linearly interpolates between (x0, y0) and (x1, y1) at point x."""
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

if __name__ == "__main__":
    main()
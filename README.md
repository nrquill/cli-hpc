# cli-hpc
#### Description: 

  This python program is made for a quick output of human proportions. Using the "**argparse**" module, the program HAS to be ran with arguments. Said arguments being:

```
py cli-hpc.py Age[m|f] Height[ft|m] {x}
py cli-hpc.py 21m 6.2ft x

Age[m|f]      Age entry along with a Gender Entry
Height[ft|m]  Height entry along with unit display, doesn't make a difference under the hood.     {x}        Optional, if you want see the length of each limb
```


After inputting the arguments, they are parsed, and used to calculates the length of human proportions based the Head to Body Ratio based on age. The size of the head will drive the heart of the calculation to our dictionaries. They're 2 dicts for each gender, inside of these are ratios of average limb length in scale of 1 head. So the length of the head is:

`head = height / amount_of_heads_tall `

The amount of heads used to divide the height is driven by the age. (explained later)

Since the fundamental operation is division, there's no need to enter a unit. The purpose is just purely for aesthetic purposes along with readability. The result formatted and meant for easy copy and pasting.

Currently the limbs ratios are locked as for matured adults. What I mean by this are in the dictionaries. Since the length of limbs change **VASTLY** at certain ages, the values are currently locked to the **average ratio of 25 yr old human**. This is why this should be handled **experimentally**, since real people have many variables to take into account.

- Height
- Gender
- Age
- Race
- Body type
- Genetic factors
- Health conditions

But in terms of this program is only:

- Age
- Height
- Gender


Even with these limitations, this tool is highly useful for quick and easy access to human proportions.


### Age to Head Ratio:
	Age 6 is 5.5 heads tall
	Age 11 is 6 heads tall
	Age 15 is 7 heads tall
	Age 21 is 7.5 heads tall
	Age 50 is 8 heads tall
	Age 70 is 7 heads tall
### Limb to Head Ratio (male for example):
```
#hstookforevertofinish
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
```

## Linear Interpolation
In order to ensure a linear interpolation between these ranges, I ran functions to do this

```python
def linear_interpolate(x0, y0, x1, y1, x):
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

def smooth_transition(age):
    for i in range(len(age_to_head) - 1):
        x0, y0 = age_to_head[i]
        x1, y1 = age_to_head[i + 1]
        if x0 <= age <= x1:
            return linear_interpolate(x0, y0, x1, y1, age)
```

Based off of basic [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation) that I used to find the head-to-height ratio for ages that are not explicitly listed in the age-to-head ratios. For example, if you know the ratios for ages 11 and 30, you can use linear interpolation to estimate the ratio for age 13. Ensuring that the calculated proportions reflect gradual changes rather than abrupt jumps.

The `smooth_transition` function implements this by checking through the list of points ratios, and then applying the linear interpolation formula to compute the estimated ratio. This method allows the program to handle a wide range of ages accurately, making it a quick tool for calculating/estimating human proportions.

> In the future I plan on looking more into the study of human proportions so this can be more accurate. 

> Another side thought would to somehow include the use of the **Golden Ratio**— heard it relates nicely with anatomic proportions

# TODO:

- Use of the Golden Ratio
- Choice to Output to a text file

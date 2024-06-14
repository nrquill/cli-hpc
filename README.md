# cli-hpc
Human Proportion Calculator From the CLI
#### Description: 
	

  This python program is made for a quick output of human proportions. With the ratios derived from [an online HPC](https://hpc.anatomy4sculptors.com/) 

```
	Args:
Age[m|f]      Age entry along with a Gender Entry
Height[ft|m]  Height entry along with unit display, doesn't make a difference under the hood.
{x}        Optional, if you want see the detailed list of each limb

>py cli-hpc.py 21m 6.2ft x
```


After inputting the arguments, they are parsed, and used to calculate the length of human proportions. The size of the head will drive the heart of the calculation to our dictionaries. They're 2 dicts for each gender, inside of these are ratios of average limb length with age.

The amount of heads used to divide the height is driven by the age. (explained later)

Since the fundamental operation is division, there's no need to enter a unit. The purpose is just purely for aesthetic purposes along with readability. The result formatted and meant for easy copy and pasting.



### This script should be handled **experimentally**, since real people have many variables to take into account for proportions:

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

## Linear Interpolation
In order to ensure a linear interpolation between these ranges, I ran functions to do this

```python
def lerpY(x0, y0, x1, y1, x):
    """Linearly interpolates between (x0, y0) and (x1, y1) at point x."""
    return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

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
```

Based off of basic [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation) that I used to find the head-to-height ratio for ages that are not explicitly listed in the age-to-head ratios. For example, if you know the ratios for ages 11 and 30, you can use linear interpolation to estimate the ratio for age 13. Ensuring that the calculated proportions reflect gradual changes rather than abrupt jumps.

So with the ratio, the head height values being:
	`"Head_Height": [(6, 5.5), (11, 6), (15, 7), (21, 7.5), (50, 8), (70, 7.5)]`
 An age of 21 would give you 7.5 HU, but 30 would give 7.65.

The `interpolate_ratio` function implements this by checking through the list of body ratios that contain arrays of tuples containing (age, ratio). Then applying the linear interpolation formula to compute the estimated ratio from the next age. This method allows the program to handle a wide range of ages accurately, making it a quick tool for calculating/estimating human proportions. To automate the process of the example from earier I made the function return a dict of all ratios rightfully interpolated.


> In the future I plan on looking more into the study of human proportions so this can be more accurate. 

> Another side thought would to somehow include the use of the **Golden Ratio**— heard it relates nicely with anatomic proportions

# TODO:

- Use of the Golden Ratio
- Choice to Output to a text file

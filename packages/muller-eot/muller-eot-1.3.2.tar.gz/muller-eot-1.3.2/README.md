# Muller-EOT
![PyPi](https://img.shields.io/pypi/v/muller-eot)
![license](https://img.shields.io/github/license/cyschneck/Muller-EOT)

A Python package for [M. Müller implementation of the "Equation of Time - Problem in Astronomy"](http://info.ifpan.edu.pl/firststep/aw-works/fsII/mul/mueller.pdf) to calculate the Equation of Time based on the individual effect of eccentricity and obliquity

The combined effect of eccentricity and obliquity create the Equation of Time components.

| Effect of Eccentricity | Effect of Obliquity |
| ------------- | ------------- |
| ![effect_eccentricity](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_eccentricity_testing.png) | ![effect_obliquity](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_obliquity_testing.png) |

Combined Effect of the Eccentricity and Obliquity = Equation of Time
![effect_eot](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_eot_testing.png)

## Overview

The length of a day on Earth is only close to being 24 hours four times a year. For the rest of the year when the sun is at its highest point (solar noon), a clock can run as much as 16 minutes ahead (12:16pm) or 13 minutes behind (11:47am). This discrepancy is the result of the combined effect of a planet's obliquity (axial tilt) and its eccentricity (as well as other smaller gravitational forces like moons that are ignored here). Both of these features form two sine curves that oscillate throughout the year. The combined sum
of these two curves form the Equation of Time, a non-uniform change in time to fix to a clock.
A planet with an obliquity of 0° and perfectly circular orbit (zero eccentricity) would have
no difference in the Expected Solar Noon and the Actual Solar Noon.

Equation of Time = (Apparent Solar Time) - (Mean Solar Time) 

**Effect of Eccentricity:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484492-bf0f6098-fe13-44d3-b372-bcb8cc4120f8.png" />
</p>

**Effect of Obliquity:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484389-613ffb3e-9719-4962-a316-eeeb887af1c5.png" />
</p>

"Equation of time is determined by the following parameters: the eccentricity of 
the orbit of the Earth, the angle between the ecliptic and the equatorial planes, the 
angle P between the winter solstice and the perihelion relative to the sun or: 
the time span ∆t from the beginning of winter to the passage through periehlion" (Müller, 1995)

<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484797-23c81e99-0eee-4431-bc21-31429a615e4f.png" />
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484692-b07bad99-3c6c-43e5-904f-04200f72c571.png" />
</p>

The effect of eccentricity is the result of Kepler's Law where:

"Two well-known features of our solar system are at the basis of the variations
 in the apparent motion of the sun: 1.) According to Kepler's second law, the angular
 velocity of the Earth relative to the sun varies throughout a year. 2) Equal angles
 which the sun in its apparent movement goes through in the eclipitic do not correspond
 to equal angles we measure on the equatorial plane. However, it is these latter angles
 which are relevant for the measure of time, since the daily movement of the sun is
 parallel to the equatorial plane" (Müller, 1995)
 
**Effect on Angular Velocity (on Eccentricity):**

As a result of Kepler's law, planets moving in an ellipitc orbit will have variable angular velocity 
as a result of the second law where the area swept during a constant period of time is constant (=dA/dt)

<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203687968-4055d194-afe0-49e8-8b73-94f1b58a3969.png" />
</p>

"1.) parameter: the eccentricity. If e = 0 a regular variation results that is caused by
the inclination of the ecliptic plane. The deviations of the apparent solar time from the
mean solar time increase with growing e in winter and autumn. Thus, the yearly variation
becomes dominant. Since at the perihelion and aphelion the equation of time is only a
function of the ecliptic inclination and the angle P, all plots have the same value at these
two points.
2.) parameter: the inclination of the ecliptic. ε = 0 yields a plot which is symmetric to
the passage through the aphelion. The greater ε the more dominant the variation with a
period of half a year. All plots have four common points at the beginning of each season,
for the equation of time depends only on the two other parameters there (eccentricity
and P). As the projection from the ecliptic plane onto the equatorial plane does not
change the polar angle relative to the winter solstice, ε does not influence the value of the
equation of time at the beginning of a season.
3.) parameter: the time interval between the beginning of winter and the passage
through the perihelion. If ∆t = 0 the two main variations vanish both at the beginning
of winter and summer (because winter begins when the earth passes the perihelion; the
aphelion is the summer solstice). Therefore, the resulting function is symmetric and the
extreme values are in autumn and winter. If ∆t increases, the two components tend to
compensate each other in winter whereas the negative value in summer begins to dominate." (Müller, 1995)

Equation of Time is the combination of the effect of eccentricity and obliquity
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484851-c96be35a-2d4a-44df-a2ee-a9d88974aa9e.png" />
</p>

To calculate the difference in time for an individual day:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203877814-c2d710f3-0681-4f72-8607-0f96e2a33256.png" />
</p>

## Documentation
**calculateDifferenceEOTMinutes**
Calculate the difference in time (in minutes) based on orbital period, eccentricity, and obliquity. Returns a list of differences in time for each day in the orbital year
```
calculateDifferenceEOTMinutes(eccentricity=None,
				obliquity_deg=None,
				orbit_period=None)
```
Returns a dictionary for the difference in time for each day in a year {day: time difference}

**plotEOT**
Plot the differences in time for the EOT as well as the individual effect of obliquity and eccentricity
```
plotEOT(planet_name=None,
	eot_dict={},
	effect_title_str=None,
	plot_title=None,
	plot_x_title=None,
	plot_y_title=None,
	showPlot=True,
	fig_plot_color="C0",
	figsize_n=12,
	figsize_dpi=100,
	save_plot_name=None)
```
## Dependencies
Python 3.7+
```
pip3 install -r requirements.txt
```
## Install
PyPi pip install at [pypi.org/project/muller-eot/](https://pypi.org/project/muller-eot/)

```
pip install muller-eot
```
## Examples

Get a list of differences in time for each day of the Earth's orbit and then plot it as a function of days in orbit

```
import muller_eot

# Get a list of time differences for each day
eot_combined_dict = muller_eot.calculateDifferenceEOTMinutes(eccentricity=0.0167,
							obliquity_deg=23.45,
							orbit_period=365.25)

# Plot differences in time as a function of days
muller_eot.plotEOT(planet_name="Earth",
		eot_dict=eot_combined_dict,
		effect_title_str="Eccentricity (0.0167) and Obliquity (23.45)")
```
![effect_eot](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_eot_testing.png)

## Tests

TODO

## TODO:

calculateOrbitalPeriod(semimajor_axis) function

calculateDistanceBetweenSolisticePerhelion() function

calculatePerihelionDay() function

calculateWinterSolsticeDay() function

calculateEccentricity() function

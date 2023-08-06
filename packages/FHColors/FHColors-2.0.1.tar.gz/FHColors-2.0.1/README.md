# FHColors

A Package containing the corporate design colers of Fraunhofer Gesellschaft

## Colors

```python
import FHColors as fhc

print(fhc.colors.green1)
```
returns

```python
array([0.09019608, 0.61176471, 0.49019608, 1.        ])
```
available colors are:

* <span style="color:#179c7d">green1</span>
* <span style="color:#eb6a0a">orange1</span>
* <span style="color:#006e92">blue1</span>
* <span style="color:#e2001a">red1</span>
* <span style="color:#b1c800">green2</span>
* <span style="color:#feefd6">orange2</span>
* <span style="color:#25bae2">blue2</span>
* <span style="color:#e1e3e3">grey1</span>
* <span style="color:#a8afaf">grey2</span>


## Maps

```python
print(fhc.maps.BlackToGreenToWhite(.5))
```
returns

```python
(0.2497071555895085, 0.6798319327731093, 0.5795772854596384, 1.0)
```
available maps are:

* BlackToGreen
* WhiteToGreen
* GreenToWhite
* OrangeToGreen
* GreenToOrange
* BlackToGreenToOrangeToWhite
* BlackToGreenToWhite
* BlackToGreenToWhite_short
* colors

## Installation

```
pip install FHcolors
```

## Example 1

```python
from FHColors import colors, maps
import numpy as np
import matplotlib.pyplot as plt

maps=[
    maps.BlackToGreen,
    maps.GreenToWhite,
    maps.GreenToOrange,
    maps.BlackToGreenToOrangeToWhite,
    maps.BlackToGreenToWhite,
    maps.BlackToGreenToWhite_short,
    maps.colors]
mapnames=[
    'maps.BlackToGreen',
    'maps.GreenToWhite',
    'maps.GreenToOrange',
    'maps.BlackToGreenToOrangeToWhite',
    'maps.BlackToGreenToWhite',
    'maps.BlackToGreenToWhite_short',
    'maps.colors']
fig,axes=plt.subplots(nrows=len(maps), ncols=1)
fig.set_figheight(20)
fig.patch.set_facecolor(colors.grey1)
for ii,m in enumerate(maps):
    for i in np.arange(0,256,1):
        light=np.sum(m(i)[:3])/3
        axes[ii].plot([i],[light], 'o', markersize=30, color=m(i))
    axes[ii].set_xlabel('Colorvalue')
    axes[ii].set_ylabel('Brightness')
    axes[ii].title.set_text(mapnames[ii])
    axes[ii].patch.set_facecolor(colors.grey1)
plt.tight_layout(pad=3)
plt.savefig('maps.png',facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()
```

![](maps.png)

## Example 2

```python
import seaborn as sns

#generate testdata
y1 = 23+np.random.randn(100)
y2 = 23.5 + np.random.randn(100)
y = y1.tolist()+y2.tolist()
x1 = np.ones_like(y1)
x2 = np.ones_like(y1)*2
x = x1.tolist()+x2.tolist()


sns.boxplot(x=x, y=y, palette=sns.color_palette([colors.green1, colors.blue1]))
sns.swarmplot(x=x, y=y,color='k')
plt.xlabel('Group')
plt.ylabel('Eta /%')
plt.tight_layout()
plt.savefig('Boxplot_Eta.png')
plt.show()
```

![](Boxplot_Eta.png)
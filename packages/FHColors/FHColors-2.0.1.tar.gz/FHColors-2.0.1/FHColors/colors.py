import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class FHcolors:
    def __init__(self):
        self.green1=np.array([23,156,125,255])/255
        self.green2=np.array([178,210,53,255])/255
        self.orange1=np.array([245,130,32,255])/255
        self.blue1=np.array([0,91,127,255])/255
        self.blue2=np.array([0,133,152,255])/255
        self.blue3=np.array([57,193,205,255])/255
        self.grey1=np.array([166,187,200,255])/255

class FHcmap:
    def __init__(self):
        self.BlackToGreen = self.create_cmap([[0,0,0,1],colors.green1])
        self.WhiteToGreen = self.create_cmap([[1,1,1,1],colors.green1])
        self.GreenToWhite = self.create_cmap([colors.green1,[1,1,1,1]])
        self.OrangeToGreen = self.create_cmap([colors.orange1,colors.green1])
        self.GreenToOrange = self.create_cmap([colors.green1, colors.orange1])
        self.GreenToBlue = self.create_cmap([colors.green1, colors.blue1])
        self.BlueToBlue = self.create_cmap([colors.blue3, colors.blue1])
        self.BlackToGreenToOrangeToWhite = self.create_cmap([[0,0,0,1],colors.green1,colors.orange1,[1,1,1,1]])
        self.BlackToGreenToWhite = self.create_cmap([[0,0,0,1],colors.green1,[1,1,1,1]],[0,100,255])
        self.BlackToGreenToWhite_short = self.create_cmap([self.BlackToGreenToWhite(50),colors.green1,self.BlackToGreenToWhite(200)],[0,85,255])
        self.colors=ListedColormap(np.vstack([colors.green1,colors.blue1,colors.grey1,colors.blue2,colors.blue3,colors.green2]),N=255)

    def startstoparray(self,start,stop,length=256):
        r=np.interp(np.linspace(0,1,length),[0,1],[start[0],stop[0]])
        g=np.interp(np.linspace(0,1,length),[0,1],[start[1],stop[1]])
        b=np.interp(np.linspace(0,1,length),[0,1],[start[2],stop[2]])
        a=np.interp(np.linspace(0,1,length),[0,1],[1,1])
        rgba=np.vstack((r,g,b,a)).T
        return rgba
        
    def create_cmap(self,tup,poss=False):
        if not poss:
            poss=np.linspace(0,255,len(tup))
        a=np.empty((0,4))
        for i in range(len(tup)-1):
            start=tup[i]
            stop =tup[i+1]
            b=self.startstoparray(start,stop,int(poss[i+1]-poss[i]))
            a=np.vstack((a,b))
        return ListedColormap(a)
        

colors=FHcolors()
maps=FHcmap()

if __name__ == "__main__":
    maps=[
        maps.BlackToGreen,maps.GreenToWhite,
        maps.GreenToOrange,
        maps.BlackToGreenToOrangeToWhite,
        maps.BlackToGreenToWhite,
        maps.BlackToGreenToWhite_short,
        maps.GreenToBlue,
        maps.BlueToBlue,
        maps.colors]
    mapnames=[
        'maps.BlackToGreen',
        'maps.GreenToWhite',
        'maps.GreenToOrange',
        'maps.BlackToGreenToOrangeToWhite',
        'maps.BlackToGreenToWhite',
        'maps.BlackToGreenToWhite_short',
        'maps.GreenToBlue',
        'maps.BlueToBlue',
        'maps.colors']
    fig,axes=plt.subplots(nrows=len(maps), ncols=1)
    fig.set_figheight(20)
    for ii,m in enumerate(maps[:-1]):
        for i in np.arange(0, 256, 1):
            light = np.sum(m(i)[:3])/3
            axes[ii].plot([i], [light], 'o', markersize=30, color=m(i))
        axes[ii].set_xlabel('Colorvalue')
        axes[ii].set_ylabel('Brightness')
        axes[ii].title.set_text(mapnames[ii])
    for i in np.arange(0, 6, 1):
        light = np.sum(maps[-1](i)[:3])/3
        axes[-1].plot([i], [light], 'o', markersize=30, color=maps[-1](i))
    axes[-1].set_xlabel('Colorvalue')
    axes[-1].set_ylabel('Brightness')
    axes[-1].title.set_text(mapnames[-1])
    plt.tight_layout(pad=3)
    plt.savefig('maps.png')
    plt.show()


'''
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
'''

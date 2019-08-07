import matplotlib.pyplot as plt
import numpy as np
def main():
    data = np.loadtxt("Gaiadat.txt")
    frequency  = data[:,0]
    Parallax = data[:,5]
    Phot_Mean_Mag = data[:,11]
    BR = data[:,12]
    GabsShort = []
    GabsLong = []
    BRShort = []
    BRLong = []
    Gabs = []
    print("mean mag: " + str(Phot_Mean_Mag) + " parallax: " + str(Parallax) + " frequency: " + str(frequency) + " br: " + str(BR))
    for i in range(len(data)):
        period = (24 / frequency[i])
        Gabs.append(Phot_Mean_Mag[i] + 5 * (np.log10(Parallax[i]/1000)+1))
        if period <= 1:
            GabsShort.append(Gabs[i])
            BRShort.append(BR[i])
        else:
            GabsLong.append(Gabs[i])
            BRLong.append(BR[i])

    #plt.plot(BRLong, GabsLong, 'bo', markersize = 5)
    #plt.plot(BRShort, GabsShort, 'ro', markersize = 5)
    plt.scatter(BR, Gabs, c = frequency, cmap = 'seismic')
    plt.xlabel("B-R")
    plt.ylabel(" Absolute Magnitude")
    plt.title("HR Diagram")
    plt.gca().invert_yaxis()
    plt.show()

    
main()
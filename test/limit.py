import time

editWells = [['G_1X', 1694.3, 1763.6],
             ['SDNE_11P', 1734, 1879.5],
             ['SDNE_12P', 2001, 2226.4],
             ['SDNE_13I', 2615.4, 3196],
             ['SDNE_2P', 1718.8, 1866.1],
             ['SDNE_3P', 2008, 2237.7],
             ['SDNE_6P', 2791.6, 3455.9998],
             ['SDNE_7P', 2060, 2293.6],
             ['SDNE_8P', 1744, 1885.7],
             ['SDNE_9P', 2014, 2175.8],
             ['SD_11P', 1929.1, 2146.7],
             ['SD_13I', 1892.4, 2050.6],
             ['SD_17P', 2028.6, 2271.2],
             ['SD_18P', 1790.4, 1935.5],
             ['SD_19P', 2081.3, 2229.2],
             ['SD_21P', 2008.2, 2153.5],
             ['SD_22P', 1862.1, 2020.7],
             ['SD_23P', 2095.805, 2402.3],
             ['SD_24P', 2133, 2366.8],
             ['SD_25P', 1727.9, 1897.6],
             ['SD_26P', 2920, 3550],
             ['SD_27P', 4314, 4986.1],
             ['SD_28P', 4280, 4829],
             ['SD_2P', 1694.2, 1834.4],
             ['SD_2X', 1714.25, 1785.5],
             ['SD_2X_DEV', 1812, 2002],
             ['SD_2X_PL', 1697, 1785.5],
             ['SD_2X_ST', 1830.5, 2034],
             ['SD_3P', 1814.9, 1895.2],
             ['SD_3X', 1701.5, 1843.5],
             ['SD_4P', 1815, 1896.4],
             ['SD_4PST1', 1828.9, 1905.8],
             ['SD_4X', 1726, 1835],
             ['SD_5P', 1732.1, 1809],
             ['SD_5X', 1756.2, 1843.7],
             ['SD_5X_PL', 1738, 1942],
             ['SD_6P', 1783.5, 1927.5],
             ['SD_6PST', 1790.5, 1936.8],
             ['SD_6X', 1687, 1840.2],
             ['SD_7P', 1882.1, 1961],
             ['SD_8I', 1946.1, 2033.2],
             ['SD_8PST', 1837.6, 1910.1],
             ['SD_9I', 1818.7, 1901.4]]
client = wilib.login("su_ess_anhnguyen", "1")

project = client.findProjectByName("SD - B9 project - ESS2CLJOC")

wells = project.getAllWells()

for well in wells:
    for editWell in editWells:
        if well.wellName == editWell[0]:
            well.limitWell(float(editWell[1]), float(editWell[2]), "m")
            print("Done ", well, float(editWell[1]), float(editWell[2]))
            time.sleep(1)

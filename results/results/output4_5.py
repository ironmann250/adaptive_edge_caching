
memory4_5 = [1.4114, 1.4114, 1.4123, 1.4127, 1.413, 1.4132, 1.4133, 1.4134, 1.4135, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136, 1.4136]
cpu4_5 = [31.7696, 31.7674, 31.6225, 31.6362, 31.6617, 31.6078, 31.6199, 31.6024, 31.5908, 31.5826, 31.6039, 31.6199, 31.6322, 31.649, 31.6558, 31.6363, 31.6497, 31.6497, 31.655, 31.6795, 31.6719, 31.679, 31.6721, 31.6953, 31.6757, 31.6699, 31.661, 31.6781, 31.6658, 31.6581, 31.6673, 31.6631, 31.6623, 31.6645, 31.658, 31.6548, 31.6464, 31.6492, 31.6415, 31.6369, 31.64, 31.6357, 31.641, 31.6346, 31.6353, 31.6316, 31.6281, 31.6269, 31.6258, 31.6208, 31.6278, 31.6306, 31.6427, 31.643, 31.6378, 31.6561, 31.6594, 31.6556, 31.6571, 31.6852, 31.7152, 31.7115, 31.7064, 31.7109, 31.7044, 31.7073, 31.7056, 31.7054, 31.7067, 31.7051, 31.7035, 31.6978, 31.6992, 31.6979, 31.7073, 31.7295, 31.7261, 31.7241, 31.7184, 31.7179, 31.7175, 31.7195, 31.7166, 31.7114, 31.7088]
delay4_5 = [0.1308, 0.1121, 0.0747, 0.0797, 0.0638, 0.0532, 0.0456, 0.0399, 0.0457, 0.0503, 0.0542, 0.0497, 0.1613, 0.1557, 0.1513, 0.2345, 0.226, 0.2134, 0.2022, 0.1921, 0.1866, 0.1813, 0.1734, 0.1693, 0.1666, 0.1602, 0.1575, 0.1542, 0.1489, 0.1469, 0.1422, 0.1409, 0.1366, 0.1349, 0.1339, 0.1302, 0.1289, 0.1534, 0.1511, 0.1473, 0.1437, 0.1405, 0.1372, 0.1341, 0.1331, 0.1322, 0.1315, 0.1288, 0.1282, 0.1259, 0.1234, 0.1522, 0.1668, 0.1637, 0.162, 0.1591, 0.1563, 0.1557, 0.1531, 0.1505, 0.1696, 0.1907, 0.1877, 0.1863, 0.1845, 0.1827, 0.18, 0.1788, 0.1762, 0.1749, 0.1724, 0.17, 0.1687, 0.1664, 0.165, 0.1628, 0.162, 0.1599, 0.159, 0.157, 0.1562, 0.1543, 0.1524, 0.1506, 0.1498, 0.149, 0.1473, 0.1456, 0.1449]
    
right_match4_5 = 532
Wrong_match4_5 = 378
right_pre_cache4_5 = 0
wrong_pre_cache4_5 = 0
total_hit_ratio4_5 = 73.69
mec_hit_ratio4_5 = 58.73
hit_ratio4_5 = 30.41

print (len(memory4_5),len(cpu4_5),len(delay4_5))

import matplotlib.pyplot as plt
def plot_delay():
    plt.plot(list(range(len(delay4_5))),delay4_5)
    plt.show()
plot_delay()

memory0_15 = [10.4558, 10.4558, 10.4568, 10.4573, 10.4576, 10.4578, 10.4579, 10.458, 10.4581, 10.4582, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583, 10.4583]
cpu0_15 = [50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0]
delay0_15 = [0.2587, 0.1293, 0.0862, 0.0802, 0.0642, 0.0535, 0.0459, 0.0497, 0.0538, 0.0563, 0.0585, 0.4476, 0.4201, 0.3901, 0.369, 0.3508, 0.3352, 0.3217, 0.3083, 0.2966, 0.2865, 0.2773, 0.2687, 0.2622, 0.2549, 0.2479, 0.2387, 0.2994, 0.3282, 0.3215, 0.3156, 0.3086, 0.3033, 0.3376, 0.3725, 0.3942, 0.4153, 0.4044, 0.394, 0.3863, 0.3808, 0.3745, 0.3677, 0.3613, 0.3533, 0.3456, 0.34, 0.3348, 0.3305, 0.3256, 0.3192, 0.3145, 0.3104, 0.3346, 0.3419, 0.3371, 0.3312, 0.3255, 0.3212, 0.3557, 0.4002, 0.3937, 0.3889, 0.3838, 0.3779, 0.3735, 0.3691, 0.365, 0.3609, 0.3568, 0.3529, 0.3491, 0.3455, 0.3419, 0.3373, 0.3339, 0.3296, 0.3254, 0.3222, 0.3193, 0.3166, 0.3137, 0.3109, 0.3082, 0.3055, 0.303, 0.3004, 0.2979, 0.2953, 0.292, 0.2898, 0.2892, 0.2861, 0.2842, 0.2812, 0.2799, 0.277, 0.2752, 0.2731, 0.2717, 0.27, 0.2674, 0.2657, 0.318, 0.316, 0.3142, 0.3113, 0.309, 0.3388, 0.3411, 0.3397, 0.3374, 0.3447, 0.3427, 0.3404, 0.3375, 0.3356, 0.3337, 0.3317, 0.3296, 0.3276, 0.3259, 0.3233, 0.3216, 0.3199, 0.3185, 0.3174, 0.3579, 0.3551, 0.3535, 0.3719]
    
right_match0_15 = 120
Wrong_match0_15 = 106
right_pre_cache0_15 = 0
wrong_pre_cache0_15 = 0
total_hit_ratio0_15 = 87.85
mec_hit_ratio0_15 = 71.31
hit_ratio0_15 = 25.21

print (len(memory0_15),len(cpu0_15),len(delay0_15))

import matplotlib.pyplot as plt
def plot_delay():
    plt.plot(list(range(len(delay0_15))),delay0_15)
    plt.show()
plot_delay()


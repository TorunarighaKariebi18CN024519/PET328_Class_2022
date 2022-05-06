Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Torunarigha Kariebi's assignment
num_of_dolomite_cores= input('Enter the number of dolomite cores ')
num_of_shale_cores= input('Enter the number of shale cores ')
num_of_all_cores= input('Enter the number of all cores ')
num_of_dolomite_cores=float(num_of_dolomite_cores)
num_of_shale_cores=float(num_of_shale_cores)
num_of_all_cores=float(num_of_all_cores)
P_d= num_of_dolomite_cores/num_of_all_cores
P_s= num_of_shale_cores/num_of_all_cores

#import your scipy.stats

import scipy.stats
Loc_D= float(input('Enter the mean value for dolomite '))
Scale_D= float(input('Enter the standard deviation value for dolomite '))
Loc_S= float(input('Enter the mean value for shale '))
Scale_S= float(input('Enter the standard deviation value for shale '))
P_gamma_greaterthan_60D= 1-scipy.stats.norm(Loc_D,Scale_D).cdf(60)
P_gamma_greaterthan_60S= 1-scipy.stats.norm(Loc_S,Scale_S).cdf(60)

P_Dgamma_greaterthan60= P_gamma_greaterthan_60D/(P_d*P_gamma_greaterthan_60D) + (P_s*P_gamma_greaterthan_60S)

#Conditional Statements

if P_Dgamma_greaterthan60>0.5 or P_Dgamma_greaterthan60==0.5:
    print('P-D gamma greater than 60 value is ', P_Dgamma_greaterthan60)
    print('The interval is dolomite ')
else:
    print('P-D gamma greater than 60 value is ',P_Dgamma_greaterthan60)
    print('The interval is shale ')


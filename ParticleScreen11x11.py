#!/usr/bin/env python

# Takes a particles.cs file from a cryoSPARC refinement and splits each particle filename, extracting the 3 digit multishot position identifier and outputting the number of particles from each multishot position incorporated in the refinement
# Must have the 3 digit identifier (000, 001, 002, etc.) selected during data acquisition in SerialEM and only do one multishot per Navigator point
# May need to change the "dynamic_ident = split_up[2]" on line 148 to a different number depending on the filename
# Where in "P152_J28_005_particles.mrc", "P152" would be split_up[0], "J28" would be split_up[1], and "005" would be split_up[2], etc.
# To check, simply print(particles) and count the sections seperated by underscores, starting at the beginning with 0, and use the section that corresponds to the multishot position
# Will screen up to an 11 by 11 multishot and output the distribution from 121 positions to the terminal and plot in a bar graph. Simply remove the numbers you don't need

import numpy as np

#change file to particles.cs file you want to iterate through
cs = np.load('P241_S1_live_particles.cs')

#Unhash to print all data headers from any .cs file
#print(cs.dtype.names)

#outputs every particle.mrc file on a new line
particles = cs['blob/path']

# initializing the count
shot000 = 0
shot001 = 0
shot002 = 0
shot003 = 0
shot004 = 0
shot005 = 0
shot006 = 0
shot007 = 0
shot008 = 0
shot009 = 0
shot010 = 0
shot011 = 0
shot012 = 0
shot013 = 0
shot014 = 0
shot015 = 0
shot016 = 0
shot017 = 0
shot018 = 0
shot019 = 0
shot020 = 0
shot021 = 0
shot022 = 0
shot023 = 0
shot024 = 0
shot025 = 0
shot026 = 0
shot027 = 0
shot028 = 0
shot029 = 0
shot030 = 0
shot031 = 0
shot032 = 0
shot033 = 0
shot034 = 0
shot035 = 0
shot036 = 0
shot037 = 0
shot038 = 0
shot039 = 0
shot040 = 0
shot041 = 0
shot042 = 0
shot043 = 0
shot044 = 0
shot045 = 0
shot046 = 0
shot047 = 0
shot048 = 0
shot049 = 0
shot050 = 0
shot051 = 0
shot052 = 0
shot053 = 0
shot054 = 0
shot055 = 0
shot056 = 0
shot057 = 0
shot058 = 0
shot059 = 0
shot060 = 0
shot061 = 0
shot062 = 0
shot063 = 0
shot064 = 0
shot065 = 0
shot066 = 0
shot067 = 0
shot068 = 0
shot069 = 0
shot070 = 0
shot071 = 0
shot072 = 0
shot073 = 0
shot074 = 0
shot075 = 0
shot076 = 0
shot077 = 0
shot078 = 0
shot079 = 0
shot080 = 0
shot081 = 0
shot082 = 0
shot083 = 0
shot084 = 0
shot085 = 0
shot086 = 0
shot087 = 0
shot088 = 0
shot089 = 0
shot090 = 0
shot091 = 0
shot092 = 0
shot093 = 0
shot094 = 0
shot095 = 0
shot096 = 0
shot097 = 0
shot098 = 0
shot099 = 0
shot100 = 0
shot101 = 0
shot102 = 0
shot103 = 0
shot104 = 0
shot105 = 0
shot106 = 0
shot107 = 0
shot108 = 0
shot109 = 0
shot110 = 0
shot111 = 0
shot112 = 0
shot113 = 0
shot114 = 0
shot115 = 0
shot116 = 0
shot117 = 0
shot118 = 0
shot119 = 0
shot120 = 0


#iterates through each particle filepath and adds to the multishot postion count if particle came from that position
for string in particles:
	split_up = string.split(b'_')
	dynamic_ident = split_up[2]
	
	if dynamic_ident == b'000':
		shot000 += 1
	
	if dynamic_ident == b'001':
		shot001 += 1
		
	if dynamic_ident == b'002':
		shot002 += 1
		
	if dynamic_ident == b'003':
		shot003 += 1
		
	if dynamic_ident == b'004':
		shot004 += 1
		
	if dynamic_ident == b'005':
		shot005 += 1
		
	if dynamic_ident == b'006':
		shot006 += 1
		
	if dynamic_ident == b'007':
		shot007 += 1
		
	if dynamic_ident == b'008':
		shot008 += 1
		
	if dynamic_ident == b'009':
		shot009 += 1
		
	if dynamic_ident == b'010':
		shot010 += 1
	
	if dynamic_ident == b'011':
		shot011 += 1
		
	if dynamic_ident == b'012':
		shot012 += 1
		
	if dynamic_ident == b'013':
		shot013 += 1
		
	if dynamic_ident == b'014':
		shot014 += 1
		
	if dynamic_ident == b'015':
		shot015 += 1
		
	if dynamic_ident == b'016':
		shot016 += 1
		
	if dynamic_ident == b'017':
		shot017 += 1
		
	if dynamic_ident == b'018':
		shot018 += 1
		
	if dynamic_ident == b'019':
		shot019 += 1
		
	if dynamic_ident == b'020':
		shot020 += 1
	
	if dynamic_ident == b'021':
		shot021 += 1
		
	if dynamic_ident == b'022':
		shot022 += 1
		
	if dynamic_ident == b'023':
		shot023 += 1

	if dynamic_ident == b'024':
		shot024 += 1

	if dynamic_ident == b'025':
		shot025 += 1
    
	if dynamic_ident == b'026':
		shot026 += 1
        
	if dynamic_ident == b'027':
		shot027 += 1
        
	if dynamic_ident == b'028':
		shot028 += 1
        
	if dynamic_ident == b'029':
		shot029 += 1
        
	if dynamic_ident == b'030':
		shot030 += 1
        
	if dynamic_ident == b'031':
		shot031 += 1
        
	if dynamic_ident == b'032':
		shot032 += 1
        
	if dynamic_ident == b'033':
		shot033 += 1

	if dynamic_ident == b'034':
		shot034 += 1
        
	if dynamic_ident == b'035':
		shot035 += 1
    
	if dynamic_ident == b'036':
		shot036 += 1
        
	if dynamic_ident == b'037':
		shot037 += 1
        
	if dynamic_ident == b'038':
		shot038 += 1
        
	if dynamic_ident == b'039':
		shot039 += 1
        
	if dynamic_ident == b'040':
		shot040 += 1
        
	if dynamic_ident == b'041':
		shot041 += 1
        
	if dynamic_ident == b'042':
		shot042 += 1
        
	if dynamic_ident == b'043':
		shot043 += 1
        
	if dynamic_ident == b'044':
		shot044 += 1
        
	if dynamic_ident == b'045':
		shot045 += 1
    
	if dynamic_ident == b'046':
		shot046 += 1
        
	if dynamic_ident == b'047':
		shot047 += 1
        
	if dynamic_ident == b'048':
		shot048 += 1
        
	if dynamic_ident == b'049':
		shot049 += 1
        
	if dynamic_ident == b'050':
		shot050 += 1
    
	if dynamic_ident == b'051':
		shot051 += 1
        
	if dynamic_ident == b'052':
		shot052 += 1
        
	if dynamic_ident == b'053':
		shot053 += 1
        
	if dynamic_ident == b'054':
		shot054 += 1
        
	if dynamic_ident == b'055':
		shot055 += 1
        
	if dynamic_ident == b'056':
		shot056 += 1
        
	if dynamic_ident == b'057':
		shot057 += 1
        
	if dynamic_ident == b'058':
		shot058 += 1
        
	if dynamic_ident == b'059':
		shot059 += 1
        
	if dynamic_ident == b'060':
		shot060 += 1
    
	if dynamic_ident == b'061':
		shot061 += 1
        
	if dynamic_ident == b'062':
		shot062 += 1
        
	if dynamic_ident == b'063':
		shot063 += 1
        
	if dynamic_ident == b'064':
		shot064 += 1
        
	if dynamic_ident == b'065':
		shot065 += 1
        
	if dynamic_ident == b'066':
		shot066 += 1
        
	if dynamic_ident == b'067':
		shot067 += 1
        
	if dynamic_ident == b'068':
		shot068 += 1
        
	if dynamic_ident == b'069':
		shot069 += 1
        
	if dynamic_ident == b'070':
		shot070 += 1
    
	if dynamic_ident == b'071':
		shot071 += 1
        
	if dynamic_ident == b'072':
		shot072 += 1
        
	if dynamic_ident == b'073':
		shot073 += 1
        
	if dynamic_ident == b'074':
		shot074 += 1
        
	if dynamic_ident == b'075':
		shot075 += 1
    
	if dynamic_ident == b'076':
		shot076 += 1
        
	if dynamic_ident == b'077':
		shot077 += 1
        
	if dynamic_ident == b'078':
		shot078 += 1
        
	if dynamic_ident == b'079':
		shot079 += 1
        
	if dynamic_ident == b'080':
		shot080 += 1
        
	if dynamic_ident == b'081':
		shot081 += 1
        
	if dynamic_ident == b'082':
		shot082 += 1
        
	if dynamic_ident == b'083':
		shot083 += 1
        
	if dynamic_ident == b'084':
		shot084 += 1
        
	if dynamic_ident == b'085':
		shot085 += 1
    
	if dynamic_ident == b'086':
		shot086 += 1
        
	if dynamic_ident == b'087':
		shot087 += 1
        
	if dynamic_ident == b'088':
		shot088 += 1
        
	if dynamic_ident == b'089':
		shot089 += 1
        
	if dynamic_ident == b'090':
		shot090 += 1
        
	if dynamic_ident == b'091':
		shot091 += 1
        
	if dynamic_ident == b'092':
		shot092 += 1
        
	if dynamic_ident == b'093':
		shot093 += 1
        
	if dynamic_ident == b'094':
		shot094 += 1
        
	if dynamic_ident == b'095':
		shot095 += 1
    
	if dynamic_ident == b'096':
		shot096 += 1
        
	if dynamic_ident == b'097':
		shot097 += 1
        
	if dynamic_ident == b'098':
		shot098 += 1
        
	if dynamic_ident == b'099':
		shot099 += 1
        
	if dynamic_ident == b'100':
		shot100 += 1
    
	if dynamic_ident == b'101':
		shot101 += 1
        
	if dynamic_ident == b'102':
		shot102 += 1
        
	if dynamic_ident == b'103':
		shot103 += 1
        
	if dynamic_ident == b'104':
		shot104 += 1
        
	if dynamic_ident == b'105':
		shot105 += 1
        
	if dynamic_ident == b'106':
		shot106 += 1
        
	if dynamic_ident == b'107':
		shot107 += 1
        
	if dynamic_ident == b'108':
		shot108 += 1
        
	if dynamic_ident == b'109':
		shot109 += 1
        
	if dynamic_ident == b'110':
		shot110 += 1
    
	if dynamic_ident == b'111':
		shot111 += 1
        
	if dynamic_ident == b'112':
		shot112 += 1
        
	if dynamic_ident == b'113':
		shot113 += 1
        
	if dynamic_ident == b'114':
		shot114 += 1
        
	if dynamic_ident == b'115':
		shot115 += 1
        
	if dynamic_ident == b'116':
		shot116 += 1
        
	if dynamic_ident == b'117':
		shot117 += 1
        
	if dynamic_ident == b'118':
		shot118 += 1
        
	if dynamic_ident == b'119':
		shot119 += 1
        
	if dynamic_ident == b'120':
		shot120 += 1


#Add up particles to check total, reports distribution
#NOTE: if a multishot was stopped and continued during collection, a few particles may have a numeric identifier
# greater than the highest multishot identifier, so total_particles may not encompass 100% of data
total_particles = shot000 + shot001 + shot002 + shot003 + shot004 + shot005 + shot006 + shot007 + shot008 + shot009 + shot010 + shot011 + shot012 + shot013 + shot014 + shot015 + shot016 + shot017 + shot018 + shot019 + shot020 + shot021 + shot022 + shot023 + shot024 + shot025 + shot026 + shot027 + shot028 + shot029 + shot030 + shot031 + shot032 + shot033 + shot034 + shot035 + shot036 + shot037 + shot038 + shot039 + shot040 + shot041 + shot042 + shot043 + shot044 + shot045 + shot046 + shot047 + shot048 + shot049 + shot050 + shot051 + shot052 + shot053 + shot054 + shot055 + shot056 + shot057 + shot058 + shot059 + shot060 + shot061 + shot062 + shot063 + shot064 + shot065 + shot066 + shot067 + shot068 + shot069 + shot070 + shot071 + shot072 + shot073 + shot074 + shot075 + shot076 + shot077 + shot078 + shot079 + shot080 + shot081 + shot082 + shot083 + shot084 + shot085 + shot086 + shot087 + shot088 + shot089 + shot090 + shot091 + shot092 + shot093 + shot094 + shot095 + shot096 + shot097 + shot098 + shot099 + shot100 + shot101 + shot102 + shot103 + shot104 + shot105 + shot106 + shot107 + shot108 + shot109 + shot110 + shot111 + shot112 + shot113 + shot114 + shot115 + shot116 + shot117 + shot118 + shot119 + shot120

print('Total particles =', total_particles)
print(shot000)
print(shot001)
print(shot002)
print(shot003)
print(shot004)
print(shot005)
print(shot006)
print(shot007)
print(shot008)
print(shot009)
print(shot010)
print(shot011)
print(shot012)
print(shot013)
print(shot014)
print(shot015)
print(shot016)
print(shot017)
print(shot018)
print(shot019)
print(shot020)
print(shot021)
print(shot022)
print(shot023)
print(shot024)
print(shot025)
print(shot026)
print(shot027)
print(shot028)
print(shot029)
print(shot030)
print(shot031)
print(shot032)
print(shot033)
print(shot034)
print(shot035)
print(shot036)
print(shot037)
print(shot038)
print(shot039)
print(shot040)
print(shot041)
print(shot042)
print(shot043)
print(shot044)
print(shot045)
print(shot046)
print(shot047)
print(shot048)
print(shot049)
print(shot050)
print(shot051)
print(shot052)
print(shot053)
print(shot054)
print(shot055)
print(shot056)
print(shot057)
print(shot058)
print(shot059)
print(shot060)
print(shot061)
print(shot062)
print(shot063)
print(shot064)
print(shot065)
print(shot066)
print(shot067)
print(shot068)
print(shot069)
print(shot070)
print(shot071)
print(shot072)
print(shot073)
print(shot074)
print(shot075)
print(shot076)
print(shot077)
print(shot078)
print(shot079)
print(shot080)
print(shot081)
print(shot082)
print(shot083)
print(shot084)
print(shot085)
print(shot086)
print(shot087)
print(shot088)
print(shot089)
print(shot090)
print(shot091)
print(shot092)
print(shot093)
print(shot094)
print(shot095)
print(shot096)
print(shot097)
print(shot098)
print(shot099)
print(shot100)
print(shot101)
print(shot102)
print(shot103)
print(shot104)
print(shot105)
print(shot106)
print(shot107)
print(shot108)
print(shot109)
print(shot110)
print(shot111)
print(shot112)
print(shot113)
print(shot114)
print(shot115)
print(shot116)
print(shot117)
print(shot118)
print(shot119)
print(shot120)


import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

objects = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120")
y_pos = np.arange(len(objects))
distribution = [shot000,shot001,shot002,shot003,shot004,shot005,shot006,shot007,shot008,shot009,shot010,shot011,shot012,shot013,shot014,shot015,shot016,shot017,shot018,shot019,shot020,shot021,shot022,shot023,shot024,shot025,shot026,shot027,shot028,shot029,shot030,shot031,shot032,shot033,shot034,shot035,shot036,shot037,shot038,shot039,shot040,shot041,shot042,shot043,shot044,shot045,shot046,shot047,shot048,shot049,shot050,shot051,shot052,shot053,shot054,shot055,shot056,shot057,shot058,shot059,shot060,shot061,shot062,shot063,shot064,shot065,shot066,shot067,shot068,shot069,shot070,shot071,shot072,shot073,shot074,shot075,shot076,shot077,shot078,shot079,shot080,shot081,shot082,shot083,shot084,shot085,shot086,shot087,shot088,shot089,shot090,shot091,shot092,shot093,shot094,shot095,shot096,shot097,shot098,shot099,shot100,shot101,shot102,shot103,shot104,shot105,shot106,shot107,shot108,shot109,shot110,shot111,shot112,shot113,shot114,shot115,shot116,shot117,shot118,shot119,shot120]

plt.bar(y_pos, distribution, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Multishot Position')
plt.ylabel('Number of Particles')
plt.title('Particle Contribution by Multishot Position')

plt.show()

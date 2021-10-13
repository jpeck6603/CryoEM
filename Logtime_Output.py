#!/usr/bin/env python

# uses a serialEM log file as input and outputs the average time spend on each subsection of the data collection script
# Plots the output as a pie chart
# This will only work if you are using the SPADataCollection script in serialEM, as it is reading a specific line output by that script


import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


log_file = open('droped_log.log')
total_shots = 0
hole_centering_total = 0
autofocus_total = 0
drift_total = 0
record_total = 0
total_time = 0
stripe_total = 0

for line in log_file:
	if 'timing' in line:
		total_shots +=1
		split_up = line.split(' ')
		hole_centering = float(split_up[1])
		autofocus = float(split_up[2])
		drift = float(split_up[3])
		record = float(split_up[4])
		full_time = float(split_up[5])
		stripe_time = float(split_up[6])
		
		
		hole_centering_total = hole_centering_total + hole_centering
		autofocus_total = autofocus_total + autofocus
		drift_total = drift_total + drift
		record_total = record_total + record
		total_time = total_time + full_time
		stripe_total = stripe_total + stripe_time
			
hole_center_avg = hole_centering_total/total_shots
autofocus_avg = autofocus_total/total_shots
drift_avg = drift_total/total_shots
record_avg = record_total/total_shots
total_avg = total_time/total_shots
stripe_avg = stripe_total/total_shots

print('This collection contained ' + str(total_shots) + ' multishots.')
print('Hole centering averaged ' + str(hole_center_avg) + ' seconds.')
print('Autofocus averaged ' + str(autofocus_avg) + ' seconds.')
print('Drift measurement averaged ' + str(drift_avg) + ' seconds.')
print('Aquisition averaged ' + str(record_avg) + ' seconds.')
print('Total time per nav item averaged ' + str(total_avg) + ' seconds.')




# Data to plot
labels = 'Hole Centering', "Autofocus", 'Drift Measurement', 'Record', 'Black Stripe'
sizes = [hole_center_avg, autofocus_avg, drift_avg, record_avg, stripe_avg]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']

# Plot
plt.pie(sizes, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

# Swarm Robotics


## Overview
The main aim of this repo is to analyze EEG data(both raw and power) to help process commands for robots in swarms. The command script should take the incoming EEG data and display a list of commands that are most likely.
The commands will be linked to a group of drones connected to each other. The end result should be a seamless interaction of robots to the mind of the attached human.


## Usage
This will be first tested with the NeuroSky headset but will optimized for the ELECTRODE CAP SYS., TOUCHPROOF biomedical electrode cap. 
Link:
* (1)BioPAC Electrodes- https://www.biopac.com/product/electrode-cap-sys-touchproof/ 
* (2)NeuroSky Headset - http://neurosky.com/biosensors/eeg-sensor/biosensors/

## Depenencies
Python:
* mne
* pandas
* numpy
* tensorflow
* matplotlib


##  Data
The data is made from us. 

Colletion Process: 
* First: Hook up data collecting loops from both groups of leader drones and data coming from the electrode cap/headset.Note: Should be displayed in a timeseries plot with those 4 columns being linked.

* Second: The data will update in increment loops of seconds. The timestamps will not come directly in 1 second intervals due to latency in the collection.

* Third: Two people will be part of this process. One thinking of specific commands in given time intervals. And the other will be controlling the robots manually.
    
* Fourth: Going through a set of 50 commands, while repeating each command 100 times.
    
Note: We can improve the type of data we get by running this process with multiple groups of people.


## Robots
The robots will be simple light drones with 3 motors and 2 servos that will collect data simultaneously with the EEG data in a timeseries. 
The goal is to have them connected to each other through IOT and have leader drones that will send all the primary data. 

## Materials
To be Updated ... 

## Problems
There are some major problems that come with this project. With some values there


## Credits
To be updated as I'm sure I will recieve help along the way. Thanks in advance!

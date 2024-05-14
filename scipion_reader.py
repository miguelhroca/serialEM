ScriptName scipion_reading
Pythonscript
#!Python
import serialem as sem
import csv
import os



sem.Echo("reading file")

defocus_offset_step = 0.2 # um



#sem.EnterString("SCIPION_FILE_PATH", "Select .csv path")

# unncoment and fill this line if SCIPION_FILE_PATH will not selected from Parameters Script
#sem.SetVariable("SCIPION_FILE_PATH", "X:/2024_04_16_fco-javier-chichon_000084_ATLAS/Apoferritin_533")
file_path = sem.GetVariable("SCIPION_FILE_PATH") + "/serialEM.csv"
#file_path="X:/2024_04_16_fco-javier-chichon_000084_ATLAS/CARBON_536/serialEM.csv"


if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
                reader = csv.DictReader(file, delimiter='|\t')
                header = next(reader)
                print("Headers :", header)
            
                #Read Variables in the serialEM.csv file
                        
                globalShift = int(header['maxGlobalShift'])
                #defocus = int(header['rangeDefocus'])
                astigmatism = int(header['astigmatism'])
                defocus = int(header['maxDefocusU'])
                        
                        
                print( "values", globalShift, defocus, astigmatism)
                        
                if int(globalShift) == 1:
                        print('Launching drift wait task')
                        sem.DriftWaitTask(0.1, 'nm', 1, 0.5, -1, 'F')
                        
                if int(defocus) != 0:
                        print('Launching autofocus offset task')
                        if int(defocus) < 0:
                                sem.SetVariable("FOCUS_OFFSET_min", "0.2")
                                print('decreasing defocus offset')
                        else:
                                sem.SetVariable("FOCUS_OFFSET_max", "0.2")
                                print('increasing defocus offset')
                else:
                        sem.SetVariable("FOCUS_OFFSET_min", str(0))
                        sem.SetVariable("FOCUS_OFFSET_max", str(0))
                
                        
                if int(astigmatism) == 1:
                        print('Launching astigmatism and coma task')
                        sem.SetVariable("CheckAstigmatism",str(1))                         
else:
        print("The .csv does not exist")
EndPythonScript 

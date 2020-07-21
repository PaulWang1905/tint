# -*- coding: UTF-8 -*-

import pitchcalculator

class InputNote:
    def __init__(self, pitch, duration):
        
        self.pitch = pitch
        #print("getting pitch")
        self.duration = duration
        # cross out non diatonic notes temporarliy 
        # But the chromatic notes need to be processed later. 
        if pitch in (1, 3, 6, 8, 10):
            print("not in scale")
        else:
            #print("getting degree by calling the function")
            self.degree = pitchcalculator.pitch_to_degree(pitch)





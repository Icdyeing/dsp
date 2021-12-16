# JES_Verse_101219148_zhousheng.py
# Digital Signal Processing
# My Favourate Music: Xiao Xing Yun
# Winter 2021
# @ Shanghai University of Engineering Science (SUES)

# Middle C = 60
# Since 1=F, we have 1=65
# 5- = 60
# 6- = 62
# 7- = 64
# 1  = 65
# 2 = 67
# 3 = 69
# 4 = 70
# 5 = 72
# 6 = 74
# 7 = 76
# 1+ = 77
# 2+ = 79
# 3+ = 81
# 4+ = 82
# 5+ = 84
# 6+ = 86
# 7+ = 88
# 1++ = 89
# 2++ = 91


def main():
    song()
    
    
def song():
    minDuration = 150  # unit: ms
    # sentence 1,2
    playNote(69, minDuration*2, 0)
    playNote(69, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    
    playNote(76, minDuration*2, 63)
    playNote(74, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(74, minDuration*10, 63)
   
    playNote(76, minDuration*2, 0)#pause
    playNote(74, minDuration*2, 63)
    playNote(74, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(81, minDuration*2, 0) #pause
    playNote(81, minDuration*2, 63)
    playNote(76, minDuration*2, 63)

    playNote(76, minDuration*2, 63)
    playNote(72, minDuration*8, 63)
    playNote(69, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(72, minDuration*8, 63)

    playNote(76, minDuration*2, 0)#pause
    playNote(69, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(76, minDuration*2, 63)

    # sentence 3
    playNote(76, minDuration*2, 63)
    playNote(74, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(76, minDuration*6, 63)
    playNote(74, minDuration*2, 63)
    playNote(76, minDuration*4, 63)
    playNote(74, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(81, minDuration*4, 63)
    playNote(79, minDuration*4, 63)
    playNote(77, minDuration*18, 63)

    playNote(76, minDuration*2, 0)#pause
    playNote(69, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(76, minDuration*2, 63)

    playNote(76, minDuration*2, 0)#pause
    playNote(74, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(74, minDuration*10, 63)

    # sentence 4
    playNote(76, minDuration*2, 0)#pause
    playNote(74, minDuration*2, 63)
    playNote(74, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(81, minDuration*4, 63)
    playNote(76, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(72, minDuration*10, 63)

    playNote(76, minDuration*2, 0)#pause
    playNote(69, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(76, minDuration*4, 63)
    
    playNote(76, minDuration*2, 63)
    playNote(74, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(74, minDuration*6, 63)
    playNote(74, minDuration*2, 63)
    playNote(76, minDuration*4, 63)

    # sentence 5
    playNote(74, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(81, minDuration*2, 63)
    playNote(81, minDuration*2, 63)
    playNote(79, minDuration*4, 63)
    playNote(77, minDuration*2, 63)
    
    #repeated
    playNote(76, minDuration*2, 0) #pause
    playNote(81, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(81, minDuration*3, 63)
    playNote(79, minDuration*4, 63)
    playNote(77, minDuration*18, 63)

    playNote(69, minDuration*2, 63)
    playNote(70, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(81, minDuration*2, 63)

    playNote(79, minDuration*2, 63)
    playNote(81, minDuration*2, 63)
    playNote(74, minDuration*6, 63)
    playNote(76, minDuration*2, 0)#pause
    playNote(76, minDuration*1, 63)
    playNote(77, minDuration*1, 63)

    playNote(79, minDuration*4, 63)
    playNote(79, minDuration*2, 63)
    playNote(79, minDuration*1, 63)
    playNote(77, minDuration*1, 63)
    playNote(79, minDuration*1, 63)
    playNote(81, minDuration*1, 63)
    playNote(82, minDuration*1, 63)
    playNote(81, minDuration*1, 63)
    playNote(82, minDuration*1, 63)
    playNote(84, minDuration*1, 63)
    playNote(82, minDuration*1, 63)
    playNote(84, minDuration*1, 63)
   
    playNote(86, minDuration*1, 63)
    playNote(84, minDuration*1, 63)
    playNote(82, minDuration*1, 63)
    playNote(86, minDuration*1, 63)
    playNote(88, minDuration*1, 63)
    playNote(86, minDuration*1, 63)
    playNote(88, minDuration*1, 63)
    playNote(89, minDuration*1, 63)
    playNote(91, minDuration*1, 63)
    playNote(89, minDuration*1, 63)
    playNote(88, minDuration*1, 63)
    playNote(86, minDuration*1, 63)
    playNote(84, minDuration*4, 63)
    
    playNote(76, minDuration*2, 0)#pause
    playNote(69, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(77, minDuration*2, 63)
    playNote(76, minDuration*2, 63)

    playNote(76, minDuration*2, 0)#pause
    playNote(74, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(74, minDuration*10, 63)
    
    playNote(76, minDuration*2, 0)#pause
    playNote(74, minDuration*2, 63)
    playNote(74, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(81, minDuration*4, 63)
    playNote(76, minDuration*2, 63)
    playNote(76, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(69, minDuration*2, 63)
    playNote(72, minDuration*10, 63)

    #Instrumental
    playNote(76, minDuration*2, 0)#pause
    playNote(69, minDuration*2, 63)
    playNote(70, minDuration*2, 63)
    playNote(72, minDuration*2, 63)
    playNote(81, minDuration*2, 63)

    playNote(79, minDuration*2, 63)
    playNote(81, minDuration*2, 63)
    playNote(74, minDuration*6, 63)
    playNote(76, minDuration*2, 0)#pause
    playNote(76, minDuration*1, 63)
    playNote(77, minDuration*1, 63)

    playNote(79, minDuration*4, 63)
    playNote(79, minDuration*2, 63)
    playNote(79, minDuration*1, 63)
    playNote(77, minDuration*1, 63)
    
    playNote(79, minDuration*1, 63)
    playNote(81, minDuration*1, 63)
    playNote(82, minDuration*1, 63)
    playNote(81, minDuration*1, 63)
    playNote(82, minDuration*1, 63)
    playNote(84, minDuration*1, 63)
    playNote(82, minDuration*1, 63)
    playNote(84, minDuration*1, 63)
   
    playNote(86, minDuration*1, 63)
    playNote(84, minDuration*1, 63)
    playNote(82, minDuration*1, 63)
    playNote(86, minDuration*1, 63)
    
    playNote(88, minDuration*1, 63)
    playNote(86, minDuration*1, 63)
    playNote(88, minDuration*1, 63)
    playNote(89, minDuration*1, 63)
    playNote(91, minDuration*1, 63)
    playNote(89, minDuration*1, 63)
    playNote(88, minDuration*1, 63)
    playNote(86, minDuration*1, 63)
    playNote(84, minDuration*4, 63)

       
main()    
    
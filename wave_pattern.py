import time, sys
starnum = 0
starIncreasing = True
try:
    while True:
        print('*' * starnum, end='')
        print('@', end='')
        print('*' * (19-starnum))
        time.sleep(0.1)
        
        if starIncreasing:
            starnum = starnum + 1
            if starnum == 19:
                starIncreasing = False
        else:
            starnum = starnum - 1
            if starnum == 0:
                starIncreasing = True
except KeyboardInterrupt:
    sys.exit() 
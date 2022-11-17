#zverokruh, Marek Guráň
den=int(input('Deň narodenia:'))
mesiac=int(input('Mesiac:'))

if (den>21) and (den<19) or (mesiac==1) and (mesiac==2):
    print('Znamenie vodnár')
elif (den>21) or (den<21) and (mesiac==5) or (mesiac==6):
    print('Znamenie blíženec')
elif (den>24) or (den<23) and (mesiac==9) or (mesiac==10):
    print('Znamenie váhy')
elif (den>20) or (den<20) and (mesiac==2) or (mesiac==3):
    print('Znamenie ryby')
elif (den>22) or (den<22) and (mesiac==6) or (mesiac==7):
    print('Znamenie rak')
elif (den>24) or (den<22) and (mesiac==10) or (mesiac==11):
    print('Znamenie škorpión')
elif (den>21) or (den<20) and (mesiac==3) or (mesiac==4):
    print('Znamenie baran')
elif (den>23) or (den<23) and (mesiac==7) or (mesiac==8):
    print('Znamenie lev')
elif (den>23) or (den<21) and (mesiac==11) or (mesiac==12):
    print('Znamenie strelec')
elif (den>21) or (den<20) and (mesiac==4) or (mesiac==5):
    print('Znamenie býk')
elif (den>24) or (den<23) and (mesiac==8) or (mesiac==9):
    print('Znamenie panna')
else:
    print('Znamenie kozorožec')

#zverokruh, Marek Guráň
den=int(input('Deň narodenia:'))
mesiac=int(input('Mesiac:'))

if (den>21)and (mesiac==1) or (den<19)  and (mesiac==2):
    print ('Tvoje znamenie je vodnar.')
elif (den>21) and (mesiac==5) or (mesiac==6) and (den<21):
    print ('Tvoje znamenie je blizenec.')
elif (den>24) and (mesiac==9) or (mesiac==10) and (den<23):
    print ('Tvoje znamenie su vahy.')
elif (den>20) and (mesiac==2) or (mesiac==3) and (den<20):
    print ('Tvoje znamenie su ryby.')
elif (den>22) and (mesiac==6) or (mesiac==7) and (den<22):
    print ('Tvoje znamenie je rak.')
elif (den>24) and (mesiac==10) or (mesiac==11) and (den<22):
    print ('Tvoje znamenie je skorpion.')
elif (den>21) and (mesiac==3) or (mesiac==4) and (den<20):
    print ('Tvoje znamenie je baran.')
elif (den>23) and (mesiac==7) or (mesiac==8) and (den<23):
    print ('Tvoje znamenie je lev.')
elif (den>23) and (mesiac==11) or (mesiac==12) and (den<21):
    print ('Tvoje znamenie je strelec.')
elif (den>21) and (mesiac==4) or (mesiac==5) and (den<20):
    print ('Tvoje znamenie je byk.')
elif (den>24) and (mesiac==8) or (mesiac==9) and (den<23):
    print ('Tvoje znamenie je panna.')
else:
    print ('Tvoje znamenie je kozorozec.')

import math

starting_ammo = int(input("Starting ammo:  "))
count = 0
tt = 0
tt_count = 0
fttc = 0
fttc_count = 0
rr_count = 0
ammo = starting_ammo

hits_per_rr = 0


while ammo > 0:
    ammo -= 1
    count += 1
    
    # triple tap
    # tt += 1
    # if tt == 3:
    #     ammo += 1
    #     tt_count += 1
    #     tt = 0
        
    # fourth times the charm
    fttc += 1
    if fttc == 4:
        ammo += 2
        fttc_count += 1
        fttc = 0
    
    # weewoo rounds
    hits_per_rr += 1
    if ammo == 0:
        if hits_per_rr >= (starting_ammo * 0.2875):
            ammo = math.ceil(starting_ammo * 0.6)
            hits_per_rr = 0
            rr_count += 1
    
    # max ammo 
    if count >= 46:
        break

        
print(f"Total shots:        {count}")
print(f"Triple Tap procs:   {tt_count}")
print(f"Fourth Times procs: {fttc_count}")
print(f"WeeWoo Procs:       {rr_count}")
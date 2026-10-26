holi=int(input("Enter the no of holidays per year :"))
rem= 365 - holi
tot=30000
work_days_play_time=rem*63
holidays_play_time=holi*127
tot_play_time=work_days_play_time + holidays_play_time
if tot_play_time >= 30000:
    print("Tom can't sleep well !!")
    print("The extra hours of play is :",tot_play_time-30000,"minutes")
elif tot_play_time < 30000:
    print("Tom can sleep well")
    print("Tom has extra",30000-tot_play_time,"minutes to sleep ")
## Welcome to the insulin pump data pipeline ##

The goal of this project is to capture insulin pump data from [Tandem Source](https://www.tandemdiabetes.com/support-center/software-and-apps/tandem-source/article/tandem-source-account-login) and create alerts and alarms for caregivers of Tandem Insulin Pumps. Nearly all of the code in the API folder was developed with the [Tconnectsync](https://github.com/jwoglom/tconnectsync) project. This project syncs data to Nightscout and I highly recommend taking a look at it if you are interested in accessing and storing Tandem insulin pump data. 

*this project is in the very early stage. More to come* 

## To-Do ##


**daily report**

- [ ] any events with duplicate timestamps ??
- [ ] total daily insulin
- [ ] total number of carbs (sum carbs from carbs_entered)
- [ ] carb bolus (count (*) drop dups from carbs_entered)
- [ ] highest bg (max currentglucosedisplayvalue from cgm_data_g7)
- [ ] lowest bg (min currentglucosedisplayvalue from cgm_data_g7)
- [ ] percent basal increased (count (*) from basal_delivery where commandedRate > profilebasalrate)
- [ ] number of automatic corrections
- [ ] number of boluses 
- [ ] break down of boluses
- [ ] precent basal decreased (count (*) from basal_delivery where commandedRate < profilebasalrate)
- [ ] percent basal at zero (count (*) from basal_delivery where commandedRate = 0)
- [ ] red flag - less than three times carbs entered 
- [ ] red flag - low between 12 and 8 am and time (select * from cgm_data_g7 where currentglucosedisplayvalue < 80 and eventTimestamp between x and x)
- [ ] red flag - high and how long
- [ ] red flag - any length of time between cgm readings that is greater than five minutes 
- [ ] max amount of time between cgm readings

** Alerts ** 
    4: LidAlertActivated,
    5: LidAlarmActivated,
    6: LidMalfunctionActivated,
    11: LidPumpingSuspended,
    12: LidPumpingResumed,

    60: LidDataLogCorruption,
  
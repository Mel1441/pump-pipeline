## Welcome to the insulin pump data pipeline ##

The goal of this project is to capture insulin pump data from [Tandem Source](https://www.tandemdiabetes.com/support-center/software-and-apps/tandem-source/article/tandem-source-account-login) and create alerts and alarms for caregivers of Tandem Insulin Pumps. Nearly all of the code in the API folder was developed with the [Tconnectsync](https://github.com/jwoglom/tconnectsync) project. This project syncs data to Nightscout and I highly recommend taking a look at it if you are interested in accessing and storing Tandem insulin pump data. 

*this project is in the very early stage. More to come* 

## To-Do ##

**daily report**

- [ ] any events with duplicate timestamps
- [ ] total daily insulin
- [ ] total number of carbs
- [ ] carb bolus
- [ ] highest bg
- [ ] lowest bg
- [ ] percent basal increased 
- [ ] number of automatic corrections
- [ ] number of boluses 
- [ ] break down of boluses
- [ ] precent basal decreased 
- [ ] percent basal at zero
- [ ] red flag - less than three times carbs entered
- [ ] red flag - low between 12 and 8 am and time 
- [ ] red flag - high and how long

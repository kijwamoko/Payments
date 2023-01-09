import position
import utiities
import period_handler

from period import  Period

#get postionf for template
positions = utiities.get_template_positions()

# for p in positions:
#     print(p.name, p.price, sep="\t")

#utiities.create_template()

#create period - test
#utiities.maintain_period()

#test with handlers
year = int(input('Get year'))
month = int(input('Get month'))

ph = period_handler.PeriodFileHandler(year, month)

ph.handle()
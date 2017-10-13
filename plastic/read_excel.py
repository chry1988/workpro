# encoding ='utf-8'
from xlrd import open_workbook
import sys
#help(xlrd)
wb = open_workbook('E:\CNTV薛丹\8.技术白皮书\CNTV信源系统20171009.xlsx')
class Arm(object):
    def __init__(self, id, dsp_name, dsp_code, hub_code, pin_code, pptl,*args):
        self.id = id
        self.dsp_name = dsp_name
        self.dsp_code = dsp_code
        self.hub_code = hub_code
        self.pin_code = pin_code
        self.pptl = pptl

    def __str__(self):
        return("Arm object:\n"
               "  Arm_id = {0}\n"
               "  DSPName = {1}\n"
               "  DSPCode = {2}\n"
               "  HubCode = {3}\n"
               "  PinCode = {4} \n"
               "  PPTL = {5}"
               .format(self.id, self.dsp_name, self.dsp_code,
                       self.hub_code, self.pin_code, self.pptl))

#wb = open_workbook('sample.xls')
sheet = wb.sheet_by_name('编码器信息-收录')

#for sheet in wb.sheets():

number_of_rows = sheet.nrows
number_of_columns = sheet.ncols
items = []
rows = []
for row in range(1, number_of_rows):
    values = []
    for col in range(number_of_columns):
        value  = (sheet.cell(row,col).value)
        try:
            value = str(int(value))
        except ValueError:
            pass
        finally:
            values.append(value)
    item = Arm(*values)
    items.append(item)

for item in items:
    print(item)
    print("Accessing one single value (eg. DSPName): {0}".format(item.dsp_name))
    print()

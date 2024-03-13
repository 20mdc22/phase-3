def GetEmpName():
    empName = input('Enter employee name: ')
    return empName

def GetDatesWorked():
    fromdate = input('Enter Start Date (mm/dd/yyyy): ')
    todate = input('Enter End Date (mm/dd/yyyy): ')
    return fromdate, todate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked: '))
    return hours

def GetHourlyRate():
    hourlyrate = float(input('Enter hourly rate: '))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input('Enter tax rate: '))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    for empList in empDetailList:
        fromdate = empList[0]
        todate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyrate = empList[4]
        taxrate = empList[5]

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empName, f'{hours:,.2f}', f'{hourlyrate:,.2f}', f'{grosspay:,.2f}', f'{taxrate:,.1%}', f'{incometax:,.2f}', f'{netpay:,.2f}')
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

        empTotals['TotEmp'] = TotEmployees
        empTotals['TotHrs'] = TotHours
        empTotals['TotGrossPay'] = TotGrossPay
        empTotals['TotTax'] = TotTax
        empTotals['TotNetPay'] = TotNetPay
        return empDetailList
def PrintTotals(empTotals):
    print()
    print(f'Total Number of Employees: {empTotals["TotEmp"]}')
    print(f'Total Hours Worked: {empTotals["TotHrs"]}')
    print(f'Total Gross Pay: {empTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax: {empTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {empTotals["TotNetPay"]:,.2f}')

def WriteEmployeeInformation(employee):
    file = open('employeeinfo.txt', 'a')
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1],employee[2], employee[3], employee[4], employee[5]))

def GetFromDate():
    valid = False
    fromdate = ''
    while not valid:
        fromdate = input('Enter From Date (mm/dd/yyyy): ')
        if (len(fromdate.split('/')) != 3 and fromdate.upper() !='ALL'):
            print('Invalid Date Format: ')
        else:
            valid = True
        return fromdate

def ReadEmployeeInformation():
    empDetailList = []
    file = open('employeeinfo.txt', 'r')
    data = file.readlines()
    condition = True
    if fromdate.upper() == 'ALL':
        condition = False
        for employee in data:
            employee = [x.strip() for x in employee.strip().split("|")]
        if not condition:
            empDetailList.append(employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5]))
        else:
            if fromdate == employee[0]:
                empDetailList.append(employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5]))
            return empDetailList

if __name__ == "__main__":
    empDetailList = []
    empTotals = {}
    while True:
        empName = GetEmpName()
        if empName.upper() == 'END':
            break
    fromdate, todate = GetDatesWorked()
    hours = GetHoursWorked()
    hourlyrate = GetHourlyRate()
    taxrate = GetTaxRate()
    print()
    empDetail = [fromdate, todate, empName, hours, hourlyrate, taxrate]
    WriteEmployeeInformation(empDetail)
    print()
    print()
    fromdate = GetFromDate()
    empDetailList = ReadEmployeeInformation()
    printinfo(empDetailList)
    print()
    PrintTotals(empTotals)
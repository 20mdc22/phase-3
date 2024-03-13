##Michael Crossno
##CIS 262
##Course Project Phase 3

def getempName():
    empName = input('Enter employee name:  ')
    return empName

def getdatesWorked():
    fromDate = input('Enter start date (DD/MM/YYYY):  ')
    toDate = input('Enter end date (DD/MM/YYYY:  ')
    return fromDate, toDate

def gethoursWorked():
    hours = float(input('Enter hours worked:  '))
    return hours

def gethourlyRate():
    hourlyRate = float(input('Enter hourly rate:  '))
    return hourlyRate

def gettaxRate():
    taxRate = float(input('Enter tax rate:  '))
    return taxRate

def CalcTaxandNetpay(hours, hourlyRate, taxRate):
    grossPay = hours * hourlyRate
    incomeTax = taxRate * grossPay
    netPay = grossPay - incomeTax
    return grossPay, incomeTax, netPay

def printInfo(empDetailList):
    totEmployees = 0
    tothours = 0.00
    totgrossPay = 0.00
    totTax = 0.00
    totnetPay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        toDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        grossPay, incomeTax, netPay = CalcTaxandNetpay(hours, hourlyRate, taxRate)
        print(fromDate, toDate, empName, f'{hourlyRate:,.2f}', f'{taxRate:,.1%}', f'{grossPay:,.2f}', f'{incomeTax:,.2f}', f'{netPay},.2f')
        totEmployees += 1
        tothours += hours
        totgrossPay += grossPay
        totTax += taxRate
        totnetPay += netPay
        empTotals['totEmp'] = totEmployees
        empTotals['totHrs'] = tothours
        empTotals['totgrossPay'] = totgrossPay
        empTotals['totTax'] = totTax
        empTotals['totnetPay'] = totnetPay
        return empDetailList

def printTotals(empTotals):
    print()
    print()
    print(f'Total number of Employees: {empTotals["totEmp"]}')
    print(f'Total number of Hours: {empTotals["totHrs"]}')
    print(f'Total Gross pay: {empTotals["totgrossPay"]}')
    print(f'Total Tax: {empTotals["totTax"]}')
    print(f'Total net pay: {empTotals["totnetPay"]}')

def WriteEmployeeInformation(employee):
    file = open('employeeinfo.txt', 'a')
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1],employee[2], employee[3], employee[4], employee[5]))

def getfromDate():
    valid = False
    fromDate = ''
    while not valid:
        fromDate = input('Enter from date (mm/dd/yyyy):  ')
        if (len(fromDate.split('/')) != 3 and fromDate.upper() != 'ALL'):
            print('Invalid date format:  ')
        else:
            valid = True

    return fromDate

def ReadEmployeeInformation(fromDate):
    empDetailList = []
    file = open('employeeinfo.txt', 'r')
    data = file.readlines()
    condition = True
    if fromDate.upper() =='ALL':
        condition = False
    for employee in data:
        employee = [x.strip() for x in employee.strip().split('|')]

        if not condition:
            empDetailList.append(
                [employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromDate == employee[0]:
                empDetailList.append(
                    [employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])

    return empDetailList

if __name__ == '__main__':
    empDetailList = []
    empTotals = {}
    while True:
        empName = getempName()
        if empName.upper == 'END':
            break
        fromDate, toDate = getdatesWorked()
        hours = gethoursWorked()
        hourlyRate = gethourlyRate()
        taxRate = gettaxRate()
        print()
        empDetail = [fromDate, toDate, empName, hours, hourlyRate, taxRate]
        WriteEmployeeInformation(empDetail)
    print()
    print()
    fromDate = getfromDate()
    empDetailList = ReadEmployeeInformation(fromDate)
    printInfo(empDetailList)
    print()
    printTotals(empTotals)
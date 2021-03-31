# global variables
salary = 20000
year = 2017
inflation = 0.02
rate = 0.05 # rate of return
nper = 12 # lifespace of investment i.e. every month
pmt = salary*0.08 # fixed payment at beginning or end of each period
fv =

# calculate compound interest
def compound_interest(principle, rate, time, nper):
    result = principle * (pow((1 + rate / nper), time / nper))
    retun result

# take away inflation from salary
salaryminusinflation = compound_interest(salary, -inflation, 2021-year, nper)

pmt = salaryminusinflation*0.08

np.fv(rate, nper, pmt, fv, when='end')

#!/usr/bin/env python

import sys

employees = sys.argv[1] if len(sys.argv) > 1 else 1

empls = {}

for i in range(employees):
    name = raw_input('enter worker name: ')
    empls[name] = {'hours':[]}
    for i in range(12):
        hours = input('enter worker hours: ')
        empls[name]['hours'].append(hours)

def earnings():
    for em in empls:
        empls[em]['earnings'] = [x * 30 for x in empls[em]['hours']] 

def raise_salary(em=None):
    if em:
        if not 'earnings' in empls[em]:
            earnings()
        for ind, earn in enumerate(empls[em]['earnings']):
            if earn <= 650:
                empls[em]['earnings'][ind] = int(earn * 1.10)
            elif earn < 850:
                empls[em]['earnings'][ind] = earn + 75
    else:
        for em in empls.keys():
            if not 'earnings' in empls[em]:
                earnings()
            for ind, earn in enumerate(empls[em]['earnings']):
                if earn <= 650:
                    empls[em]['earnings'][ind] = int(earn * 1.10)
                elif earn < 850:
                    empls[em]['earnings'][ind] = earn + 75

def show(empl=None):
    if empl:
        print '\n\t', empl, ':\n', 'Earnings for year: ', empls[empl]['earnings'], '\n', 'Hours of work: ',  empls[empl]['hours']
    else:
        for em in empls.keys():
            print '\n\t', em, ':\n', 'Earnings for year: ', empls[em]['earnings'], '\n', 'Hours of work: ', empls[em]['hours']
    
run = True

helper = {'q': 'quit', 'raise' :'raise salary', 'show' : 'show stats', 'h or help': 'show this helper', 'set': 'set earnings based on work hours for all employees'}

while True:
    com = raw_input('Type a command: ')
    if com == 'q':
        print 'quitting...'
        break
    elif com == 'show':
        show(raw_input('Type name of eployee (or type nothing to show all): '))
    elif com == 'raise':
        raise_salary(raw_input('Type name of employee (or type nothing to raise salary of all employees): '))
    elif com == 'help' or com == 'h':
        for key in helper.keys():
            print key, ':', helper[key]
    elif com == 'set':
        earnings()
    else:
        print 'fatal error code 666: quitting...'
        break



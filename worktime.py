import PySimpleGUI as sg
from datetime import datetime

# Layout
layout = [
    [sg.Text('0000/00/00(00)', key='date', font=('Helvetica', 18)), sg.Button('Start', font=('Helvetica', 14)), sg.Button('End', font=('Helvetica', 14)), sg.Button('Reset', font=('Helvetica', 14))],
    [sg.Text('00:00:00', key='clock', font=('Helvetica', 48)), sg.Text('00:00:00', key='worktime', font=('Helvetica', 24))]
]

# window
win = sg.Window('Work Time', layout)

while True:
    event, val = win.read(timeout=10) # 10times/
    work = '00:00:00'
    if event in ('Exit', 'Quit', None): break
    if event == 'Start':
        starttime = datetime.now()
        win['worktime'].update(text_color='#FF0000')
    if event == 'End':
        end = datetime.now()
        work = end - starttime
        win['worktime'].update(work)
        win['worktime'].update(text_color='#0000FF')
    if event == 'Reset':
        win['worktime'].update(text_color='#FFFFFF')        
        win['worktime'].update('00:00:00')

    date = datetime.now().strftime('%Y/%m/%d(%a)')
    time = datetime.now().strftime('%H:%M:%S')
 
    win['date'].update(date)
    win['clock'].update(time)
    
win.close()

import PySimpleGUI as sg
import time
from datetime import datetime

def time_as_int():
    return int(round(time.time() * 100))

# Create Form
layout = [
    [sg.Text('0000/00/00(000)', key='date', font=('Helvetica', 18)), 
        sg.Button('Start', font=('Helvetica', 14)),
        sg.Button('Pause', font=('Helvetica', 14)),
        sg.Button('End', font=('Helvetica', 14)),
        sg.Button('Reset', font=('Helvetica', 14))],
    [sg.Text('00:00:00', key='clock', font=('Helvetica', 48)),
        sg.Text('00:00:00', key='worktime', font=('Helvetica', 24))]
]

win = sg.Window('Work Time', layout,
    auto_size_buttons = True,
    element_padding=(1, 0)
)

pause_time, start, pause = 0, False, False
start_time, work_time = 0, 0

while True:
    # read and update window
    event, values = win.read(timeout=100)

    # Button Event
    if start == True and pause == False:
        event, values = win.read(timeout=100)
        work_time = time_as_int() - start_time
        win['worktime'].update('{:02d}:{:02d}:{:02d}'.format(
        ((work_time // 100) // 60 // 60) % 60, ((work_time // 100) // 60) % 60, (work_time // 100) % 60)
        )

    if event in ('Exit', 'Quit', None):
        break

    if event == 'Start':
        if start == True and pause == True:
            pause = False
            start_time = start_time + time_as_int() - pause_time
        elif start == False and pause == False:
            start = True
            start_time = time_as_int()
        win['worktime'].update(text_color='#FF0000')
    elif event == 'End':
        start = False
        pause = False
        end_time = time_as_int()
        work_time = end_time - start_time
        win['worktime'].update(text_color='#0000FF')
        win['worktime'].update('{:02d}:{:02d}:{:02d}'.format(
        ((work_time // 100) // 60 // 60) % 60, ((work_time // 100) // 60) % 60, (work_time // 100) % 60)
        )
    elif event == 'Reset':
        start = pause = False
        pause_time = start_time = time_as_int()
        work_time = 0
        win['worktime'].update(text_color='#FFFFFF')        
        win['worktime'].update('00:00:00')
    elif event == 'Pause':
        pause = True
        if pause == True:
            pause_time = time_as_int()
            win['worktime'].update(text_color='#FFFF00')
    # Current time    
    date = datetime.now().strftime('%Y/%m/%d(%a)')
    clock = datetime.now().strftime('%H:%M:%S')
    work_time = time_as_int() - start_time

    win['date'].update(date)
    win['clock'].update(clock)
    
win.close()

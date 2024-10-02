import subprocess
import datetime

def commit_week(first_day): # first_day: '2020-01-01 00:00:00'
    for i in range(7):
        date_str = (first_day +datetime.timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')
        print(date_str)
        subprocess.run(['git', 'commit', '--allow-empty','--date', date_str, '-m', 'Commit du futur'])

def commit_day(date): # date: '2020-01-01 00:00:00'
    print(date)
    date = date.strftime('%Y-%m-%d %H:%M:%S')
    subprocess.run(['git', 'commit', '--allow-empty','--date', date, '-m', 'Commit du futur'])

def diag_bas(first_day):
    for i in range(7):
        date_str = (first_day +datetime.timedelta(days=i*8)).strftime('%Y-%m-%d %H:%M:%S')
        print(date_str)
        subprocess.run(['git', 'commit', '--allow-empty','--date', date_str, '-m', 'Commit du futur'])

def diag_haut(first_day):
    for i in range(7):
        date_str = (first_day +datetime.timedelta(days=i*6)).strftime('%Y-%m-%d %H:%M:%S')
        print(date_str)
        subprocess.run(['git', 'commit', '--allow-empty','--date', date_str, '-m', 'Commit du futur'])

def commit_v(date):
    # I want something like this:
    # x     x
    # x     x
    #  x   x
    #  x   x
    #   x x
    #   x x
    #    x
    commit_day(date)
    date = date + datetime.timedelta(days=1)
    commit_day(date)
    date = date + datetime.timedelta(days=8)
    commit_day(date)
    date = date + datetime.timedelta(days=1)
    commit_day(date)
    date = date + datetime.timedelta(days=8)
    commit_day(date)
    date = date + datetime.timedelta(days=1)
    commit_day(date)
    date = date + datetime.timedelta(days=8)
    commit_day(date)
    date = date + datetime.timedelta(days=6)
    commit_day(date)
    date = date - datetime.timedelta(days=1)
    commit_day(date)
    date = date + datetime.timedelta(days=6)
    commit_day(date)
    date = date - datetime.timedelta(days=1)
    commit_day(date)
    date = date + datetime.timedelta(days=6)
    commit_day(date)
    date = date - datetime.timedelta(days=1)
    commit_day(date)
    

def commit_i(date):
    for i in range(7):
        if i == 2:
            continue
        else:
            date_str = (date + datetime.timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')
            date_str2 = (date + datetime.timedelta(days=i+7)).strftime('%Y-%m-%d %H:%M:%S')
            print(date_str)
            print(date_str2)
            subprocess.run(['git', 'commit', '--allow-empty','--date', date_str, '-m', 'Commit du futur'])
            subprocess.run(['git', 'commit', '--allow-empty','--date', date_str2, '-m', 'Commit du futur'])

def commit_d(date):
    commit_week(date)
    date = date + datetime.timedelta(days=7)
    #demi diag bas
    for i in range(4):
        date_str = (date + datetime.timedelta(days=i*8)).strftime('%Y-%m-%d %H:%M:%S')
        print(date_str)
        subprocess.run(['git', 'commit', '--allow-empty','--date', date_str, '-m', 'Commit du futur'])

    date = date + datetime.timedelta(days=6)
    #demi diag haut
    for i in range(4):
        date_str = (date + datetime.timedelta(days=i*6)).strftime('%Y-%m-%d %H:%M:%S')
        print(date_str)
        subprocess.run(['git', 'commit', '--allow-empty','--date', date_str, '-m', 'Commit du futur'])

def commit_line(date):
    for i in range(4):
        date_str = (date + datetime.timedelta(days=i*7)).strftime('%Y-%m-%d %H:%M:%S')
        print(date_str)
        subprocess.run(['git', 'commit', '--allow-empty','--date', date_str, '-m', 'Commit du futur'])

        
def commmit_array(dates,year): # dates: ["10/2", "10/3", "10/4", "10/5", "10/6", "10/7", "10/8"] jour mois
    for i in dates:
        date = datetime.datetime(year, int(i.split("/")[1]), int(i.split("/")[0]), 4, 20, 59)
        commit_day(date)

def commit_four_down(date):
    for i in range(4):
        date_str = (date + datetime.timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')
        print(date_str)
        subprocess.run(['git', 'commit', '--allow-empty','--date', date_str, '-m', 'Commit du futur'])

def commit_three_side(date):
    for i in range(3):
        date_str = (date + datetime.timedelta(days=i*7)).strftime('%Y-%m-%d %H:%M:%S')
        print(date_str)
        subprocess.run(['git', 'commit', '--allow-empty','--date', date_str, '-m', 'Commit du futur'])
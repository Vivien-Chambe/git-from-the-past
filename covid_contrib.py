import drawing_contributions as dc
import datetime

def main():
    # Draw the letter 'C'
    date = datetime.datetime(2020, 2, 2, 4, 20, 59)
    dc.commit_week(date)
    dc.commit_line(date)
    dc.commit_line(date + datetime.timedelta(days=6))

    # Draw the letter 'O'
    date = datetime.datetime(2020, 3, 8, 4, 20, 59)
    dc.commit_week(date)
    dc.commit_line(date)
    dc.commit_week(date + datetime.timedelta(days=3*7))
    dc.commit_line(date + datetime.timedelta(days=6))

    # Draw the letter 'V'
    date = datetime.datetime(2020, 4, 12, 4, 20, 59)
    dc.commit_v(date)


    # Draw the letter 'I'
    date = datetime.datetime(2020, 6, 7, 4, 20, 59)
    dc.commit_i(date)

    # Draw the letter 'D'
    date = datetime.datetime(2020, 6, 28, 4, 20, 59)
    dc.commit_d(date)
    
    # Draw the hyphen

    date = datetime.datetime(2020, 8, 12, 4, 20, 59)
    dc.commit_line(date)

    # Draw the number '1'
    date = datetime.datetime(2020, 9, 27, 4, 20, 59)
    dc.commit_i(date)
    date = date + datetime.timedelta(days=2)
    dc.commit_day(date)
    date = date + datetime.timedelta(days=7)
    dc.commit_day(date)
    date = datetime.datetime(2020, 9, 21, 4, 20, 59)
    dc.commit_day(date)
    date = date + datetime.timedelta(days=1)
    dc.commit_day(date)
    date = date - datetime.timedelta(days=7)
    dc.commit_day(date)


    # Draw the number '9'

    date = datetime.datetime(2020, 10, 18, 4, 20, 59)
    dc.commit_line(date)
    dc.commit_line(date + datetime.timedelta(days=6))

    dc.commit_week(date + datetime.timedelta(days=21))
    dc.commit_week(date + datetime.timedelta(days=28))

    dc.commit_day(date + datetime.timedelta(days=1))
    dc.commit_day(date + datetime.timedelta(days=2))
    dc.commit_day(date + datetime.timedelta(days=10))
    dc.commit_day(date + datetime.timedelta(days=17))

if __name__ == "__main__":
    main()
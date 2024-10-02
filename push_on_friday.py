import drawing_contributions as dc
import datetime

def main():
    ##P 
    dc.commit_four_down(datetime.datetime(2021, 1, 17, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 1, 24, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 1, 26, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 2, 1, 4, 20, 59))

    ##U
    dc.commit_four_down(datetime.datetime(2021, 2, 14, 4, 20, 59))
    dc.commit_four_down(datetime.datetime(2021, 2, 28, 4, 20, 59))
    dc.commit_three_side(datetime.datetime(2021, 2, 17, 4, 20, 59))

    ##S
    dc.commit_three_side(datetime.datetime(2021, 3, 14, 4, 20, 59))
    dc.commit_three_side(datetime.datetime(2021, 3, 17, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 3, 15, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 3, 23, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 3, 30, 4, 20, 59))

    ##H
    dc.commit_four_down(datetime.datetime(2021, 4, 11, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 4, 19, 4, 20, 59))
    dc.commit_four_down(datetime.datetime(2021, 4, 25, 4, 20, 59))



    ##O
    dc.commit_four_down(datetime.datetime(2021, 5, 16, 4, 20, 59))
    dc.commit_four_down(datetime.datetime(2021, 5, 30, 4, 20, 59))
    dc.commit_three_side(datetime.datetime(2021, 5, 16, 4, 20, 59))
    dc.commit_three_side(datetime.datetime(2021, 5, 19, 4, 20, 59))

    ##N
    dc.commit_four_down(datetime.datetime(2021, 6, 13, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 6, 21, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 6, 29, 4, 20, 59))
    dc.commit_four_down(datetime.datetime(2021, 7, 4, 4, 20, 59))

    ##F
    dc.commit_four_down(datetime.datetime(2021, 7, 25, 4, 20, 59))
    dc.commit_three_side(datetime.datetime(2021, 7, 25, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 8, 3, 4, 20, 59))

    ##R
    dc.commit_four_down(datetime.datetime(2021, 8, 22, 4, 20, 59))
    dc.commit_three_side(datetime.datetime(2021, 8, 22, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 8, 31, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 9, 6, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 9, 8, 4, 20, 59))

    ##I
    dc.commit_four_down(datetime.datetime(2021, 9, 19, 4, 20, 59))

    ##D
    dc.commit_four_down(datetime.datetime(2021, 10, 3, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 10, 10, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 10, 19, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 10, 18, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 10, 13, 4, 20, 59))

    ##A
    dc.commit_four_down(datetime.datetime(2021, 10, 31, 4, 20, 59))
    dc.commit_three_side(datetime.datetime(2021, 10, 31, 4, 20, 59))
    dc.commit_four_down(datetime.datetime(2021, 11, 14, 4, 20, 59))
    dc.commit_three_side(datetime.datetime(2021, 11, 2, 4, 20, 59))

    ##Y
    dc.commit_day(datetime.datetime(2021, 11, 28, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 12, 12, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 12, 6, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 12, 7, 4, 20, 59))
    dc.commit_day(datetime.datetime(2021, 12, 8, 4, 20, 59))

    #Commit every friday
    date = datetime.datetime(2021, 1, 1, 4, 20, 59)
    for i in range(52):
        date = date + datetime.timedelta(days=7)
        dc.commit_day(date)
if __name__ == '__main__':
    main()


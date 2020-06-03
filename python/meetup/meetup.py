""" SOME TESTS STILL NOT PASSING!!!
"""
from datetime import date
from calendar import Calendar

cal = Calendar()
days = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
weeks = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4}


def meetup(year, month, week, day_of_week):
    month_weeks = cal.monthdatescalendar(year, month)
    if week == "last":
        return get_last(month, month_weeks, days[day_of_week])
    elif week == "teenth":
        return get_teenth(month, month_weeks, days[day_of_week])
    elif week in weeks and month <= 12:
        return get_nth_day(month, month_weeks, weeks[week], days[day_of_week])
    else:
        return MeetupDayException()


def get_nth_day(month, month_weeks, week, day):
    # count = 0
    # while count <= week:
    #     for wk in range(len(month_weeks)):
    #         if month_weeks[wk][day].month == month:
    #             count += 1
    # return month_weeks[count][day]

    if month_weeks[week][day].month == month:
        return month_weeks[week][day]
    else:
        return month_weeks[week + 1][day]


def get_last(month, month_weeks, day):
    if month_weeks[-1][day].month == month:
        return month_weeks[-1][day]
    else:
        return month_weeks[-2][day]


def get_teenth(month, month_weeks, day):
    if month_weeks[1][day].day >= 13:
        return month_weeks[2][day]
    elif month_weeks[2][day].day >= 13:
        return month_weeks[2][day]
    else:
        return month_weeks[3][day]


def MeetupDayException():
    raise ValueError('Invalid meetup')


# def main():
#     print(meetup(2013,6,"4th","Tuesday"))


# if __name__ == '__main__':
#     main()
import datetime
from .liturgical_grade import LiturgicalGrade


class CalendarGenerator:
    def __init__(self, year: int) -> None:
        self._year = year

    def __generate_easter_triduum(self):
        easter_date = self.__get_easter_date()
        holy_thurs = {
            "name": "Holy Thursday",
            "date": easter_date - datetime.timedelta(days=3),
            "liturgical_color": "white",
            "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
        }
        good_fri = {
            "name": "Good Friday",
            "date": easter_date - datetime.timedelta(days=2),
            "liturgical_color": "red",
            "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
        }
        easter_vigil = {
            "name": "Easter Vigil",
            "date": easter_date - datetime.timedelta(days=1),
            "liturgical_color": "white",
            "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
        }
        easter = {
            "name": "Easter Sunday",
            "date": easter_date,
            "liturgical_color": "white",
            "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
        }
        return [holy_thurs, good_fri, easter_vigil, easter]

    def __generate_christmas_epiphany(self):
        christmas = {
            "name": "Christmas",
            "date": datetime.datetime(self._year, 12, 25),
            "liturgical_color": "white",
            "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
        }
        epiphany = {
            "name": "Epiphany",
            "date": datetime.datetime(self._year, 1, 6),
            "liturgical_color": "white",
            "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
        }

        festivities = [christmas, epiphany]

        for i in range(2, 6):
            date = datetime.datetime(self._year, 1, i)
            if date.weekday() == 6:
                festivities.append(
                    {
                        "name": "2nd Sunday after Christmas",
                        "date": date,
                        "liturgical_color": "white",
                        "liturgical_grade": LiturgicalGrade.FEAST_LORD,
                    }
                )
            else:
                festivities.append(
                    {
                        "name": f"{date.strftime('%A')} - Christmas Weekday",
                        "date": date,
                        "liturgical_color": "white",
                        "liturgical_grade": LiturgicalGrade.WEEKDAY,
                    }
                )

        return festivities

    def __generate_ascension_pentecost(self):
        easter_date = self.__get_easter_date()
        ascension = {
            "name": "Ascension",
            "date": easter_date + datetime.timedelta(days=39),
            "liturgical_color": "white",
            "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
        }
        easter7 = {
            "name": "Seventh Sunday of Easter",
            "date": easter_date + datetime.timedelta(days=42),
            "liturgical_color": "white",
            "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
        }
        pentecost = {
            "name": "Pentecost",
            "date": easter_date + datetime.timedelta(days=49),
            "liturgical_color": "red",
            "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
        }
        return [ascension, easter7, pentecost]

    def generate_festivities(self):
        festivities = []
        festivities.extend(self.__generate_easter_triduum())
        festivities.extend(self.__generate_christmas_epiphany())
        festivities.extend(self.__generate_ascension_pentecost())

        festivities_dict = {}
        for festivity in festivities:
            if festivity["date"] not in festivities_dict:
                festivities_dict.update({festivity["date"]: []})
            festivities_dict[festivity["date"]].append(festivity)
        return festivities_dict

    def __get_easter_date(self):
        d = 225 - 11 * (self._year % 19)

        while d > 50:
            d -= 30

        if d > 48:
            d -= 1

        e = (self._year + self._year // 4 + d + 1) % 7

        day = d + 7 - e

        month = 4
        if day > 31:
            day -= 31
        elif day < 32:
            month = 3

        return datetime.datetime(self._year, month, day)

import datetime
from .liturgical_grade import LiturgicalGrade
import json
import os


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

    def __get_last_sunday_of_advent(self):
        last_sunday_of_advent = datetime.datetime(self._year, 12, 25)
        while last_sunday_of_advent.weekday() != 6:
            last_sunday_of_advent -= datetime.timedelta(days=1)
        return last_sunday_of_advent

    def __generate_sunday_major_seasons(self):
        easter_date = self.__get_easter_date()
        last_sunday_of_advent = self.__get_last_sunday_of_advent()

        festivities = []
        festivities.append(
            {
                "name": "First Sunday of Advent",
                "date": last_sunday_of_advent - datetime.timedelta(days=21),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Second Sunday of Advent",
                "date": last_sunday_of_advent - datetime.timedelta(days=14),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Third Sunday of Advent (Gaudete)",
                "date": last_sunday_of_advent - datetime.timedelta(days=7),
                "liturgical_color": "pink",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Fourth Sunday of Advent",
                "date": last_sunday_of_advent,
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "First Sunday of Lent",
                "date": easter_date - datetime.timedelta(days=42),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Second Sunday of Lent",
                "date": easter_date - datetime.timedelta(days=35),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Third Sunday of Lent",
                "date": easter_date - datetime.timedelta(days=28),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Fourth Sunday of Lent",
                "date": easter_date - datetime.timedelta(days=21),
                "liturgical_color": "pink",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Fifth Sunday of Lent",
                "date": easter_date - datetime.timedelta(days=14),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Palm Sunday",
                "date": easter_date - datetime.timedelta(days=7),
                "liturgical_color": "red",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Second Sunday of Easter",
                "date": easter_date + datetime.timedelta(days=7),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Third Sunday of Easter",
                "date": easter_date + datetime.timedelta(days=14),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Fourth Sunday of Easter",
                "date": easter_date + datetime.timedelta(days=21),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Fifth Sunday of Easter",
                "date": easter_date + datetime.timedelta(days=28),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Sixth Sunday of Easter",
                "date": easter_date + datetime.timedelta(days=35),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Holy Trinity Sunday",
                "date": easter_date + datetime.timedelta(days=56),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        return festivities

    def __generate_ash_wednesday(self):
        easter_date = self.__get_easter_date()

        festivities = []
        festivities.append(
            {
                "name": "Ash Wednesday",
                "date": easter_date - datetime.timedelta(days=46),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        return festivities

    def __generate_weekdays_holy_week(self):
        easter_date = self.__get_easter_date()

        festivities = []
        festivities.append(
            {
                "name": "Monday of Holy Week",
                "date": easter_date - datetime.timedelta(days=6),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Tuesday of Holy Week",
                "date": easter_date - datetime.timedelta(days=5),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Wednesday of Holy Week",
                "date": easter_date - datetime.timedelta(days=4),
                "liturgical_color": "purple",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        return festivities

    def __generate_easter_octave(self):
        easter_date = self.__get_easter_date()

        festivities = []
        festivities.append(
            {
                "name": "Monday of the Octave of Easter",
                "date": easter_date + datetime.timedelta(days=1),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Tuesday of the Octave of Easter",
                "date": easter_date + datetime.timedelta(days=2),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Wednesday of the Octave of Easter",
                "date": easter_date + datetime.timedelta(days=3),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Thursday of the Octave of Easter",
                "date": easter_date + datetime.timedelta(days=4),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Friday of the Octave of Easter",
                "date": easter_date + datetime.timedelta(days=5),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Saturday of the Octave of Easter",
                "date": easter_date + datetime.timedelta(days=6),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.HIGHER_SOLEMNITY,
            }
        )
        return festivities

    def __generate_mobile_solemnities_of_the_lord(self):
        easter_date = self.__get_easter_date()
        last_sunday_of_advent = self.__get_last_sunday_of_advent()

        festivities = []
        festivities.append(
            {
                "name": "Most Sacred Heart of Jesus",
                "date": easter_date + datetime.timedelta(days=68),
                "liturgical_color": "red",
                "liturgical_grade": LiturgicalGrade.SOLEMNITY,
            }
        )
        festivities.append(
            {
                "name": "Christ the King",
                "date": last_sunday_of_advent - datetime.timedelta(days=28),
                "liturgical_color": "red",
                "liturgical_grade": LiturgicalGrade.SOLEMNITY,
            }
        )
        return festivities

    def __generate_fixed_solemnities(
        self, current_solemnity_dates, sundays_of_advent_lent_easter
    ):
        festivities = []
        festivities.append(
            {
                "name": "Mary, Mother of God",
                "date": datetime.datetime(self._year, 1, 1),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.SOLEMNITY,
            }
        )

        working_dir = os.path.dirname(__file__)
        propriumdesanctis_1970 = []
        propriumdesanctis_1970_tags = {}
        with open(f"{working_dir}/propriumdesanctis_1970.json") as json_file:
            propriumdesanctis_1970 = json.load(json_file)
        with open(f"{working_dir}/propriumdesanctis_1970_tags.json") as json_file:
            propriumdesanctis_1970_tags = json.load(json_file)

        easter_date = self.__get_easter_date()

        for festivity in propriumdesanctis_1970:
            if festivity["GRADE"] == LiturgicalGrade.SOLEMNITY:
                festivity_to_add = {
                    "name": propriumdesanctis_1970_tags[festivity["TAG"]],
                    "date": datetime.datetime(
                        self._year, festivity["MONTH"], festivity["DAY"]
                    ),
                    "liturgical_color": festivity["COLOR"][0],
                    "liturgical_grade": festivity["GRADE"],
                }
                if festivity_to_add["date"] in current_solemnity_dates:
                    if (
                        festivity["TAG"] == "StJoseph"
                        and festivity_to_add["date"]
                        >= (easter_date - datetime.timedelta(days=7))
                        and festivity_to_add["date"] <= easter_date
                    ):
                        festivity_to_add["date"] = easter_date - datetime.timedelta(
                            days=8
                        )
                    elif (
                        festivity["TAG"] == "Annunciation"
                        and festivity_to_add["date"]
                        >= (easter_date - datetime.timedelta(days=7))
                        and festivity_to_add["date"]
                        <= (easter_date + datetime.timedelta(days=7))
                    ):
                        festivity_to_add["date"] = easter_date + datetime.timedelta(
                            days=8
                        )
                    elif (
                        festivity["TAG"]
                        in ["Annunciation", "StJoseph", "ImmaculateConception"]
                        and festivity_to_add["date"] in sundays_of_advent_lent_easter
                    ):
                        festivity_to_add["date"] += datetime.timedelta(days=1)

                festivities.append(festivity_to_add)
        return festivities

    def generate_festivities(self):
        festivities = []
        festivities.extend(self.__generate_easter_triduum())
        festivities.extend(self.__generate_christmas_epiphany())
        festivities.extend(self.__generate_ascension_pentecost())
        festivities.extend(self.__generate_sunday_major_seasons())
        festivities.extend(self.__generate_ash_wednesday())
        festivities.extend(self.__generate_weekdays_holy_week())
        festivities.extend(self.__generate_easter_octave())
        festivities.extend(self.__generate_mobile_solemnities_of_the_lord())

        current_solemnity_dates = []
        for festivity in festivities:
            if festivity["liturgical_grade"] == LiturgicalGrade.SOLEMNITY:
                current_solemnity_dates.append(festivity["date"])

        sundays_of_advent_lent_easter = []
        for festivity in festivities:
            if (
                festivity["name"].endswith("Sunday of Advent")
                or festivity["name"].endswith("Sunday of Lent")
                or festivity["name"].endswith("Sunday of Easter")
            ):
                sundays_of_advent_lent_easter.append(festivity["date"])

        festivities.extend(
            self.__generate_fixed_solemnities(
                current_solemnity_dates, sundays_of_advent_lent_easter
            )
        )

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

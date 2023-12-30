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

    def __get_sunday_after_epiphany(self):
        sunday_after_epiphany = datetime.datetime(self._year, 1, 6)
        while sunday_after_epiphany.weekday() != 6:
            sunday_after_epiphany += datetime.timedelta(days=1)

        return sunday_after_epiphany

    def __generate_feasts_mary_saints(self):
        festivities = []
        working_dir = os.path.dirname(__file__)
        propriumdesanctis_1970 = []
        propriumdesanctis_1970_tags = {}
        with open(f"{working_dir}/propriumdesanctis_1970.json") as json_file:
            propriumdesanctis_1970 = json.load(json_file)
        with open(f"{working_dir}/propriumdesanctis_1970_tags.json") as json_file:
            propriumdesanctis_1970_tags = json.load(json_file)

        for festivity in propriumdesanctis_1970:
            if festivity["GRADE"] == LiturgicalGrade.FEAST:
                festivity_to_add = {
                    "name": propriumdesanctis_1970_tags[festivity["TAG"]],
                    "date": datetime.datetime(
                        self._year, festivity["MONTH"], festivity["DAY"]
                    ),
                    "liturgical_color": festivity["COLOR"][0],
                    "liturgical_grade": festivity["GRADE"],
                }
                festivities.append(festivity_to_add)

        return festivities

    def __generate_feasts_of_the_lord(self):
        sunday_after_epiphany = self.__get_sunday_after_epiphany()

        festivities = []
        festivities.append(
            {
                "name": "Baptism of the Lord",
                "date": sunday_after_epiphany,
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.FEAST_LORD,
            }
        )

        working_dir = os.path.dirname(__file__)
        propriumdesanctis_1970 = []
        propriumdesanctis_1970_tags = {}
        with open(f"{working_dir}/propriumdesanctis_1970.json") as json_file:
            propriumdesanctis_1970 = json.load(json_file)
        with open(f"{working_dir}/propriumdesanctis_1970_tags.json") as json_file:
            propriumdesanctis_1970_tags = json.load(json_file)

        for festivity in propriumdesanctis_1970:
            if festivity["GRADE"] == LiturgicalGrade.FEAST_LORD:
                festivities.append(
                    {
                        "name": propriumdesanctis_1970_tags[festivity["TAG"]],
                        "date": datetime.datetime(
                            self._year, festivity["MONTH"], festivity["DAY"]
                        ),
                        "liturgical_color": festivity["COLOR"][0],
                        "liturgical_grade": festivity["GRADE"],
                    }
                )

        if datetime.datetime(self._year, 12, 25).weekday() == 6:
            festivities.append(
                {
                    "name": "Holy Family of Jesus, Mary and Joseph",
                    "date": datetime.datetime(self._year, 12, 30),
                    "liturgical_color": "white",
                    "liturgical_grade": LiturgicalGrade.FEAST_LORD,
                }
            )
        else:
            sunday_after_christmas = datetime.datetime(self._year, 12, 25)
            while sunday_after_christmas.weekday() != 6:
                sunday_after_christmas += datetime.timedelta(days=1)
            festivities.append(
                {
                    "name": "Holy Family of Jesus, Mary and Joseph",
                    "date": sunday_after_christmas,
                    "liturgical_color": "white",
                    "liturgical_grade": LiturgicalGrade.FEAST_LORD,
                }
            )

        return festivities

    def __generate_sundays_christmas_ordinary_time(self, current_solemnity_dates):
        festivities = []

        working_dir = os.path.dirname(__file__)

        propriumdetempore_tags = {}
        with open(f"{working_dir}/propriumdetempore_tags.json") as json_file:
            propriumdetempore_tags = json.load(json_file)

        first_ordinary = self.__get_sunday_after_epiphany()
        first_ordinary_limit = self.__get_easter_date() - datetime.timedelta(days=53)
        ord_sun = 1
        while (
            first_ordinary >= self.__get_sunday_after_epiphany()
            and first_ordinary < first_ordinary_limit
        ):
            first_ordinary = self.__get_sunday_after_epiphany() + datetime.timedelta(
                days=7 + (ord_sun - 1) * 7
            )
            ord_sun += 1
            if first_ordinary not in current_solemnity_dates:
                festivities.append(
                    {
                        "name": propriumdetempore_tags[f"OrdSunday{ord_sun}"],
                        "date": first_ordinary,
                        "liturgical_color": "green",
                        "liturgical_grade": LiturgicalGrade.FEAST_LORD,
                    }
                )

        last_ordinary = self.__get_last_sunday_of_advent() - datetime.timedelta(days=28)
        last_ordinary_lower_limit = self.__get_easter_date() + datetime.timedelta(
            days=63
        )
        ord_sun = 34
        ord_sun_cycle = 4
        while (
            last_ordinary
            <= self.__get_last_sunday_of_advent() - datetime.timedelta(days=28)
            and last_ordinary > last_ordinary_lower_limit
        ):
            ord_sun_cycle -= 1
            last_ordinary = self.__get_last_sunday_of_advent() - datetime.timedelta(
                days=ord_sun_cycle * 7
            )
            ord_sun -= 1
            if last_ordinary not in current_solemnity_dates:
                festivities.append(
                    {
                        "name": propriumdetempore_tags[f"OrdSunday{ord_sun}"],
                        "date": last_ordinary,
                        "liturgical_color": "green",
                        "liturgical_grade": LiturgicalGrade.FEAST_LORD,
                    }
                )

        return festivities

    def __generate_weekdays_advent(self, current_solemnities_feast_memorials):
        festivities = []
        last_sunday_of_advent = self.__get_last_sunday_of_advent()

        advent_1 = last_sunday_of_advent - datetime.timedelta(days=21)
        weekday_advent = last_sunday_of_advent - datetime.timedelta(days=21)
        weekday_advent_cnt = 1
        while weekday_advent >= advent_1 and weekday_advent < datetime.datetime(
            self._year, 12, 25
        ):
            weekday_advent = advent_1 + datetime.timedelta(days=weekday_advent_cnt)

            if (
                weekday_advent not in current_solemnities_feast_memorials
                and weekday_advent.weekday() != 6
            ):
                upper = int(weekday_advent.strftime("%j"))
                diff = upper - int(advent_1.strftime("%j"))
                current_adv_week = ((diff - diff % 7) // 7) + 1

                ordinal = self.__get_ordinal(current_adv_week)

                name = (
                    f"{weekday_advent.strftime('%A')} of the {ordinal} Week of Advent"
                )
                festivities.append(
                    {
                        "name": name,
                        "date": weekday_advent,
                        "liturgical_color": "purple",
                        "liturgical_grade": LiturgicalGrade.WEEKDAY,
                    }
                )

            weekday_advent_cnt += 1

        return festivities

    def __generate_weekdays_christmas_octave(self, current_solemnities_feast_memorials):
        festivities = []

        weekday_christmas = datetime.datetime(self._year, 12, 25)
        weekday_christmas_cnt = 1
        while weekday_christmas >= datetime.datetime(
            self._year, 12, 25
        ) and weekday_christmas < datetime.datetime(self._year, 12, 31):
            weekday_christmas = datetime.datetime(
                self._year, 12, 25
            ) + datetime.timedelta(days=weekday_christmas_cnt)
            if (
                weekday_christmas not in current_solemnities_feast_memorials
                and weekday_christmas.weekday() != 6
            ):
                ordinal = self.__get_ordinal(weekday_christmas_cnt + 1)

                name = f"{ordinal} Day of the Octave of Christmas"

                festivities.append(
                    {
                        "name": name,
                        "date": weekday_christmas,
                        "liturgical_color": "white",
                        "liturgical_grade": LiturgicalGrade.WEEKDAY,
                    }
                )
            weekday_christmas_cnt += 1

        return festivities

    def __get_ordinal(self, i):
        ordinal = ""
        if i == 1:
            ordinal = "1st"
        if i == 2:
            ordinal = "2nd"
        if i == 3:
            ordinal = "3rd"
        if i >= 4:
            ordinal = f"{i}th"
        return ordinal

    def __generate_weekdays_lent(self, current_solemnities):
        festivities = []

        ash_wednesday = self.__get_easter_date() - datetime.timedelta(days=46)
        palm_sunday = self.__get_easter_date() - datetime.timedelta(days=7)

        weekday_lent = self.__get_easter_date() - datetime.timedelta(days=46)
        weekday_lent_cnt = 1

        while weekday_lent >= ash_wednesday and weekday_lent < palm_sunday:
            weekday_lent = ash_wednesday + datetime.timedelta(days=weekday_lent_cnt)
            if weekday_lent not in current_solemnities and weekday_lent.weekday() != 6:
                if weekday_lent > self.__get_easter_date() - datetime.timedelta(
                    days=42
                ):
                    upper = int(weekday_lent.strftime("%j"))
                    diff = upper - int(
                        (
                            self.__get_easter_date() - datetime.timedelta(days=42)
                        ).strftime("%j")
                    )
                    current_lent_week = ((diff - diff % 7) // 7) + 1
                    ordinal = self.__get_ordinal(current_lent_week)

                    name = (
                        f"{weekday_lent.strftime('%A')} of the {ordinal} Week of Lent"
                    )

                    festivities.append(
                        {
                            "name": name,
                            "date": weekday_lent,
                            "liturgical_color": "purple",
                            "liturgical_grade": LiturgicalGrade.WEEKDAY,
                        }
                    )
                else:
                    name = f"{weekday_lent.strftime('%A')} after Ash Wednesday"
                    festivities.append(
                        {
                            "name": name,
                            "date": weekday_lent,
                            "liturgical_color": "purple",
                            "liturgical_grade": LiturgicalGrade.WEEKDAY,
                        }
                    )
            weekday_lent_cnt += 1

        return festivities

    def __get_solemnities(self, festivities):
        current_solemnity_dates = []
        for festivity in festivities:
            if festivity["liturgical_grade"] >= LiturgicalGrade.FEAST_LORD:
                current_solemnity_dates.append(festivity["date"])
        return current_solemnity_dates

    def __get_solemnities_feast_memorials(self, festivities):
        current_dates = []
        for festivity in festivities:
            if festivity["liturgical_grade"] >= LiturgicalGrade.MEMORIAL:
                current_dates.append(festivity["date"])
        return current_dates

    def __generate_memorials(self):
        festivities = []
        festivities.append(
            {
                "name": "The Immaculate Heart of the Blessed Virgin Mary",
                "date": self.__get_easter_date() + datetime.timedelta(days=69),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.MEMORIAL,
            }
        )

        working_dir = os.path.dirname(__file__)

        for year in [1970, 2002, 2008]:
            propriumdesanctis = []
            propriumdesanctis_tags = {}
            with open(f"{working_dir}/propriumdesanctis_{year}.json") as json_file:
                propriumdesanctis = json.load(json_file)
            with open(f"{working_dir}/propriumdesanctis_{year}_tags.json") as json_file:
                propriumdesanctis_tags = json.load(json_file)

            for festivity in propriumdesanctis:
                if (
                    festivity["GRADE"] == LiturgicalGrade.MEMORIAL
                    or festivity["GRADE"] == LiturgicalGrade.MEMORIAL_OPT
                ):
                    festivities.append(
                        {
                            "name": propriumdesanctis_tags[festivity["TAG"]],
                            "date": datetime.datetime(
                                self._year, festivity["MONTH"], festivity["DAY"]
                            ),
                            "liturgical_color": festivity["COLOR"][0],
                            "liturgical_grade": festivity["GRADE"],
                        }
                    )

        return festivities

    def __generate_decrees(self):
        festivities = []
        festivities.append(
            {
                "name": "The Immaculate Heart of the Blessed Virgin Mary",
                "date": self.__get_easter_date() + datetime.timedelta(days=69),
                "liturgical_color": "white",
                "liturgical_grade": LiturgicalGrade.MEMORIAL,
            }
        )

        working_dir = os.path.dirname(__file__)

        propriumdesanctis = []
        propriumdesanctis_tags = {}
        with open(f"{working_dir}/memorialsFromDecrees.json") as json_file:
            propriumdesanctis = json.load(json_file)
        with open(f"{working_dir}/memorialsFromDecrees_tags.json") as json_file:
            propriumdesanctis_tags = json.load(json_file)

        for festivity in propriumdesanctis:
            if "GRADE" in festivity and (
                festivity["GRADE"] == LiturgicalGrade.MEMORIAL
                or festivity["GRADE"] == LiturgicalGrade.MEMORIAL_OPT
            ):
                festivities.append(
                    {
                        "name": propriumdesanctis_tags[festivity["TAG"]],
                        "date": datetime.datetime(
                            self._year, festivity["MONTH"], festivity["DAY"]
                        ),
                        "liturgical_color": festivity["COLOR"][0],
                        "liturgical_grade": festivity["GRADE"],
                    }
                )

        return festivities

    def __generate_weekdays_major_seasons(self, current_solemnities_feast_memorials):
        festivities = []
        weekday_easter = self.__get_easter_date()
        weekday_easter_cnt = 1
        while (
            weekday_easter >= self.__get_easter_date()
            and weekday_easter < self.__get_easter_date() + datetime.timedelta(days=49)
        ):
            weekday_easter = self.__get_easter_date() + datetime.timedelta(
                days=weekday_easter_cnt
            )
            if (
                weekday_easter not in current_solemnities_feast_memorials
                and weekday_easter.weekday() != 6
            ):
                upper = int(weekday_easter.strftime("%j"))
                diff = upper - int(self.__get_easter_date().strftime("%j"))
                current_easter_week = ((diff - diff % 7) // 7) + 1
                ordinal = self.__get_ordinal(current_easter_week)
                name = (
                    f"{weekday_easter.strftime('%A')} of the {ordinal} Week of Easter"
                )
                festivities.append(
                    {
                        "name": name,
                        "date": weekday_easter,
                        "liturgical_color": "white",
                        "liturgical_grade": LiturgicalGrade.WEEKDAY,
                    }
                )

            weekday_easter_cnt += 1

        return festivities

    def __generate_weekdays_ordinary_time(self, current_solemnities_feast_memorials):
        festivities = []
        sunday_after_epiphany = self.__get_sunday_after_epiphany()
        first_weekdays_lower_limit = sunday_after_epiphany
        first_weekdays_upper_limit = self.__get_easter_date() - datetime.timedelta(
            days=46
        )

        ord_weekday = 1
        current_ord_week = 1
        first_ordinary = self.__get_sunday_after_epiphany()
        first_sunday = self.__get_sunday_after_epiphany() + datetime.timedelta(days=7)
        day_first_sunday = int(first_sunday.strftime("%j"))

        while (
            first_ordinary >= first_weekdays_lower_limit
            and first_ordinary < first_weekdays_upper_limit
        ):
            first_ordinary = self.__get_sunday_after_epiphany() + datetime.timedelta(
                days=ord_weekday
            )
            if first_ordinary not in current_solemnities_feast_memorials:
                if first_ordinary > first_sunday:
                    upper = int(first_ordinary.strftime("%j"))
                    diff = upper - day_first_sunday
                    current_ord_week = ((diff - diff % 7) // 7) + 2

                ordinal = self.__get_ordinal(current_ord_week)
                name = f"{first_ordinary.strftime('%A')} of the {ordinal} Week of Ordinary Time"
                festivities.append(
                    {
                        "name": name,
                        "date": first_ordinary,
                        "liturgical_color": "green",
                        "liturgical_grade": LiturgicalGrade.WEEKDAY,
                    }
                )
            ord_weekday += 1

        second_weekdays_lower_limit = self.__get_easter_date() + datetime.timedelta(
            days=49
        )
        second_weekdays_upper_limit = (
            self.__get_last_sunday_of_advent() - datetime.timedelta(21)
        )

        ord_weekday = 1
        last_ordinary = self.__get_easter_date() + datetime.timedelta(days=49)
        day_last_sunday = int(
            (self.__get_last_sunday_of_advent() - datetime.timedelta(21)).strftime("%j")
        )

        while (
            last_ordinary >= second_weekdays_lower_limit
            and last_ordinary < second_weekdays_upper_limit
        ):
            last_ordinary = self.__get_easter_date() + datetime.timedelta(
                days=49 + ord_weekday
            )
            if last_ordinary not in current_solemnities_feast_memorials:
                lower = int(last_ordinary.strftime("%j"))
                diff = day_last_sunday - lower
                week_diff = (diff - diff % 7) // 7
                current_ord_week = 34 - week_diff

                ordinal = self.__get_ordinal(current_ord_week)
                name = f"{last_ordinary.strftime('%A')} of the {ordinal} Week of Ordinary Time"
                festivities.append(
                    {
                        "name": name,
                        "date": last_ordinary,
                        "liturgical_color": "green",
                        "liturgical_grade": LiturgicalGrade.WEEKDAY,
                    }
                )
            ord_weekday += 1
        return festivities

    def __generate_saturday_memorial_bvm(self, current_solemnities_feast_memorials):
        festivities = []
        current_saturday = datetime.datetime(self._year, 1, 1)
        while current_saturday.weekday() != 5:
            current_saturday += datetime.timedelta(days=1)

        last_sat_dt = datetime.datetime(self._year, 12, 31)
        while last_sat_dt.weekday() != 5:
            last_sat_dt -= datetime.timedelta(days=1)

        while current_saturday <= last_sat_dt:
            current_saturday = current_saturday + datetime.timedelta(days=7)
            if current_saturday not in current_solemnities_feast_memorials:
                festivities.append(
                    {
                        "name": "Saturday Memorial of the Blessed Virgin Mary",
                        "date": current_saturday,
                        "liturgical_color": "white",
                        "liturgical_grade": LiturgicalGrade.MEMORIAL_OPT,
                    }
                )
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
                self.__get_solemnities(festivities), sundays_of_advent_lent_easter
            )
        )

        festivities.extend(self.__generate_feasts_of_the_lord())

        festivities.extend(
            self.__generate_sundays_christmas_ordinary_time(
                self.__get_solemnities(festivities)
            )
        )

        festivities.extend(self.__generate_feasts_mary_saints())

        festivities.extend(
            self.__generate_weekdays_advent(
                self.__get_solemnities_feast_memorials(festivities)
            )
        )

        festivities.extend(
            self.__generate_weekdays_christmas_octave(
                self.__get_solemnities_feast_memorials(festivities)
            )
        )

        festivities.extend(
            self.__generate_weekdays_lent(self.__get_solemnities(festivities))
        )

        festivities.extend(self.__generate_memorials())
        festivities.extend(self.__generate_decrees())
        festivities.extend(
            self.__generate_weekdays_major_seasons(
                self.__get_solemnities_feast_memorials(festivities)
            )
        )

        festivities.extend(
            self.__generate_weekdays_ordinary_time(
                self.__get_solemnities_feast_memorials(festivities)
            )
        )

        festivities.extend(
            self.__generate_saturday_memorial_bvm(
                self.__get_solemnities_feast_memorials(festivities)
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

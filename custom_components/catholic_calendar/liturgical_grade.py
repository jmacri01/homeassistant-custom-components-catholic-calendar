class LiturgicalGrade:
    HIGHER_SOLEMNITY = 7
    SOLEMNITY = 6
    FEAST_LORD = 5
    FEAST = 4
    MEMORIAL = 3
    MEMORIAL_OPT = 2
    COMMEMORATION = 1
    WEEKDAY = 0

    @staticmethod
    def descr(grade):
        if grade == LiturgicalGrade.WEEKDAY:
            return "Weekday"
        if grade == LiturgicalGrade.COMMEMORATION:
            return "Commemoration"
        if grade == LiturgicalGrade.MEMORIAL_OPT:
            return "Optional Memorial"
        if grade == LiturgicalGrade.MEMORIAL:
            return "Memorial"
        if grade == LiturgicalGrade.FEAST:
            return "Feast"
        if grade == LiturgicalGrade.FEAST_LORD:
            return "Feast of our Lord"
        if grade == LiturgicalGrade.SOLEMNITY:
            return "Solemnity"
        if grade == LiturgicalGrade.HIGHER_SOLEMNITY:
            return "Higher Solemnity"

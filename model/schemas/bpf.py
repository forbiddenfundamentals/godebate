from .base import Slot, Team, Schema


class BPFTeam1Slot1(Slot):

    NAME = "Премьер-Министр"
    SHORTCUT = "ПМ"


class BPFTeam1Slot2(Slot):

    NAME = "Заместитель Премьер-Министра"
    SHORTCUT = "ЗПМ"


class BPFTeam1(Team):

    NAME = "Открывающее правительство"
    SHORTCUT = "ОП"


class BPFTeam2Slot1(Slot):

    NAME = "Лидер Оппозиции"
    SHORTCUT = "ЛО"


class BPFTeam2Slot2(Slot):

    NAME = "Заместитель Лидера Оппозиции"
    SHORTCUT = "ЗЛО"


class BPFTeam2(Team):

    NAME = "Открывающая Оппозиция"
    SHORTCUT = "ОО"


class BPFTeam3Slot1(Slot):

    NAME = "Член Правительства"
    SHORTCUT = "ЧП"


class BPFTeam3Slot2(Slot):

    NAME = "Секретарь Правительства"
    SHORTCUT = "ЗЛО"


class BPFTeam3(Team):

    NAME = "Закрывающее Правительство"
    SHORTCUT = "ЗП"


class BPFTeam4Slot1(Slot):

    NAME = "Член Оппозиции"
    SHORTCUT = "ЧО"


class BPFTeam4Slot2(Slot):

    NAME = "Секретарь Оппозиции"
    SHORTCUT = "СО"


class BPFTeam4(Team):

    NAME = "Закрывающая Оппозиция"
    SHORTCUT = "ЗО"


class BPFSchema(Schema):

    NAME = "Британский Парламентский Формат"
    TEAM_CLASSES = [BPFTeam1, BPFTeam2, BPFTeam3, BPFTeam4]
    PLAYER_LIMIT = 8

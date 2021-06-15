from GENERAL_CONFIG import GeneralConfig
from pathlib import Path


def asf(name):
    """
    Установить префикс для таблицы аерика.
    При операциях супер импорта... Когда используется самая тёмная магия...

    :param name:
    :return:
    """
    name_prefix = get_project_prefix()
    return f'{name_prefix}{name}'.lower()


def get_project_prefix():
    """
    Общий глобальный префикс проекта

    Даже модуль Pathlib может воткнуть на ровном месте и вернуть точку вместо имени
    Отсюда вот эта фича: Path(GeneralConfig.PROJECT_GENERAL_FOLDER.absolute()).name
    """

    if getattr(GeneralConfig, 'PROJECT_TABLE_NAMESPACE_PREFIX', None):
        name_prefix = GeneralConfig.PROJECT_TABLE_NAMESPACE_PREFIX
    else:
        name_prefix = Path(GeneralConfig.PROJECT_GENERAL_FOLDER.absolute()).name

    return f'__{name_prefix}_'.lower()

"""
Основная конфигурация проекта.
Сначала мы решаем какое ядро используем - потом наследуем его в GeneralConfig
"""

from MODS.scripts.python.easy_scripts import PROJECT_GENERAL_FOLDER as general_path


class GeneralConfig():
    """
    Общая конфа - она импортируется по проекту
    """

    PROJECT_GENERAL_FOLDER = general_path
    PROJECT_TABLE_NAMESPACE_PREFIX = 'input your namespace table prefix!'

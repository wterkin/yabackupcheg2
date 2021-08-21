#! /usr/bin/python3
## -*- coding: utf-8 -*-
# @author: Andrey Pakhomenkov pakhomenkov@yandex.ru

import json

class CBackupManager:
    """Основной класс."""
    
    def __init__(self):
        """Конструктор"""
        self.master_config = dict()
    
    def load_master_config():
        """Загружает основной конфиг программы."""
        config_file = open(Path.home() / CONFIG_FOLDER / CONFIG_FILE_NAME, "r", encoding="utf-8")
        self.config = json.load(config_file)      
    
if __name__ == "__main__":
    
    manager = CBackupManager()
    manager.run

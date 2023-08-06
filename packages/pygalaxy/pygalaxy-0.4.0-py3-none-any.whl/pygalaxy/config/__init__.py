#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser


class Config:
    """
    解析并获取.ini 配置文件中的配置信息
    """

    def __init__(self, config_file_path: str):
        self.parser = configparser.ConfigParser()
        self.parser.read(r'%s' % config_file_path)

    def get_attr(self, section: str, key: str):
        """
        获取配置信息
        """
        try:
            return self.parser.get(section, key)
        except Exception as e:
            return None


if __name__ == '__main__':
    print(Config('').get_attr('path', 'images'))

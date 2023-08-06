#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def get_project_path(project_name: str):
    path = os.path.abspath(os.path.dirname(__file__))
    p_path = path[:path.find(project_name)+len(project_name)]
    return p_path


if __name__ == '__main__':
    pass

# -*- coding: utf-8 -*-
"""
用于本地开发环境的全局配置
"""
from settings import APP_ID


# ===============================================================================
# 数据库设置, 本地开发数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # 默认用mysql
        'NAME': 'db.sqlite3',                    # 数据库名 (默认与APP_ID相同)
    },
}


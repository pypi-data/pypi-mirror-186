from functools import wraps
from flask import current_app
from .CoreController import CoreController

class Uiadmin:
    # 构造函数
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    # 初始化应用
    def init_app(self, app):
        print('init uiadmin')

        # 在 app 应用中存储所有扩展实例, 可验证扩展是否完成实例化
        app.extensions['uiadmin'] = self

        # 配置
        app.config.setdefault('UIADMIN_SITE_TITLE', "UiAdmin")
        app.config.setdefault('UIADMIN_SITE_LOGO', "")
        app.config.setdefault('UIADMIN_SITE_LOGO_TITLE', "")
        app.config.setdefault('UIADMIN_SITE_LOGO_BADGE', "")
        app.config.setdefault('UIADMIN_SYTE_VERSION', "1.0.0")

        # 路由
        app.add_url_rule('/xyadmin/', view_func=CoreController.xyadmin)
        app.add_url_rule('/xyadmin/api', view_func=CoreController.xyadmin_api)
 
    # 接口方法装饰器，被装饰的接口将自动生成菜单。
    def menu_item(self, func):
        app = self.app or current_app
        @wraps(func)
        def decorator(*args, **kwargs):

            ret = func(*args, **kwargs)

            return ret

        return decorator

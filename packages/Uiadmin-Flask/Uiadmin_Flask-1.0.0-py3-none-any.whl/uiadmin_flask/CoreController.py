import requests
from flask import current_app,request
from .util import jsonres

app = current_app()

host = request.host

class CoreController:
    # @self.app.route("/xyadmin/")
    def xyadmin():
        url = "https://uiadmin.net/xyadmin/?version=2.0.0"
        res = requests.get(url)
        return res.text

    # @app.route("/xyadmin/api")
    def xyadmin_api():
        # 返回json数据的方法
        data = {
            "code": 200,
            "msg": "success",
            "data": {
                "framework": "flask",
                "stype": "应用",
                "name": "pyadmin",
                "api": {
                    "apiLogin": "/v1/admin/user/login",
                    "apiConfig": "/v1/site/info",
                    "apiBase": host + "/api",
                    "apiUserInfo": "/v1/admin/user/info",
                    "apiAdmin": "/v1/admin/index/index",
                    "apiMenuTrees": "/v1/admin/menu/trees"
                },
                "lang": "python",
                "title": app.config['UIADMIN_SITE_TITLE'],
                "domainRoot": host,
                "siteInfo": {
                    "title": app.config['UIADMIN_SITE_TITLE']
                },
                "version": app.config['UIADMIN_SYTE_VERSION'],
                "config": {
                    "useVerify": "",
                    # "headerRightToolbar": [
                    #         {
                    #             "type": "url",
                    #             "title": "接口文档",
                    #             "class": "xyicon xyicon-map",
                    #             "url": "/doc.html"
                    #         }
                    # ]
                }
            }
        }
        return jsonres(data)
 
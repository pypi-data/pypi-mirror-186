from py_wechat_tools.libs.tools import WeChatBase, get_parameter
from py_wechat_tools.mini_program.analysis import Analysis
from py_wechat_tools.mini_program.auth import Auth
from py_wechat_tools.mini_program.broadcast import Broadcast
from py_wechat_tools.mini_program.img import SuperResolution
from py_wechat_tools.mini_program.ocr import Ocr
from py_wechat_tools.mini_program.risk_control import RiskControl
from py_wechat_tools.mini_program.security import Security
from py_wechat_tools.mini_program.shortlink import ShortLink
from py_wechat_tools.mini_program.soter import Soter
from py_wechat_tools.mini_program.subscribe_message import SubscribeMessage
from py_wechat_tools.mini_program.updatable_message import UpdatableMessage
from py_wechat_tools.official_account.oauth2 import OAuth2
from py_wechat_tools.mini_program.check import Check
from py_wechat_tools.official_account.img import SuperResolution as OASuperResolution


class MPTools(Analysis, Auth, SuperResolution, Security, Ocr, SubscribeMessage, UpdatableMessage, RiskControl,
              ShortLink, Soter, Broadcast):
    """ 微信小程序工具 """

    def get_access_token_cache(self, access_token=None):
        """
        重写设置access_token接口，缓存access_token
        如果不使用缓存，注释当前接口，在参数中传递access_token
        :param access_token: 临时access_token，如果传了，以这个access_token为准
        :return:
        """

        cache = self.cache
        access_token = access_token or cache.get("access_token")
        if not access_token:

            data = self.get_access_token()
            access_token = data.access_token
            # 缓存access_token，有效时间为7200秒(2小时) - 200 秒 提前200秒主动失效，避免发现失效后再重新获取。
            # 提前失效重新获取，避免接口出现access_token无效的返回
            expires_in = 60 * 60
            if hasattr(data, "expires_in"):
                expires_in = data.expires_in - 200

            cache.set("access_token", access_token,  expires_in)
        return access_token


class OATools(OAuth2, OASuperResolution):
    """ 微信公众号工具 """

    def get_access_token_cache(self, access_token=None):
        """
        重写设置access_token接口，缓存access_token
        如果不使用缓存，注释当前接口，在参数中传递access_token
        :param access_token: 临时access_token，如果传了，以这个access_token为准
        :return:
        """

        cache = self.cache
        access_token = access_token or cache.get("access_token")
        if not access_token:

            data = self.get_access_token()
            access_token = data.access_token
            # 缓存access_token，有效时间为7200秒(2小时) - 200 秒 提前200秒主动失效，避免发现失效后再重新获取。
            # 提前失效重新获取，避免接口出现access_token无效的返回
            expires_in = 60 * 60
            if hasattr(data, "expires_in"):
                expires_in = data.expires_in - 200

            cache.set("access_token", access_token, expires_in)
        return access_token

    def init_oa_access_token(self, redirect_uri=None, refresh_token=None, scope=None, state=None, force_popup=None,
                             force_snap_shot=None, code=None):
        """
        类内部初始化access_token

        :param redirect_uri: [选填]授权后重定向的回调链接地址， 请使用 urlEncode 对链接进行处理，需要修改时可传入
        :param refresh_token: 用户刷新 oa_access_token
        :param scope: [选填]应用授权作用域，合法值：
                    snsapi_base或Auth2.snsApiBase （不弹出授权页面，直接跳转，只能获取用户openid）
                    snsapi_userinfo或Auth2.snsApiUserInfo（弹出授权页面，可通过 openid 拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息 ）
        :param state: [选填]重定向后会带上 state 参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节
        :param force_popup: [选填]强制此次授权需要用户弹窗确认；默认为false；需要注意的是，若用户命中了特殊场景下的静默授权逻辑，则此参数不生效
        :param force_snap_shot: [选填]强制此次授权进入快照页；默认为false；需要注意的是，若本次登录命中了近期登录过免授权逻辑逻辑或特殊场景下的静默授权逻辑，则此参数不生效
        :param code: 此参数为回调时携带的参数，无需手动传入。

        :return: 返回url, data 两个参数
            url不为None时，请重定向到该url，此时data为None

            data：WechatData对象，包含参数：
                属性                  类型              说明
                access_token        string          网页授权接口调用凭证,注意：此access_token与基础支持的access_token不同
                expires_in          number          access_token接口调用凭证超时时间，单位（秒）
                refresh_token       string          用户刷新access_token，有效期为30天
                openid              string          用户唯一标识，请注意，在未关注公众号时，用户访问公众号的网页，也会产生一个用户和公众号唯一的OpenID
                scope               string          用户授权的作用域，使用逗号（,）分隔
        """

        # 通过传入的refresh_token获取access_token
        if refresh_token:
            data = self.update_oa_access_token(refresh_token)
            return None, data

        # ------- 重新授权获取code -------
        # 没有code就取code

        if code is None:
            url = self.authorize(redirect_uri=redirect_uri, scope=scope, state=state, force_popup=force_popup,
                                 force_snap_shot=force_snap_shot)
            return url, None

        print("step2: code换access_token")
        data = self.get_oa_access_token(code)

        return None, data

    def authorize_userinfo(self, redirect_uri=None, openid=None, oa_access_token=None, refresh_token=None,
                           cache_fun=None, cache_args=None,  cache_kwargs=None, scope=None, state=None,
                           force_popup=None, force_snap_shot=None, code=None):
        """
        一个方法弹出授权并且获取用户信息，无需关心如何获取code、access_token等。
        示例：
            # 1、接收一个GET请求的参数code，以Django框架为例
            code = request.GET.get("code")

            # 2、必须传接收到的code，否则会无限刷新授权页面
            #    接收两个参数 url, user_info
            url, user_info = authorize_userinfo(code=code)

            # url不为None时，重定向到url
            if url:
                redirect(url)   # 重定向到url

            # 业务逻辑
            return

        获取access_token
            方式1（传入openid与refresh_token）：通过传入的refresh_token更新access_token，
            方式2（传入openid）：缓存获取access_token，或者缓存获取refresh_token，更新access_token，或者通过授权code获取access_token
            方式3（不传openid与refresh_token）：通过授权code获取access_token


        :param redirect_uri: [选填]授权后重定向的回调链接地址， 请使用 urlEncode 对链接进行处理，需要修改时可传入

            # 可以对以下三个参数做缓存，每次请求可以从缓存中读取
        :param openid: [选填]用户openid，建议提供，提供该参数可以减少请求微信接口次数，该参数与oa_access_token一起传入方可生效
        :param oa_access_token: [选填]用户oa_access_token 建议提供，提供该参数可以减少请求微信接口次数，该参数与openid一起传入方可生效
        :param refresh_token: [选填]用户刷新 oa_access_token，建议提供，提供该参数可以减少请求微信接口次数

        :param cache_fun: [选填]允许传入一个回调方法，实现缓存
        :param cache_args: [选填]缓存方法的args传参，类型为元组()
        :param cache_kwargs: [选填]缓存方法的kwargs传参，类型为字典{}
        :param scope: [选填]应用授权作用域，合法值：
                    snsapi_base或Auth2.snsApiBase （不弹出授权页面，直接跳转，只能获取用户openid）
                    snsapi_userinfo或Auth2.snsApiUserInfo（弹出授权页面，可通过 openid 拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息 ）
        :param state: [选填]重定向后会带上 state 参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节
        :param force_popup: [选填]强制此次授权需要用户弹窗确认；默认为false；需要注意的是，若用户命中了特殊场景下的静默授权逻辑，则此参数不生效
        :param force_snap_shot: [选填]强制此次授权进入快照页；默认为false；需要注意的是，若本次登录命中了近期登录过免授权逻辑逻辑或特殊场景下的静默授权逻辑，则此参数不生效
        :param code: 此参数为回调时携带的参数，无需手动传入。
        :return: 返回两个参数，(url: str, userinfo: WeChatData)  url不为空：301重定向到url，userinfo不为空：完成所有验证，userinfo为用户的信息

            url：用户授权地址，301重定向到url即可

            userinfo包含参数：
                属性                  类型                  说明
                openid              string              用户的唯一标识
                nickname            string              用户昵称
                sex                 number              用户的性别，值为1时是男性，值为2时是女性，值为0时是未知
                province            string              用户个人资料填写的省份
                city                string              普通用户个人资料填写的城市
                country             string              国家，如中国为CN
                headimgurl          string              用户头像，最后一个数值代表正方形头像大小（有0、46、64、96、132数值可选，0代表640*640正方形头像），
                                                        用户没有头像时该项为空。若用户更换头像，原有头像 URL 将失效。
                privilege           <Array>.string      用户特权信息，json 数组，如微信沃卡用户为（chinaunicom）
                unionid             string              只有在用户将公众号绑定到微信开放平台帐号后，才会出现该字段。

        """

        if openid is None or oa_access_token is None:

            url, data = self.init_oa_access_token(
                redirect_uri=redirect_uri,
                refresh_token=refresh_token,
                scope=scope,
                state=state,
                force_popup=force_popup,
                force_snap_shot=force_snap_shot,
                code=code
            )

            if url:
                return url, None

            if cache_fun:
                cache_fun(data, *(cache_args or ()), **(cache_kwargs or {}))

            openid = data.openid
            oa_access_token = data.access_token

        print("step3: access_token 换 userinfo")
        user_info = self.get_userinfo(openid, oa_access_token)
        return None, user_info


class check(Check):
    pass

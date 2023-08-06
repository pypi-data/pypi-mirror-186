from urllib.parse import quote

from py_wechat_tools.libs.tools import OABase


class OAuth2(OABase):
    snsApiBase = "snsapi_base"  # 不弹出授权，只获取openid
    snsApiUserInfo = "snsapi_userinfo"  # 弹出授权，可获取用户昵称、性别等信息

    def authorize(self, redirect_uri=None, scope=None, state=None, force_popup=None, force_snap_shot=None):
        """
        弹出授权获取code
        如果用户同意授权，页面将跳转至 redirect_uri/?code=CODE&state=STATE。

        微信官方文档：
        https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html#0

        :param redirect_uri: 授权后重定向的回调链接地址， 请使用 urlEncode 对链接进行处理
        :param scope: 应用授权作用域，合法值：
                    snsapi_base或Auth2.snsApiBase （不弹出授权页面，直接跳转，只能获取用户openid）
                    snsapi_userinfo或Auth2.snsApiUserInfo（弹出授权页面，可通过 openid 拿到昵称、性别、所在地。并且， 即使在未关注的情况下，只要用户授权，也能获取其信息 ）
        :param state: 重定向后会带上 state 参数，开发者可以填写a-zA-Z0-9的参数值，最多128字节
        :param force_popup:强制此次授权需要用户弹窗确认；默认为false；需要注意的是，若用户命中了特殊场景下的静默授权逻辑，则此参数不生效
        :param force_snap_shot: 强制此次授权进入快照页；默认为false；需要注意的是，若本次登录命中了近期登录过免授权逻辑逻辑或特殊场景下的静默授权逻辑，则此参数不生效
        :return: url链接，让用户重定向到该地址即可
        """

        params = self.check_params(
            appid=self.appid,
            redirect_uri=quote(redirect_uri or self.redirect_uri),  # 回调地址
            response_type="code",
            scope=scope or self.snsApiUserInfo,
            state=state,
            forcePopup=force_popup,
            forceSnapShot=force_snap_shot
        )

        params = "&".join(["%s=%s" % (k, v) for k, v in params.items()])
        url = "https://open.weixin.qq.com/connect/oauth2/authorize?{params}#wechat_redirect".format(params=params)

        return url

    def get_oa_access_token(self, code):
        """
        code换access_token，这里的access_token与基础支持的access_token不同，为了方便区分，这里称为oa_access_token

        微信官方文档：
        https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html#1

        :param code: 填写第一步获取的 code 参数，在回调参数中的code
        :return: 返回WechatData对象，包含参数：

                属性                  类型              说明
                access_token        string          网页授权接口调用凭证
                                                    注意：此access_token与基础支持的access_token不同，这个是用户的access_token
                expires_in          number          access_token接口调用凭证超时时间，单位（秒）
                refresh_token       string          刷新access_token的凭证，有效期为30天
                openid              string          用户唯一标识，请注意，在未关注公众号时，用户访问公众号的网页，也会产生一个用户和公众号唯一的OpenID
                scope               string          用户授权的作用域，使用逗号（,）分隔

        """
        url = "https://api.weixin.qq.com/sns/oauth2/access_token"

        params = self.get_full_params(
            code=code,
            grant_type="authorization_code"
        )
        data = self.get(url, params=params)

        return data

    def update_oa_access_token(self, refresh_token):
        """
        更新access_token
        这里的access_token与基础支持的access_token不同，为了方便区分，这里称为oa_access_token

        微信官方文档：
        https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html#2

        :param refresh_token: 上次授权获取的 refresh_token
        :return: WechatData对象，包含参数：

                属性                  类型              说明
                access_token        string          网页授权接口调用凭证,注意：此access_token与基础支持的access_token不同
                expires_in          number          access_token接口调用凭证超时时间，单位（秒）
                refresh_token       string          用户刷新access_token，有效期为30天
                openid              string          用户唯一标识，请注意，在未关注公众号时，用户访问公众号的网页，也会产生一个用户和公众号唯一的OpenID
                scope               string          用户授权的作用域，使用逗号（,）分隔

        """
        url = "https://api.weixin.qq.com/sns/oauth2/refresh_token"

        params = self.get_full_params(
            appid=self.appid,
            grant_type="refresh_token",
            refresh_token=refresh_token
        )

        data = self.get(url, params=params)

        return data

    def get_userinfo(self, openid, oa_access_token):
        """
        获取用户信息
        如果网页授权作用域为snsapi_userinfo, 则可以通过该接口拉取用户信息了。

        微信官方文档：
        https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html#3

        :param openid: 用户openid
        :param oa_access_token: 用户的oa_access_token
        :return: WechatData对象，包含参数：
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
        url = "https://api.weixin.qq.com/sns/userinfo"

        params = self.check_params(
            openid=openid,
            access_token=oa_access_token,
            lang="zh_CN"
        )

        return self.get(url, params=params)

    def auth_access_token(self, openid, oa_access_token):
        """
        检验授权凭证（access_token）是否有效

        微信官方文档：
        https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html#4

        :param oa_access_token: 授权凭证
        :param openid: 用户的唯一标识
        :return: WechatData对象

        """
        url = "https://api.weixin.qq.com/sns/auth"

        params = self.get_full_params(
            openid=openid,
            access_token=oa_access_token
        )

        return self.get(url, params=params)

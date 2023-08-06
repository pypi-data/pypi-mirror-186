from py_wechat_tools.mini_program import auth, subscribe_message, uniform_message, ocr, analysis, img, security


class Auth(auth.Auth):
    """
    用户信息相关
    """


class UniformMessages(uniform_message.UniformMessages):
    """
    统一服务消息
    """


class SubscribeMessage(subscribe_message.SubscribeMessage):
    """
    获取小程序消息模板
    """


class Ocr(ocr.Ocr):
    pass


class Analysis(analysis.Analysis):
    pass


class SuperResolution(img.SuperResolution):
    pass


class Security(security.Security):
    pass

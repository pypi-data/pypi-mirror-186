from py_wechat_tools.libs.tools import WeChatBase


class TemplateInfo:
    member_count = None  # target_state = 0 时必填，文字内容模板中 member_count 的值
    room_limit = None  # target_state = 0 时必填，文字内容模板中 room_limit 的值
    path = None  # target_state = 1 时必填，点击「进入」启动小程序时使用的路径。对于小游戏，没有页面的概念，可以用于传递查询字符串（query），如 "?foo=bar"
    version_type = None  # target_state = 1 时必填，点击「进入」启动小程序时使用的版本。有效参数值为：develop（开发版），trial（体验版），release（正式版）

    def __init__(self, member_count=None, room_limit=None, path=None, version_type=None, **kwargs):
        par = locals()
        par.pop("self", None)
        par.pop("kwargs", None)
        [setattr(self, k, v) for k, v in par.items()]

    def get(self):

        parameter_list = []
        [parameter_list.append({"name": k, "values": v}) for k, v in self.__dict__.items() if v is not None]

        template_info = {
            "parameter_list": parameter_list
        }
        print(template_info)
        return template_info


class UpdatableMessage(WeChatBase):

    def create_activity_id(self, unionid=None, openid=None):
        """
        创建被分享动态消息或私密消息的 activity_id

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/updatable-message/updatableMessage.createActivityId.html

        openid与 unionid 填一个即可
        :param unionid: 为私密消息创建activity_id时，指定分享者为 unionid 用户。其余用户不能用此activity_id分享私密消息
        :param openid:  为私密消息创建activity_id时，指定分享者为 openid 用户。其余用户不能用此activity_id分享私密消息
        :return:  返回 WeChatData 类型 返回包含
                属性	                类型	            说明
                activity_id	        string	        动态消息的 ID
                expiration_time	    number	        activity_id 的过期时间戳。默认24小时后过期。

        """
        url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/activityid/create"

        if self.m2n(unionid, openid) is False:
            raise ValueError("unionid与openid至少填一个")

        params = self.check_params(
            access_token=self.access_token,
            unionid=unionid
        )

        data = self.check_params(
            openid=openid
        )

        return self.get(url, params=params, data=data)

    def set_updatable_msg(self, activity_id, target_state, template_info: TemplateInfo):
        """
        修改被分享的动态消息

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/updatable-message/updatableMessage.setUpdatableMsg.html

        :param activity_id: 动态消息的 ID，通过 updatableMessage.createActivityId 接口获取
        :param target_state:  动态消息修改后的状态, 合法值: 0 未开始；1 已开始
        :param template_info:  TemplateInfo类型 动态消息对应的模板信息
            template_info 的结构
                值	            说明
                member_count    target_state = 0 时必填，文字内容模板中 member_count 的值
                room_limit	    target_state = 0 时必填，文字内容模板中 room_limit 的值
                path	        target_state = 1 时必填，点击「进入」启动小程序时使用的路径。对于小游戏，没有页面的概念，可以用于传递查询字符串（query），如 "?foo=bar"
                version_type	target_state = 1 时必填，点击「进入」启动小程序时使用的版本。有效参数值为：develop（开发版），trial（体验版），release（正式版

        :return:  返回 WeChatData 类型 返回包含
                属性	                类型	            说明

        """
        url = "https://api.weixin.qq.com/cgi-bin/message/wxopen/updatablemsg/send"

        params = self.check_params(access_token=self.access_token)

        data = self.check_params(
            activity_id=activity_id,
            target_state=target_state,
            template_info=template_info.get(),
        )

        return self.post(url, params=params, data=data)

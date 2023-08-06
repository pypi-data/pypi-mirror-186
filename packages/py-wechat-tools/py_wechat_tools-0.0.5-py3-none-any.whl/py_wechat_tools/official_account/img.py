from io import BytesIO

from py_wechat_tools.libs.tools import dict2obj, WeChatBase
import requests


class SuperResolution(WeChatBase):

    def ai_crop(self, img_url: str = None, file_name: str = None, file: bytes = None):
        """
        本接口提供基于小程序的图片智能裁剪能力

        详细文档请参考：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/img/img.aiCrop.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数（img_url 或（file_name、file）二选一"）
        :param file_name: 文件名称 （img_url 或（file_name、file）二选一"）
        :param file: 二进制文件，通过二进制文件上传时file_name必填 （img_url 或（file_name、file）二选一"）
        :return: 返回一个 WeChatData 类，包含：
                属性              类型              说明
                results         array           智能裁剪结果
                img_size        objects         图片大小

            results:    智能裁剪结果
                属性              类型              说明
                crop_left       number
                crop_top        number
                crop_right      number
                crop_bottom     number

            img_size:   图片大小
                属性              类型              说明
                w               number
                y               number
        """
        url = "https://api.weixin.qq.com/cv/img/aicrop"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url
        )

        if img_url:
            return self.post(url, params=params)

        elif file_name and file:
            params = self.check_params(
                access_token=self.access_token,
            )
            return self.file_post(url, file_name, file, params=params)

        raise ValueError("传参错误，img_url 或（file_name、file）必填一项")

    def scan_qr_code(self, img_url: str = None, file_name: str = None, file: bytes = None):
        """
        本接口提供基于小程序的条码/二维码识别的API。

        详细文档请参考：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/img/img.scanQRCode.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数（img_url 或（file_name、file）二选一"）
        :param file_name: 文件名称 （img_url 或（file_name、file）二选一"）
        :param file: 二进制文件，通过二进制文件上传时file_name必填 （img_url 或（file_name、file）二选一"）
        :return: 返回一个 WeChatData 类
                属性              类型              说明
                code_results    array           扫码结果
                img_size        objects         图片大小

            code_results:
                属性              类型              说明
                type_name       QR_CODE         类型，QR_CODE、EAN_13、CODE_128
                data            str             二维码/条形码包含的内容
                pos             WechatData      坐标位置，仅二维码包含该字段

            pos:
                属性              类型              说明
                left_top       WechatData         左上角
                right_top      WechatData         右上角
                right_bottom   WechatData         右下角
                left_bottom    WechatData         左下角

            left_top、right_top、right_bottom、left_bottom:
                属性              类型              说明
                x               number           x坐标
                y               number           y坐标

            img_size:   图片大小
                属性              类型              说明
                x               number           x坐标
                y               number           y坐标
        """
        url = "https://api.weixin.qq.com/cv/img/qrcode"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url
        )
        if img_url:
            return self.post(url, params=params)

        elif file_name and file:
            params = self.check_params(
                access_token=self.access_token,
            )
            return self.file_post(url, file_name, file, params=params)

        raise ValueError("传参错误，img_url 或（file_name、file）必填一项")

    def superresolution(self, img_url=None, file_name: str = None, file: bytes = None):
        """
        本接口提供基于小程序的图片高清化能力。

        不能说效果不好，只能说几乎就是返回原图，参考本代码中的图片文件：docs/diff.png

        详细文档请参考：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/img/img.superresolution.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数（img_url 或（file_name、file）二选一"）
        :param file_name: 文件名称 （img_url 或（file_name、file）二选一"）
        :param file: 二进制文件，通过二进制文件上传时file_name必填 （img_url 或（file_name、file）二选一"）
        :return: 返回一个 WeChatData 类，包含：
                属性              类型              说明
                media_id         string         有效期为3天，期间可以通过“获取临时素材”接口获取图片二进制
                                                .get_media() 方法获取

        """
        url = "https://api.weixin.qq.com/cv/img/superresolution"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url,
        )
        if img_url:
            return self.post(url, params=params)

        elif file_name and file:
            params = self.check_params(
                access_token=self.access_token,
            )
            return self.file_post(url, file_name, file, params=params)

        raise ValueError("传参错误，img_url 或（file_name、file）必填一项")

    def upload_media(self, file_name: str, file_url: str = None, file: bytes = None, file_type: str = "image"):
        """
        上传临时素材（添加临时素材）

        公众号经常有需要用到一些临时性的多媒体素材的场景，例如在使用接口特别是发送消息时，对多媒体文件、多媒体消息的获取和调用等操作，
        是通过media_id来进行的。素材管理接口对所有认证的订阅号和服务号开放。通过本接口，公众号可以新增临时素材（即上传临时多媒体文件）

        官方文档：https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html

        :param file_name: [必填] 文件名称
        :param file_url: [选填] 文件url，通过url获取文件并上传
        :param file: [选填] 二进制文件，通过二进制文件上传（url、file二选一）
        :param file_type: [默认image] 媒体文件类型，分别有图片（image）、语音（voice）、视频（video）和缩略图（thumb）
        :return: 返回request

                属性              类型              说明
                type            string          媒体文件类型，分别有图片（image）、语音（voice）、视频（video）和缩略图（thumb，主要用于视频与音乐格式的缩略图）
                media_id        string          有效期为3天，期间可以通过“获取临时素材”接口获取图片二进制 通过.get_media() 方法获取
                created_at      int             媒体文件上传时间戳（单位：秒）

        """
        url = "https://api.weixin.qq.com/cgi-bin/media/upload"

        if file_url:
            res = requests.get(file_url, headers={'content-type': 'image/jpeg'})
            file = res.content

        params = self.check_params(
            access_token=self.access_token,
            type=file_type
        )
        return self.file_post(url, file_name, file, params=params)

    def get_media(self, media_id, file_path_name=None):
        """
        获取临时素材接口

        该接口提供保存到本地文件，供测试使用。传入绝对路径名称，可保存到文件，如：file_path_name="/Users/mjinnn/Desktop/aaa.jpg"
        官方文档：https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Get_temporary_materials.html

        详细文档请参考：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/img/img.superresolution.html

        :param media_id: 媒体id
        :param file_path_name: 保存的文件路径名称（绝对路径或相对路径）
        :return: , 返回图片二进制，file_path_name不为None时 返回 ok
        """
        url = "https://api.weixin.qq.com/cgi-bin/media/get"

        params = self.check_params(
            access_token=self.access_token,
            media_id=media_id,
        )
        content = self.get(url, params=params, content_type="media")
        # 保存文件
        if file_path_name:
            fo = open(file_path_name, 'wb')
            fo.write(content)
            fo.close()
            return "ok"

        return content

    # 永久素材：

    def uploadimg_media(self, file_name: str, file_url: str = None, file: bytes = None, file_type: str = "image"):
        """
        新增永久素材
        对于常用的素材，开发者可通过本接口上传到微信服务器，永久使用。新增的永久素材也可以在公众平台官网素材管理模块中查询管理。

        官方文档url： https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Adding_Permanent_Assets.html

        :param file_name: [必填] 文件名称
        :param file_url: [选填] 文件url，通过url获取文件并上传
        :param file: [选填] 二进制文件，通过二进制文件上传（url、file二选一）
        :param file_type: [默认image] 媒体文件类型，分别有图片（image）、语音（voice）、视频（video）和缩略图（thumb）
        :return: 返回request

            属性              类型              说明
            url             string          上传图片的URL

        """
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"

        if file_url:
            res = requests.get(file_url, headers={'content-type': 'image/jpeg'})
            file = res.content

        params = self.check_params(
            access_token=self.access_token,
            type=file_type
        )
        return self.file_post(url, file_name, file, params=params)

    def get_material(self, media_id: str, file_path_name: str = None):
        """
        获取永久素材接口

        该接口提供保存到本地文件，测试可使用。传入绝对路径+名称或相对路径+名称，可保存文件，如：file_path_name="/Users/mjinnn/Desktop/aaa.jpg"

        详细文档请参考：
        https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Getting_Permanent_Assets.html

        :param media_id: 媒体id
        :param file_path_name: 保存的文件路径名称（绝对路径或相对路径）
        :return: 返回图片二进制，file_path_name不为None时 返回 ok
        """
        url = "https://api.weixin.qq.com/cgi-bin/material/get_material"

        params = self.check_params(
            access_token=self.access_token,
        )
        data = self.check_params(
            media_id=media_id,
        )
        content = self.post(url, params=params, data=data, content_type="auto")
        # 保存文件
        if file_path_name and isinstance(content, bytes):
            fo = open(file_path_name, 'wb')
            fo.write(content)
            fo.close()
            return "ok"

        return content

    def del_material(self, media_id: str):
        """
        删除永久素材接口

        详细文档请参考：
        https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Deleting_Permanent_Assets.html

        :param media_id: 媒体id
        :return: WechatData类型
        """
        url = "https://api.weixin.qq.com/cgi-bin/material/del_material"

        params = self.check_params(
            access_token=self.access_token,
        )
        data = self.check_params(
            media_id=media_id,
        )
        return self.post(url, params=params, data=data, content_type="json")

    def get_material_count(self):
        """
        获取永久素材总数

        详细文档请参考：
        https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Get_the_total_of_all_materials.html

        :return: WechatData类型
            属性              类型              说明
            voice_count     number          语音总数量
            video_count     number          视频总数量
            image_count     number          图片总数量
            news_count      number          图文总数量

        """
        url = "https://api.weixin.qq.com/cgi-bin/material/get_materialcount"

        params = self.check_params(access_token=self.access_token)
        return self.post(url, params=params)

    def batchget_material(self, file_type: str = "image", page: int = None, limit: int = None):
        """
        获取素材列表
        在新增了永久素材后，开发者可以分类型获取永久素材的列表。

        官方文档：https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Get_materials_list.html

        :param file_type: 素材的类型，图片（image）、视频（video）、语音 （voice）、图文（news）
        :param page: 页码（第几页）
        :param limit: 每页数量（限制1-20）
        :return: WeChatData类型，参数如下
            属性              类型              说明
            total_count     number          该类型的素材的总数
            item_count      number          本次调用获取的素材的数量
            item            list<obj>       列表数据


            item 对象【图片（image）、视频（video）、语音 （voice）类型返回】：
                media_id        string          媒体id
                name            string          文件名称
                update_time     number          这篇图文消息素材的最后更新时间（时间戳）
                url             string          图文页的URL，或者，当获取的列表是图片素材列表时，该字段是图片的URL


            item 对象【图文（news）类型返回数据】：
                属性              类型              说明
                media_id        string          媒体id
                content         objects         内容
                update_time     number          这篇图文消息素材的最后更新时间（时间戳）

                content 对象：
                    属性                  类型              说明
                    title               string          图文消息的标题
                    thumb_media_id      string          图文消息的封面图片素材id（必须是永久mediaID）
                    show_cover_pic      number          是否显示封面，0为false，即不显示，1为true，即显示
                    author	            string          作者
                    digest              string          图文消息的摘要，仅有单图文消息才有摘要，多图文此处为空
                    content             string          图文消息的具体内容，支持 HTML 标签，必须少于2万字符，小于1M，且此处会去除JS
                    url                 string          图文页的URL，或者，当获取的列表是图片素材列表时，该字段是图片的URL
                    content_source_url	string          图文消息的原文地址，即点击“阅读原文”后的URL

        """
        url = "https://api.weixin.qq.com/cgi-bin/material/batchget_material"
        if not page or page < 1:
            page = 1
        if not limit or limit < 1:
            limit = 10

        params = self.check_params(
            access_token=self.access_token,
        )

        data = self.check_params(
            type=file_type,
            offset=limit * (page - 1),
            count=limit
        )

        content = self.post(url, params=params, data=data)

        return content

from py_wechat_tools.libs.tools import WeChatBase


class Ocr(WeChatBase):

    def bankcard(self, img_url=None, img=None):
        """
        提供基于小程序的银行卡 OCR 识别

        该接口需要购买，如果报错 101003 可以打开下面的链接购买，有免费的100/天，测试够用了
        https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/ocr/ocr.bankcard.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数。
        :param img: form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。
        :return: 返回 WeChatData 类型 返回信息：
                属性              类型              说明
                number	        number	        银行卡号（id）

        """
        url = "https://api.weixin.qq.com/cv/ocr/bankcard"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url,
        )
        data = self.check_params(
            img=img
        )

        return self.post(url, params=params, data=data)

    def business_license(self, img_url=None, img=None):
        """
        营业执照 OCR 识别

        该接口需要购买，如果报错 101003 可以打开下面的链接购买，有免费的100/天，测试够用了
        https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/ocr/ocr.businessLicense.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数。
        :param img: form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。
        :return: 返回 WeChatData 类型 返回信息：
                属性	                    类型	                说明
                errcode                 string              错误码
                errmsg	                string	            错误信息
                reg_num	                string	            注册号
                serial	                string	            编号
                legal_representative    string	            法定代表人姓名
                enterprise_name	        string	            企业名称
                type_of_organization	string	            组成形式
                address	                string	            经营场所/企业住所
                type_of_enterprise	    string	            公司类型
                business_scope	        string	            经营范围
                registered_capital	    string	            注册资本
                paid_in_capital	        string	            实收资本
                valid_period	        string	            营业期限
                registered_date	        string	            注册日期/成立日期
                cert_position	        string	            营业执照位置
                img_size	            string	            图片大小
        """
        url = "https://api.weixin.qq.com/cv/ocr/bizlicense"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url,
        )
        data = self.check_params(
            img=img
        )

        return self.post(url, params=params, data=data)

    def driver_license(self, img_url=None, img=None):
        """
        驾驶证 OCR 识别

        效果一般，有个别字识别错误。还是比较清晰的文字
        该接口需要购买，如果报错 101003 可以打开下面的链接购买，有免费的100/天，测试够用了
        https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/ocr/ocr.driverLicense.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数。
        :param img: form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。
        :return: 返回 WeChatData 类型 返回信息：
                属性              类型              说明
                errcode	        string	        错误码
                errmsg	        string	        错误信息
                id_num	        string	        证号
                name	        string	        姓名
                sex	            string	        性别
                address	        string	        地址
                birth_date	    string	        出生日期
                issue_date	    string	        初次领证日期
                car_class	    string	        准驾车型
                valid_from	    string	        有效期限起始日
                valid_to	    string	        有效期限终止日
                official_seal	string	        印章文构
        """
        url = "https://api.weixin.qq.com/cv/ocr/drivinglicense"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url,
        )
        data = self.check_params(
            img=img
        )

        return self.post(url, params=params, data=data)

    def vehicle_license(self, img_url=None, img=None):
        """
        行驶证 OCR 识别

        该接口需要购买，如果报错 101003 可以打开下面的链接购买，有免费的100/天，测试够用了
        https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/ocr/ocr.vehicleLicense.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数。
        :param img: form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。
        :return: 返回 WeChatData 类型 返回信息：
                属性                              类型              说明
                errcode	                        string	        错误码
                errmsg	                        string	        错误信息
                vehicle_type	                string	        车辆类型
                owner	                        string	        所有人
                addr	                        string	        住址
                use_character	                string	        使用性质
                model	                        string	        品牌型号
                vin	                            string	        车辆识别代
                engine_num	                    string	        发动机号码
                register_date	                string	        注册日期
                issue_date	                    string	        发证日期
                plate_num_b	                    string	        车牌号码
                record	                        string	        号牌
                passengers_num	                string	        核定载人数
                total_quality	                string	        总质量
                totalprepare_quality_quality	string	        整备质量
        """
        url = "https://api.weixin.qq.com/cv/ocr/driving"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url,
        )
        data = self.check_params(
            img=img
        )

        return self.post(url, params=params, data=data)

    def idcard(self, img_url=None, img=None):
        """
        身份证 OCR 识别

        该接口需要购买，如果报错 101003 可以打开下面的链接购买，有免费的100/天，测试够用了
        https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/ocr/ocr.idcard.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数。
        :param img: form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。
        :return: 返回 WeChatData 类型 返回信息：
                属性              类型              说明
                errcode	        string	        错误码
                errmsg	        string	        错误信息
                type	        string	        正面或背面，Front / Back

                # 背面返回字段
                valid_date	    string	        有效期

                # 正面返回字段
                name	        string	        姓名
                id	            string	        证号
                addr	        string	        地址
                gender	        string	        性别
                nationality	    string	        民族
        """
        url = "https://api.weixin.qq.com/cv/ocr/idcard"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url,
        )
        data = self.check_params(
            img=img
        )

        return self.post(url, params=params, data=data)

    def printed_text(self, img_url=None, img=None):
        """
        通用印刷体 OCR 识别

        该接口需要购买，如果报错 101003 可以打开下面的链接购买，有免费的100/天，测试够用了
        https://fuwu.weixin.qq.com/service/detail/000ce4cec24ca026d37900ed551415

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/ocr/ocr.printedText.html

        :param img_url: 要检测的图片 url，传这个则不用传 img 参数。
        :param img: form-data 中媒体文件标识，有filename、filelength、content-type等信息，传这个则不用传 img_url。
        :return: 返回 WeChatData 类型 返回信息：
                属性              类型              说明
                items           array           识别结果
                img_size        objects         图片大小

            items:
                属性              类型              说明
                text            string          识别到的文本
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
        url = "https://api.weixin.qq.com/cv/ocr/comm"

        params = self.check_params(
            access_token=self.access_token,
            img_url=img_url,
        )
        data = self.check_params(
            img=img
        )

        return self.post(url, params=params, data=data)

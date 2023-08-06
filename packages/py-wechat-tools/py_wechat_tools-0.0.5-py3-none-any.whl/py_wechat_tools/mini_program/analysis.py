import calendar
import datetime

from py_wechat_tools.libs.tools import dict2obj, WeChatBase

# TODO 待完善接口
"""
往下：
https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/data-analysis/analysis.getPerformanceData.html
"""


class Analysis(WeChatBase):

    def get_retain(self, begin_date, end_date, url):

        params = self.check_params(access_token=self.access_token)
        data = self.check_params(begin_date=begin_date, end_date=end_date)

        result = self.post(url, params=params, data=data)

        return result

    @staticmethod
    def get_month_last_day(month_start):
        """
        获取月份的最后一天
        :param month_start: 月份随便一天 格式：yyyymmdd
        :return: 月份的最后一天 格式：yyyymmdd
        """
        date = datetime.datetime.strptime(month_start, "%Y%m%d")
        week_day, month_count_day = calendar.monthrange(date.year, date.month)
        end_date = datetime.date(date.year, date.month, month_count_day).strftime("%Y%m%d")
        return end_date

    @staticmethod
    def get_sunday_date(sunday_date):
        """
        获取周日日期
        :param sunday_date: 周一的日期 格式：yyyymmdd
        :return: 周日日期 格式：yyyymmdd
        """
        end_date = datetime.datetime.strptime(sunday_date, "%Y%m%d") + datetime.timedelta(days=6)
        end_date = end_date.strftime("%Y%m%d")
        return end_date

    def get_daily_retain(self, begin_date, end_date=None):
        """
        获取用户访问小程序日留存

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/data-analysis/visit-retain/analysis.getDailyRetain.html

        :param begin_date: 开始日期 格式：20220101
        :param end_date: 结束日期，限定查询1天数据，允许设置的最大值为昨日 格式：20220101。不传时默认与开始日期相同
        :return: 返回 WeChatData类型
                属性                  类型              说明
                ref_date	        string          日期
                visit_uv_new	    WechatData      新增用户留存
                visit_uv	        WechatData      活跃用户留存

            visit_uv_new 的结构
                属性	                  类型	           说明
                key                 number	        标识，0开始，表示当天，1表示1天后。依此类推，key取值分别是：0,1,2,3,4,5,6,7,14,30
                value	            number	        key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）

            visit_uv 的结构
                属性	                类型	                说明
                key	                number	        标识，0开始，表示当天，1表示1天后。依此类推，key取值分别是：0,1,2,3,4,5,6,7,14,30
                value	            number          key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）

        """
        url = "https://api.weixin.qq.com/datacube/getweanalysisappiddailyretaininfo"
        return self.get_retain(begin_date, end_date or begin_date, url)

    def get_monthly_retain(self, begin_date, end_date=None):
        """
        获取用户访问小程序月留存

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/data-analysis/visit-retain/analysis.getMonthlyRetain.html

        :param begin_date: 开始日期，必须为每个月的第一天，格式：20220101
        :param end_date: [选填]结束日期，必须为每个月的最后一天，默认为当月最后一天，格式：20220131
        :return:  返回 WeChatData类型
                属性                  类型              说明
                ref_date	        string          日期
                visit_uv_new	    WechatData      新增用户留存
                visit_uv	        WechatData      活跃用户留存

            visit_uv_new 的结构
                属性	                  类型	           说明
                key                 number	        标识，0开始，表示当月，1表示1月后。key取值分别是：0,1
                value	            number	        key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）

            visit_uv 的结构
                属性	                类型	                说明
                key	                number	        标识，0开始，表示当月，1表示1月后。key取值分别是：0,1
                value	            number          key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）

        """
        url = "https://api.weixin.qq.com/datacube/getweanalysisappidmonthlyretaininfo"

        if end_date is None:
            end_date = self.get_month_last_day(begin_date)

        return self.get_retain(begin_date, end_date, url)

    def get_weekly_retain(self, begin_date, end_date=None):
        """
        获取用户访问小程序周留存

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/data-analysis/visit-retain/analysis.getWeeklyRetain.html

        :param begin_date: 开始日期，为周一日期。 格式：yyyymmdd
        :param end_date: 结束日期，为周日日期，限定查询一周数据。 格式：yyyymmdd
        :return:  WeChatData 返回信息
                属性                  类型              说明
                ref_date	        string          日期
                visit_uv_new	    WechatData      新增用户留存
                visit_uv	        WechatData      活跃用户留存

            visit_uv_new 的结构
                属性	                  类型	           说明
                key                 number	        标识，0开始，表示当周，1表示1周后。依此类推，取值分别是：0,1,2,3,4
                value	            number	        key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）

            visit_uv 的结构
                属性	                类型	                说明
                key	                number	        标识，0开始，表示当周，1表示1周后。依此类推，取值分别是：0,1,2,3,4
                value	            number          key对应日期的新增用户数/活跃用户数（key=0时）或留存用户数（k>0时）

        """
        url = "https://api.weixin.qq.com/datacube/getweanalysisappidweeklyretaininfo"

        if not end_date:
            end_date = self.get_sunday_date(begin_date)

        return self.get_retain(begin_date, end_date, url)

    def get_daily_summary(self, begin_date, end_date=None):
        """
        获取用户访问小程序数据概况

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/data-analysis/analysis.getDailySummary.html

        :param begin_date: 开始日期 格式：20220101
        :param end_date: 结束日期，限定查询1天数据，允许设置的最大值为昨日。格式 20220101。不传时默认与开始日期相同
        :return:  WeChatData 返回信息
                属性                  类型              说明
                list	            Array           数据列表

            list 的结构
                属性	                  类型	           说明
                ref_date	        string	        日期，格式为 yyyymmdd
                visit_total	        number	        累计用户数
                share_pv	        number	        转发次数
                share_uv	        number	        转发人数

        """
        url = "https://api.weixin.qq.com/datacube/getweanalysisappiddailysummarytrend"

        return self.get_retain(begin_date, end_date or begin_date, url)

    def get_daily_visit_trend(self, begin_date, end_date=None):
        """
        获取用户访问小程序数据日趋势

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/data-analysis/visit-trend/analysis.getDailyVisitTrend.html

        :param begin_date: 开始日期。格式为 yyyymmdd
        :param end_date: 结束日期，限定查询1天数据，允许设置的最大值为昨日。格式为 yyyymmdd。不传时默认与开始日期相同
        :return:   WeChatData 返回信息
                属性                  类型              说明
                list	            Array           数据列表

            list 的结构
                属性	                  类型	           说明
                ref_date	        string	        日期，格式为 yyyymmdd
                session_cnt	        number	        打开次数
                visit_pv	        number	        访问次数
                visit_uv	        number	        访问人数
                visit_uv_new	    number	        新用户数
                stay_time_uv	    number	        人均停留时长 (浮点型，单位：秒)
                stay_time_session	number	        次均停留时长 (浮点型，单位：秒)
                visit_depth	        number	        平均访问深度 (浮点型)

        """
        url = "https://api.weixin.qq.com/datacube/getweanalysisappiddailyvisittrend"

        return self.get_retain(begin_date, end_date or begin_date, url)

    def get_monthly_visit_trend(self, begin_date, end_date):
        """
        获取用户访问小程序数据月趋势(能查询到的最新数据为上一个自然月的数据)

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/data-analysis/visit-trend/analysis.getMonthlyVisitTrend.html

        :param begin_date: 开始日期，为自然月第一天。格式为 yyyymmdd
        :param end_date: 结束日期，为自然月最后一天，限定查询一个月的数据。格式为 yyyymmdd
        :return: WeChatData 返回信息
                属性                  类型              说明
                list	            Array           数据列表

            list 的结构
                属性	                  类型	           说明
                ref_date	        string	        时间，格式为 yyyymm，如："201702"
                session_cnt	        number	        打开次数（自然月内汇总）
                visit_pv	        number	        访问次数（自然月内汇总）
                visit_uv	        number	        访问人数（自然月内去重）
                visit_uv_new	    number	        新用户数（自然月内去重）
                stay_time_uv	    number	        人均停留时长 (浮点型，单位：秒)
                stay_time_session	number	        次均停留时长 (浮点型，单位：秒)
                visit_depth	        number	        平均访问深度 (浮点型)
        """
        url = "https://api.weixin.qq.com/datacube/getweanalysisappidmonthlyvisittrend"

        if end_date is None:
            end_date = self.get_month_last_day(begin_date)
        return self.get_retain(begin_date, end_date, url)

    def get_weekly_visit_trend(self, begin_date, end_date=None):
        """
        获取用户访问小程序数据周趋势

        官方文档：
        https://developers.weixin.qq.com/miniprogram/dev/api-backend/open-api/data-analysis/visit-trend/analysis.getWeeklyVisitTrend.html

        :param begin_date: 开始日期，为周一日期。格式为 yyyymmdd
        :param end_date: 结束日期，为周日日期，限定查询一周数据。格式为 yyyymmdd
        :return: WeChatData 返回信息
                属性                  类型              说明
                list	            Array           数据列表

            list 的结构
                属性	                  类型	           说明
                ref_date	        string	        时间，格式为 yyyymmdd-yyyymmdd，如："20170306-20170312"
                session_cnt	        number	        打开次数（自然周内汇总）
                visit_pv	        number	        访问次数（自然周内汇总）
                visit_uv	        number	        访问人数（自然周内去重）
                visit_uv_new	    number	        新用户数（自然周内去重）
                stay_time_uv	    number	        人均停留时长 (浮点型，单位：秒)
                stay_time_session	number	        次均停留时长 (浮点型，单位：秒)
                visit_depth	        number	        平均访问深度 (浮点型)

        """
        url = "https://api.weixin.qq.com/datacube/getweanalysisappidweeklyvisittrend"

        if end_date is None:
            end_date = self.get_sunday_date(begin_date)

        return self.get_retain(begin_date, end_date, url)

# -*- 编码: utf-8 -*-
# 由 @嗷呜
导入系统模块
sys.path.append('..')
从 base.spider 导入 Spider
导入requests


类蜘蛛(蜘蛛):

    def init(self, extend=""):
        通过

    def getName(self):
        return "hitv"

    def isVideoFormat(self, url):
        通过

    def manualVideoCheck(self):
        通过

    def destroy(self):
        通过

    def homeContent(self, filter):
        result = {}
        cateManual = {
            # "直播": "live",
            '排行榜': '排名',
            "电影": "1",
            "剧集": "2",
            "综艺": "3",
            "动画": "4",
            "短片": "5"
        }
        classes = []
        对于 k 在 cateManual:
            classes.append({
                'type_name': k,
                'type_id': cateManual[k]
            })
        result['class'] = classes
        返回结果

    host = "https://wys.upfuhn.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/80.0.3987.149 Safari/537.36"
    }

    def 列表(self, 列表):
        videos = []
        对于列表中的it：
            videos.append({
                "vod_id": it['video_site_id'],
                "vod_name": it['video_name'],
                "vod_pic": it['video_horizontal_url'] or it['video_vertical_url'],
                "vod_remarks": it['newest_series_num'],
                "vod_year": it['years'],
            })
        返回视频

    def homeVideoContent(self):
        url = f'/{self.host}/v1/ys_videoSites/hot?t=1'
        data = requests.get(url, headers=self.headers).json()
        videos = self.list(data['data']['data'])
        result = {'列表': 视频}
        返回结果

    def categoryContent(self, tid, pg, filter, extend):

        path = f'/v1/ys_videoSites?t={tid}&s_t=0&a&y&o=0&ps=21&pn={pg}'
        排名 = False
        if tid == 'rank':
            if pg == 1:
                path = f'/v1/ys_videoSites/ranking'
                排名 = True
            否则:
                path = ''
        # elif tid == 'live' and pg == 1:
        #     path = f'/v1/ys_live_tvs'
        videos = []
        result = {}
        尝试:
            data = requests.get(self.host + path, headers=self.headers).json()
            如果排名：
                对于 data['data'] 中的视频：
                    videos.extend(data['data'][video])
            否则:
                videos = data['data']['data']
            result = {}
            result['list'] = self.list(videos)
            result['page'] = pg
            result['pagecount'] = 9999
            result['limit'] = 90
            result['total'] = 999999
        例外:
            result['list'] = []
        返回结果

    def detailContent(self, ids):
        tid = ids[0]
        url = f'/{self.host}/v1/ys_video_series/by_vid/{tid}'
        data = requests.get(url, headers=self.headers).json()
        data1 = data['data']['ys_video_site']
        urls = []
        对于 data['data']['data'] 中的 it：
            urls.append(it['系列编号'] + '$' + it['视频链接'])
        vod = {
            'vod_name': data1['video_name'],
            'type_name': data1['tag'],
            'vod_year': data1['years'],
            'vod_area': data1['area'],
            'vod_director': data1['main_actor'],
            'vod_content': data1['video_desc'],
            'vod_play_from': '在线播放',
            'vod_play_url': '#'.join(urls),
        }
        结果 = {
            'list': [
                水
            ]
        }
        返回结果

    def searchContent(self, key, quick, pg=1):
        url = f'/{self.host}/v1/ys_video_sites/search?s={key}&o=0&ps=200&pn={pg}'
        data = requests.get(url, headers=self.headers).json()
        videos = data['data']['video_sites']
        if data['data']['first_video_series'] is not None:
            videos = [data['data']['first_video_series']] + videos
        result = {}
        result['list'] = self.list(videos)
        result['page'] = pg
        返回结果

    def playerContent(self, flag, id, vipFlags):
        结果 = {
            'url': id,
            '解析': 0,
            'header': self.headers
        }
        返回结果

    def localProxy(self, param):
        通过
Google 翻译
原文
提供更好的翻译建议

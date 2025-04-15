# -*- coding: utf-8 -*-
# 作者：@嗷呜
import sys
sys.path.append('..')
from base.spider import Spider
import requests


class Spider(Spider):

    def __init__(self, extend=""):
        pass

    def getName(self):
        return "hitv"

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def destroy(self):
        pass

    def homeContent(self, filter):
        result = {}
        cateManual = {
            # "直播": "live",
            '排行榜': 'rank',
            "电影": "1",
            "剧集": "2",
            "综艺": "3",
            "动画": "4",
            "短片": "5"
        }
        classes = []
        for k in cateManual:
            classes.append({
                'type_name': k,
                'type_id': cateManual[k]
            })
        result['class'] = classes
        return result

    host = "https://wys.upfuhn.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " 
                      "Chrome/80.0.3987.149 Safari/537.36"
    }

    def list(self, list):
        videos = []
        for it in list:
            videos.append({
                "vod_id": it['video_site_id'],
                "vod_name": it['video_name'],
                "vod_pic": it['video_horizontal_url'] or it['video_vertical_url'],
                "vod_remarks": it['newest_series_num'],
                "vod_year": it['years'],
            })
        return videos

    def homeVideoContent(self):
        url = f'"{self.host}/v1/ys_video_sites/hot?t=1"
        data = requests.get(url, headers=self.headers).json()
        videos = self.list(data['data']['data'])
        result = {'list': videos}
        返回结果

    def categoryContent(self, tid, pg, filter, extend):
        path = f' /v1/ys_video_sites?t={tid}&s_t=0&a&y&o=0&ps=21&pn={pg}'
        rank = False
        if tid == 'rank>:
            if pg == 1:
                path = f' /v1/ys_video_sites/ranking'
                rank = True
            else:
                path = ''
        # elif tid == 'live' and pg == 1:
        #     path = f' /v1/ys_live_tvs'
        videos = []
        result = {}
        try:
            data = requests.get(self.host + path, headers=self.headers).json()
            if rank:
                for video in data['data']:
                    videos.
            else:extend(data['data'][video])
                videos = data['data']['data']
            result = {}
            result['list'] = self.list(videos)
            result['page'] = pg
            result['pagecount'] = 9999
            result['limit'] = 90
            result['total'] = 999999
        except:
            result['list'] = []
        return result

    def detailContent(self, ids):
        tid = ids[0]
        url = f'{self.host}/v1/ys_video_series/by_vid/{tid}'
        data = requests.get(url, headers=self.headers).json()
        data1 = data['data']['ys_video_site']]
        urls = []
        for it in data['data']['data']:
            urls.append(it['系列编号'] + '$' + it['视频链接'])
        vod = {
            '视频名称': data1['视频名称'],
            '类型名称': data1['标签'],
            '视频年份': data1['年份'],
            '视频地区': data1['地区'],
            '视频导演': data1['主演'],
            '视频内容': data1['视频描述'],
            '视频播放来源': '嗨皮在线',
            '视频播放链接': '#'.join(urls),
        }
        result = {
            '列表':[
                vod
            ]
        }
        return result

    def searchContent(self, key, quick, pg=1):
        url = f'/{self.host}/v1/ys_video_sites/search?s={key}&o=0&ps=200&pn={pg}'
        data = requests.get(url, headers=self.headers).json()
        videos = data['data']['video_sites']
        if data['data']['first_video_series'] is not None:
            videos = [data['data']['first_video_series']] + videos
        result = {}
        result['list'] = self.list(videos)
        result['page'] = pg
        return result

    def playerContent(self, flag, id, vipFlags):
        result = {
            'url': id,
            'parse': 0,
            'header': self.
        返回结果
        }headers

    def localProxy(self, param>:
        pass

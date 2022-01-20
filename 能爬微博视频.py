import requests
url = 'https://weibo.com/tv/api/component?page=%2Ftv%2Fshow%2F1034%3A4725864357888081'
data = {'data': '{"Component_Play_Playinfo":{"oid":"1034:4725864357888081"}}'}
headers = {
    'cookie': 'SUB=_2AkMWuJ0Gf8NxqwJRmP0dz2rjZY5yygjEieKg5GzdJRMxHRl-yT9jqmoItRB6PTiz6YRoPNuQmhnFjCsRR3eR7yuHqwKD; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFpzJ55kj15F0Txa3TCNWE.; SINAGLOBAL=3400756052629.177.1642336817708; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; _s_tentry=-; Apache=9992151456252.889.1642641806570; ULV=1642641806648:3:3:3:9992151456252.889.1642641806570:1642488693713; XSRF-TOKEN=fI_JWAxlLT4TaBSe9lVP_Lqf; WBPSESS=a_YZA6I5qCR3U8i3Rfvlpp4O4vRhTMjBcq8WcoQvWqSOLzgAqPD_v48xdKHPDw2gtPIZhqAoMa314yTQfllHxTc0qWssWIiWQ6WMZS8yv2EYae1hx2MpXxGJb5m4q4tt5swZWQ1i0PJO89JXmK_57EAKnS3QD_pEHzrIxYlVr_I=',
    'referer': 'https://weibo.com/tv/show/1034:4725864357888081?mid=4725866133196408',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


json_data = requests.post(url=url,data=data,headers=headers).json()
video_url = 'https:' + json_data['data']['Component_Play_Playinfo']['urls']['高清 1080P']
video_data = requests.get(video_url).content
with open('video\\1.MP4','wb')as f:
    f.write(video_data)
print('视频爬取好啦！')


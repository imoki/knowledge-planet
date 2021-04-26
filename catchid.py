import requests

urlpath = '.\cookie_and_url.txt'

def catch(cookie):
	headers = {
	'Host': 'api.zsxq.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate',
	'X-Request-Id': 'd9b9b252c-c873-e660-5251-d5c80304b2d',
	'X-Version': '2.4.0',
	'X-Signature': 'e353c32ffb7a7291cd0fe73fbaf6b6a86aecafb6',
	'X-Timestamp': '1619436281',
	'Origin': 'https://wx.zsxq.com',
	'DNT': '1',
	'Connection': 'close',
	'Referer': 'https://wx.zsxq.com/dweb2/index/group',
	'Cookie': cookie,
	'Cache-Control': 'no-cache',
	}
	
	url = ' https://api.zsxq.com/v2/groups/unread_topics_count'
	reply = requests.get(url,headers=headers)
	j = reply.json()
	groups = j['resp_data']['groups']
	with open(urlpath,'a+',encoding='utf-8') as f:
		for id in groups:
			print(id['group_id'])
			f.write(str(id['group_id']) + '\n')
	

if __name__ == '__main__':
	with open(urlpath,'r',encoding='utf-8') as f:
		cookie = f.readline().strip()
	catch(cookie)
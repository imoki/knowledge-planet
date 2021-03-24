import json
import uuid
import time
import urllib
import requests
import json

urlpath = '.\cookie_and_url.txt'

def downUrl(down_url):
	headers = {
	'Host': 'api.zsxq.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate',
	'X-Request-Id': '0b44e51b8-b053-7934-8e13-05d0edba8ba',
	'X-Version': '1.10.50',
	'X-Signature': '9baaf7560520490f686ffd04161e3ee656db8dcd',
	'X-Timestamp': '1609233376',
	'Origin': 'https://wx.zsxq.com',
	'DNT': '1',
	'Connection': 'close',
	'Referer': 'https://wx.zsxq.com/dweb2/index/files',
	'Cookie': cookie
	}

	downheaders = {
	'Host': 'api.zsxq.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Accept-Encoding': 'gzip, deflate',
	'DNT': '1',
	'Connection': 'close',
	'Cookie': cookie,
	'Upgrade-Insecure-Requests': '1',
	'Cache-Control': 'max-age=0'
	}

	reply = requests.get(down_url, headers=headers)
	j = reply.json()
	fileids = j['resp_data']['files']
	length = len(fileids)
	try:
		endtime = fileids[19]['file']['create_time']
		print(endtime)
	except:
		pass
	for fileid in fileids:
		id = fileid['file']['file_id']
		title = fileid['file']['name']
		createtime = fileid['file']['create_time']
		print(str(title) + ':' + str(id))
		fdownloadurl = 'https://api.zsxq.com/v1.10/files/' + str(id) + '/download_url'
		downloadurl_tmp2 = requests.get(fdownloadurl, headers = downheaders)
		downloadurl_tmp = downloadurl_tmp2.json()
		downloadurl = downloadurl_tmp['resp_data']['download_url']
		download = requests.get(downloadurl)
		try:
			with open('.\\pdf\\' + title,'wb') as fp:
				fp.write(download.content)
				fp.close()
		except:
			pass
		try:
			with open('.\\log.txt','a+',encoding = 'utf-8') as flog:
				flog.write("TIME:" + createtime + '\n')
				flog.write(title + ':' + str(id) + '\n')
				flog.write("DOWNURL:" + downloadurl + '\n')
				flog.close()
		except:
			pass
	if length == 20:
		url_encode = urllib.parse.quote(endtime)
		next_url = down_url + '&end_time=' + str(url_encode)
		downUrl(next_url)
	

if __name__ == '__main__':
	'''
	print("请输入url：（例如：https://api.zsxq.com/v1.10/groups/51281152281444/files?count=20）")
	url = input()
	print("请输入cookie：（例如：abtest_env=product; zsxq_access_token=00000000-6666-BBBB-FFFF-222222222222_8888888888888888）")
	cookie = input()
	'''
	with open(urlpath,'r',encoding='utf-8') as f:
		cookie = f.readline()
		lines = f.readlines()
		cookie = cookie.strip()
		for line in lines:
			url = line.strip()
			print(url)
			try:
				downUrl(url)
			except:
				pass
	f.close()


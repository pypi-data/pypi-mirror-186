# author: Reinan Br
# project: rocketlc
# LICENSE: BSDv3
# Date: dez31 02:54 2022
# About: a lib of scrapping for getting date and info from launch rocket's

from bs4 import BeautifulSoup as bs
import mechanicalsoup as mec
import time as tm


headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
            'connection': 'keep-alive', 'upgrade-insecure-requests': '1', 
#            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6'}



def past_launchs():

    url_past = 'https://www.rocketlaunch.live/?pastOnly=1'

    br = mec.StatefulBrowser()
    br.session.headers = headers
    br.session.headers.update(headers)

    url_html = br.get(url_past)
    url_html = url_html.text
    canaveral = bs(url_html,features="html.parser")
    base_launch = canaveral.find('div',{'class':'launchloop'})

    divs = base_launch.find_all('div')

    rockets = []
    time_init = tm.time()
    for div in divs:
        if ('row' in div['class']) and ('launch' in div['class']):
            #print(div)
            date = div.find('div',{'class':'launch_date'}).text
            time = div.find('div',{'class':'launch_time'}).text
            rocket_name = div.find('div',{'class':'rlt-vehicle'}).text
            mother_rocket = div.find('div',{'class':'rlt-provider'}).text
            loc_launch = div.find('div',{'class':'rlt-location'}).text
            mission = div.find('div',{'class':'mission_name'}).text

            if mother_rocket=='SpaceX':
                rocket_series = div.find('div',{'class':'launch_tag'}).text
            else:
                rocket_series = None

            rocket = {'mission':mission.replace('\n',''),
                      'date_launch':date.replace('\n',''),
                      'time_launch':time.replace('\n',''),
                      'name':rocket_name.replace('\n',''),
                      'empire':mother_rocket.replace('\n',''),
                      'location':loc_launch.replace('\n',''),
                      'series':rocket_series}
            rockets.append(rocket)
    ping = tm.time() - time_init
    len_videos = len(rockets)
    return {'ping':ping,'len_videos':len_videos,'rockets':rockets}






def future_launchs():

    url_past = 'https://www.rocketlaunch.live/'

    br = mec.StatefulBrowser()
    br.session.headers = headers
    br.session.headers.update(headers)

    url_html = br.get(url_past)
    url_html = url_html.text
    canaveral = bs(url_html,features="html.parser")
    base_launch = canaveral.find('div',{'class':'launchloop'})

    divs = base_launch.find_all('div')

    rockets = []
    time_init = tm.time()
    for div in divs:
        try:
            if ('row' in div['class']) and ('launch' in div['class']):
                #print(div)
                date = div.find('div',{'class':'launch_date'}).text
                time = div.find('div',{'class':'launch_time'}).text
                rocket_name = div.find('div',{'class':'rlt-vehicle'}).text
                mother_rocket = div.find('div',{'class':'rlt-provider'}).text
                loc_launch = div.find('div',{'class':'rlt-location'}).text
                mission = div.find('div',{'class':'mission_name'}).text

                if mother_rocket=='SpaceX':
                    rocket_series = div.find('div',{'class':'launch_tag'}).text
                else:
                    rocket_series = None

                rocket = {'mission':mission.replace('\n',''),
                        'date_launch':date.replace('\n',''),
                        'time_launch':time.replace('\n',''),
                        'name':rocket_name.replace('\n',''),
                        'empire':mother_rocket.replace('\n',''),
                        'location':loc_launch.replace('\n',''),
                        'series':rocket_series}
                rockets.append(rocket)
        except:
            pass

    ping = tm.time() - time_init
    len_videos = len(rockets)
    return {'ping':ping,'len_videos':len_videos,'rockets':rockets}
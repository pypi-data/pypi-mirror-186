

from bs4 import BeautifulSoup as bs
import mechanicalsoup as mec
import cssutils as css
import time as tm


headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36(KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
            'connection': 'keep-alive', 'upgrade-insecure-requests': '1', 
#            'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'pt-BR,pt-PT;q=0.9,pt;q=0.8,en-US;q=0.7,en;q=0.6'}

url_base = 'https://www.spacelaunchschedule.com'

br = mec.StatefulBrowser()
br.session.headers = headers
br.session.headers.update(headers)

def launchs(page_limit:int=2)-> list:
    p = 1
    rockets = []
    for i in range(page_limit):
        url = f'{url_base}/page/{p}/'
        url_html = br.get(url)
        url_html = url_html.text
        canaveral = bs(url_html,features="html.parser")
        div_mother = canaveral.find('div',{'class':'col-lg-8'})
        
        divs = div_mother.find_all('div')
        #print(divs)
        for dv in divs:
            if ('my-2' in dv['class']) and ('container' in dv['class']):
                name = dv.find('span',{'class':'mt-2'}).text
                mission = dv.find('h2',{'class':'h4'}).text.replace('\n','')
                mother = dv.find('h3',{'class':'h6'}).text
                time_lst = dv.find('time').text.split('\n')
                #print(time_lst,len(time_lst))
                loc = dv.find('div',{'class':'mb-0'}).text.replace('\n','')
                style_dv = dv.find('div',{'class':'launch-list-thumbnail'})['style']
                #print(style_dv)
                url_img = style_dv.split(':')[-1].split('url(')[-1].replace(')','').replace(';','').replace('//','')
                #img_url = css.parseStyle(style_dv)['background-image']
                #print(time_lst)
                if  'Projected To Launch' in time_lst:
                    date = time_lst[2]
                    hour = None
                else:
                    date = time_lst[0].split(',')[0]
                    hour = time_lst[0].split(',')[1]
                
                rocket = {'name':name,
                          'mission':mission,
                          'empire':mother,
                          'date':date,
                          'hour':hour,
                          'location':loc,
                          'img_url':url_img
                          }
                rockets.append(rocket)
                
            
        p = p+1
    
    return rockets
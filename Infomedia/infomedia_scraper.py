from string import Template
import requests


def get_infomedia_ids(location):
    url = "https://apps.infomedia.dk/mediearkiv/search/basicsearch"

    t = Template("{\"SelectedProjectId\":null,\"IsArticleIdSearch\":false,\"ProjectId\":null,\"SortOrder\":\"Relevance\",\"DisableSearch\":true,\"SearchClause\":{\"Text\":\"${location}\",\"Stem\":true,\"CaseSensitive\":false,\"SearchMethod\":1,\"SearchLocation\":0,\"ManagedIsNear\":false,\"IsNearSearchMethod\":false,\"AvailableSearchLocations\":[0,1,2,3]},\"HasActiveEntityFilter\":false,\"FilterSpecs\":{\"Media\":[]},\"CursorMark\":\"\",\"AbsoluteOffset\":0,\"PageSize\":1000,\"UniqueId\":\"636863604777932862\",\"SearchResultOptions\":{\"ReturnFacets\":false,\"ReturnArticles\":true,\"GroupOnHeading\":true},\"FacetSpecs\":{\"Media\":[],\"MediaBySourceType\":[],\"Organizations\":[],\"Places\":[],\"People\":[],\"MediaByRegion\":[],\"DateRange\":{\"From\":null,\"To\":null}},\"DrilldownSearchClauses\":[]}")
    payload = t.substitute(location=location)
    headers = {
        'Cookie': "_ga=GA1.2.770482877.1550587713; _cb_ls=1; _cb=CRKo9KBnpPS9OG_-_; Insight.Web.Ms.SessionId=vfi3xval3cvrkkkrlnczu4ao; _gid=GA1.2.385371364.1550749393; _cb_svref=null; ADRUM=s=1550760074771&r=https%3A%2F%2Fapps.infomedia.dk%2Fmediearkiv%2Flink%3F-1180778776; _gat=1; _chartbeat2=.1550587713786.1550760149435.101.Br1UK_gPbszZ6Be-BCcLGIDyrSoV.91; _chartbeat5=1165,267,https%3A%2F%2Fapps.infomedia.dk%2Fmediearkiv%2F,https%3A%2F%2Fapps.infomedia.dk%2Fmediearkiv%2F,Y8g8GCc5Jr1ClGR3GB12WxiDh5j0p,,c,fRADgB13WIBCX-avD0Ti0BCiAtHr,apps.infomedia.dk,",
        'Origin': "https://apps.infomedia.dk",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7,nb;q=0.6,de;q=0.5",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        'Content-Type': "application/json; charset=UTF-8",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Referer': "https://apps.infomedia.dk/mediearkiv/",
        'X-Requested-With': "XMLHttpRequest",
        'Connection': "keep-alive",
        'ADRUM': "isAjax:true",
        'cache-control': "no-cache",
        'Postman-Token': "a7cf42fc-9bfe-497a-8d27-c72f19d2dd71"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    log = open(location+'_infomedia_ids'+".txt", "w")
    for line in response.text.split(','):
        if 'Duid' in line:
            infomedia_id = line.split(':')[1].strip('"')
            print(infomedia_id)
            log.write(infomedia_id)
            log.write('\n')
    log.close()

with open('infomedia_locations.txt', 'r') as loc:
    for line in loc:
        print('scraping:', line)
        location = line.strip()
        get_infomedia_ids(location)
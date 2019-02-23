from string import Template
import requests
import json

def get_infomedia_article(id):
    url = "https://apps.infomedia.dk/mediearkiv/article/getarticlebodytext"

    t = Template("{\"ArticleId\":\"${id}\",\"BasicSearchFilter\":{\"SelectedProjectId\":null,\"IsArticleIdSearch\":false,\"ProjectId\":null,\"SortOrder\":\"Relevance\",\"DisableSearch\":true,\"SearchClause\":{\"Text\":\"valby\",\"Stem\":true,\"CaseSensitive\":false,\"SearchMethod\":1,\"SearchLocation\":0,\"ManagedIsNear\":false,\"IsNearSearchMethod\":false,\"AvailableSearchLocations\":[0,1,2,3]},\"HasActiveEntityFilter\":false,\"FilterSpecs\":{\"DateRange\":{\"From\":\"2019-01-22T23:00:00.000Z\",\"To\":\"2019-02-20T23:00:00.000Z\"},\"Media\":[]},\"CursorMark\":\"\",\"AbsoluteOffset\":0,\"PageSize\":10,\"UniqueId\":\"636863586231742631\",\"SearchResultOptions\":{\"ReturnFacets\":false},\"FacetSpecs\":{\"Media\":[],\"MediaBySourceType\":[],\"Organizations\":[],\"Places\":[],\"People\":[],\"MediaByRegion\":[],\"DateRange\":{\"From\":\"2019-01-22T23:00:00.000Z\",\"To\":\"2019-02-20T23:00:00.000Z\"}},\"DrilldownSearchClauses\":[]}}")
    payload = t.substitute(id=id)
    headers = {
        'Cookie': "_ga=GA1.2.770482877.1550587713; _cb_ls=1; _cb=CRKo9KBnpPS9OG_-_; Insight.Web.Ms.SessionId=vfi3xval3cvrkkkrlnczu4ao; _gid=GA1.2.385371364.1550749393; _cb_svref=null; ADRUM=s=1550758207357&r=https%3A%2F%2Fapps.infomedia.dk%2Fmediearkiv%3F0; _chartbeat2=.1550587713786.1550758224019.101.Br1UK_gPbszZ6Be-BCcLGIDyrSoV.38; _chartbeat5=363,299,https%3A%2F%2Fapps.infomedia.dk%2Fmediearkiv,https%3A%2F%2Fapps.infomedia.dk%2Fmediearkiv%2Flink%3Farticles%3De714035d,NfcopDSXBnHCMdpaXDD1okACk-uot,,c,BB2t6g5dtdgB5CwQDDvBzBTBE5Qy0,apps.infomedia.dk,; _gat=1",
        'Origin': "https://apps.infomedia.dk",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7,nb;q=0.6,de;q=0.5",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        'Content-Type': "application/json; charset=UTF-8",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Referer': "https://apps.infomedia.dk/mediearkiv",
        'X-Requested-With': "XMLHttpRequest",
        'Connection': "keep-alive",
        'ADRUM': "isAjax:true",
        'cache-control': "no-cache",
        'Postman-Token': "a800e0b3-eddd-4846-89e4-ca7c3a209528"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    try:
        text = json.loads(response.text).get('BodyText')
    except Exception:
        print('error on fetch')
        return None
    return text




with open('infomedia_locations.txt', 'r') as loc:
    for line in loc:
        print(line)
        count = 0
        log = open(line.strip() + '_infomedia_articles.txt', 'w')
        with open(line.strip() + '_infomedia_ids.txt', 'r') as ids:
            for id in ids:
                print(count)
                count += 1
                text = get_infomedia_article(id)
                if text:
                    log.write(text)
        log.close()
import requests
#写的很随意，凑合用吧..

# 定时 0 * * * *

#填入你的cookie↓↓↓
cookie=''

url = 'https://m.jingxi.com/jxbfd/user/ExchangePearlState?__t=1633304470814&strZone=jxbfd&dwExchangeType=undefined&_stk=__t%2CstrZone&_ste=1&h5st=20211004074110836%3B6043022618846161%3B10032%3Btk01wa2681be830nxLv%2BL14ezp%2FIzzHZj94Boaehq6gKHsQ1FxR8yuQXpXDUpW4TWPqN%2B4uI9G%2F7bMzOtpr%2F21r%2Fbwbl%3Bd0abe8d981852035d8296252646f83b49542d3275ed5e2de145f173c63c3adcf&_=1633304470840&sceneval=2&g_login_type=1&callback=jsonpCBKC&g_ty=ls'
header = {
        'Host':'m.jingxi.com',
        'user-agent':'jdpingou;android;5.6.0;11;5a527bc866ec0094;network/wifi;model/V2055A;appBuild/18771;partner/vivo01;;session/762;aid/5a527bc866ec0094;oaid/03ce5bbe994e3b80b0aaa431e6ecd1106a46cd5e10e5b0654ec7a2a601d9f3a3;pap/JA2019_3111789;brand/vivo;eu/5316532373263683;fv/6363563603039343;Mozilla/5.0 (Linux; Android 11; V2055A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36',
        'accept':'*/*',
        'Referer':'https://st.jingxi.com/fortune_island/index2.html?ptag=7155.9.47&sceneval=2',
        'cookie':cookie
    }
ret=requests.get(url=url,headers=header)
print(ret.text)

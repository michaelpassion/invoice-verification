import requests
import logging
import table, data
from datetime import datetime

logging = logging.basicConfig(level='DEBUG')

API_KEY = "yNCWPW4ImX2pGe2EnG5xAqoF"
SECRET_KEY = "XkVqZRs3siMGCYQqDYAMjBsupg4z81o4"
{
  "code": "011002301111",
  "number": "44917292",
  "issue_date": "20231127",
  "check_code": "350289",
  "subtotal_amount": "108.30"
}

def get_payload():
    info = {
        "code": "011002200711",
        "number": "18849159",
        "issue_date": "20221121",
        "check_code": "006483",
        "subtotal_amount": "11.49"
        }
    payload='invoice_code={code}&invoice_num={number}&invoice_date={issue_date}&invoice_type=special_vat_invoice&check_code={check_code}&total_amount={subtotal_amount}'
    payload = payload.format(**info)
    return payload

def check():
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice_verification?access_token=" + get_access_token()
    payload = get_payload()    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    if response.status_code == '200':
        res = response.json()
        if res['VerifyResult'] == '0001':
            return res
        else:
            logging("error")
        
    print(response.text)        
    
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def modify_web_page(check_info:dict):
    
    cycs_header = table.table_head.format(check_info['VerifyFrequency'],datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
    words_result = check_info['words_result']
    table_footer = table.heji_table.format(words_result['TotalAmount'], words_result['TotalTax'],Translate(words_result['AmountInFiguers']),words_result['AmountInFiguers'])
    print(table_footer)

def Translate(num):
    '''数字转人民币格式'''
    #判断参数类型
    if type(num)==type(''):
        try: f=float(num)
        except: return u'金额字符串无法转换成数字！'
        if f<0: num=num[1:]
        tmp = num.split('.')
    elif type(num) in [type(0),type(0.0)]:
        fNum=1.0e+16 # 如果是数字大于100兆会被截尾处理,字符串不受影响
        if not 0<=num<fNum: return f'金额必须为非负数且小于{fNum}！'
        tmp = str(num).split('.')
    else: return u'金额必须是数字或字符串！'
    #汉字格式字符串
    ret,cn='', ['']*3
    cnStr = (u'角分整',u'零壹贰叁肆伍陆柒捌玖',u'元拾佰仟万拾佰仟亿拾佰仟兆拾佰仟京拾佰仟')
    for i in range(3): cn[i]=[c for c in cnStr[i]]
    if len(tmp[0])>len(cn[2]): return u'金额数值过大，已超过设置的最大值！'
    if len(tmp)>1 and len(tmp[1])>2: tmp[1]=tmp[1][:2] #小数大于2位截尾处理
    #转换整数和小数
    for i,n in enumerate(reversed(list(tmp[0]))): ret = cn[1][int(n)]+cn[2][i]+ret
    if len(tmp)>1:
        if tmp[0][-1]=='0': ret += cn[1][0]
        for i,n in enumerate(list(tmp[1])): ret += cn[1][int(n)] + cn[0][i]
    #根据书写规则替换掉不该出现的字串
    for i in range(2): ret=ret.replace(cn[1][0]+cn[0][i],cn[1][0])
    for i in range(1,4): ret=ret.replace(cn[1][0]+cn[2][i],cn[1][0])
    for i in range(3,1,-1): ret=ret.replace(cn[1][0]*i,cn[1][0])
    for i in range(0,len(cn[2]),4): ret=ret.replace(cn[1][0]+cn[2][i],cn[2][i])
    for i in range(4,10,4): ret=ret.replace(cn[2][i+4]+cn[2][i],cn[2][i+4])
    if ret[0] in {cn[1][0],cn[2][0]}: ret=ret[1:]
    if len(ret)>1:
        if ret[-1] == cn[1][0]: ret=ret[:-1]+cn[0][2]
        if ret[-1] == cn[2][0]: ret+=cn[0][2]
        if ret[0] in {cn[1][0],cn[2][0]}: ret=ret[1:]
    else:
        ret=cn[1][0]+cn[2][0] 
    return ret

if __name__ == '__main__':
    # info = check()
    modify_web_page(data.resp)

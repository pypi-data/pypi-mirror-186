"""
测试数据主文件
created by ywp 2018-1-16
"""
import random
import string
import time
import json
import requests
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from .chinacitycode import CITYCODE_LIST
from .chinesename import SURNAME_LIST, FIRSTNAME_LIST
from .chinesecardbin import CARDBIN_LIST
from .dbhelper import exec_sql


class PersonalInfo:
    """
    个人信息
    """

    def create_phone(self):
        """
        创建手机号码
        """
        prelist = [
            "130", "131", "132", "133", "134", "135", "136", "137", "138",
            "139", "147", "150", "151", "152", "153", "155", "156", "157",
            "158", "159", "186", "187", "188", "189"
        ]
        return random.choice(prelist) + "".join(
            random.choice("0123456789") for i in range(8))

    def sur(self):
        """
        姓
        """
        return random.choice(SURNAME_LIST)

    def name(self):
        """
        名字
        """
        return random.choice(FIRSTNAME_LIST)

    def full_name(self):
        """
        姓名
        """
        sur = random.choice(SURNAME_LIST)
        name = random.choice(FIRSTNAME_LIST)
        return "{0}{1}".format(sur, name)

    def _generateCheckCode(self, idCard):
        """
        身份证最后1位，校验码
        """
        def haoma_validate(idCard):
            if type(idCard) in [str, list, tuple]:
                if len(idCard) == 17:
                    return True
            raise Exception('Wrong argument')

        if haoma_validate(idCard):
            if type(idCard) == str:
                seq = map(int, idCard)
            elif type(idCard) in [list, tuple]:
                seq = idCard

            t = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            s = sum(map(lambda x: x[0] * x[1], zip(t, map(int, seq))))
            b = s % 11
            bd = {
                0: '1',
                1: '0',
                2: 'X',
                3: '9',
                4: '8',
                5: '7',
                6: '6',
                7: '5',
                8: '4',
                9: '3',
                10: '2'
            }
            return bd[b]

    def create_idcard(self, min_age=18, max_age=50, city_code_list=None) -> str:
        """
        身份证
        """
        cur = datetime.now()
        if not city_code_list:
            city_code_list = CITYCODE_LIST
        id = str(random.choice(city_code_list))  #地区码
        id = id + str(random.randint(cur.year-max_age, cur.year-min_age))  #年份项
        da = date.today() + timedelta(days=random.randint(1, 366))  #月份和日期项
        id = id + da.strftime('%m%d')
        id = id + str(random.randint(100, 300))  #顺序号简单处理
        id = id + self._generateCheckCode(id)
        return id

    def create_bankcardno(self):
        """
        银行卡
        """
        return random.choice(CARDBIN_LIST) + "".join(
            random.choice("0123456789") for i in range(10))

    def fourelements(self):
        """
        四要素
        """
        return {
            "CardNo": self.create_idcard(),
            "Name": self.full_name(),
            "BankNo": self.create_bankcardno(),
            "Phone": self.create_phone()
        }


class DateTimeUtil:
    """
    封装一些常用的日期/时间
    """
    def get_sql_dt(self, days=0):
        '''
        获取当前日期时间，格式'2015-07-08 08:51:59'
        '''
        onedatetime = datetime.now() + timedelta(days=days)
        return onedatetime.strftime(r'%Y-%m-%d %H:%M:%S')

    def get_noseparators_dt(self, days=0):
        '''
        获取当前日期时间，格式'20150708085159'
        '''
        onedatetime = datetime.now() + timedelta(days=days)
        return onedatetime.strftime(r'%Y%m%d%H%M%S')

    def get_request_no(self):
        """
        获取时间流水号
        """
        requestno = self.get_noseparators_dt() + "".join(
            random.choice(string.ascii_letters) for i in range(4))
        return requestno

    def strtodate(self, datestr):
        '''
        仅限yy-mm-dd 格式
        '''
        tmp = [int(x) for x in datestr.split('-')]
        return datetime(tmp[0], tmp[1], tmp[2])

    def get_today(self):
        '''
        获取当前日期时间，格式'20170821'
        '''
        return time.strftime(r'%Y%m%d', time.localtime(time.time()))

    def get_tomorrow(self):
        '''
        获取当前日期时间，格式'20170821'
        '''
        tomorrow = datetime.now() + timedelta(days=+1)
        return tomorrow.strftime(r'%Y%m%d')

    def get_yesterday(self):
        '''
        获取当前日期时间，格式'20170821'
        '''
        yesterday = datetime.now() + timedelta(days=-1)
        return yesterday.strftime(r'%Y%m%d')

    def get_oneday(self, days):
        '''
        通过日期偏移量获取某一天，格式'2017-08-21'
        '''
        tmp = datetime.now() + timedelta(days)
        return tmp.strftime("%Y-%m-%d")

    def get_timexint(self):
        """
        获取时间戳
        """
        return str(time.time()).replace('.', '')

    def get_aftermonth(self, months):
        '''
        通过月数偏移量获取某一天，格式'2017-08-21'
        '''
        tmp = datetime.now() + relativedelta(months=months)
        return tmp.strftime("%Y-%m-%d")

    def get_day(self):
        '''
        获取今天是这个月的第几天
        '''
        return str(date.today().day)


import json
import requests
from lazy_testdata.dbhelper import exec_sql


class Swagger2Case():

    def __init__(self, env_name, conn, domain_url=None, swagger_json_file=None):
        self.swagger = None
        self.env_name = env_name
        self.conn = conn
        self.domain_url = domain_url
        self.test_cases = []
        self.original_ref_list = []
        if domain_url:
            session = requests.session()
            self.swagger = session.get(domain_url + '/v2/api-docs').json()
        if swagger_json_file:
            with open(swagger_json_file, 'r') as file:
                self.swagger = json.load(file)
            self.domain_url = "http://" + self.swagger["host"]
        if self.swagger:
            self.paths = self.swagger["paths"]
            self.definitions = self.swagger["definitions"]
        self.type_value = {
            "integer": 1,
            "boolean": True,
            "string": "string",
            "object": "object",
            "array": []
        }

    def combine_all_args_case(self, case_type='全参数'):
        paths = self.paths
        for path in paths:
            path_content = paths[path]
            for md in path_content:
                method_content = path_content[md]
                case_dict = {}
                case_dict['flow_name'] = method_content['tags'][0]
                case_dict['case_name'] = method_content['summary'] + \
                    '-' + case_type
                case_dict['method'] = md
                para = None
                if 'parameters' in method_content:
                    para = method_content['parameters']
                if 'get' in md.lower():
                    case_dict['body'] = ''
                    if para:
                        case_dict['path'] = self.deal_get_para(para, path)
                    else:
                        case_dict['path'] = path
                else:
                    case_dict['path'] = path
                    if para:
                        case_dict['body'] = self.deal_not_get_para(para)
                    else:
                        case_dict['body'] = {}
            self.test_cases.append(case_dict)

    def combine_none_args_case(self, case_type='传空或者不传'):
        paths = self.paths
        para_type = [None, {}, ""]
        for path in paths:
            path_content = paths[path]
            for md in path_content:
                for para in para_type:
                    method_content = path_content[md]
                    case_dict = {}
                    case_dict['flow_name'] = method_content['tags'][0]
                    case_dict['case_name'] = method_content['summary'] + \
                        '-' + case_type + str(para)
                    case_dict['method'] = md
                    case_dict['path'] = path
                    case_dict['body'] = para
                    self.test_cases.append(case_dict)

    def deal_get_para(self, para, path):
        type_value = self.type_value
        qry_str = '?'
        arg = ''
        if path.count('{') > 0:
            path_arg_count = path.count('{')
            print(f"path_arg_count ={path_arg_count}")
            arg = path.split('{')[-1].split('}')[0]
        for x in para:
            if arg == '' or arg not in x["name"]:
                print(x["name"])
                try:
                    if 'schema' in x:
                        if 'originalRef' in x['schema']:
                            inner_dict = self.deal_para_from_def(
                                x['schema']['originalRef'])
                            for k, v in inner_dict.items():
                                qry_str = qry_str + \
                                    f'{k}={type_value.setdefault(v,v)}&'
                        else:
                            qry_str = qry_str + \
                                f'{x["name"]}={type_value.setdefault(x["schema"]["type"],x["schema"]["type"])}&'
                    else:
                        if 'array' in x["type"]:
                            default_value = type_value.setdefault(
                                type_value[x["items"]["type"]], type_value[x["items"]["type"]])
                            x["type"] = default_value + \
                                ',' + default_value
                        else:
                            x["type"] = type_value[x["type"]]
                        qry_str = qry_str + f'{x["name"]}={x["type"]}&'
                except Exception as err:
                    print(err)
                    print('❌'*66)
                    print(x)
            elif arg in x["name"]:
                ori_arg = "{" + arg + "}"
                defaul_value = type_value.setdefault(x["type"])
                path = path.replace(ori_arg, str(defaul_value))

        qry_str = qry_str[:-1]

        path = path + qry_str
        return path

    def deal_not_get_para(self, para):
        type_value = self.type_value
        para_dict = {}
        for x in para:
            name = x['name']
            if "schema" in x:
                tmp = x["schema"]
                if "originalRef" in tmp:
                    def_key = tmp["originalRef"]
                    para_dict = self.deal_para_from_def(def_key)
                if "items" in tmp:
                    if "originalRef" in tmp["items"]:
                        def_key = tmp["items"]["originalRef"]
                        para_dict[name] = [self.deal_para_from_def(def_key)]
                    else:
                        try:
                            para_dict[name] = [type_value.setdefault(
                                tmp["items"]["type"], tmp["items"]["type"])]
                        except Exception as err:
                            print(f"出异常了，相关变量：tmp['items']={tmp['items']},详细信息：{err}")
            else:
                if 'array' in x["type"]:
                    try:
                        para_dict[name] = [type_value.setdefault(
                        x["items"]["type"], x["items"]["type"])]
                    except Exception as err:
                        print("出错了～")
                        print(x["type"])
                else:
                    para_dict[name] = type_value.setdefault(
                        x["type"], x["type"])

        try:
            result = json.dumps(para_dict)
        except Exception as err:
            print('🆖'*66)
            print(err)
        return result

    def deal_para_from_def(self, key, max_layer=3):
        type_value = self.type_value
        original_ref_list = self.original_ref_list
        definitions = self.definitions
        para_dict = {}
        count = original_ref_list.count(key)
        if count < max_layer + 1:
            original_ref_list.append(key)
            props = definitions[key]["properties"]
            for p in props:
                tmp = props[p]
                try:
                    if "items" in tmp:
                        if "originalRef" in tmp["items"]:
                            inner_key = tmp["items"]["originalRef"]
                            print("❌……❌"*66, inner_key)
                            print(original_ref_list)
                            count = original_ref_list.count(inner_key)
                            print(count)
                            if original_ref_list.count(inner_key) < max_layer:
                                para_dict[p] = [
                                    self.deal_para_from_def(inner_key)]
                            else:
                                para_dict[p] = []
                        else:
                            para_dict[p] = [type_value.setdefault(
                                tmp["items"]["type"], tmp["items"]["type"])]
                    elif "originalRef" in tmp:
                        inner_key = tmp["originalRef"]
                        if original_ref_list.count(inner_key) < max_layer:
                            para_dict[p] = self.deal_para_from_def(inner_key)
                        else:
                            para_dict[p] = {}
                        print('🐛'*66)
                        print(p, inner_key)
                    else:
                        para_dict[p] = type_value.setdefault(
                            tmp["type"], tmp["type"])
                except Exception as err:
                    print('❌'*66)
                    print(f'{err}\n')
                    para_dict[p] = 'too deep!!'
        original_ref_list = []
        return para_dict

    def get_first_resp(self,headers=None):
        session = requests.session()
        if headers:
            session.headers = headers
        test_cases = self.test_cases
        domain_url = self.domain_url
        for x in test_cases:
            url = x["path"]
            method = x["method"]
            para = x["body"]
            para = json.dumps(para)
            try:
                if para == "":
                     x["resp"] = session.request(
                        method, domain_url + url).json()            
                else:
                    x["resp"] = session.request(
                        method, domain_url + url, json=para).json()
            except Exception as err:
                print(err)
                x["resp"] = ""
            resp = x["resp"]
            resp = json.dumps(resp,ensure_ascii=False)
            print(f"请求url={url}，method={method}，使用参数={para}，响应内容={resp}")

    def insert_db(self):
        env_name = self.env_name
        conn = self.conn
        test_cases = self.test_cases
        length = len(test_cases)
        flow_sql = '''insert into test_scenario(`scenario_code`,
                                                `scenario_name`,
                                                `priority`,
                                                `account`,
                                                `password`,
                                                `run_env`,
                                                `state`,
                                                `create_time`,
                                                `update_time`,
                                                `creater`,
                                                `modifier`,
                                                `tags`) values '''

        node_sql = '''insert into test_case(`scenario_id`,
                                                `case_code`,
                                                `case_name`,
                                                `order_id`,
                                                `method`,
                                                `path`,
                                                `parameter`,
                                                `expect_response`,
                                                `ischechdb`,
                                                `sql_str`,
                                                `sql_para`,
                                                `expect_db`,
                                                `pre_keys`,
                                                `sleep_time`,
                                                `isexcute_pre_sql`,
                                                `pre_sql_str`,
                                                `pre_sql_para`,
                                                `pre_sql_out`,
                                                `post_keys`,
                                                `post_keys_extractor`,
                                                `post_keys_default`,
                                                `run_env`,
                                                `state`,
                                                `create_time`,
                                                `update_time`,
                                                `creater`,
                                                `modifier`) values '''
        for x in range(length):
            tmp = f''' ('test{x}', '{test_cases[x]['flow_name']}', 1, '', '', '{env_name}', 1, now(), now(), 'ywp', 'ywp', '{test_cases[x]['flow_name']}'),'''
            flow_sql = flow_sql + tmp
            body = test_cases[x]['body']
            if not body:
                body = 'null'
            if 'resp' not in test_cases[x]:
                test_cases[x]['resp'] = ''
            resp = json.dumps(test_cases[x]['resp'],ensure_ascii=False).replace('\'', '\\\'')
            if  len(resp) > 65535:
                resp = ''
            temp = f'''({x+1}, 'test{x}', '{test_cases[x]['case_name']}', 1, '{test_cases[x]['method']}', '{test_cases[x]['path']}', '{body}', '{resp}', 0, '', '', '', '', 0, 0, '', '', '', '', '', '', '{env_name}', 1, now(), now(), 'ywp', 'ywp'),'''
            node_sql = node_sql + temp

        flow_sql = flow_sql[:-1] + ';'
        node_sql = node_sql[:-1] + ';' 
        node_flow_sql = f'''update test_case tc, test_scenario ts
                set tc.scenario_id = ts.scenario_id
                where tc.run_env= '{env_name}' and ts.run_env = '{env_name}' and ts.scenario_code = tc.case_code and tc.creater ='ywp' and ts.creater ='ywp';
                '''
        sql = flow_sql + '\n' + node_sql + '\n' + node_flow_sql
        with open('init.sql','w') as file:
            file.write(sql)
        exec_sql(conn,flow_sql)
        # exec_sql(conn,node_sql)
        # exec_sql(conn,node_flow_sql)   

if __name__ == '__main__':
    # TMP = PersonalInfo()
    # su = DateTimeUtil()
    # print(su.get_sql_dt(6))
    # print(TMP.fourelements())
    # print(TMP.full_name())
    env_name = 'scfp-test-v1'
    conn = 'mysql+pymysql://root:pwd@localhost:3306/common_api_test'
    url = 'http://10.228.64.54:24009/'
    json_file = 'swagger2case-gauge/resource/swagger.json'
    sc = Swagger2Case(env_name, conn, domain_url=url)
    # sc = Swagger2Case(env_name, conn, swagger_json_file=json_file)
    sc.combine_all_args_case()
    sc.combine_none_args_case()
    sc.get_first_resp()
    sc.insert_db()

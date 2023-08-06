from __future__ import annotations

try:
    from . import orator
    from .Lock import Lock
    from .. import Lg
    from .. import Base64
    from .. import Time 
except:
    import orator
    from Lock import Lock
    import sys
    sys.path.append("..")
    import Lg
    import Base64
    import Time 

import pickle
import typing
import bagbag
import pymysql
import threading
import multiprocessing

class mySQLSQLiteTable():
    def __init__(self, db: MySQLSQLiteBase, schema: orator.Schema, tbname: str):
        """
        This function initializes the class with the database, schema, and table name
        
        :param db: The database object
        :type db: MySQLSQLiteBase
        :param schema: orator.Schema
        :type schema: orator.Schema
        :param tbname: The name of the table you want to use
        :type tbname: str
        """
        self.db = db
        self.schema = schema
        self.tbname = self.filterTableName(tbname)
        self.table = {}
        self.data = {}
    
    def _id(self) -> str:
        return threading.current_thread().name + multiprocessing.current_process().name

    def filterTableName(self, tbname: str) -> str:
        nl = []
        for t in tbname:
            if t in "_qazwsxedcrfvtgbyhnujmikolopQAZWSXEDCRFVTGBYHNUJMIKOLP0123456789":
                nl.append(t)
            elif bagbag.String(t).HasChinese():
                nl.append(t)
            else:
                nl.append("_")
        
        return ''.join(nl)

    def AddColumn(self, colname: str, coltype: str, default=None, nullable:bool = True) -> mySQLSQLiteTable:
        """
        添加一个字段, 如果字段存在就跳过, 不会修改.

        :param colname: The name of the column to add
        :type colname: str
        :param coltype: int, string, float, text
        :type coltype: str
        :param default: The default value for the column
        :param nullable: Whether the column can be null, defaults to True
        :type nullable: bool (optional)
        """
        if self.schema.has_table(self.tbname):
            with self.schema.table(self.tbname) as table:
                exists = self.schema.has_column(self.tbname, colname)

                if not exists:
                    if coltype in ["int", "integer"]:
                        col = table.big_integer(colname)
                    elif coltype in ["string", "str", "varchar"] :
                        col = table.string(colname, 256)
                    elif coltype in ["float", "double"]:
                        col = table.double(colname)
                    elif coltype in ["text", "longtext"]:
                        col = table.long_text(colname)
                    else:
                        raise Exception("列的类型可选为: int, string, float, text")
                    
                    if default != None:
                        col.default(default)
                    
                    if nullable:
                        col.nullable()
                
                # if exists:
                #     col.change()
        else:
            with self.schema.create(self.tbname) as table:
                table.increments('id')

                if coltype in ["int", "integer"]:
                    col = table.big_integer(colname)
                elif coltype in ["string", "str", "varchar"] :
                    col = table.string(colname, 256)
                elif coltype in ["float", "double"]:
                    col = table.double(colname)
                elif coltype in ["text", "longtext"]:
                    col = table.long_text(colname)
                else:
                    raise Exception("列的类型可选为: int, string, float, text")
                
                if default:
                    col.default(default)
                
                if nullable:
                    col.nullable()

        return self
    
    def AddIndex(self, *cols: str) -> mySQLSQLiteTable:
        """
        It adds an index to the table
        
        :param : `tbname`: The name of the table
        :type : str
        :return: The table object itself.
        """
        try:
            with self.schema.table(self.tbname) as table:
                table.index(*cols)
        except Exception as e:
            if "Duplicate key name" not in str(e) and "already exists" not in str(e):
                raise e

        return self
    
    # 由于不同的线程使用同一个table的时候, 条件会串, 例如多个线程同时调用where的时候.
    # 所以为每个线程生成一个orator的table对象
    def initTableObj(func): # func是被包装的函数
        def ware(self, *args, **kwargs): # self是类的实例
            if self._id() not in self.table:
                self.table[self._id()] = self.db.db.table(self.tbname)
            
            res = func(self, *args, **kwargs)
            return res
        
        return ware
    
    def avoidError(func): # func是被包装的函数
        def ware(self, *args, **kwargs): # self是类的实例
            if self.db.driver == "mysql":
                while True:
                    try:
                        res = func(self, *args, **kwargs)
                        break
                    except bagbag.Tools.orator.exceptions.query.QueryException as e:
                        if str(e).startswith('(1054, ') or str(e).startswith('(1406, '):
                            raise e 
                        # MySQL驱动默认不允许一个连接跨多个线程, 重连就行
                        Lg.Trace("重连, 因为:", e)
                        self.db.db.reconnect()
                    except pymysql.err.OperationalError as e:  
                        if e.args[0] == 2003:
                            Time.Sleep(0.5)
                        else:
                            raise e 

            elif self.db.driver == "sqlite":
                # SQLite驱动默认不允许一个连接跨多个线程
                # 在连接的时候禁止了同线程的检测, 所以自己这里要保证同时只有一个线程在操作数据库
                self.db.lock.Acquire()
                res = func(self, *args, **kwargs)
                self.db.lock.Release()

            return res

        return ware
    
    @initTableObj
    def Fields(self, *cols: str) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].select(*cols)
        return self
    
    @initTableObj
    def Where(self, key:str, opera:str, value:str) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].where(key, opera, value)
        return self
    
    @initTableObj
    def WhereIn(self, key:str, value: list) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].where_in(key, value)
        return self 

    @initTableObj
    def WhereNotIn(self, key:str, value: list) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].where_not_in(key, value)
        return self

    @initTableObj
    def WhereNull(self, key:str) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].where_null(key)
        return self 
    
    @initTableObj
    def WhereNotNull(self, key:str) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].where_not_null(key)
        return self

    @initTableObj
    def WhereBetween(self, key:str, start:int|float|str, end:int|float|str) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].where_between(key, [start, end])
        return self 
    
    @initTableObj
    def WhereNotBetween(self, key:str, start:int|float|str, end:int|float|str) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].where_not_between(key, [start, end])
        return self 

    @initTableObj
    def OrWhere(self, key:str, opera:str, value:str) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].or_where(key, opera, value)
        return self 

    @initTableObj
    def OrWhereIn(self, key:str, value: list) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].or_where_in(key, value)
        return self

    @initTableObj
    def OrderBy(self, *key:str) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].order_by(*key)
        return self 

    @initTableObj
    def Limit(self, num:int) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].limit(num)
        return self 

    @initTableObj
    def Paginate(self, size:int, page:int) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].simple_paginate(size, page)
        return self 

    @initTableObj
    def Data(self, value:map|list[map]) -> mySQLSQLiteTable:
        """
        在Insert的时候可以是map或者list[map], 在Update的时候只能是map
        
        :param value: The value to be inserted into the table
        :type value: map|list[map]
        :return: The object itself.
        """
        self.data = value
        return self 

    @initTableObj
    def Offset(self, num:int) -> mySQLSQLiteTable:
        self.table[self._id()] = self.table[self._id()].offset(num)
        return self 

    @initTableObj
    @avoidError
    def Insert(self):
        self.table[self._id()].insert(self.data)

        self.data = {}
        del(self.table[self._id()])

    @initTableObj
    @avoidError
    def Update(self):
        self.table[self._id()].update(self.data)
        
        del(self.table[self._id()])

    @initTableObj
    @avoidError
    def Delete(self):
        self.table[self._id()].delete()

        del(self.table[self._id()])

    @initTableObj
    @avoidError
    def InsertGetID(self) -> int:
        id = self.table[self._id()].insert_get_id(self.data)

        self.data = {}
        del(self.table[self._id()])

        return id

    def Exists(self) -> bool: 
        exists = False
        if self.First():
            exists = True

        return exists

    def NotExists(self) -> bool: 
        notexists = True
        if self.First():
            notexists = False

        return notexists

    @initTableObj
    @avoidError
    def Count(self) -> int:
        count = self.table[self._id()].count()

        del(self.table[self._id()])
        return count

    @initTableObj
    @avoidError
    def Find(self, id:int) -> dict | None:
        res = self.db.db.table(self.tbname).where('id', "=", id).first()
        return res 
        
    @initTableObj
    @avoidError
    def First(self) -> dict | None: 
        """
        :return: A map of the first row in the table. Return None if the table is empty. 
        """
        lastqueryiserror = False 
        while True:
            try:
                res = self.table[self._id()].first()
                if lastqueryiserror and res == None:
                    Time.Sleep(0.5)
                else:
                    break 
            except pymysql.err.OperationalError as e:
                if e.args[0] == 2003:
                    lastqueryiserror = True 
                    Time.Sleep(0.5)
                else:
                    raise e 

        del(self.table[self._id()])
        return res

    @initTableObj
    @avoidError
    def Get(self) -> list[dict]:
        """
        It gets the data from the table and then resets the table
        len(result) == 0 if the result set is empty.

        :return: A list of dictionaries.
        """
        lastqueryiserror = False 
        while True:
            try:
                res = [dict(i) for i in self.table[self._id()].get()]
                if lastqueryiserror and len(res) == 0:
                    Time.Sleep(0.5)
                else:
                    break 
            except pymysql.err.OperationalError as e:  
                if e.args[0] == 2003:
                    lastqueryiserror = True 
                    Time.Sleep(1)
                else:
                    raise e 

        del(self.table[self._id()])
        return res

    def Columns(self) -> list[dict]:
        """
        It returns a list of dictionaries, each dictionary containing the name and type of a column in a
        table
        :return: A list of dictionaries.
        """
        res = []
        if self.db.driver == "mysql":
            for i in self.db.Execute("SHOW COLUMNS FROM `"+self.tbname+"`"):
                res.append({'name': i["Field"], 'type': i["Type"]})
        elif self.db.driver == "sqlite":
            for i in self.db.db.select("PRAGMA table_info(`"+self.tbname+"`);"):
                res.append({'name': i["name"], 'type': i["type"]})
        return res

class mySQLSQLiteKeyValueTable():
    def __init__(self, db:MySQLSQLiteBase, tbname:str) -> None:
        self.db = db 
        (
            self.db.Table(tbname). 
                AddColumn("key", "string"). 
                AddColumn("value", "text"). 
                AddIndex("key")
        )
        self.tbname = tbname
        self.namespace = []
    
    def Namespace(self, namespace:str) -> mySQLSQLiteKeyValueTable:
        if len(':'.join(self.namespace)) > 200:
            raise Exception("Namespace too long: " + str(len(':'.join(self.namespace))))
        self.namespace.append(namespace)
        return self
    
    def __key(self, key:str) -> str:
        if len(self.namespace) == 0:
            return key 
        else:
            return ':'.join(self.namespace) + ":" + key
    
    def Exists(self, key:str) -> bool:
        tb = self.db.Table(self.tbname)
        return tb.Where("key", "=", self.__key(key)).Exists()
    
    def Get(self, key:str, default:typing.Any=None) -> typing.Any:
        tb = self.db.Table(self.tbname)
        res = tb.Where("key", "=", self.__key(key)).First()

        if res != None:
            value = res["value"]
            if value[:2] == "i ":
                value = int(value[2:])
            elif value[:2] == "s ":
                value = value[2:]
            elif value[:2] == "f ":
                value = float(value[2:])
            elif value[:2] == "p ":
                value = pickle.loads(Base64.Decode(value[2:])) 
            else:
                value = pickle.loads(Base64.Decode(value)) # 为了兼容之前的代码
        else:
            value = default 

        return value
    
    def Set(self, key:str, value:typing.Any):
        tb = self.db.Table(self.tbname)

        if type(value) == int:
            value = "i " + str(value)
        elif type(value) == str:
            value = "s " + str(value)
        elif type(value) == float:
            value = "f " + str(value)
        else:
            value = "p " + Base64.Encode(pickle.dumps(value, protocol=2))

        if tb.Where("key", "=", self.__key(key)).Exists():
            tb.Where("key", "=", self.__key(key)).Data({
                "value": value,
            }).Update()
        else:
            tb.Data({
                "key": self.__key(key), 
                "value": value,
            }).Insert()
    
    def Del(self, key:str):
        tb = self.db.Table(self.tbname)
        tb.Where("key", "=", self.__key(key)).Delete()

class mySQLSQLiteConfirmQueue():
    def __init__(self, db:MySQL|SQLite, name:str, timeout:int, size:int) -> None:
        self.db = db 
        self.name = name 
        self.lock = Lock()
        self.timeout = timeout
        self.size = size
    
    def Size(self) -> int:
        """
        返回未曾开始过的新任务个数
        :return: The number of rows in the table.
        """
        return self.db.Table(self.name).Where("stime", "=", 0).Count()
    
    def SizeStarted(self) -> int:
        """
        返回正在执行的任务个数
        :return: The number of rows in the table where the stime column is not equal to 0.
        """
        return self.db.Table(self.name).Where("stime", "!=", 0).Count()
    
    def SizeTotal(self) -> int:
        """
        返回所有任务总数
        :return: The number of rows in the table.
        """
        return self.db.Table(self.name).Count()
    
    def Get(self, block:bool=True) -> typing.Tuple[int, typing.Any]:
        self.lock.Acquire()
        while True:
            r = self.db.Table(self.name).Where("stime", "<", int(Time.Now()) - self.timeout).OrderBy("id").First()

            if r == None:
                r = self.db.Table(self.name).Where("stime", "=", 0).OrderBy("id").First()

                if r == None:
                    if not block:
                        self.lock.Release()
                        return None, None 
                    else:
                        Time.Sleep(0.1)
                else:
                    break 
            else:
                break
        
        self.db.Table(self.name).Where("id", "=", r["id"]).Data({
            "stime": int(Time.Now()),
        }).Update()

        self.lock.Release()
        return r["id"], pickle.loads(Base64.Decode(r["data"]))
    
    def Put(self, item:typing.Any, block:bool=True, force:bool=False):
        if force == False:
            if block:
                while self.size > 0 and self.Size() >= self.size:
                    Time.Sleep(0.1)
            else:
                if self.size > 0 and self.Size() >= self.size:
                    return False

        self.db.Table(self.name).Data({
            "data": Base64.Encode(pickle.dumps(item, protocol=2)),
            "stime": 0,
        }).Insert()

        return True

    def Done(self, id:int):
        r = self.db.Table(self.name).Where("id", "=", id).First()
        if r == None:
            raise Exception("任务没找到")
        else:
            if r["stime"] == 0:
                raise Exception("任务未开始")
            else:
                self.db.Table(self.name).Where("id", "=", id).Delete()
    
    def __iter__(self):
        while True:
            yield self.Get()

class mySQLSQLiteQueue():
    def __init__(self, db:MySQL|SQLite, name:str, size:int) -> None:
        self.db = db 
        self.name = name 
        self.lock = Lock()
        self.size = size
    
    def Size(self) -> int:
        return self.db.Table(self.name).Count()
    
    def Get(self, wait=True) -> typing.Any:
        self.lock.Acquire()
        r = self.db.Table(self.name).OrderBy("id").First()
        if r == None:
            if not wait:
                self.lock.Release()
                return None 
            else:
                while r == None:
                    Time.Sleep(0.1)
                    r = self.db.Table(self.name).OrderBy("id").First()
        
        self.db.Table(self.name).Where("id", "=", r["id"]).Delete()

        self.lock.Release()
        return pickle.loads(Base64.Decode(r["data"]))
    
    def Put(self, item:typing.Any):
        while self.size > 0 and self.Size() >= self.size:
            Time.Sleep(0.1)

        self.db.Table(self.name).Data({
            "data": Base64.Encode(pickle.dumps(item, protocol=2)),
        }).Insert()
    
    def __iter__(self):
        while True:
            yield self.Get()

# > The class is a base class for MySQL and SQLite
class MySQLSQLiteBase():
    def __init__(self) -> None:
        self.db:orator.DatabaseManager = None

    def Queue(self, tbname:str, size:int=0) -> mySQLSQLiteQueue:
        if tbname not in self.Tables():
            self.Table(tbname).AddColumn("data", "text")
        
        return mySQLSQLiteQueue(self, tbname, size)

    def QueueConfirm(self, tbname:str, size:int=0, timeout:int=300) -> mySQLSQLiteConfirmQueue:
        """
        这是一个需要调用Done方法来确认某个任务完成的队列
        如果不确认某个任务完成, 它就会留在队列当中等待timeout之后重新能被Get到
        优先Get到timeout的任务
        """

        if tbname not in self.Tables():
            (
                self.Table(tbname).
                    AddColumn("data", "text"). 
                    AddColumn("stime", "int"). 
                    AddIndex("stime")
            )
        
        return mySQLSQLiteConfirmQueue(self, tbname, timeout, size)

    def Table(self, tbname: str) -> mySQLSQLiteTable:
        if not tbname in self.Tables():
            with self.schema.create(tbname) as table:
                table.increments('id')

        return mySQLSQLiteTable(self, self.schema, tbname)

    def Execute(self, sql: str) -> (bool | int | list):
        """
        :param sql: The SQL statement to execute
        :type sql: str
        """
        action = sql.split()[0].lower() 

        try:
            if action == "insert":
                res = self.db.insert(sql)
            elif action in ["select", "show"]:
                res = self.db.select(sql)
            elif action == "update":
                res = self.db.update(sql)
            elif action == "delete":
                res = self.db.delete(sql)
            else:
                res = self.db.statement(sql)
        except orator.exceptions.query.QueryException as e:
            if self.driver == "mysql":
                if action == "insert":
                    res = self.db.insert(sql)
                elif action in ["select", "show"]:
                    res = self.db.select(sql)
                elif action == "update":
                    res = self.db.update(sql)
                elif action == "delete":
                    res = self.db.delete(sql)
                else:
                    res = self.db.statement(sql)
            else:
                raise e
                
        return res

    def Tables(self) -> list:
        """
        It returns a list of all the tables in the database
        :return: A list of tables in the database.
        """
        res = []
        if self.driver == "mysql":
            tbs = self.Execute("show tables;")
        elif self.driver == "sqlite":
            tbs = self.Execute("SELECT `name` FROM sqlite_master WHERE type='table';")
        for i in tbs:
            for k in i:
                res.append(i[k])
        return res
    
    def Close(self):
        self.db.disconnect()
    
    def KeyValue(self, tbname:str) -> mySQLSQLiteKeyValueTable:
        return mySQLSQLiteKeyValueTable(self, tbname)
    
    def BeginTransaction(self):
        self.db.begin_transaction()
    
    def Rollback(self):
        self.db.rollback()
    
    def Commit(self):
        self.db.commit()

# > This class is a wrapper for the orator library, which is a wrapper for the mysqlclient library,
# which is a wrapper for the MySQL C API
class MySQL(MySQLSQLiteBase):
    def __init__(self, host:str, port:int=3306, user:str="root", password:str="r", database:str="others", prefix:str="", charset:str="utf8mb4"):
        """
        This function creates a database connection using the orator library
        
        :param host: The hostname of the database you are connecting to. (localhost)
        :type host: str
        :param port: The port number to connect to the database
        :type port: int
        :param user: The username to connect to the database with
        :type user: str
        :param password: The password for the user you're connecting with
        :type password: str
        :param database: The name of the database you want to connect to
        :type database: str
        :param prefix: The prefix for the table names
        :type prefix: str
        """
        config = {
            'mysql': {
                'driver': 'mysql',
                'host': host,
                'database': database,
                'user': user,
                'password': password,
                'prefix': prefix,
                'port': port,
                'charset': charset,
            }
        }
        self.db = orator.DatabaseManager(config)
        self.schema = orator.Schema(self.db)
        self.driver = "mysql"
    
# > This class is a wrapper for the orator library, which is a wrapper for the sqlite3 library
class SQLite(MySQLSQLiteBase):
    def __init__(self, path:str=":memory:", prefix:str = ""):
        """
        :param path: The path to the database file
        :type path: str
        :param prefix: The prefix to use for the table names
        :type prefix: str
        """
        config = {
            'sqlite': {
                'driver': 'sqlite',
                'database': path,
                'prefix': '',
                'check_same_thread': False, # 会被传入到SQLite的驱动作为参数
            }
        }
        self.db = orator.DatabaseManager(config)
        self.schema = orator.Schema(self.db)
        self.driver = "sqlite"
        self.lock = Lock()

if __name__ == "__main__":
    # db = SQLite("data.db")
    # tbl = db.Table("test_tbl").AddColumn("string", "string").AddColumn("int", "string").AddIndex("int")
    # tbl.Data({"string":"string2", "int": 2}).Insert()
    # c = tbl.Where("string", "=", "string2").Count()
    # print(c)

    # print("exists:", tbl.Where("string", "=", "string555").Exists())

    # db.Close()

    # import os 
    # os.unlink("data.db")

    # print(db.Table("test_tbl").First())

    # db = MySQL("192.168.168.5", 3306, "root", "r", "test")

    # for row in db.Table("__queue__name__name").Get():
    #     print(row)

    # print(db.Table("__queue__name__name").Columns())

    # 执行SQL语句
    # In [4]: db.Execute("select distinct(`Column1`) from `table1`")
    # Out[4]: ({'Column1': '1'}, {'Column1': '2'}, {'Column1': '3'}, {'Column1': '4'})
    # 
    # In [3]: db.Execute("select count(`id`) as `count`, `data` from `table` group by `data`")
    # Out[3]: 
    # ({'count': 2, 'data': '1'},
    # {'count': 1, 'data': '2'},
    # {'count': 1, 'data': '3'},
    # {'count': 1, 'data': '4'})

    # db = MySQL("192.168.1.230")

    # 中文字段
    # (
    #     db.Table("俄罗斯号码段"). 
    #         AddColumn("开始", "int"). 
    #         AddColumn("结束", "int"). 
    #         AddColumn("运营商", "string").
    #         AddColumn("地区", "string")
    # )

    # tb = db.Table("test").AddColumn("col", "string")
    # tb.Data({
    #     "col": "😆😆😆😆😆",
    # }).Insert()

    # Lg.Trace(db.Table("chainabuse").Columns())

    db = MySQL("192.168.1.230")

    qn = db.Queue("queue_test")
    qn.Put(b'\x00\x00\x00\x1cftypisom\x00\x00\x02\x00isom')
    print(qn.Size())
    print(repr(qn.Get()))

    print("开启一个需要确认任务完成的队列, 3秒超时")
    qnc = db.QueueConfirm("queue_confirm_test", timeout=3)
    qnc.Put(b'\x00\x00\x00\x1cftypisom\x00\x00\x02\x00isom')

    print("获取任务内容")
    idx, data = qnc.Get()
    print(repr(data))

    print("等待5秒")
    Time.Sleep(5)

    print("再次获取任务")
    idx, data = qnc.Get()
    print(repr(data))

    print("确认任务完成")
    Time.Sleep(1)
    qnc.Done(idx)

    print("等待5秒")
    Time.Sleep(5)

    print("再次获取任务, 不等待")
    idx, data = qnc.Get(False)
    print(repr(data))
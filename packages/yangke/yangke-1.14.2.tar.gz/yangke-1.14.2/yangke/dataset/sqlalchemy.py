import datetime
from typing import Any

from sqlalchemy import create_engine, MetaData, Column, inspect, Table, String, text
from sqlalchemy.dialects.mysql import INTEGER, DOUBLE, BIGINT, VARCHAR, CHAR, TEXT, DATETIME
from sqlalchemy.engine import Engine, Row
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy.sql import Select

# # 创建基类, 使用ORM方式操作数据库是继承该类
Base = declarative_base()


class YkTable(Table):
    def __init__(self, name, metadata, columns=None):
        if columns is None:
            columns = []
        super().__init__(name, metadata, *columns)


class YkColumn(Column):
    def __init__(self, name, dtype, primary_key=False, nullable=False):
        """
        Sqlite数据库不只是foreignKey关键字
        """
        super().__init__(name, dtype, primary_key=primary_key, nullable=nullable)


# class Base(Base_):
#     __tablename__ = "default"  # 也可以是 __tablename__
#
#     def __init__(self):
#         # super().__init__()
#         ...


class ModifyTime(Base):
    """
    用来记录数据库表格最后更新时间的表格，因为目前MySql和Sqlite数据库均无法查询表格的最后更新时间，因此使用数据库表格记录所有表格的最后更新
    时间
    """
    __tablename__ = "modifyTime"
    table = Column(String(50), nullable=False, primary_key=True)  # autoincrement=True
    datetime = Column(DATETIME, nullable=False)

    def __init__(self, table, date_time):
        self.table = table
        self.datetime = date_time

    def __repr__(self):
        return f"ModifyTime(table={self.table}, 修改时间={self.datetime})"


class SqlOperator:
    def __init__(self, engine: Engine = None):
        """
        SQL数据库操作类，同时支持MySql和Sqlite数据库，使用示例：
        engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306", pool_recycle=7200)
        engine = create_engine('sqlite:///stocks.db', echo=True)
        so = SqlOperator(engine=engine)
        然后可以调用so的增删改查等方法，所有方法均同时支持MySql和Sqlite数据库
        """
        # 创建数据库引擎，ps:这里并没有连接具体数据库
        # engine = create_engine("mysql+mysqlconnector://root:password@localhost:3306", pool_recycle=7200)
        self.engine = engine
        self.insp = inspect(self.engine)
        self.meta_data = MetaData(bind=engine)
        self.meta_data.reflect(schema=None)  # schema为表在数据库中的上一级，例如在Sqlite数据库中，新建的表默认上一级是"main"
        self.session = sessionmaker(bind=engine)()  # 使用sessionmaker保持数据库会话连接
        self.base = Base

    def create_table(self, table_name, columns):
        """
        创建数据库表，如果同名表存在，会报错
        示例1：
        self.create_table(table_name=f"daily{symbol}",
                          columns=[
                              YkColumn('trade_date', DATE(), primary_key=True),
                              YkColumn('open', Float()),
                              YkColumn('high', Float()),
                              YkColumn('low', Float()),
                              YkColumn('close', Float()),
                              YkColumn('vol', Float()),
                              YkColumn('amount', Float()),
                          ])
        """
        table = Table(table_name, self.meta_data, *columns)
        table.create()

    def create_all_base_table(self):
        """
        创建所有继承自Base类的Python类的映射数据库表。也就是说，只要定义了继承自本模块中Base类的类，则该类会被映射成一个数据库表，
        本方法会自动创建所有映射的数据库表。
        """
        self.base.metadata.create_all(self.engine)

    def get_type_of_column(self, table_name=None, column_name=None):
        """
        获取mysql表中字段的类型，如果不设置column_name则返回所有的字段类型
        :param table_name:
        :param column_name: 为空则依次返回所有列的类型，封装为一个列表
        :return:
        """
        cols = self.insp.get_columns(table_name)
        res = None
        if column_name is None:
            res = {}
            for col in cols:
                res.update({col["name"]: col["type"]})
        else:
            for col in cols:
                if col["name"] == column_name:
                    res = col["type"]
                    break
        return res

    def get_column_names(self, table_name):
        """
        获取表格中的列名，返回列名列表
        """
        cols = self.insp.get_columns(table_name)
        res = []
        for col in cols:
            res.append(col["name"])
        return res

    def get_update_time_of_table(self, table_name):
        """
        获取表的最后更新时间
        """
        if self.has_table(table_name):
            # 查询modifyTime表，modifyTime表中记录了所有表格的最后更新时间
            if self.has_table("modifyTime"):
                table: Table = self.get_table("modifyTime")
                select: Select = table.select().where(table.c.table == table_name)  # 构建一个选择语句
                res = self.session.execute(select)  # 执行选择语句并获取结果
                res = res.fetchone()
                if res is None:
                    return None
                return res["datetime"]  # res.datetime
            else:
                return None
        else:
            return None

    def update_update_time_of_table(self, table_name):
        """
        更新表的最后更新时间
        """
        if not self.has_table("modifyTime"):
            self.create_all_base_table()
        if self.has_table("modifyTime"):
            self.session.add(ModifyTime(table_name, datetime.datetime.now()))
            self.session.commit()

    def exists_in_table(self, table_name: str = None, col_name: str = None, value: str = None,
                        condition_dict: dict = None,
                        return_result: bool = False, cursor=None):

        """
        表tableName中是否存在列col_name的值位value的行

        :param cursor: 连接了db文件的游标
        :param table_name: 表名
        :param col_name: 列名
        :param value: 列的值
        :param condition_dict: 查询的键值对字典值，优先于col_name和value传入的值，即会覆盖col_name和value传入的值
        :param return_result: 是否需要返回查找到的数据行，如果为真，则返回所有符合查找条件的数据行
        :return:
        """

        ...

    def select_in_table(self, table_name=None, condition_dict: dict = None, result_col: list | str = None, limit=10,
                        offset=0,
                        fuzzy=False, first_or_all="first", result_type=None, cls=None, **kwargs) -> Row | list | Any:
        """
        查

        精确查询，设置fuzzy为True，且condition_dict中的value为字符串值
        模糊查询，设置fuzzy为False，日期列不能使用模糊查询，只能使用范围查询
        范围查询，设置fuzzy为True，且condition_dict中的value为长度为2的列表，列表第一、二项分别为范围下、上限，且包含上下限

        当result_type=="json"时，返回的是一个list(dict)的json对象，即[{col1: value1, col2: value2,...}, ...}的json对象
        列表的每一项对应一条匹配的查询结果
        每一项的字典分别是{列名：值}

        kwargs={"date_format": "%Y-%m-%d %H:%M:%S"} 如果mysql中存在日期列，需要将日期转换为字符串，该参数定义日期字符串格式

        示例1：
        fetch = self.sql.select_in_table(cls=Holiday, condition_dict={"calendarDate": day_datetime},
                                         result_col=['isOpen'])

        :param table_name: 当使用传统查询方式时，需要传入数据库表名
        :param cls: 当使用ORM模型时，只需要传入数据库表在python中对应的映射类名，如果通过该方法查询，则查询到的数据会被自动转换为cls对象
        :param condition_dict:
        :param result_col: 不传入或传入空列表，则返回数据库中所有列
        :param limit:
        :param offset:
        :param fuzzy: 是否模糊查询
        :param first_or_all: 返回满足条件的第一个还是所有，支持"first", "all",
        :param result_type: 返回类型，如果为json，则返回为json格式的字符串
        :return: None或查询的列值列表或数据条的列表或sqlalchemy.engine.Row对象，出错时返回None，如列明不存在等；否则返回一个tuple类型的数据，长度为0表示未查询到满足条件的数据
        """
        # ---------------------- 如果使用table_name查询，则构建Table对象 ------------------------
        # Table对象可以当cls一样使用
        if cls is None:
            if self.has_table(table_name):
                table: Table = self.get_table(table_name)
                cls = table
        # ---------------------- 如果使用table_name查询，则构建Table对象 ------------------------
        # ----------------------- 根据条件字典，构建查询条件 --------------------------------
        condition = []
        for col, val in condition_dict.items():
            if isinstance(val, datetime.datetime) or isinstance(val, datetime.date):
                condition.append(f"{col}={val.__repr__()}")
            else:
                condition.append(f"{col}='{val}'")
        condition = ",".join(condition)
        # ----------------------- 根据条件字典，构建查询条件 --------------------------------

        # .filter_by(node=node, password=password).all()  # filter()不支持组合查询，filter_by支持
        _: Query = self.session.query(cls)
        expression = f"_.filter_by({condition})"
        _: Query = eval(expression)
        item = eval(f"_.{first_or_all}()")

        # ------------------------ 如果指定了返回的数据列，则取出数据列并返回 -----------------------
        if isinstance(result_col, str):
            result_col = [result_col]
        if result_col is None or len(result_col) == 0:
            return item
        else:
            # noinspection all
            _ = [getattr(item, col) for col in result_col]  # table_name和cls两种方法都适用
            if len(_) == 1:
                _ = _[0]
            return _
        # ------------------------ 如果指定了返回的数据列，则取出数据列并返回 -----------------------

    def insert_item(self, table_name: str = None, values: list = None,
                    col_names: list = None, ignore=False,
                    replace=False, filter_warning=None):
        """
        向数据库中插入数据，这里传入的列名不要用反引号括起来，增

        values中的数据类型需要与表中每列的数据类型一致，数据库和python中数据类型对应如下：
        SqlAlchemy          python
        DATETIME            datetime.datetime/datetime.date
        VARCHAR             str

        cols_names和values两个列表一一对应。

        :param table_name: 表名
        :param values:
        :param col_names: 列名，如果是插入带有auto_increment属性的表数据，则必须指定列名，否则就需要指定auto_increment属性的字段的值
        :param ignore: 当插入数据重复时，是否忽略
        :param replace: 当插入数据重复时，是否替换，ignore和replace不能同时为True
        :param filter_warning: 过滤警告信息，[1062, 1265, 1366]，分别对应["Duplicate", "Data truncated", "Incorrect integer value"]
        """
        _: Table = self.get_table(table_name)
        if col_names is None:
            col_names = self.get_column_names(table_name)
        paras = []
        for col, val in zip(col_names, values):
            if isinstance(val, datetime.datetime) or isinstance(val, datetime.date):
                val = val.__repr__()
                paras.append(f"{col}={val}")
            else:
                paras.append(f"{col}='{val}'")
        paras = ",".join(paras)
        state = f"_.insert().values({paras})"
        eval(state)
        self.session.commit()

    def has_table(self, table_name):
        """
        判断数据库中是否存在某个表
        """
        return self.engine.has_table(table_name)
        # tables = self.insp.get_table_names()
        # if table_name in tables:
        #     return True
        # else:
        #     return False

    def exist_table(self, table_name):
        """
        同has_table()
        """
        return self.has_table(table_name)

    def get_table(self, table_name=None):
        """
        获取表名为table_name的表对象，返回的是 Table()对象。
        如果不传入table_name，则返回数据库中的所有表，返回的是Table()对象的列表。
        """
        tables = [i for i in self.meta_data.tables.values()]
        if table_name is not None:
            for table in tables:
                if table.name == table_name:
                    return table
        return [i for i in self.meta_data.tables.values()]

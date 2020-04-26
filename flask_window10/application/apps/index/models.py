from application import db
from datetime import datetime
from application.utils.models import BaseModel


# 这里只用到了1对多，如果想了解更多的数据库关系可以移步到我的博客有一篇SQLAlchemy写了
class Department(BaseModel, db.Model):
    """部门表
    tablename 表示注册到数据库的表名称
    primary_key: 主键
    comment: 字段注释
    relationship（其实不用写，多对多才用到）: 表示关系的表，前面的Users是对象名，backref表示对方可以通过它来查到这个表，lazy懒惰式动态加载（可以提高性能）
    """
    __tablename__ = "department"
    id = db.Column(db.Integer, primary_key=True, comment="ID")
    name = db.Column(db.String(64), nullable=True, comment="部门名称")
    describe = db.Column(db.String(512), nullable=False, comment="部门描述")
    user_list = db.relationship('Users', backref='department', lazy='dynamic')


class Users(BaseModel, db.Model):
    """用户信息
    ForeignKey 连接模型的外键，用User查department则是正向查询
    """
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    username = db.Column(db.String(64), index=True, comment="用户名")
    password = db.Column(db.String(64), index=True, comment="密码")
    mobile = db.Column(db.String(64), index=True, comment="手机")
    department_id = db.Column(
        db.Integer,
        db.ForeignKey("department.id"),
        comment="部门ID")


class UsersWechart(BaseModel, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, comment="")
    uid = db.Column(db.String(128), nullable=False, comment="用户openid")
    uname = db.Column(db.String(40), comment="用户微信名")
    ugender = db.Column(db.SmallInteger, comment="用户性别")
    uaddress = db.Column(db.String(128), comment="用户地址")
    ubalance = db.Column(db.Integer, comment="用户积分余额")
    uavatar = db.Column(db.String(256), comment="用户头像引用地址")
    skey = db.Column(db.String(128), nullable=False, comment="用户登录态标识")
    sessionkey = db.Column(db.String(128), nullable=False, comment="微信登录态标识")


class Books(BaseModel, db.Model):
    __tablename__ = "books"
    bkid = db.Column(db.Integer, primary_key=True, comment="书籍id")
    bkclass = db.Column(db.Integer, comment="书籍类别")
    bkname = db.Column(db.String(48), nullable=False, comment="书籍名称")
    bkauthor = db.Column(db.String(32), nullable=False, comment="书籍作者")
    bkpublisher = db.Column(db.String(16), comment="书籍出版社")
    bkfile = db.Column(db.String(256), nullable=False, comment="书籍文件地址")
    bkcover = db.Column(db.String(120), comment="书籍封面")
    bkprice = db.Column(db.Integer, nullable=False, comment="书籍积分")

class BooksComment(BaseModel, db.Model):
    __tablename__ = "books_comment"
    cmid = db.Column(db.Integer, primary_key=True, comment="评论id")
    uid = db.Column(db.String(128), nullable=False, comment="用户openid")
    uname = db.Column(db.String(48), nullable=False, comment="用户名称")
    ccontent = db.Column(db.String(128), comment="评论内容")
    bkname = db.Column(db.String(16), nullable=False, comment="书籍名称")
    bkid = db.Column(db.String(256), nullable=False, comment="书籍ID")
    uavatar = db.Column(db.String(256), nullable=False, comment="用户头像")
    ctime = db.Column(db.DateTime, default=datetime.now, nullable=False, comment="评论时间")

class Orders(BaseModel, db.Model):
    __tablename__ = "orders"
    oid = db.Column(db.Integer, primary_key=True, comment="订单ID")
    uid = db.Column(db.String(128), nullable=False, comment="用户openid")
    oprice = db.Column(db.Integer, nullable=False, comment="商品价格")
    otime = db.Column(db.DateTime, default=datetime.now, comment="订单创建时间")
    gid = db.Column(db.String(16), nullable=False, comment="商品ID")

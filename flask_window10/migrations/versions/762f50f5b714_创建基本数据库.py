"""'创建基本数据库'

Revision ID: 762f50f5b714
Revises: 7653cb72994c
Create Date: 2020-04-26 21:30:15.033671

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '762f50f5b714'
down_revision = '7653cb72994c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('sort', sa.Integer(), nullable=True, comment='排序'),
    sa.Column('is_deleted', sa.Boolean(), nullable=True, comment='逻辑删除'),
    sa.Column('is_show', sa.Boolean(), nullable=True, comment='是否显示'),
    sa.Column('oid', sa.Integer(), nullable=False, comment='订单ID'),
    sa.Column('uid', sa.String(length=128), nullable=False, comment='用户openid'),
    sa.Column('oprice', sa.Integer(), nullable=False, comment='商品价格'),
    sa.Column('otime', sa.DateTime(), nullable=True, comment='订单创建时间'),
    sa.Column('gid', sa.String(length=16), nullable=False, comment='商品ID'),
    sa.PrimaryKeyConstraint('oid')
    )
    op.alter_column('users', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               comment='',
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               comment=None,
               existing_comment='',
               autoincrement=True)
    op.drop_table('orders')
    # ### end Alembic commands ###

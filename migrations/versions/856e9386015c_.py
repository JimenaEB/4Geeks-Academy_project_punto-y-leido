"""empty message

Revision ID: 856e9386015c
Revises: 
Create Date: 2020-11-23 15:53:19.637432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '856e9386015c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('biography', sa.Text(), nullable=False),
    sa.Column('image', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('synopsis', sa.Text(), nullable=False),
    sa.Column('format_type', sa.Enum('Tapa dura', 'Bolsillo', 'Ebook', 'Ilustrado', 'Tapa blanda'), nullable=False),
    sa.Column('genre', sa.Enum('Histórica', 'Romántica y erótica', 'Thriller', 'Ciencia ficción y fantástica', 'Biográfica', 'Juvenil', 'Novela gráfica', 'Clásicos'), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reader',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('follower',
    sa.Column('id_follower', sa.Integer(), nullable=True),
    sa.Column('id_followed', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_followed'], ['reader.id'], ),
    sa.ForeignKeyConstraint(['id_follower'], ['reader.id'], )
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('final_price', sa.Float(), nullable=False),
    sa.Column('reader_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reader_id'], ['reader.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_reader', sa.Integer(), nullable=False),
    sa.Column('id_book', sa.Integer(), nullable=False),
    sa.Column('stars', sa.Enum('1', '2', '3', '4', '5'), nullable=False),
    sa.Column('review', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['id_book'], ['book.id'], ),
    sa.ForeignKeyConstraint(['id_reader'], ['reader.id'], ),
    sa.PrimaryKeyConstraint('id', 'id_reader', 'id_book')
    )
    op.create_table('shelf',
    sa.Column('id_reader', sa.Integer(), nullable=False),
    sa.Column('id_book', sa.Integer(), nullable=False),
    sa.Column('shelf_name', sa.Enum('Comentados', 'Leídos', 'Favoritos', 'Pendientes', 'Comprados'), nullable=False),
    sa.ForeignKeyConstraint(['id_book'], ['book.id'], ),
    sa.ForeignKeyConstraint(['id_reader'], ['reader.id'], ),
    sa.PrimaryKeyConstraint('id_reader', 'id_book')
    )
    op.create_table('written_by',
    sa.Column('id_author', sa.Integer(), nullable=True),
    sa.Column('id_book', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_author'], ['author.id'], ),
    sa.ForeignKeyConstraint(['id_book'], ['book.id'], )
    )
    op.create_table('order_line',
    sa.Column('id_book', sa.Integer(), nullable=True),
    sa.Column('id_order', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_book'], ['book.id'], ),
    sa.ForeignKeyConstraint(['id_order'], ['order.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_line')
    op.drop_table('written_by')
    op.drop_table('shelf')
    op.drop_table('review')
    op.drop_table('order')
    op.drop_table('follower')
    op.drop_table('reader')
    op.drop_table('book')
    op.drop_table('author')
    # ### end Alembic commands ###

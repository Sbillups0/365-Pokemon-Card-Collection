"""create global inventory

Revision ID: e91d0c24f7d0
Revises:
Create Date: 2025-03-30 11:23:36.782933

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic. 
revision: str = "e91d0c24f7d0"
down_revision: Union[str, None] = "9b4118923246"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "packs",
        sa.Column("id", sa.Integer, sa.Identity(always=True, start=1), autoincrement=True, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("price", sa.Integer, nullable=False),
    )
    op.execute(sa.text(
            """
            INSERT INTO packs (name, price) 
            VALUES 
            ('Basic', 25), ('Jungle', 50), ('Fossil', 100), ('Team Rocket', 200)
            """
        )
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, sa.Identity(always=True, start=1), autoincrement=True, primary_key=True),
        sa.Column("username", sa.Text, nullable=False),
    )
    op.create_table(
        "inventory",
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), primary_key=True),
        sa.Column("pack", sa.Text, sa.ForeignKey("packs.name"), primary_key=True),
        sa.Column("quantity", sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table("packs")
    op.drop_table("users")
    op.drop_table("inventory")


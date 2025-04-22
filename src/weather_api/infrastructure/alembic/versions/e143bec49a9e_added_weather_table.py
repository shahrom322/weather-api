"""Added Weather table

Revision ID: e143bec49a9e
Revises:
Create Date: 2025-04-22 13:03:42.539774

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "e143bec49a9e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "weather",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column(
            "city",
            sa.Enum("MOSCOW", "LONDON", "TOKYO", name="cityenum"),
            nullable=False,
        ),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("temperature", sa.Numeric(precision=5, scale=2), nullable=False),
        sa.Column("humidity", sa.SmallInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_weather")),
    )
    op.create_index("idx_weather_city_date", "weather", ["city", "date"], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("idx_weather_city_date", table_name="weather")
    op.drop_table("weather")
    op.execute("DROP TYPE cityenum")

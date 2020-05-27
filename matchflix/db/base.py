# Import all the models, so that Base has them before being
# imported by Alembic
from matchflix.db.base_class import Base  # noqa
from matchflix.models.answer import Answer  # noqa
from matchflix.models.release import Release  # noqa
from matchflix.models.user import User  # noqa

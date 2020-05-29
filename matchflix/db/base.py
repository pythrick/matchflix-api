# Import all the models, so that Base has them before being
# imported by Alembic
from matchflix.db.base_class import Base  # noqa
from .models import Answer  # noqa
from .models import Release  # noqa
from .models import User  # noqa

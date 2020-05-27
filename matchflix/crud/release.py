from matchflix.crud.base import CRUDBase
from matchflix.models.release import Release
from matchflix.schemas.release import ReleaseCreate, ReleaseUpdate


class CRUDRelease(CRUDBase[Release, ReleaseCreate, ReleaseUpdate]):
    pass


release = CRUDRelease(Release)

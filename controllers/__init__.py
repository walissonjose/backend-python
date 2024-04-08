from . import user
from . import room
from . import meeting

routes = [
    user.router,
    room.router,
    meeting.router
]

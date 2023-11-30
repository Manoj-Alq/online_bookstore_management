from configuration.config import *
from api.admin.admin_router import *
from api.author.author_router import *
import uvicorn

Base.metadata.create_all(bind=engine)
router.mount('/api/v1', router )

if __name__ == '__main__':
    uvicorn.run("main:router", host="localhost",port=5001, reload=True)
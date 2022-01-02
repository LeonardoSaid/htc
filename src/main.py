import uvicorn
from starlette.applications import Starlette

from router import Router

from config.settings import SERVICE_HOST, SERVICE_PORT, LOGGER


def main():
    app = Starlette(debug=True, routes=Router.get_routes())
    LOGGER.debug('############# Cart Service Initialized #############')
    uvicorn.run(app, host=SERVICE_HOST, port=SERVICE_PORT)


if __name__ == '__main__':
    main()

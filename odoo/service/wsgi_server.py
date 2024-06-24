import warnings
import crossnow.http


def application(environ, start_response):

    warnings.warn("The WSGI application entrypoint moved from "
                  "crossnow.service.wsgi_server.application to crossnow.http.root "
                  "in 15.3.",
                  DeprecationWarning, stacklevel=1)
    return crossnow.http.root(environ, start_response)

import logging

import azure.functions as func


def main( req: func.HttpRequest ) -> func.HttpResponse:
    logging.info( "Python HTTP trigger function processed a request." )

    name = req.params.get( "name" )
    if not name:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )

    return func.HttpResponse( f"Hello {name}!" )

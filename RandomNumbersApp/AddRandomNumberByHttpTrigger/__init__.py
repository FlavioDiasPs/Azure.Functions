import logging
import pyodbc
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:dblearning.database.windows.net,1433;Database=DbLearning;Uid=flaviodiasps@dblearning;Pwd=Flavio973119;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()    

    cursor.execute("insert into RandomNumbers values(1, 1, 1, 1)")
    conn.commit()

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    
    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )

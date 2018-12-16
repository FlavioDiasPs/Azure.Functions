import pyodbc
import logging
import azure.functions as func

def main(event: func.EventHubEvent):
    logging.info(f'Event Hubs trigger function processed message: {event.get_body()}')
    logging.info(f'  EnqueuedTimeUtc = {event.enqueued_time}')
    logging.info(f'  SequenceNumber = {event.sequence_number}')
    logging.info(f'  Offset = {event.offset}')
    
    conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:dblearning.database.windows.net,1433;Database=DbLearning;Uid=flaviodiasps@dblearning;Pwd=Flavio973119;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()

    cursor.execute("insert into RandomNumbers values(1, 1, 1, 1)")
    conn.commit()

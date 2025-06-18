import grpc
import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

import patient_pb2
import patient_pb2_grpc

# Load env variables
load_dotenv()
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]

# Connect to db
try:
    conn = psycopg2.connect(
        dbname = "quackmed",
        user = DB_USERNAME,
        password = DB_PASSWORD,
        host = "127.0.0.1"
    )
    cur = conn.cursor()
except:
    print("DB connection error")


# Service for patient stuff
class PatientService(patient_pb2_grpc.PatientService):

    def CreatePatient(self, request, context):
        print(f"Creating patient {request.firstname}")
        dob = datetime.strptime(request.dob, "%d-%m-%Y").date()
        cur.execute("INSERT INTO patients (first_name, last_name, notes, date_of_birth) values (%s, %s, %s, %s)", (request.first_name, request.last_name, request.notes, dob))
        conn.commit()
        return patient_pb2.create_patient_response(success=True)

    def GetPatientDetails(self, request, context):
        pass


    def ListPatients(self, request, context):
        cur.execute("SELECT id FROM patients WHERE first_name = %s AND last_name = %s", (request.first_name, request.last_name))
        rows = cur.fetchall()
        patients = []
        for row in rows:
            print(row)
            cur.execute("SELECT * FROM patients WHERE id = %s", (row))
            patient_data = cur.fetchone()
            id = patient_data[0]
            first_name = patient_data[1]
            last_name = patient_data[2]
            notes = patient_data[3]
            dob = patient_data[4]
            patients.append(patient_pb2.patient_details(patient_id=id, first_name=first_name, last_name=last_name, notes=notes, dob=dob))

        return patient_pb2.list_patients_response(patients=patients)


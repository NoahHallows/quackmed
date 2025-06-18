import patient_pb2
import patient_pb2_grpc
from backend.connectionManager import GRPCConnectionManager

class PatientManager:
    def __init__(self):
        self.conn = GRPCConnectionManager()
        self.stub = self.conn.get_stub(patient_pb2_grpc.PatientServiceStub)

    def update_stub(self):
        self.stub = self.conn.get_stub(patient_pb2_grpc.PatientServiceStub)

    def create_patient(self, first_name, last_name, notes, dob): 
        print(dob, notes)
        response = self.stub.CreatePatient(patient_pb2.patient_details(patient_id=0, first_name=first_name, last_name=last_name, notes=notes, dob=dob))
        return response.success

    def get_patient_details(self, patient_id):
        response = self.stub.GetPatientDetails(patient_pb2.patient_details_request(patient_id=patient_id))
        print(response)
        return response

    def get_patient_list(self, first_name, last_name):
        response = self.stub.ListPatients(patient_pb2.list_patients_request(patient_id=1, first_name=first_name, last_name=last_name, number_of_results=5))
        return response

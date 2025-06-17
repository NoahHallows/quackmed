pyside6-uic ui/mainwindow.ui -o ui/MainWindow.py
pyside6-uic ui/appointmentBook.ui -o ui/AppointmentBook.py
pyside6-uic ui/LoginWidget.ui -o ui/LoginWindow.py
pyside6-uic ui/userList.ui -o ui/UserListWindow.py
pyside6-uic ui/patientList.ui -o ui/PatientList.py

python -m grpc_tools.protoc -I ../proto --python_out=backend/grpc \
         --grpc_python_out=backend/grpc ../proto/auth.proto

python -m grpc_tools.protoc -I ../proto --python_out=backend/grpc \
         --grpc_python_out=backend/grpc ../proto/appointment_book.proto

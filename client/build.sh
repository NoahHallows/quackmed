pyside6-uic ui/mainwindow.ui -o ui/MainWindowCompiled.py
pyside6-uic ui/appointmentBook.ui -o ui/AppointmentBookCompiled.py
pyside6-uic ui/LoginWidget.ui -o ui/LoginWindowCompiled.py
pyside6-uic ui/userList.ui -o ui/UserListWindowCompiled.py
pyside6-uic ui/patientList.ui -o ui/PatientListCompiled.py
pyside6-uic ui/createUser.ui -o ui/CreateUserCompiled.py

python -m grpc_tools.protoc -I ../proto --python_out=backend/grpc \
         --grpc_python_out=backend/grpc ../proto/auth.proto

python -m grpc_tools.protoc -I ../proto --python_out=backend/grpc \
         --grpc_python_out=backend/grpc ../proto/appointment_book.proto

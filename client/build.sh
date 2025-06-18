pyside6-uic ui/mainwindow.ui -o ui/MainWindowCompiled.py
pyside6-uic ui/appointmentBook.ui -o ui/AppointmentBookCompiled.py
pyside6-uic ui/LoginWidget.ui -o ui/LoginWindowCompiled.py
pyside6-uic ui/userList.ui -o ui/UserListWindowCompiled.py
pyside6-uic ui/patientList.ui -o ui/PatientListCompiled.py
pyside6-uic ui/createUser.ui -o ui/CreateUserCompiled.py
pyside6-uic ui/PatientDetails.ui -o ui/PatientDetails.py

python -m grpc_tools.protoc -I ../proto --python_out=. \
         --grpc_python_out=. ../proto/auth.proto

python -m grpc_tools.protoc -I ../proto --python_out=. \
         --grpc_python_out=. ../proto/appointment_book.proto

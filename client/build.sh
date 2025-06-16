pyside6-uic ui/mainwindow.ui -o ui/MainWindow.py
pyside6-uic ui/appointmentBook.ui -o ui/AppointmentBook.py
pyside6-uic ui/LoginWidget.ui -o ui/LoginWindow.py
pyside6-uic ui/userList.ui -o ui/UserListWindow.py

python -m grpc_tools.protoc -I ../proto --python_out=. \
         --grpc_python_out=. ../proto/auth.proto

python -m grpc_tools.protoc -I ../proto --python_out=. \
         --grpc_python_out=. ../proto/appointment_book.proto

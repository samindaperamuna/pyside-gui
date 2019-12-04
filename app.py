import os
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QLabel, QGridLayout, QLineEdit, QDialog, QPushButton, QMessageBox


class Main(QDialog):
    width = 1024
    height = 600
    stylesheet = "styles.qss"

    def __init__(self):
        super().__init__()

        self.setStyleSheet(open(self.stylesheet, 'r').read())

        self.lblPath = QLabel("OTP write script path:")
        self.lblPathParam = QLabel()
        self.txtPath = QLineEdit()

        self.lblBoard = QLabel("Board")
        self.lblBoardParam = QLabel("-b")
        self.txtBoard = QLineEdit()

        self.lblEyeQAddress = QLabel("EyeQ serial port address:")
        self.lblEyeQAddressParam = QLabel("--eyeq_port")
        self.txtEyeQAddress = QLineEdit()

        self.lblMCUAddress = QLabel("MCU serial port address:")
        self.lblMCUAddressParam = QLabel("--mcu_port")
        self.txtMCUAddress = QLineEdit()

        self.lblMCUBaudRate = QLabel("MCU baud rate:")
        self.lblMCUBaudRateParam = QLabel("--mcu_baudrate")
        self.txtMCUBaudRate = QLineEdit()

        self.lblPathToImage = QLabel("Path to image that write OTP:")
        self.lblPathToImageParam = QLabel("-x")
        self.txtPathToImage = QLineEdit()

        self.lblSerialNumber = QLabel("Serial number:")
        self.lblSerialNumberParam = QLabel("-s")
        self.txtSerialNumber = QLineEdit()

        self.button = QPushButton("Flash OTP")
        self.button.clicked.connect(self.button_click)

        layout = QGridLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setVerticalSpacing(5)
        layout.setColumnMinimumWidth(0, 300)
        layout.setRowStretch(7, 1)

        layout.addWidget(self.lblPath, 0, 0)
        layout.addWidget(self.lblPathParam, 0, 1)
        layout.addWidget(self.txtPath, 0, 2)

        layout.addWidget(self.lblBoard, 1, 0)
        layout.addWidget(self.lblBoardParam, 1, 1)
        layout.addWidget(self.txtBoard, 1, 2)

        layout.addWidget(self.lblEyeQAddress, 2, 0)
        layout.addWidget(self.lblEyeQAddressParam, 2, 1)
        layout.addWidget(self.txtEyeQAddress, 2, 2)

        layout.addWidget(self.lblMCUAddress, 3, 0)
        layout.addWidget(self.lblMCUAddressParam, 3, 1)
        layout.addWidget(self.txtMCUAddress, 3, 2)

        layout.addWidget(self.lblMCUBaudRate, 4, 0)
        layout.addWidget(self.lblMCUBaudRateParam, 4, 1)
        layout.addWidget(self.txtMCUBaudRate, 4, 2)

        layout.addWidget(self.lblPathToImage, 5, 0)
        layout.addWidget(self.lblPathToImageParam, 5, 1)
        layout.addWidget(self.txtPathToImage, 5, 2)

        layout.addWidget(self.lblSerialNumber, 6, 0)
        layout.addWidget(self.lblSerialNumberParam, 6, 1)
        layout.addWidget(self.txtSerialNumber, 6, 2)

        layout.addWidget(self.button, 7, 0, 1, 3, alignment=Qt.AlignVCenter)

        self.setLayout(layout)

    def button_click(self):
        if self.validate():
            script_path = self.txtPath.text()
            board = self.txtBoard.text()
            eye_q_serial = self.txtEyeQAddress.text()
            mcu_serial = self.txtMCUAddress.text()
            baud_rate = self.txtMCUBaudRate.text()
            image_path = self.txtPathToImage.text()
            serial = self.txtSerialNumber.text()

            # Run in a OS shell because the script uses Python 2
            os.system(("python2.7 {script_path} -b {board} --eyeq_port {eye_q_serial} --mcu_port {mcu_serial}" +
                       " --mcu_baudrate {baud_rate} -x {image_path} -s {serial}").format(script_path=script_path,
                                                                                         board=board,
                                                                                         eye_q_serial=eye_q_serial,
                                                                                         mcu_serial=mcu_serial,
                                                                                         baud_rate=baud_rate,
                                                                                         image_path=image_path,
                                                                                         serial=serial))

    def validate(self):
        invalid_control = None
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Missing required field(s)")
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.addButton('OK', QMessageBox.AcceptRole)

        if self.txtPath.text().__eq__(""):
            msg_box.setText("Please enter the OTP write script path.")
            invalid_control = self.txtPath
        elif self.txtBoard.text().__eq__(""):
            msg_box.setText("Please enter the board.")
            invalid_control = self.txtBoard
        elif self.txtEyeQAddress.text().__eq__(""):
            msg_box.setText("Please enter the EyeQ serial port address.")
            invalid_control = self.txtEyeQAddress
        elif self.txtMCUAddress.text().__eq__(""):
            msg_box.setText("Please enter the MCU serial port address.")
            invalid_control = self.txtMCUAddress
        elif self.txtMCUBaudRate.text().__eq__(""):
            msg_box.setText("Please enter the MCU baud rate.")
            invalid_control = self.txtMCUBaudRate
        elif self.txtPathToImage.text().__eq__(""):
            msg_box.setText("Please enter the path to image that write OTP.")
            invalid_control = self.txtPathToImage
        elif self.txtSerialNumber.text().__eq__(""):
            msg_box.setText("Please enter the serial number.")
            invalid_control = self.txtSerialNumber

        if invalid_control is None:
            return True
        else:
            msg_box.exec()
            invalid_control.setFocus()
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = Main()
    widget.setFixedSize(Main.width, Main.height)
    widget.show()

    sys.exit(app.exec_())

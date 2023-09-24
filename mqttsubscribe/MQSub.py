from PyQt5 import QtWidgets,uic
import sys
from functionsforMQTTBasicUI import sub
class BasicUI(QtWidgets.QDialog):
    def __init__(self):
        super(BasicUI, self).__init__()
        uic.loadUi('MQTTBasicUI2.ui',self)
        self.btnShow.clicked.connect(self.showinstantdata)
    def showinstantdata(self):
        username=self.txtUsername.text()
        password=self.txtPassword.text()
        broker=self.cmbboxBrokerAdrr.currentText()
        #wait=int(self.txtWaitTime.text())
        topic=self.txtTopic.text()

        #sub(broker,username,password,topic)
        #print(type(message))
        sub(broker, username, password, topic)

        #self.lblExtract.setText(message)




app = QtWidgets.QApplication(sys.argv)
window = BasicUI()
widget=QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(910)
widget.setFixedHeight(670)
widget.show()
app.exec_()

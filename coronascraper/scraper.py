from PyQt5 import QtCore, QtGui, QtWidgets

import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(r.content, "html5lib")
data = {x.text: y.text for x, y in zip(soup.select(
    "#maincounter-wrap h1"), soup.select("#maincounter-wrap span"))}


links = {'USA': 'country/us/', 'Spain': 'country/spain/', 'Italy': 'country/italy/', 'France': 'country/france/', 'Germany': 'country/germany/', 'UK': 'country/uk/', 'Turkey': 'country/turkey/', 'Iran': 'country/iran/', 'Russia': 'country/russia/', 'Brazil': 'country/brazil/', 'Belgium': 'country/belgium/', 'Canada': 'country/canada/', 'Netherlands': 'country/netherlands/', 'Switzerland': 'country/switzerland/', 'India': 'country/india/', 'Portugal': 'country/portugal/', 'Ecuador': 'country/ecuador/', 'Peru': 'country/peru/', 'Ireland': 'country/ireland/', 'Sweden': 'country/sweden/', 'Saudi Arabia': 'country/saudi-arabia/', 'Austria': 'country/austria/', 'Israel': 'country/israel/', 'Mexico': 'country/mexico/', 'Japan': 'country/japan/', 'Singapore': 'country/singapore/', 'Chile': 'country/chile/', 'Pakistan': 'country/pakistan/', 'Poland': 'country/poland/', 'S. Korea': 'country/south-korea/', 'Romania': 'country/romania/', 'Belarus': 'country/belarus/', 'Qatar': 'country/qatar/', 'UAE': 'country/united-arab-emirates/', 'Indonesia': 'country/indonesia/', 'Denmark': 'country/denmark/', 'Ukraine': 'country/ukraine/', 'Serbia': 'country/serbia/', 'Norway': 'country/norway/', 'Philippines': 'country/philippines/', 'Czechia': 'country/czech-republic/', 'Australia': 'country/australia/', 'Dominican Republic': 'country/dominican-republic/', 'Malaysia': 'country/malaysia/', 'Panama': 'country/panama/', 'Bangladesh': 'country/bangladesh/', 'Colombia': 'country/colombia/', 'Finland': 'country/finland/', 'South Africa': 'country/south-africa/', 'Egypt': 'country/egypt/', 'Morocco': 'country/morocco/', 'Luxembourg': 'country/luxembourg/', 'Argentina': 'country/argentina/', 'Algeria': 'country/moldova/', 'Moldova': 'country/algeria/', 'Thailand': 'country/thailand/', 'Kuwait': 'country/kuwait/', 'Bahrain': 'country/bahrain/', 'Kazakhstan': 'country/kazakhstan/', 'Greece': 'country/greece/', 'Hungary': 'country/hungary/', 'Croatia': 'country/croatia/', 'Oman': 'country/oman/', 'Uzbekistan': 'country/uzbekistan/', 'Iceland': 'country/iceland/', 'Iraq': 'country/iraq/', 'Armenia': 'country/armenia/', 'Estonia': 'country/estonia/', 'Azerbaijan': 'country/azerbaijan/', 'Cameroon': 'country/cameroon/', 'Bosnia and Herzegovina': 'country/bosnia-and-herzegovina/', 'Afghanistan': 'country/afghanistan/', 'New Zealand': 'country/new-zealand/', 'Lithuania': 'country/lithuania/', 'Slovenia': 'country/slovenia/', 'Slovakia': 'country/slovakia/', 'North Macedonia': 'country/macedonia/', 'Cuba': 'country/cuba/', 'Ghana': 'country/ghana/', 'Bulgaria': 'country/bulgaria/', 'Nigeria': 'country/nigeria/', 'Ivory Coast': 'country/cote-d-ivoire/', 'Hong Kong': 'country/china-hong-kong-sar/', 'Djibouti': 'country/djibouti/', 'Guinea': 'country/guinea/', 'Tunisia': 'country/tunisia/', 'Bolivia': 'country/bolivia/', 'Cyprus': 'country/cyprus/', 'Latvia': 'country/latvia/', 'Andorra': 'country/andorra/', 'Albania': 'country/albania/', 'Lebanon': 'country/lebanon/', 'Costa Rica': 'country/costa-rica/', 'Niger': 'country/niger/', 'Kyrgyzstan': 'country/kyrgyzstan/', 'Burkina Faso': 'country/burkina-faso/', 'Senegal': 'country/senegal/', 'Honduras': 'country/honduras/', 'Uruguay': 'country/uruguay/', 'Channel Islands': 'country/channel-islands/', 'San Marino': 'country/san-marino/', 'Palestine': 'country/state-of-palestine/', 'Georgia': 'country/georgia/', 'Malta': 'country/malta/', 'Jordan': 'country/jordan/', 'Sri Lanka': 'country/sri-lanka/', 'Guatemala': 'country/guatemala/', 'Taiwan': 'country/taiwan/', 'DRC': 'country/democratic-republic-of-the-congo/', 'Réunion': 'country/reunion/', 'Mayotte': 'country/somalia/', 'Kenya': 'country/mayotte/', 'Mauritius': 'country/kenya/', 'Somalia': 'country/mauritius/', 'Mali': 'country/mali/', 'Montenegro': 'country/montenegro/', 'Venezuela': 'country/venezuela/', 'Isle of Man': 'country/isle-of-man/', 'Tanzania': 'country/tanzania/', 'Jamaica': 'country/jamaica/', 'El Salvador': 'country/el-salvador/', 'Vietnam': 'country/viet-nam/', 'Paraguay': 'country/paraguay/', 'Equatorial Guinea': 'country/equatorial-guinea/', 'Congo': 'country/congo/', 'Faeroe Islands': 'country/faeroe-islands/', 'Rwanda': 'country/rwanda/', 'Sudan': 'country/sudan/', 'Gabon': 'country/gabon/', 'Martinique': 'country/martinique/', 'Guadeloupe': 'country/guadeloupe/', 'Myanmar': 'country/myanmar/', 'Brunei ': 'country/brunei-darussalam/', 'Maldives': 'country/maldives/', 'Gibraltar': 'country/gibraltar/', 'Madagascar': 'country/madagascar/', 'Ethiopia': 'country/ethiopia/', 'Cambodia': 'country/cambodia/', 'Liberia': 'country/liberia/', 'Trinidad and Tobago': 'country/trinidad-and-tobago/', 'French Guiana': 'country/french-guiana/', 'Aruba': 'country/aruba/', 'Bermuda': 'country/bermuda/', 'Monaco': 'country/togo/', 'Togo': 'country/monaco/', 'Cabo Verde': 'country/cabo-verde/', 'Zambia': 'country/zambia/', 'Sierra Leone': 'country/sierra-leone/', 'Liechtenstein': 'country/liechtenstein/', 'Barbados': 'country/barbados/', 'Uganda': 'country/uganda/', 'Sint Maarten': 'country/sint-maarten/', 'Bahamas': 'country/bahamas/', 'Guyana': 'country/guyana/', 'Haiti': 'country/haiti/', 'Cayman Islands': 'country/cayman-islands/', 'Mozambique': 'country/mozambique/', 'Libya': 'country/libya/', 'French Polynesia': 'country/french-polynesia/', 'Benin': 'country/benin/', 'Guinea-Bissau': 'country/guinea-bissau/', 'Nepal': 'country/nepal/', 'Macao': 'country/china-macao-sar/', 'Syria': 'country/syria/', 'Eswatini': 'country/swaziland/', 'Chad': 'country/chad/', 'Eritrea': 'country/eritrea/', 'Saint Martin': 'country/saint-martin/', 'Mongolia': 'country/mongolia/', 'Malawi': 'country/malawi/', 'Zimbabwe': 'country/zimbabwe/', 'Angola': 'country/angola/', 'Antigua and Barbuda': 'country/antigua-and-barbuda/', 'Timor-Leste': 'country/timor-leste/', 'Botswana': 'country/botswana/', 'Laos': 'country/laos/', 'Belize': 'country/belize/', 'Fiji': 'country/fiji/', 'New Caledonia': 'country/new-caledonia/', 'Curaçao': 'country/curacao/', 'CAR': 'country/central-african-republic/', 'Dominica': 'country/dominica/', 'Namibia': 'country/namibia/', 'Grenada': 'country/grenada/', 'Saint Kitts and Nevis': 'country/saint-kitts-and-nevis/', 'Saint Lucia': 'country/saint-lucia/', 'St. Vincent Grenadines': 'country/saint-vincent-and-the-grenadines/', 'Falkland Islands': 'country/falkland-islands-malvinas/', 'Nicaragua': 'country/nicaragua/', 'Burundi': 'country/burundi/', 'Montserrat': 'country/montserrat/', 'Turks and Caicos': 'country/turks-and-caicos-islands/', 'Greenland': 'country/greenland/', 'Seychelles': 'country/seychelles/', 'Gambia': 'country/gambia/', 'Suriname': 'country/suriname/', 'Vatican City': 'country/holy-see/', 'Papua New Guinea': 'country/papua-new-guinea/', 'Mauritania': 'country/mauritania/', 'Bhutan': 'country/bhutan/', 'St. Barth': 'country/saint-barthelemy/', 'Western Sahara': 'country/western-sahara/', 'British Virgin Islands': 'country/british-virgin-islands/', 'Caribbean Netherlands': 'country/caribbean-netherlands/', 'South Sudan': 'country/south-sudan/', 'Sao Tome and Principe': 'country/sao-tome-and-principe/', 'Anguilla': 'country/anguilla/', 'Saint Pierre Miquelon': 'country/saint-pierre-and-miquelon/', 'Yemen': 'country/yemen/', 'China': 'country/china/'}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 257)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 60, 451, 121))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.layoutform = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.layoutform.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layoutform.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.layoutform.setContentsMargins(0, 0, 0, 0)
        self.layoutform.setObjectName("layoutform")
        self.label_country = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        self.label_country.setFont(font)
        self.label_country.setObjectName("label_country")
        self.layoutform.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_country)
        self.label_cases = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        self.label_cases.setFont(font)
        self.label_cases.setObjectName("label_cases")
        self.layoutform.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_cases)
        self.data_case = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        self.data_case.setFont(font)
        self.data_case.setObjectName("data_case")
        self.layoutform.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.data_case)
        self.label_deaths = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        self.label_deaths.setFont(font)
        self.label_deaths.setObjectName("label_deaths")
        self.layoutform.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_deaths)
        self.data_deaths = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        self.data_deaths.setFont(font)
        self.data_deaths.setObjectName("data_deaths")
        self.layoutform.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.data_deaths)
        self.comboBox_country = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox_country.setEditable(False)
        self.comboBox_country.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_country.setObjectName("comboBox_country")
        self.layoutform.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_country)
        self.comboBox_country.addItem("")
        self.comboBox_country.setItemText(0, QtCore.QCoreApplication.translate("MainWindow", "Global"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Fira Mono for Powerline")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 40, 171, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(390, 180, 113, 32))
        self.pushButton_submit.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_submit.setAutoDefault(False)
        self.pushButton_submit.setDefault(False)
        self.pushButton_submit.setFlat(False)
        self.pushButton_submit.setObjectName("pushButton_submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 533, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_country.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_submit.clicked.connect(self.request)

    def request(self):
        if self.comboBox_country.currentText()=="Global":
            r = requests.get(
                "https://www.worldometers.info/coronavirus/")
        else:
            r = requests.get(
                "https://www.worldometers.info/coronavirus/"+links[self.comboBox_country.currentText()])
        soup = BeautifulSoup(r.content, "html5lib")
        data = {x.text: y.text for x, y in zip(soup.select(
            "#maincounter-wrap h1"), soup.select("#maincounter-wrap span"))}
        self.data_case.setText(data["Coronavirus Cases:"])
        self.data_deaths.setText(data["Deaths:"])
        self.data_case.repaint()
        self.data_deaths.repaint()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CoronaScraper"))
        self.label_country.setText(_translate("MainWindow", "Country"))
        self.label_cases.setText(_translate("MainWindow", "Coronavirus Cases"))
        self.data_case.setText(_translate("MainWindow", data["Coronavirus Cases:"]))
        self.label_deaths.setText(_translate("MainWindow", "Deaths"))
        self.data_deaths.setText(_translate("MainWindow", data["Deaths:"]))
        for i in range(len(links.keys())):
	        self.comboBox_country.addItem("")
	        self.comboBox_country.setItemText(i+1, _translate("MainWindow", sorted(links.keys())[i]))
        self.label.setText(_translate("MainWindow", "Coronavirus (COVID-19) Data)"))
        self.comboBox_country.setCurrentText(_translate("MainWindow", "Global"))
        self.label_2.setText(_translate("MainWindow", "from WORLDOMETER.COM"))
        self.pushButton_submit.setText(_translate("MainWindow", "Submit"))
        self.pushButton_submit.setShortcut(_translate("MainWindow", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

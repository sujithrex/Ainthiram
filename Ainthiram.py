import glob
import shutil

from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyPDF2 import PdfFileReader, PdfFileWriter
from googleapiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import subprocess
import time
import os
import io
import httplib2
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(731, 658)
        self.headingLabel = QtWidgets.QLabel(Dialog)
        self.headingLabel.setGeometry(QtCore.QRect(90, 30, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(26)
        self.headingLabel.setFont(font)
        self.headingLabel.setObjectName("headingLabel")
        self.autherLabel = QtWidgets.QLabel(Dialog)
        self.autherLabel.setGeometry(QtCore.QRect(90, 80, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Source Serif Pro Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.autherLabel.setFont(font)
        self.autherLabel.setObjectName("autherLabel")
        self.pdfLabel = QtWidgets.QLabel(Dialog)
        self.pdfLabel.setGeometry(QtCore.QRect(90, 160, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pdfLabel.setFont(font)
        self.pdfLabel.setObjectName("pdfLabel")
        self.scLabel = QtWidgets.QLabel(Dialog)
        self.scLabel.setGeometry(QtCore.QRect(20, 230, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scLabel.setFont(font)
        self.scLabel.setObjectName("scLabel")
        self.pdfTextEdit = QtWidgets.QLineEdit(Dialog)
        self.pdfTextEdit.setGeometry(QtCore.QRect(380, 190, 211, 22))
        self.pdfTextEdit.setObjectName("pdfTextEdit")
        self.scTextEdit = QtWidgets.QLineEdit(Dialog)
        self.scTextEdit.setGeometry(QtCore.QRect(380, 260, 211, 22))
        self.scTextEdit.setObjectName("scTextEdit")
        self.scButton = QtWidgets.QPushButton(Dialog)
        self.scButton.setGeometry(QtCore.QRect(610, 260, 81, 21))
        self.scButton.setObjectName("scButton")
        self.pdfButton = QtWidgets.QPushButton(Dialog)
        self.pdfButton.setGeometry(QtCore.QRect(610, 190, 81, 21))
        self.pdfButton.setObjectName("pdfButton")
        self.convertButton = QtWidgets.QPushButton(Dialog)
        self.convertButton.setGeometry(QtCore.QRect(350, 330, 93, 28))
        self.convertButton.setObjectName("convertButton")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(50, 420, 631, 191))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 629, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.processText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.processText.setGeometry(QtCore.QRect(0, 0, 631, 191))
        self.processText.setObjectName("processText")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.processLabel = QtWidgets.QLabel(Dialog)
        self.processLabel.setGeometry(QtCore.QRect(60, 380, 191, 21))
        self.processLabel.setObjectName("processLabel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(590, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(590, 70, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.headingLabel.setText(_translate("Dialog", "Ainthiram"))
        self.autherLabel.setText(_translate("Dialog", "Multi Lingustic Bulk OCR "))
        self.pdfLabel.setText(_translate("Dialog", "Please select your PDF  File  :"))
        self.scLabel.setText(_translate("Dialog", "Please select your Secret Client  File  :"))
        self.scButton.setText(_translate("Dialog", "Browse"))
        self.pdfButton.setText(_translate("Dialog", "Browse"))
        self.convertButton.setText(_translate("Dialog", "Convert"))
        self.processLabel.setText(_translate("Dialog", "Progress Terminal"))
        self.label.setText(_translate("Dialog", "@sujithRex"))
        self.label_2.setText(_translate("Dialog", "Github"))



class myForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pdfButton.clicked.connect(self.pdfbrowseFiles)
        self.ui.scButton.clicked.connect(self.scbrowseFiles)
        self.ui.convertButton.clicked.connect(self.functionBase)



    def pdfbrowseFiles(self):
        pdffname = QFileDialog.getOpenFileName(self, "open file", 'C:\\')
        self.ui.pdfTextEdit.setText(pdffname[0])
        pdfPath = pdffname[0]



    def scbrowseFiles(self):
        scname = QFileDialog.getOpenFileName(self, "open file", 'C:\\')
        self.ui.scTextEdit.setText(scname[0])
        scPath = scname[0]


    '''Function Base Started '''

    def functionBase(self):
        self.folderCreator()

        '''Working Thread'''

        self.pdftosignal = workingThread(str(self.ui.pdfTextEdit.text()),str(self.ui.scTextEdit.text()))
        self.pdftosignal.start()
        self.pdftosignal.update_process.connect(self.threadDone)




    def threadDone(self, str):
        self.ui.processText.appendPlainText(str)


    '''Click Actions Strated from Here!!'''

    def folderCreator(self):
        self.ui.processText.appendPlainText("Preprocessing Started")
        mydir = self.ui.pdfTextEdit.text().replace('.pdf', '')
        os.mkdir(mydir)
        os.mkdir(mydir + '/first_process')
        os.mkdir(mydir + '/jpg')
        os.mkdir(mydir + '/text')




class workingThread(QThread):
    update_process = pyqtSignal(str)

    def __init__(self, foo,boo):
        super(workingThread, self).__init__()
        self.foo = foo
        self.boo = boo

    def run(self):
        def singlePdfSplit ():
            try:
                path = self.foo
                firstProcess = path.replace('.pdf', '') + '/first_process'
                self.update_process.emit("Your PDF Split into Pages")
                pdf = PdfFileReader(path)
                for page in range(pdf.getNumPages()):
                    pdf_writer = PdfFileWriter()
                    pdf_writer.addPage(pdf.getPage(page))
                    output_filename = firstProcess + '/' + '{}.pdf'.format(page + 10000)
                    with open(output_filename, 'wb') as out:
                        pdf_writer.write(out)
                        processField = page
                    self.update_process.emit("Page number " + str(page) + " is Converted to single Page")

            except:
                self.update_process.emit("Sorry We Cannot Process your PDF Please Try Again")

        def secondProcesspa():

            try:
                path = self.foo
                firstProcess = path.replace('.pdf', '') + '/first_process'
                jpg = path.replace('.pdf', '') + '/jpg'
                for root, dirs, file in os.walk(firstProcess):
                    for i, files in enumerate(file):
                        cmd = r'magick convert -density 300 -trim ' + root + '/' + files + ' -quality 100 ' + jpg + '/' + files + '.jpg'
                        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                             stdin=subprocess.PIPE)
                        self.update_process.emit("Page number " +str(i)+ " is Converted to Image")

            except:
                self.update_process.emit("Please Install Magix and GHostScript For Image conversion")

        def googleImageVision():

            path = self.foo
            mykey = self.boo
            def googleVision():

                sctkey = mykey
                jpg = path.replace('.pdf', '') + '/jpg'
                # googleApi.googleDriveApi(sctkey,jpg)
                try:
                    import argparse
                    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
                except ImportError:
                    flags = None

                SCOPES = 'https://www.googleapis.com/auth/drive'
                CLIENT_SECRET_FILE = sctkey
                APPLICATION_NAME = 'Drive API Python Quickstart'
                self.update_process.emit("Gathering Data from your secret File")

                def get_credentials():
                    credential_path = os.path.join(path.replace('.pdf', '')+"/", 'drive-python-quickstart.json')
                    store = Storage(credential_path)
                    credentials = store.get()
                    if not credentials or credentials.invalid:
                        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
                        flow.user_agent = APPLICATION_NAME
                        if flags:
                            credentials = tools.run_flow(flow, store, flags)
                        else:  # Needed only for compatibility with Python 2.6
                            credentials = tools.run(flow, store)
                    return credentials

                def googleBack():
                    credentials = get_credentials()
                    for root, dirs, file in os.walk(jpg):
                        for i, files in enumerate(file):
                            self.update_process.emit("Your Image file " + files.replace('.pdf', '') + " is Uploading to google Tunnel")
                            time.sleep(2)
                            main(credentials, root, files)

                def main(credentials, root, files):
                    http = credentials.authorize(httplib2.Http())
                    service = discovery.build('drive', 'v3', http=http)
                    try:
                        name_file = os.path.splitext(files)[0]
                        imgfile = root + "/" + files  # Image with texts (png, jpg, bmp, gif, pdf)
                        txtfile = root + "/" + files + '.txt'  # Text file outputted by OCR
                        self.update_process.emit("Your Image file " + files.replace('.pdf', '') + " is Converting to text")
                        mime = 'application/vnd.google-apps.document'
                        res = service.files().create(
                            body={
                                'name': imgfile,
                                'mimeType': mime
                            },
                            media_body=MediaFileUpload(imgfile, mimetype=mime, resumable=True)
                        ).execute()

                        self.update_process.emit("Yout Text file " + files.replace('.pdf', '') + " is downloading from Google tunnel")
                        time.sleep(3)
                        downloader = MediaIoBaseDownload(
                            io.FileIO(txtfile, 'wb'),
                            service.files().export_media(fileId=res['id'], mimeType="text/plain")
                        )
                        done = False
                        while done is False:
                            status, done = downloader.next_chunk()

                        service.files().delete(fileId=res['id']).execute()

                        self.update_process.emit("Download file Sucessfully")

                    except:
                        self.update_process.emit("Authentication Error. Retrying ..")
                        try:
                            name_file = os.path.splitext(files)[0]
                            imgfile = root + "/" + files  # Image with texts (png, jpg, bmp, gif, pdf)
                            txtfile = root + "/" + files + '.txt'  # Text file outputted by OCR
                            self.update_process.emit("Your Image file " + files.replace('.pdf', '') + " is Converting to text")
                            mime = 'application/vnd.google-apps.document'
                            res = service.files().create(
                                body={
                                    'name': imgfile,
                                    'mimeType': mime
                                },
                                media_body=MediaFileUpload(imgfile, mimetype=mime, resumable=True)
                            ).execute()
                            self.update_process.emit("Yout Text file " + files.replace('.pdf', '') + " is downloading from Google tunnel")

                            downloader = MediaIoBaseDownload(
                                io.FileIO(txtfile, 'wb'),
                                service.files().export_media(fileId=res['id'], mimeType="text/plain")
                            )
                            done = False
                            while done is False:
                                status, done = downloader.next_chunk()

                            service.files().delete(fileId=res['id']).execute()
                            self.update_process.emit("Download file Sucessfully")

                        except:
                            self.update_process.emit("Sorry !! We cannot connect to Google Server. Please Check your internet Connecetion and Try again!")

                time.sleep(2)
                self.update_process.emit("Connecting to Google Tunnel for Auth Credits")
                time.sleep(1)
                googleBack()

            self.update_process.emit("Connecting to Google Vision API")
            time.sleep(2)
            googleVision()

        def appendingData():
            path = path = self.foo
            source_dir = path.replace('.pdf', '') + '/jpg'
            dest_dir = path.replace('.pdf', '') + '/text'

            for root, dirnames, filenames in os.walk(source_dir):
                for file in filenames:
                    (shortname, extension) = os.path.splitext(file)
                    if extension == ".txt":
                        shutil.copy2(os.path.join(root, file), os.path.join(dest_dir,
                                                                            os.path.relpath(os.path.join(root, file),
                                                                                            source_dir)))

            self.update_process.emit("Collecting and Appending is Completed.")

        def preprocessingCleaning():
            path = self.foo
            text = path.replace('.pdf', '') + '/text'

            read_files = glob.glob(text + '/' + "*.txt")

            with open(path.replace('.pdf', '') + '/' + "with_line_breaking.txt", "wb") as outfile:
                for f in read_files:
                    with open(f, "rb") as infile:
                        outfile.write(infile.read())

        def cleaningprocess():
            path = self.foo
            text = path.replace('.pdf', '') + '/text'

            def Createbat():
                a_file = open(path.replace('.pdf', '') + '/' + "with_line_breaking.txt", "r", encoding="utf8")
                string_without_line_breaks = ""
                for line in a_file:
                    stripped_line = line.rstrip()
                    string_without_line_breaks += stripped_line
                a_file.close()
                with open(path.replace('.pdf', '') + '/' + "without_line_breaking.txt", "w", encoding="utf8") as output:
                    output.write(str(string_without_line_breaks))

            def Fixingbook():
                with open(path.replace('.pdf', '') + '/' + "without_line_breaking.txt", "rt", encoding="utf8") as fin:
                    with open(path.replace('.pdf', '') + '/' + "Final.txt", "wt", encoding="utf8") as fout:
                        for line in fin:
                            fout.write(line.replace(' )', ')').replace('( ', '(').replace('.', '. ').replace(',',
                                                                                                             ', ').replace(
                                '  ', ' ').replace(' ?', '?').replace('|', ''))

            Createbat()
            time.sleep(2)
            Fixingbook()

        def tempFiles():
            path = self.foo

            shutil.rmtree(path.replace('.pdf', '') + '/text')
            time.sleep(10)
            shutil.rmtree(path.replace('.pdf', '') + '/jpg')
            time.sleep(10)
            shutil.rmtree(path.replace('.pdf', '') + '/first_process')




        singlePdfSplit()
        self.update_process.emit("Your Pages Converted Into Images... Please Wait")
        time.sleep(2)
        secondProcesspa()
        self.update_process.emit("Your Images Converted Into Texts... Please Wait")
        time.sleep(2)
        googleImageVision()
        self.update_process.emit("Collecting and Appending your Text Files")
        time.sleep(2)
        appendingData()
        self.update_process.emit("Collecting Parameters to Cleaning your Data")
        time.sleep(2)
        preprocessingCleaning()
        self.update_process.emit("Cleaning your Data")
        time.sleep(2)
        cleaningprocess()
        self.update_process.emit("Cleaning Finished. Please wait, We are Removing Temperory files")
        time.sleep(2)
        tempFiles()
        self.update_process.emit("Conversion Finsihed\n Thanks for using \n Follow me on \ngithub :@sujithrex \n facebook: @indiantheologian \n protfolio: sujithrex.github.io ")
        time.sleep(2)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myForm()
    w.show()
    sys.exit(app.exec_())
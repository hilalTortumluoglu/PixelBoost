import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QThread, pyqtSignal
import cv2
from edsr import upscale_image
from resolutionConverter import Ui_MainWindow


class ImageProcessingWorker(QThread):
    result_ready = pyqtSignal(object)

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        try:
            result = upscale_image(self.file_name)
            self.result_ready.emit(result)
        except Exception as e:
            print(f"Error during image processing: {e}")
            self.result_ready.emit(None)


class MainWindow:
    def __init__(self) -> None:
        self.main_win = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.indexOf(self.ui.page1))

        self.ui.pathButton.clicked.connect(self.add_file)
        self.ui.convButton.clicked.connect(self.convert_image)
        self.ui.returnButton.clicked.connect(self.return_to_main_page)
        self.ui.saveButton.clicked.connect(self.save_image)

        self.result_image = None

    def return_to_main_page(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.indexOf(self.ui.page1))
        self.ui.convertPhoto.clear()
        self.ui.pathText.clear()

    def add_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self.main_win, 'Open file', '', 'Image files (*.jpg *.jpeg *.png)')
        if file_name:
            self.ui.pathText.setText(file_name)

    def convert_image(self):
        file_name = self.ui.pathText.toPlainText()

        if file_name:
            self.ui.stackedWidget.setCurrentIndex(self.ui.stackedWidget.indexOf(self.ui.page2))
            pixmap = QPixmap(file_name)
            self.ui.orginalPhoto.setPixmap(pixmap.scaled(self.ui.orginalPhoto.size(), aspectRatioMode=1))

            # Start the background thread for image processing
            self.worker = ImageProcessingWorker(file_name)
            self.worker.result_ready.connect(self.update_image)
            self.worker.start()

    def update_image(self, result):
        if result is not None:
            result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
            height, width, channel = result_rgb.shape
            bytes_per_line = 3 * width
            qimage = QImage(result_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            self.ui.convertPhoto.setPixmap(pixmap.scaled(self.ui.convertPhoto.size(), aspectRatioMode=1))
            self.result_image = result
        else:
            print("Failed to process image.")

    def save_image(self):
        if self.result_image is not None:
            save_path, _ = QFileDialog.getSaveFileName(self.main_win, 'Save file', '', 'PNG files (*.png);;JPEG files (*.jpg *.jpeg);;All files (*.*)')
            if save_path:
                try:
                    cv2.imwrite(save_path, self.result_image)
                except Exception as e:
                    print(f"Error saving image: {e}")

    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

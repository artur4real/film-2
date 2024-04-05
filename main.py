import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from database.queries import insert_movie_data


class MovieApp(QDialog):
    def __init__(self):
        super(MovieApp, self).__init__()
        loadUi("ui/main_window.ui", self)

        self.pushButton.clicked.connect(self.add_movie)

    def add_movie(self):
        name = self.lineEdit.text()
        genre = self.lineEdit_2.text()
        year = int(self.lineEdit_3.text())
        rating = int(self.lineEdit_4.text())
        director = self.lineEdit_5.text()

        movie_data = (name, genre, year, rating, director)

        insert_movie_data(movie_data)

        print("Данные добавлены успешно!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MovieApp()
    window.show()
    sys.exit(app.exec_())

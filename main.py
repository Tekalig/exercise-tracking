import os
from app.gui_app import app


def initialize_app():
    folders = ["data", "logs"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    files = ["data/exercises.json", "logs/app.log"]
    for file in files:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                f.write("")

initialize_app()


if __name__ == "__main__":
    app.mainloop()

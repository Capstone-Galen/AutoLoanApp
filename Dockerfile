FROM cdrx/pyinstaller-linux
COPY . /LoanApp.py
COPY . /icons8carbadge.ico
WORKDIR /LoanApp.py
RUN pip install pyinstaller
CMD pyinstaller --onefile --windowed --icon=icons8carbadge.ico LoanApp.py

FROM cdrx/pyinstaller-windows
COPY . /LoanApp.py /LoanApp.py/src/
COPY . /icons8carbadge.ico /LoanApp.py/src/
WORKDIR /LoanApp.py/src/
RUN pip install pyinstaller
CMD pyinstaller --onefile --windowed --icon=icons8carbadge.ico LoanApp.py

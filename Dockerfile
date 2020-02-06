FROM python:3
ADD . /LoanApp.py 
WORKDIR /LoanApp
RUN pip install pyinstaller 
RUN pyinstaller --onefile --windowed --icon=icons8carbadge.ico LoanApp.py
CMD ["python", "LoanApp.py"]

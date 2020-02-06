FROM python
ADD . /LoanApp/src
WORKDIR /LoanApp/src
RUN pip install pyinstaller 
RUN pyinstaller --onefile --windowed --icon=icons8carbadge.ico LoanApp.py
CMD ["python", "LoanApp.py"]

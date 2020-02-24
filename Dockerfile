FROM python
ADD LoanApp.py /
RUN pip install pyinstaller
RUN pyinstaller --onefile --windowed LoanApp.py
CMD ["python LoanApp.py"]



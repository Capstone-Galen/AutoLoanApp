FROM python
ADD LoanApp.py /
RUN cdrx/pyinstaller-windows
CMD [ "pyinstaller", "./LoanApp.py"]


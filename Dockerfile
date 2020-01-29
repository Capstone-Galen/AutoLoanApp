FROM python:3
ADD LoanApp.py /
RUN cdrx/pyinstaller-windows
CMD [ "pyinstaller", "./LoanApp.py"]


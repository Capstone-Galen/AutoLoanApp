FROM python
ADD LoanApp.py /
RUN pyinstaller
CMD [ "--onefile --windowed --icon=icons8carbadge.ico", "./LoanApp.py"]


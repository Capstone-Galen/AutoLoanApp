FROM cdrx/pyinstaller-windows
COPY . /LoanApp.py
COPY . /icons8carbadge.ico
WORKDIR /LoanApp.py
RUN chmod 777 /LoanApp.py
RUN pip install pyinstaller
RUN cd ..
RUN pwd
RUN pyinstaller --onefile --windowed --icon=icons8carbadge.ico LoanApp.py
CMD python, LoanApp.py

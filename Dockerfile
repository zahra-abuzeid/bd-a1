FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip

RUN pip3 install pandas


RUN pip3 install numpy


RUN pip3 install seaborn


RUN pip3 install matplotlib


RUN pip3 install scikit-learn


RUN pip3 install scipy

RUN mkdir -p /home/doc-bd-a1

COPY fatalities_isr_pse_conflict_2000_to_2023.csv /home/doc-bd-a1/

CMD ["/bin/bash"]
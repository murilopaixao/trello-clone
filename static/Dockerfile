FROM python:3.10-alpine

#Ajustando horario
ENV TZ=America/Sao_Paulo
RUN apk add --no-cache tzdata
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

RUN pip install --upgrade pip 
RUN apk add gcc libc-dev g++ libffi-dev libxml2 unixodbc-dev

#Download pacotes
RUN apk --no-cache add curl
RUN curl -O https://download.microsoft.com/download/1/f/f/1fffb537-26ab-4947-a46a-7a45c27f6f77/msodbcsql18_18.2.1.1-1_amd64.apk
RUN curl -O https://download.microsoft.com/download/1/f/f/1fffb537-26ab-4947-a46a-7a45c27f6f77/mssql-tools18_18.2.1.1-1_amd64.apk

#Instalando Microsoft ODBC 18 e mssql-tools
RUN apk add --allow-untrusted msodbcsql18_18.2.1.1-1_amd64.apk
RUN apk add --allow-untrusted mssql-tools18_18.2.1.1-1_amd64.apk

#Deletando arquivos desnecessarios
RUN rm msodbcsql18_18.2.1.1-1_amd64.apk
RUN rm mssql-tools18_18.2.1.1-1_amd64.apk

#Copiando projeto
RUN mkdir /app
#ADD . /app
#ADD . /app
ADD requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["flask", "run"]

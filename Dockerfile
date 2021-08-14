FROM python:3.8-slim as builder
WORKDIR /opt/challenge-backend
ADD  ./ /opt/challenge-backend/
RUN python3 -m venv venv 
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip3 install -r requirements.txt

FROM python:3.8-slim
WORKDIR /opt/challenge-backend
COPY --from=builder /opt/challenge-backend /opt/challenge-backend
EXPOSE 5000  
CMD /bin/bash -c "source ./venv/bin/activate"
FROM python:3.5

RUN mkdir /opt/pets
COPY pet.py /opt/pets/pet.py
COPY test.py /opt/pets/test.py
CMD ["python", "/opt/pets/test.py"]

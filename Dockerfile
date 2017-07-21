FROM python:2.7.13

RUN mkdir /opt/pets
COPY pet.py /opt/pets/pet.py
CMD ["python", "/opt/pets/pet.py"]

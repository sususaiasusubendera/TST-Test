FROM python:3.10.7
WORKDIR /mnt/d/alph/!0CA/STI/5/TST/TST-Test
ADD . /mnt/d/alph/!0CA/STI/5/TST/TST-Test
CMD ["python", "test.py"]

#!/bin/bash
cd /home/ubuntu/student-result-predictor
sudo docker build -t student-result-predictor .
sudo docker run -d --name student-app -p 80:5000 student-result-predictor

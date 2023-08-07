import os
import subprocess
import boto3

def update_apt():
    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "install", "awscli", "-y"])
    subprocess.run(["sudo", "apt", "install", "docker-compose", "-y"])
    subprocess.run(["docker-compose", "version"])
    
def create_directory():
    os.makedirs("/etc/prometheus", exist_ok=True)
    os.makedirs("/etc/blackbox_exporter", exist_ok=True)
    os.makedirs("/etc/alertmanager", exist_ok=True)
    
def download_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    s3 = boto3.client('s3')
    s3.download_file(config['S3']['bucket'], config['S3']['docker_compose'], '/etc/prometheus/docker-compose.yml')
    s3.download_file(config['S3']['bucket'], config['S3']['prometheus'], '/etc/prometheus/prometheus.yml')
    s3.download_file(config['S3']['bucket'], config['S3']['alert_rules'], '/etc/prometheus/alert.rules.yml')
    s3.download_file(config['S3']['bucket'], config['S3']['blackbox'], '/etc/blackbox_exporter/blackbox.yml')
    s3.download_file(config['S3']['bucket'], config['S3']['alertmanager'], '/etc/alertmanager/alertmanager.yml')
    
def start_prometheus():
    subprocess.run(["sudo", "docker-compose", "-f", "/etc/prometheus/docker-compose.yml", "up", "-d"])
    print("end of the file")

if __name__ == '__main__':
    update_apt()
    create_directory()
    download_config()
    start_prometheus()

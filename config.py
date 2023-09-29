# config.py

class Config:
    def __init__(self):
        self.region = 'us-west-2'
        self.cluster_identifier = '10-08-2023'
        self.new_cluster_identifier = 'new-cluster'
        self.record_name = 'your_record_name'
        self.hosted_zone_id = 'your_hosted_zone_id'
        self.remote_host = 'your_remote_host'
        self.ssh_key_path = '/path/to/your/ssh/key.pem'
        self.ssh_user = 'your_ssh_username'
        self.url_to_check = 'https://example.com'  # Replace with your URL

# main.py

from rds_manager import RDSManager
from ssh_manager import SSHManager
from url_checker import URLChecker

if __name__ == '__main__':
    rds_manager = RDSManager()
    ssh_manager = SSHManager()
    url_checker = URLChecker()

    snapshots = rds_manager.list_snapshots()

    if snapshots:
        source_snapshot_identifier = snapshots[0]
        print(f"Selected snapshot: {source_snapshot_identifier}")

        source_cluster = rds_manager.get_source_cluster()

        print(f"Snapshots created one day ago for cluster {rds_manager.config.cluster_identifier}:")

        response_restore = rds_manager.restore_db_cluster(source_snapshot_identifier, source_cluster)

        print(f"Creating a new Aurora cluster with identifier: {rds_manager.config.new_cluster_identifier}")
        print(f"Using snapshot: {source_snapshot_identifier}")

        if response_restore:
            cluster_endpoint = rds_manager.get_cluster_endpoint(response_restore)

            print(f"New Aurora cluster '{rds_manager.config.new_cluster_identifier}' created successfully.")

            route53_response = rds_manager.update_route53_record(cluster_endpoint)

            if route53_response:
                print(f"Updated Route 53 record with new cluster endpoint: {cluster_endpoint}")
            else:
                print("Error updating Route 53 record.")
        else:
            print("Error creating Aurora cluster and updating its endpoint on Route 53. Please check.")

        replica_identifier = rds_manager.get_replica_identifier()

        response_replica = rds_manager.create_read_replica(replica_identifier)

        if response_replica:
            print(f"Read replica '{replica_identifier}' created successfully.")
        else:
            print(f"Error creating read replica '{replica_identifier}'.")

        if ssh_manager.execute_ssh_command('sudo systemctl stop jira && echo "jira has been stopped"'):
            print("Jira service stopped successfully.")
        else:
            print("Error stopping Jira service.")

        if ssh_manager.execute_ssh_command('sudo systemctl start jira && echo "jira has been started now"'):
            print("Jira service started successfully.")
        else:
            print("Error starting Jira service.")

        url_result = url_checker.check_url()
        print(url_result)
    else:
        print(f"No snapshots found for cluster {rds_manager.config.cluster_identifier}.")

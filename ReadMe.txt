This web application is hosted in AWS EC2 which enables user to provide a query (for table which is manually uploaded to RDS) and key (for memcache) and it checks AWS memcache whether the data associated with key is cached if yes, then it provides the time taken to get the data from cache(lesser time). If not, it gives the time taken to get the data from AWS RDS.

Requirements:
1. Pip installed - Flask
2. AWS EC2 instance
3. AWS RDS instance
4. AWS Memcache instance

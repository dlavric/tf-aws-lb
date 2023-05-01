# diagram.py
from diagrams import Cluster, Diagram
from diagrams.aws.general import Client
from diagrams.aws.network import VPC
from diagrams.aws.compute import EC2
from diagrams.onprem.network import Internet
from diagrams.aws.network import PrivateSubnet
from diagrams.aws.network import PublicSubnet
from diagrams.aws.network import InternetGateway
from diagrams.aws.network import NATGateway
from diagrams.aws.network import ElbApplicationLoadBalancer
from diagrams.onprem.network import Nginx

    
with Diagram("aws-lab", show=False, direction="TB"):
        #client = Client("Machine/User")
        internet = Internet("Internet")
        
        with Cluster("eu-west-1"):
            with Cluster("VPC"):
                intgat  = InternetGateway("Internet Gateway")
                natgat  = NATGateway("NATGateway")  
                lb      = ElbApplicationLoadBalancer ("Application Load Balancer")
                
                with Cluster("eu-west-1a"):
                    with Cluster("Private Subnet"):
                        ec1     = EC2("EC2 Instance")
                
                with Cluster("eu-west-1b"): 
                    with Cluster("Public Subnet"):
                        ec2     = EC2("EC2 Instance")
                
            #client >> 
            internet >> lb >> [ec1,ec2] 
            internet << intgat << natgat << [ec1,ec2]
        
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

    
# with Diagram("AWS-LoadBalancer", show=False, direction="TB"):
#     Client("Client") >> EC2("EC2") >> VPC("VPC") >> PublicSubnet("PublicSubnet") >> PrivateSubnet("PrivateSubnet") >> InternetGateway("InternetGateway") >> NATGateway("NATGateway") >> ElbApplicationLoadBalancer("ElbApplicationLoadBalancer") >> Nginx("Nginx")


with Diagram("AWS-LoadBalancer", show=False):
        client = Client("Machine/User")
        
        with Cluster("Daniela VPC"):
            intgat  = InternetGateway("Internet Gateway")
            natgat  = NATGateway("NATGateway")  
            lb      = ElbApplicationLoadBalancer ("Application Load Balancer")
            
            with Cluster("eu-west-1a"):
                with Cluster("Private Subnet"):
                    ec2     = EC2("EC2 Instance")
             
            with Cluster("eu-west-1b"): 
                with Cluster("Public Subnet"):
                    ec     = EC2("EC2 Instance")
                    
        internet = Internet("Internet")
             
            # ec2 >> private
             
        client >> lb >> [ec2,ec] 
            
        ec2 >> natgat >> intgat >> internet

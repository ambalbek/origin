provider "aws" {
  region     = "us-east-2"
}

resource "aws_instance" "aziz1" {
    ami = "ami-02ccb28830b645a41"
    instance_type = "t2.micro"
    key_name = "aws"
    

    
    provisioner "remote-exec" {
        inline = [
        "sudo amazon-linux-extras install -y jenkins",
        "sudo systemctl start jenkins"
        
    ]
    
        connection {
        type ="ssh"
        user="ec2-user"
        private_key = file("./aws.pem")
        host = self.public_ip
    }
    }
}


provider "aws" {
  region     = "us-east-2"
  access_key = "AKIAWNCV5BD4W2JIIJ62"
  secret_key = "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"
}
resource "aws_instance" "akmana"  {
  ami = "ami-0e38b48473ea57778"
  instance_type = "t2.micro"
  security_groups = ["akmana"]
  key_name = "root"
  count = 5
  tags = {
    Name = "http"
  }
  provisioner "remote-exec" {
    inline = [
    "sudo yum install update -y",
    "sudo sudo yum install httpd -y",
    "sudo systemctl start httpd",
    "sudo systemctl enable httpd"
    ]

    connection {
    type ="ssh"
    user="ec2-user"
    private_key = file("./root.pem")
    host = self.public_ip
    }
}
}




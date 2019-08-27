resource "aws_security_group" "allow_me_ssh" {
  name        = "allow_me_ssh"
  description = "Allow SSH"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = #Add my IP address here
    }

  egress {
   from_port = 0
   to_port = 0
   protocol = "-1"
   cidr_blocks = ["0.0.0.0/0"]
    }

  tags = {
    Name = "allow_ssh"
  }
}

resource "aws_instance" "DockerBase" {
    ami =  #Insert Packer AMI here
    instance_type = "t2.micro"
    vpc_security_group_ids = [aws_security_group.instance.id]
    
    tags = {
        Name = "PackerEC2"
    }
}
#Create environment variables to run script
#export TF_VAR_AWSAccessKey= (Insert Access Key Here)
#export TF_VAR_AWSSecretKey= (Insert Secret Key Here)
#export TF_VAR_region=us-west-1

resource "aws_security_group" "allow_me_ssh" {
  name        = "allow_me_ssh"
  description = "Allow SSH"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks =  #Add my IP address here such as ["174.114.60.31/32"]
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
    ami = #Insert Packer AMI here such as "ami-08fd8ae3806f09a08"
    instance_type = "t2.micro"
    vpc_security_group_ids = ["${aws_security_group.allow_me_ssh.id}"]

    tags = {
        Name = "PackerEC2"
    }
}

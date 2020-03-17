terraform {
  backend "s3" {
    bucket = "ambalbek"
    key    = "backend.tfstate"
    region = "us-east-2"
    dynamodb_table = "s3_backend"
  }
}
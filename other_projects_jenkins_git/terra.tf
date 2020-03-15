data "digitalocean_droplet" "example" {
  name = "web"
}

output "droplet_output" {
  value = data.digitalocean_droplet.example.ipv4_address
}
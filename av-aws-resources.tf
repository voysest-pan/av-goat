###########################
# RESOURCES
###########################

resource "random_id" "seed" {
  byte_length = 4
}

resource "azurerm_resource_group" "vnet" {
  name     = local.name
  location = var.region
}

module "network" {
  source              = "Azure/network/azurerm"
  version             = "3.1.1"
  resource_group_name = azurerm_resource_group.vnet.name
  vnet_name           = local.name
  address_space       = "10.0.0.0/16"
  subnet_prefixes     = ["10.0.0.0/24","10.0.2.0/24","10.0.3.0/24"]
  subnet_names        = ["subnet1", "subnet2","subnet3"]

  depends_on = [azurerm_resource_group.vnet]
}

  resource "azurerm_network_security_group" "allow_ssh" {
    name = "allow_ssh"
    location = var.region
    resource_group_name = azurerm_resource_group.vnet.name
    
    security_rule {
      name = "allow_ssh"
      priority = 100
      direction = "Allow"
      protocol = "Tcp"
      source_port_range = "*"
      source_address_prefix = "*"
      destination_port_range = "22"
      destination_address_prefix = "*"
    }
  }

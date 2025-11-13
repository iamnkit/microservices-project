resource "azurerm_container_registry" "acr" {
  name                = "${var.prefix}acr${random_integer.suffix.result}"
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "random_integer" "suffix" {
  min = 100
  max = 999
}

output "acr_id" {
  value = azurerm_container_registry.acr.id
}

output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}

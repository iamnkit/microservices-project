resource "random_integer" "suffix" {
  min = 100
  max = 999
}

resource "azurerm_storage_account" "sa" {
  name                     = lower("${var.prefix}sa${random_integer.suffix.result}")
  resource_group_name      = var.resource_group_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"

  blob_properties {
    versioning_enabled = true
  }

  tags = {
    Environment = "Assignment"
    ManagedBy   = "Terraform"
  }
}

resource "azurerm_storage_container" "container" {
  name                  = "terraform-state"
  storage_account_name  = azurerm_storage_account.sa.name
  container_access_type = "private"
}

output "storage_account_name" {
  value = azurerm_storage_account.sa.name
}

output "storage_account_id" {
  value = azurerm_storage_account.sa.id
}

output "container_name" {
  value = azurerm_storage_container.container.name
}

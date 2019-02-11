
# Create Resources for WebApp for Containers in Azure

#### Create Resource Group
az group create --name flasky --location "West Europe"

#### Create App Service Plan
az appservice plan create --name mflaske2eAppServicePlan --resource-group flasky --sku B1 --is-linux

#### Create WebApp for Container
az webapp create --name flaske2e --resource-group flasky --plan mflaske2eAppServicePlan --deployment-container-image-name salmaniqbal/flaske2e

#### Expose port externally
az webapp config appsettings set --resource-group flasky --name flaske2e --settings WEBSITES_PORT=5000

check this video for commands: https://www.youtube.com/watch?v=aJ8EPAH9G6E
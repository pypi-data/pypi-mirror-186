# geoapi-client
Geospatial API for TAPIS


- API version: 0.1
- Package version: 2.10
- Build package: io.swagger.codegen.languages.PythonClientCodegen

For more information about the [GeoAPI](https://github.com/TACC-Cloud/geoap) and how this client is generated using [Swagger Codegen](https://github.com/swagger-api/swagger-codegen), visit https://github.com/TACC-Cloud/geoap .

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

The python package can be found at [PyPi](https://pypi.org/project/geoapi-client/)

```sh
pip install geoapi-client --user
```

Then import the package:
```python
import geoapi_client 
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import geoapi_client
from geoapi_client.rest import ApiException
from pprint import pprint

configuration = geoapi_client.Configuration()
configuration.host = MY_HOST # e.g. https://agave.designsafe-ci.org/geo/v2
configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration.api_key['Authorization'] = TOKEN

api_client = geoapi_client.ApiClient(configuration)
api_instance = geoapi_client.ProjectsApi(api_client=api_client)

try:
    project = api_instance.create_project(payload={"name": "My project"})
    pprint(project)
    features = api_instance.upload_file(project.id, 'image.jpg')
    pprint(features)
except ApiException as e:
    print("Exception: %s\n" % e)
```

## API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*NotificationsApi* | **delete** | **DELETE** /notifications/progress | 
*NotificationsApi* | **delete_0** | **DELETE** /notifications/progress/{progressUUID} | 
*NotificationsApi* | **get** | **GET** /notifications/ | 
*NotificationsApi* | **get_0** | **GET** /notifications/progress | 
*NotificationsApi* | **get_1** | **GET** /notifications/progress/{progressUUID} | 
*ProjectsApi* | **add_feature_asset** | **POST** /projects/{projectId}/features/{featureId}/assets/ | 
*ProjectsApi* | **add_geo_json_feature** | **POST** /projects/{projectId}/features/ | 
*ProjectsApi* | **add_overlay** | **POST** /projects/{projectId}/overlays/ | 
*ProjectsApi* | **add_point_cloud** | **POST** /projects/{projectId}/point-cloud/ | 
*ProjectsApi* | **add_streetview_sequence_to_feature** | **POST** /projects/{projectId}/streetview/ | 
*ProjectsApi* | **add_tile_server** | **POST** /projects/{projectId}/tile-servers/ | 
*ProjectsApi* | **add_user** | **POST** /projects/{projectId}/users/ | 
*ProjectsApi* | **cluster_features** | **GET** /projects/{projectId}/features/cluster/{numClusters}/ | 
*ProjectsApi* | **create_project** | **POST** /projects/ | 
*ProjectsApi* | **delete_feature** | **DELETE** /projects/{projectId}/features/{featureId}/ | 
*ProjectsApi* | **delete_point_cloud** | **DELETE** /projects/{projectId}/point-cloud/{pointCloudId}/ | 
*ProjectsApi* | **delete_project** | **DELETE** /projects/{projectId}/ | 
*ProjectsApi* | **get_all_features** | **GET** /projects/{projectId}/features/ | 
*ProjectsApi* | **get_all_point_clouds** | **GET** /projects/{projectId}/point-cloud/ | 
*ProjectsApi* | **get_feature** | **GET** /projects/{projectId}/features/{featureId}/ | 
*ProjectsApi* | **get_overlays** | **GET** /projects/{projectId}/overlays/ | 
*ProjectsApi* | **get_point_cloud** | **GET** /projects/{projectId}/point-cloud/{pointCloudId}/ | 
*ProjectsApi* | **get_project_by_id** | **GET** /projects/{projectId}/ | 
*ProjectsApi* | **get_project_users_resource** | **GET** /projects/{projectId}/users/ | 
*ProjectsApi* | **get_projects** | **GET** /projects/ | 
*ProjectsApi* | **get_streetview_sequence_from_feature** | **GET** /projects/{projectId}/streetview/{featureId}/ | 
*ProjectsApi* | **get_tasks** | **GET** /projects/{projectId}/tasks/ | 
*ProjectsApi* | **get_tile_servers** | **GET** /projects/{projectId}/tile-servers/ | 
*ProjectsApi* | **import_file_from_tapis** | **POST** /projects/{projectId}/features/files/import/ | 
*ProjectsApi* | **import_overlay_from_tapis** | **POST** /projects/{projectId}/overlays/import/ | 
*ProjectsApi* | **import_point_cloud_file_from_tapis** | **POST** /projects/{projectId}/point-cloud/{pointCloudId}/import/ | 
*ProjectsApi* | **remove_overlay** | **DELETE** /projects/{projectId}/overlays/{overlayId}/ | 
*ProjectsApi* | **remove_tile_server** | **DELETE** /projects/{projectId}/tile-servers/{tileServerId}/ | 
*ProjectsApi* | **remove_user** | **DELETE** /projects/{projectId}/users/{username}/ | 
*ProjectsApi* | **update_feature_properties** | **POST** /projects/{projectId}/features/{featureId}/properties/ | 
*ProjectsApi* | **update_feature_styles** | **POST** /projects/{projectId}/features/{featureId}/styles/ | 
*ProjectsApi* | **update_point_c_loud** | **PUT** /projects/{projectId}/point-cloud/{pointCloudId}/ | 
*ProjectsApi* | **update_project** | **PUT** /projects/{projectId}/ | 
*ProjectsApi* | **update_tile_server** | **PUT** /projects/{projectId}/tile-servers/{tileServerId}/ | 
*ProjectsApi* | **update_tile_servers** | **PUT** /projects/{projectId}/tile-servers/ | 
*ProjectsApi* | **upload_file** | **POST** /projects/{projectId}/features/files/ | 
*ProjectsApi* | **upload_point_cloud** | **POST** /projects/{projectId}/point-cloud/{pointCloudId}/ | :raises InvalidCoordinateReferenceSystem: in case  file missing coordinate reference system
*PublicProjectsApi* | **get_all_features** | **GET** /public-projects/{projectId}/features/ | 
*PublicProjectsApi* | **get_all_point_clouds** | **GET** /public-projects/{projectId}/point-cloud/ | 
*PublicProjectsApi* | **get_feature** | **GET** /public-projects/{projectId}/features/{featureId}/ | 
*PublicProjectsApi* | **get_overlays** | **GET** /public-projects/{projectId}/overlays/ | 
*PublicProjectsApi* | **get_point_cloud** | **GET** /public-projects/{projectId}/point-cloud/{pointCloudId}/ | 
*PublicProjectsApi* | **get_project_by_id** | **GET** /public-projects/{projectId}/ | 
*PublicProjectsApi* | **get_projects** | **GET** /public-projects/ | 
*PublicProjectsApi* | **get_tile_servers** | **GET** /public-projects/{projectId}/tile-servers/ | 
*StreetviewApi* | **add_streetview_sequence** | **POST** /streetview/sequences/ | 
*StreetviewApi* | **create_streetview_organizations** | **POST** /streetview/services/{service}/organization/ | 
*StreetviewApi* | **create_streetview_service_resource** | **POST** /streetview/services/ | 
*StreetviewApi* | **delete_streetview_instance** | **DELETE** /streetview/instances/{instance_id}/ | 
*StreetviewApi* | **delete_streetview_organization** | **DELETE** /streetview/services/{service}/organization/{organization_id}/ | 
*StreetviewApi* | **delete_streetview_sequence** | **DELETE** /streetview/sequences/{sequence_id}/ | 
*StreetviewApi* | **delete_streetview_service_resource** | **DELETE** /streetview/services/{service}/ | 
*StreetviewApi* | **get_streetview_organizations** | **GET** /streetview/services/{service}/organization/ | 
*StreetviewApi* | **get_streetview_sequence** | **GET** /streetview/sequences/{sequence_id}/ | 
*StreetviewApi* | **get_streetview_service_resource** | **GET** /streetview/services/{service}/ | 
*StreetviewApi* | **get_streetview_service_resources** | **GET** /streetview/services/ | 
*StreetviewApi* | **publish_files_to_streetview** | **POST** /streetview/publish/ | 
*StreetviewApi* | **update_streetview_organization** | **PUT** /streetview/services/{service}/organization/{organization_id}/ | 
*StreetviewApi* | **update_streetview_sequence** | **PUT** /streetview/sequences/{sequence_id}/ | 
*StreetviewApi* | **update_streetview_service_resource** | **PUT** /streetview/services/{service}/ | 


## Models

 - Asset
 - Feature
 - FeatureCollection
 - NotificationResponse
 - OkResponse
 - Overlay
 - Payload
 - PointCloud
 - ProgressNotificationResponse
 - Project
 - Streetview
 - StreetviewInstance
 - StreetviewOrganization
 - StreetviewParams
 - StreetviewSequence
 - TapisFile
 - TapisFileImport
 - TapisFileUpload
 - TapisFolderImport
 - Task
 - TileServer
 - User
 - UserPayload


## Documentation For Authorization


## JWT

- **Type**: API key
- **API key parameter name**: X-JWT-Assertion-designsafe
- **Location**: HTTP header

## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

Texas Advanced Computing Center
CICsupport@tacc.utexas.edu

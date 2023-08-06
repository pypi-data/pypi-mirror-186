

# Formal Admin Python SDK


This is the Python SDK for the Formal Admin API.


## Installing


    pip install formal-sdk


## Example Use

```python
import os
from formal_sdk import Client, aa_service_pb2

if __name__ == '__main__':
    path = ""
    tagId = ""
    datastoreId = ""
    newClient = Client(os.environ.get('TEST_CLIENT_ID'),
                       os.environ.get('TEST_SECRET_KEY'))

    # Create Inventory Tag
    res = newClient.Service.CreateInventoryTag(
        aa_service_pb2.CreateInventoryTagRequest(name='newtag'),
        timeout=10,
    )

    # Get Inventory Tags
    res = newClient.Service.GetInventoryTags(
        aa_service_pb2.GetInventoryTagsRequest(),
        timeout=10,
    ) 

    # Delete Tag

    res = newClient.Service.DeleteInventoryTag(
        aa_service_pb2.DeleteInventoryTagRequest(id=tagId),
        timeout=10,
    )

    # Create Inventory Object

    res = newClient.Service.CreateInventoryObject(
        aa_service_pb2.CreateInventoryObjectRequest(datastore_id=datastoreId, object_type="sub-column",
                                                    sub_column=aa_service_pb2.CreateInventoryObjectRequest.SubColumn(path=path, name="name", sub_type="json")),
        timeout=10,
    )

    # Update Inventory Object Tags
    res = newClient.Service.UpdateInventoryObjectTags(
        aa_service_pb2.UpdateInventoryObjectTagsRequest(datastore_id=datastoreId, path=path,
                                                        tags=[tagId]),
        timeout=10,
    )

    # Update Column Lock Status
    res = newClient.Service.UpdateColumnLockStatus(
        aa_service_pb2.UpdateColumnLockStatusRequest(datastore_id=datastoreId, path=path,
                                                     validated=True),
        timeout=10,
    )

    res = newClient.Service.UpdateColumnDataLabel(
        aa_service_pb2.UpdateColumnDataLabelRequest(datastore_id=datastoreId, path=path,
                                                    data_label="email"),
        timeout=10,
    )

    # Delete Inventory Object
    res = newClient.Service.DeleteInventoryObject(
        aa_service_pb2.DeleteInventoryObjectRequest(
            datastore_id=datastoreId, path=path),
        timeout=10,
    )


```



# Formal Admin Python SDK


This is the Python SDK for the Formal Admin API.


## Installing


    pip install formal-sdk


## Example Use

```python
import os
from formal_sdk import Client, admin_pb2

if __name__ == '__main__':
    path = ""
    tagId = ""
    datastoreId = ""
    newClient = Client(os.environ.get('TEST_CLIENT_ID'),
                       os.environ.get('TEST_SECRET_KEY'))

    # Create Inventory Tag
    res = newClient.InventoryService.CreateInventoryTag(
        admin_pb2.CreateInventoryTagRequest(name='newtag')
    )

    # Get Inventory Tags
    res = newClient.InventoryService.GetInventoryTags(
        admin_pb2.GetInventoryTagsRequest()
    ) 

    # Delete Tag
    res = newClient.InventoryService.DeleteInventoryTag(
        admin_pb2.DeleteInventoryTagRequest(id=tagId)
    )

    # Create Inventory Object

    res = newClient.InventoryService.CreateInventoryObject(
        admin_pb2.CreateInventoryObjectRequest(datastore_id=datastoreId, object_type="sub-column",
        sub_column=admin_pb2.CreateInventoryObjectRequest.SubColumn(path=path, name="name", sub_type="json"))
    )

    # Update Inventory Object Tags
    res = newClient.InventoryService.UpdateInventoryObjectTags(
        admin_pb2.UpdateInventoryObjectTagsRequest(datastore_id=datastoreId, path=path,
                                                        tags=[tagId])
    )

    # Update Column Lock Status
    res = newClient.InventoryService.UpdateColumnLockStatus(
        admin_pb2.UpdateColumnLockStatusRequest(datastore_id=datastoreId, path=path,
                                                     validated=True)
    )

    res = newClient.InventoryService.UpdateColumnDataLabel(
        admin_pb2.UpdateColumnDataLabelRequest(datastore_id=datastoreId, path=path,
                                                    data_label="email")
    )

    # Delete Inventory Object
    res = newClient.InventoryService.DeleteInventoryObject(
        admin_pb2.DeleteInventoryObjectRequest(
            datastore_id=datastoreId, path=path)
    )
```
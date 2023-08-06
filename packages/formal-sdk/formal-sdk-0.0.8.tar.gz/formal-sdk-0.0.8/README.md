

# Formal Admin Python SDK


This is the Python SDK for the Formal Admin API.


## Installing


    pip install formal-sdk


## Example Use

```python
import os
from formal_sdk import Client, admin_pb2

if __name__ == '__main__':
    # Inventory Tags
    res = newClient.InventoryService.GetInventoryTags(
        admin_pb2.GetInventoryTagsRequest(),
        timeout=10,
    ) 

    # Delete Tag
    res = newClient.InventoryService.DeleteInventoryTag(
        admin_pb2.DeleteInventoryTagRequest(id=tagId),
        timeout=10,
    )

    # Create Inventory Object

    res = newClient.InventoryService.CreateInventoryObject(
        admin_pb2.CreateInventoryObjectRequest(datastore_id=datastoreId, object_type="sub-column",
                                                    sub_column=admin_pb2.CreateInventoryObjectRequest.SubColumn(path=path, name="name", sub_type="json")),
        timeout=10,
    )

    # Update Inventory Object Tags
    res = newClient.InventoryService.UpdateInventoryObjectTags(
        admin_pb2.UpdateInventoryObjectTagsRequest(datastore_id=datastoreId, path=path,
                                                        tags=[tagId]),
        timeout=10,
    )

    # Update Column Lock Status
    res = newClient.InventoryService.UpdateColumnLockStatus(
        admin_pb2.UpdateColumnLockStatusRequest(datastore_id=datastoreId, path=path,
                                                     validated=True),
        timeout=10,
    )

    res = newClient.InventoryService.UpdateColumnDataLabel(
        admin_pb2.UpdateColumnDataLabelRequest(datastore_id=datastoreId, path=path,
                                                    data_label="email"),
        timeout=10,
    )

    # Delete Inventory Object
    res = newClient.InventoryService.DeleteInventoryObject(
        admin_pb2.DeleteInventoryObjectRequest(
            datastore_id=datastoreId, path=path),
        timeout=10,
    )

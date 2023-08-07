from synctera_client.paths.relationships_relationship_id.get import ApiForget
from synctera_client.paths.relationships_relationship_id.delete import ApiFordelete
from synctera_client.paths.relationships_relationship_id.patch import ApiForpatch


class RelationshipsRelationshipId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass

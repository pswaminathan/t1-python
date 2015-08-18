# -*- coding: utf-8 -*-
"""Provides Creative Approval object for working with creatives."""

from __future__ import absolute_import
from ..errors import ClientError
from ..entity import Entity

class CreativeApproval(Entity):
    """T1 Creative entity, or an atomic_creative entity."""
    collection = 'creative_approvals'
    resource = 'creative_approval'
    _relations = {
        
    }
    _approval_types = Entity._enum({'APPROVED', 'REJECTED', 'PENDING'}, 'PENDING')
    _pull = {
        'additional_detail': None,
        'approval_status': None,
        'atomic_creative_id': int,
        'created_on': Entity._strpt,
        'creative_import_file_id': int,
        'external_identifier': None,
        'id': int,
        'rejected_reason': None,
        'supply_source_id': int,
        'updated_on': Entity._strpt,
        'version': int,
    }

    _readonly = Entity._readonly 

    def save(self, *args, **kwargs):
        raise ClientError('This object is not editable.')

    def __init__(self, session, properties=None, **kwargs):
        super(CreativeApproval, self).__init__(session, properties, **kwargs)

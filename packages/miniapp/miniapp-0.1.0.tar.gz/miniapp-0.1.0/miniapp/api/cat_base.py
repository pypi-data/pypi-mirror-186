import copy
import time
import traceback
import itertools

from miniapp.data.const import ROW_ID
from miniapp.data.impl import compile_query, apply_update, add_to_update_operation
from miniapp.errs import GeneralError, AccessDenied403, BadRequest
from miniapp.utils.generic_obj import make_object
from miniapp.utils.json_utils import traceback_to_json
from miniapp.utils.misc import is_uuid, detect_xss


class ApiCategoryBase(object):
    """
    Overall base class for API categories.
    """
    def __init__(self, api, sequence=None):
        self.api = api
        self.sequence = sequence or 100

    def disable_endpoint(self, method_name: str):
        """
        It may be necessary to disable certain endpoints based on configuration.
        """
        if not hasattr(self, method_name):
            return
        method = getattr(self, method_name)
        if not hasattr(method, "endpoint"):
            return
        method.endpoint.enabled = False


class ApiCategoryBaseCRUD(ApiCategoryBase):
    """
    Base class that supports basic CRUD functionality (create, read, update, delete).
    """
    def __init__(self, api, sequence=None, collection_name=None, validator=None):
        """
        :param api:             API to which this group of calls is being added.
        :param sequence:        Sequence for this group of API calls in the overall API.
        :param collection_name: Name for collection in database.
        :param validator:       Name of JSON file with validation rules.
        """
        super(ApiCategoryBaseCRUD, self).__init__(api, sequence)
        self._collection_name = collection_name or self.__class__.__name__.lower()
        self._validator = validator
        # you can always use "_id" to look up a record, this fieldname serves as an alternative
        self._alt_lookup_field = None
        # indicates which fields must be available to check permissions
        self._visibility_check_fields = None
        # the field named here stores the time.time() value for any change to the record
        self._timestamp_field = None
        # the field here accumulates changes, not storing them officially until _commit() is called
        self._draft_field = None
        # fields that can't be changed by a draft
        self._non_draft_fields = []
        # built-in records which appear in results but cannot be deleted - this is an array of {}s
        self._built_in_records = []

    def alt_lookup_field(self, field_name: str):
        """
        Define an alternate lookup field; a human-readable value representing each record.  For example, a
        user record should have a distinct UUID that never changes but it usually also has a 'username' field.  This
        field does not strictly have to be filled in, or be unique.

        To enforce that a field is unique, call the _enforce_unique() method from a subclassed
        _extra_validation() implementation.  NOTE: To robustly enforce that a field is unique it is a good idea to have
        the database do this with an index.  See SimplestDb.ensure_index().

        :param field_name:  Name of a field which will be allowed wherever the ROW_ID is accepted, i.e. in _lookup() or
            _update().
        """
        self._alt_lookup_field = field_name

    def modification_time_field(self, field_name: str):
        """
        Define a field to hold the modification time for a given record.  It will be set when new records are created
        and when updates are made.

        :param field_name:  Name of field to use for this purpose.
        """
        self._timestamp_field = field_name

    def normalize_id(self, record_id: str):
        """
        Ensure that a reference to a record is a real record UUID.
        :param record_id:   Either the record UUID, the alternate lookup value, or None.
        """
        if is_uuid(record_id):
            return record_id
        if record_id and self._alt_lookup_field:
            found = self._query({self._alt_lookup_field: record_id}, fields=[])
            if found:
                return found[0][ROW_ID]

    def _query(self, query=None, fields=None, limit=None, sort=None, _as_responses: bool=True, _call_prepare: bool=True, all_visible: bool=False, _include_built_in: bool=True):
        """
        Search the collection.
        """
        fields = self._restrict_field_visibility(fields)
        # in order to support _is_visible() and _prepare_record(), we temporarily add their required fields
        use_fields, strip_fields = _include_more_fields(fields, self._visibility_check_fields)
        json_rows = self.api.get_db().query(self._collection_name, query, use_fields, limit=limit, sort=sort)
        if self._built_in_records and _include_built_in:
            filt = compile_query(query)
            json_rows = itertools.chain(json_rows, filter(filt, self._built_in_records))
        if not all_visible:
            json_rows = filter(self._is_visible, json_rows)
        if _call_prepare:
            json_rows = map(self._prepare_record, json_rows)
        # now we can remove the fields we added
        if strip_fields:
            json_rows = map(strip_fields, json_rows)
        # return either as objects or {}s
        if _as_responses:
            records = map(lambda r: make_object(**r), json_rows)
            return list(records)
        return list(json_rows)

    def _lookup(self, record_id: str, fields=None, not_found_error: bool=True, _call_prepare: bool=True):
        """
        Look up one record.
        """
        fields = self._restrict_field_visibility(fields)
        use_fields, strip_fields = _include_more_fields(fields, self._visibility_check_fields)
        records = self._query({ROW_ID: record_id}, fields=use_fields, _call_prepare=_call_prepare) if record_id else None
        if not records and self._alt_lookup_field and record_id:
            records = self._query({self._alt_lookup_field: record_id}, fields=use_fields, _call_prepare=_call_prepare)
        if not records:
            if not_found_error:
                raise GeneralError(code="record-not-found", public_details={
                    "record_type": self.__class__.__name__
                }, private_details={
                    "record_id": record_id,
                    "trace": traceback_to_json(traceback.extract_stack()[:-1])
                })
            else:
                return
        return records[0]

    def _prepare_record(self, record: dict):
        """
        Make changes to records before they are returned.  This is a good place to add calculated fields.
        """
        return record

    def _restrict_field_visibility(self, fields):
        """
        Restrict which fields can be seen.

        Use wbcommon.mini.db.modify_field_list() to make changes.
        """
        return fields

    def _clean_new_record(self, record: dict):
        """
        Derive fields, make any adjustments before storage.
        """
        return dict(record)

    def _clean_changes(self, changes, old_rec: dict):
        """
        Apply standard clean-ups to a record update.  Override to provide standard cleanings.
        """
        return changes

    def _clean_and_extract_changes(self, changes, old_rec: dict):
        """
        Thin wrapper around _clean_changes() which adds support for '$set'.
        """
        if "$set" in changes:
            changes["$set"] = self._clean_changes(changes["$set"], old_rec)
        else:
            changes = self._clean_changes(changes, old_rec)
        return changes

    def _extra_validation(self, record, exclude_record_id=None):
        """
        Do any validation that isn't covered by the JSON schema ('validator')
        """

    def _detect_xss(self, record: dict, *field_names):
        """
        Detect XSS in any of the listed fields.  Call this method from _extra_validation().
        """
        for field_name in field_names:
            if field_name in record:
                value = str(record[field_name])
                if detect_xss(value):
                    raise GeneralError(
                        code="xss-detected", message="XSS blocked",
                        private_details={
                            "collection": self._collection_name, "field": field_name,
                            "value": value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                        }
                    )

    def _validation(self, record_id: (str, None), changes: dict, partial_record: bool=False, repair: bool=False):
        """
        Do all validation for a new record or a set of changes.
        :param record_id:   Record being updated.
        :param changes:     Content to validate.
        :param partial_record: True to ignore top level required fields.
        :param repair:      True to ignore and remove unrecognized fields (other fixes may be added over time).
        """
        if self._validator:
            self.api.validate_schema(self._validator, changes, partial_record=partial_record, repair=repair)
        self._extra_validation(changes, record_id)

    def _enforce_unique(self, record, exclude_id, field_name):
        """
        Function to call from _extra_validation() to ensure a given field has no duplicates.
        """
        if isinstance(field_name, str):
            value = record.get(field_name)
            existing = self._query({field_name: value})
        else:
            value = [record.get(f) for f in field_name]
            existing = self._query({f: record.get(f) for f in field_name})
        if exclude_id:
            existing = list(filter(lambda r: r[ROW_ID] != exclude_id and r[self._alt_lookup_field] != exclude_id, existing))
        if existing:
            raise GeneralError(
                code="field-must-be-unique", message="%s=%s already exists" % (field_name, value),
                public_details={"field": field_name, "value": value},
                private_details={"exclude_id": exclude_id}
            )

    def _make_unique(self, field: str, base_value: str, exclude_id: str=None, formatter: callable=None):
        """
        Synthesize a value that will be unique for a given field.
        """
        query = {}
        if exclude_id:
            query[ROW_ID] = exclude_id
        values = set(getattr(rec, field) for rec in self._query(query, [field]))
        # allow supplied value if possible
        if base_value not in values:
            return base_value
        # try numbered suffixes (or whatever 'formatter' gives us as variants)
        for n_try in range(1, 100):
            v_try = base_value + "-%d" % n_try if not formatter else formatter(n_try)
            if v_try not in values:
                return v_try
        raise GeneralError(code="make-unique-value", message="could not generate distinct value, base=%s" % base_value)

    def _is_visible(self, record):
        """
        Extra rules can be added to limit visibility of records to the current user.
        """
        return True

    def _is_writable(self, record: dict, deleting: bool=True):
        """
        Extra rules determining whether the current user can modify this record.
        """
        return True

    def _check_writable(self, record: dict, deleting: bool=False):
        """
        Verify a record can be updated by the current user.
        """
        if not self._is_writable(record, deleting=deleting):
            raise AccessDenied403(private_details={
                "collection": self._collection_name,
                "record": record[ROW_ID],
                "user": self.api.current_username()
            })

    def _verify_set_tags(self, record: dict):
        """
        Make sure the current user has permission to grant access to a given set of tags by writing these tags to
        a record they own or have access to.
        """
        if "tags" not in record:
            return
        u_tags = self.api.current_user_tags()
        a_tags = record.get("tags", [])
        invalid_tags = set(a_tags) - set(u_tags)
        if invalid_tags:
            raise AccessDenied403(message=f"no access to tags: {list(invalid_tags)}")

    def _on_delete(self, old_rec: dict):
        """
        Special handling after a record is deleted.
        """

    def _capture_draft(self, orig_rec: dict):
        """
        Extract draft-compatible fields from a full record.
        """
        if not orig_rec:
            return {}
        return {k: v for k, v in orig_rec.items() if k not in self._non_draft_fields and k != ROW_ID}

    def _create(self, record):
        """
        Generic record creation.
        """
        db = self.api.get_db()
        # clean up record
        store = self._clean_new_record(record)
        # validate record
        self._validation(None, store)
        # set timestamp
        if self._timestamp_field:
            store[self._timestamp_field] = time.time()
        # store it
        return db.insert(self._collection_name, store)

    def _assert_not_builtin(self, record_id: str):
        if not self._built_in_records:
            return
        collision = False
        for built_in in self._built_in_records:
            if record_id == built_in["_id"]:
                collision = True
            if self._alt_lookup_field and built_in[self._alt_lookup_field] == record_id:
                collision = True
        if collision:
            raise BadRequest(message=f"Cannot modify built-in record with _id={record_id}")

    def _update(self, record_id: str, changes: dict, _no_timestamp_change: bool=False):
        """
        Generic record updates.
        """
        self._assert_not_builtin(record_id)
        # load old record, making sure it exists
        old_rec = orig_rec = self._lookup(record_id, _call_prepare=False)._to_json()
        self._check_writable(old_rec)
        record_id = old_rec[ROW_ID]
        if self._draft_field:
            if changes == {self._draft_field: None}:
                # special case: clear draft changes
                self._raw_update(record_id, changes)
                return make_object()
            old_rec = old_rec.get(self._draft_field) or old_rec
            old_rec.pop(self._draft_field, None)
        # clean-ups
        changes = self._clean_and_extract_changes(changes, old_rec)
        # predict value for new record
        new_rec = copy.deepcopy(old_rec)
        new_rec.pop(ROW_ID, None)
        apply_update(new_rec, changes)
        # validate
        out = make_object()
        try:
            self._validation(record_id, new_rec, repair=True)
        except GeneralError as err:
            if not self._draft_field:
                raise
            # we just report, rather than raise, any error when in draft mode
            out = make_object(ok=False, error=err.to_json(include_private_details=False))
        # apply changes
        if self._draft_field:
            # draft mode: we only update the draft field
            draft = self._capture_draft(new_rec)
            # - prevent storing a draft field that exactly matches the original
            if draft == self._capture_draft(orig_rec):
                draft = None
            self._raw_update(record_id, {self._draft_field: draft})
            return out
        # set timestamp and update the record
        if self._timestamp_field and not _no_timestamp_change:
            add_to_update_operation(changes, self._timestamp_field, time.time())
        self._raw_update(record_id, changes)
        return out

    def _on_commit(self, record: dict):
        """
        Additional changes can be made just before committing.
        """
        return record

    def _commit(self, record_id, fields: list=None, force: bool=False):
        """
        Apply changes made in draft mode.  Returns a diff of what was applied.
        """
        old_rec = self._lookup(record_id, _call_prepare=False)._to_json()
        draft_changes = old_rec.get(self._draft_field)
        if fields:
            draft_changes = {k: v for k, v in draft_changes.items() if k in fields}
        if draft_changes or force:
            # start with original record & apply valid changes
            new_rec = dict(old_rec)
            new_rec.update(self._capture_draft(draft_changes))
            # do custom processing
            new_rec = self._on_commit(new_rec)
            # any changes?
            if new_rec != old_rec:
                # store an up-to-date timestamp, remove any row ID, and make sure there are no recursive draft changes
                self._check_writable(old_rec)
                record_id = old_rec[ROW_ID]
                if self._timestamp_field:
                    new_rec[self._timestamp_field] = time.time()
                new_rec.pop(ROW_ID, None)
                upd_draft = None
                if fields:
                    upd_draft = {k: v for k, v in new_rec[self._draft_field].items() if k not in fields}
                new_rec[self._draft_field] = upd_draft or None
                # validate and store
                self._validation(record_id, new_rec, repair=True)
                self._raw_update(record_id, new_rec)
                # return diff
                diff = {}
                for k in set(new_rec)|set(old_rec):
                    if k in (self._draft_field, ROW_ID):
                        continue
                    if new_rec.get(k) != old_rec.get(k):
                        diff[k] = new_rec.get(k)
                return diff

    def _raw_update(self, record_id: str, updates: dict):
        """
        Low level update of a record.
        """
        self._assert_not_builtin(record_id)
        db = self.api.get_db()
        db.update(self._collection_name, record_id, updates)

    def _delete(self, record_id: str):
        """
        Generic record deletion.
        """
        self._assert_not_builtin(record_id)
        if not isinstance(record_id, str):
            raise ValueError("invalid record_id type")
        old_rec = self._lookup(record_id, _call_prepare=False)._to_json()
        self._check_writable(old_rec, deleting=True)
        db = self.api.get_db()
        db.delete(self._collection_name, old_rec[ROW_ID])
        self._on_delete(old_rec)
        return make_object()

    def _delete_bulk(self, query: dict):
        """
        Bulk record deletion.
        """
        if not isinstance(query, dict):
            raise ValueError("invalid query type")
        db = self.api.get_db()
        db.delete(self._collection_name, query)
        return make_object()


def _include_more_fields(field_spec: (list, dict), fields: set=None):
    """
    Temporarily increase a set of fields to include sone that are needed.
    :returns:  A tuple with the extended field list, and a filter function to reduce records to only the requested
        fields.
    """
    if field_spec is None or not fields:
        return field_spec, None
    if isinstance(field_spec, dict) and list(field_spec.values())[0] == 0:
        if not (fields | set(field_spec)):
            return field_spec, None
        def rmv0(r):
            return {k: v for k, v in r.items() if k not in field_spec}
        return None, rmv0
    if not (fields - set(field_spec)):
        return field_spec, None
    combined = set(field_spec) | fields
    def rmv1(r):
        return {k: v for k, v in r.items() if k in field_spec}
    return list(combined), rmv1

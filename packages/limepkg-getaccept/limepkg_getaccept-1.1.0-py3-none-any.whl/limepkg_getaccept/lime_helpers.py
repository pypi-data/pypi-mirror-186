from lime_filter import Filter, OrOperator, EqualsOperator
from lime_filter.filter import LikeOperator
from lime_type.unit_of_work import _serialize_properties_and_values
from lime_type.limeobjects import (BelongsToPropertyAccessor,
                                   OptionPropertyAccessor,
                                   SetPropertyAccessor,
                                   HasManyPropertyAccessor)


def get_filter(config, value):
    filter = None
    for key, field in config['properties'].items():
        operator = LikeOperator(field, value)
        if not filter:
            filter = operator
            continue
        filter = OrOperator(operator, filter)
    return Filter(filter)


def search_lime_objects(app, limetype_config, search, limit, offset):
    limetype = app.limetypes.get_limetype(limetype_config['limetype'])
    filter = get_filter(limetype_config, search)
    return [_serialize_properties_and_values(get_lime_values(obj))
            for obj in limetype.get_all(
                filter=filter, limit=limit, offset=offset
    )]


def get_documents(app, limetype, record_id):
    documents = app.limetypes.get_limetype('document').get_all(
        filter=Filter(EqualsOperator(limetype, record_id)))
    return [dict(**doc.values(), id=doc.id) for doc in documents]


def get_contacts_for_current_limetype(app, limetype, record_id):
    current_limetype = app.limetypes.get_limetype(limetype).get(record_id)
    properties = current_limetype.properties
    has_company = hasattr(properties, 'company')
    related_company = properties.company if has_company else False

    if limetype == "company":
        contacts = app.limetypes.get_limetype('person').get_all(
            filter=Filter(EqualsOperator(limetype, record_id)))
    elif related_company:
        contacts = app.limetypes.get_limetype('person').get_all(filter=Filter(
            EqualsOperator("company", app.limetypes.get_limetype(limetype)
                           .get(record_id).properties.company.id)))
    else:
        contacts = []
    return [dict(**contact.values(), id=contact.id) for contact in contacts]


def match_merge_fields(limeobject, data):
    fields = data.get('fields', [])
    for field in fields:
        value = get_merge_field_value(limeobject, field)
        field.update({
            'field_label': field.get('field_label') or
            field.get('field_value'),
            'field_value': value
        })
    return fields


def get_file_data(app, document_id):
    document = app.limetypes.get_limetype('document').get(document_id)
    return document.properties.document.fetch()


def get_merge_field_value(limeobject, field):
    try:
        key = field['field_value'].replace(
            '{{', '').replace('}}', '')

        value = _serialize_properties_and_values(
            get_lime_values(limeobject))[key]
        return value
    except Exception:
        return field['field_value']


def extract_value(prop, fetch_nested=True):
    if isinstance(prop, BelongsToPropertyAccessor):
        nested_obj = prop.fetch()
        if not nested_obj or not fetch_nested:
            return prop.descriptive
        return {
          nested_prop.name: extract_value(nested_prop, False)
          for nested_prop in nested_obj.get_properties_with_value()
        }
    if isinstance(prop, OptionPropertyAccessor):
        return prop.value.key
    if isinstance(prop, SetPropertyAccessor):
        return [p.key for p in prop.value]
    if isinstance(prop, HasManyPropertyAccessor):
        if not fetch_nested:
            return prop.value
        result = []
        for nested_obj in prop.fetch():
            properties_dict = {
                nested_prop.name: extract_value(nested_prop, False)
                for nested_prop in nested_obj.get_properties_with_value()
            }
            result.append(properties_dict)
        return result
    return prop.value


def get_lime_values(limeobject):
    props = limeobject.properties

    def get_prop_names_to_ignore():
        ignored_props = {
            '*': ['history', 'todo']
        }
        return ignored_props.get(
            limeobject.limetype.name,
            ignored_props.get('*', [])
        )

    values = {}

    for prop in props:
        if prop.name in get_prop_names_to_ignore():
            break
        value = extract_value(prop)

        if isinstance(value, dict):
            for k, v in value.items():
                values[f'{prop.name}.{k}'] = v
        elif isinstance(value, list):
            for i, item in enumerate(value, 1):
                for k, v in item.items():
                    values[f'{prop.name}{i}.{k}'] = v
        else:
            values[f'{limeobject.limetype.name}.{prop.name}'] = value

    return values

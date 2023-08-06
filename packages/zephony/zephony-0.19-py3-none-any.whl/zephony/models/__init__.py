import os
import datetime
import logging

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, or_, cast, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.types import (
    Date,
    String,
    Integer,
    Boolean,
    DateTime,
    Time,
)

from zephony.exceptions import InvalidRequestData, NonUpdatableFields

from zephony.helpers import(
    is_valid_datetime,
    get_rows_from_csv,
    serialize_datetime,
)

db = SQLAlchemy()
logger = logging.getLogger(__name__)


class BaseModel(db.Model):
    __abstract__ = True

    id_ = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(200), unique=True)
    status = db.Column(db.String(20), nullable=False, default='active')
    deleted_data = db.Column(JSONB)
    created_at = db.Column(db.DateTime, server_default=func.now())
    last_updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    readable_fields = []
    updatable_fields = []
    filterable_fields = []

    # TODO: Do assignments by doing datatype conversions for datetime, etc
    def __init__(self, data, from_seed_file=False):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    # TODO: Needs refactoring
    @staticmethod
    def _add_key_from_csv_row(data, k, v, row):
        if type(v) == tuple:
            if len(v) == 1:  # Value hardcoded right in the index being sent
                data[k] = v[0]
            elif len(v) == 2:  # Value has to be type casted
                # Do nothing if value is empty
                if not row[v[0]].strip():
                    return

                if v[1] is int:
                    data[k] = int(row[v[0]])
                elif v[1] is bool:
                    if row[v[0]] in ['true', 1, '1', '1.0', 'TRUE', 'True']:
                        data[k] = True
                    elif row[v[0]] in ['false', 0, '0', '0.0', 'FALSE', 'False']:
                        data[k] = False
                    else:
                        data[k] = None
                elif v[1] == 'datetime':
                    try:
                        date_str_format = '%d/%m/%Y' if '/' in row[v[0]] else '%Y-%m-%d'
                        data[k] = datetime.datetime.strptime(row[v[0]], date_str_format).isoformat()
                    except ValueError:
                        #TODO: Doing this only to make import work quickly
                        data[k] = None
                        # raise ValueError('`{}`: Cannot parse datetime'.format(row[v[0]]))
                elif v[1] == 'datetime_iso':
                    try:
                        date_str_format = '%d/%m/%Y' if '/' in row[v[0]] else '%Y-%m-%d'
                        data[k] = datetime.datetime.strptime(row[v[0]], date_str_format).isoformat()
                    except ValueError:
                        #TODO: Doing this only to make import work quickly
                        data[k] = None
                        # raise ValueError('`{}`: Cannot parse datetime'.format(row[v[0]]))
                elif callable(v[1]):
                    data[k] = v[1](row[v[0]])
                else:
                    raise ValueError('`{}`: Unsupported type to type case to'.format(v[1]))
            elif len(v) == 3:
                if v[2] == 'power_of_2':  # Used for permissions to calculate & store permission bit
                    # Permission bit cannot be empty
                    if not row[v[0]].strip():
                        raise ValueError('Permission bit value cannot be empty')

                    if v[1] is not int:
                        raise ValueError('`{}`: Cannot type cast to integer'.format(v[1]))

                    data[k] = str(2 ** (int(row[v[0]]) - 1))
                elif v[2] == 'boolean':
                    if row[v[0]].strip() == 'x':
                        data[k] = True
                    else:
                        data[k] = False
                elif v[2] == 'permission_tokens':
                    # Queries permissions table
                    from .permission import Permission
                    permissions_map = Permission.get_map()

                    permission_bit_sequence = 0
                    # Split by comma
                    if row[v[0]].strip():
                        permission_tokens = row[v[0]].strip().split(',')
                        for token in permission_tokens:
                            permission_bit_sequence |= int(permissions_map[token.strip()])

                    data[k] = str(permission_bit_sequence)
                elif v[2] == 'foreign_key':  # For foreign key relationships
                    cls = v[1]

                    # Query and get the object ID, if found, else, create new entry in the database and return the ID.
                    obj = cls.query.filter_by(
                        original_name=row[v[0]],
                        status='active'
                    ).first()

                    if not obj:
                        obj = cls({
                            'original_name': row[v[0]]
                        })
                        db.session.add(obj)
                        db.session.commit()

                    data[k] = obj.id_
                else:
                    raise Exception('Invalid value: `{}`'.format(v[2]))
            else:
                raise Exception('Invalid tuple length: `{}`'.format(len(v)))
        else:
            data[k] = row[v]

    def _get_base_details(self):
        
        base_details = {
            'id': self.id_,
            'token': self.token,
            'status': self.status,
            'created_at': serialize_datetime(
                self.created_at, '%Y-%m-%d %H:%M:%S.%f'
            ),
        }
        if self.last_updated_at:
            base_details['last_updated_at'] = serialize_datetime(
                self.last_updated_at, '%Y-%m-%d %H:%M:%S.%f'
            )
        else:
            base_details['last_updated_at'] = None
        
        return base_details

    @staticmethod
    def _convert_filters_map_to_list(filter_map):
        """
        Each filter parameter has a filter operator (starts_with,
        ends_with, etc.) and a field name. If a operator is not
        present, `equals` is used as the default operator.

        The filter parameter takes the following format:
            __<filter_operator>__<field_name>

        For example, if you want to get users who are younger than 20,
        you can use the filter parameter `__lesser_than__age` where
        `lesser_than` is the operator and `age` is the field name.

        The following filter parameter formats are allowed:

            1. Type: VARCHAR
                - __starts_with__<field_name>
                - __ends_with__<field_name>
                - __contains__<field_name>
                - __equals__<field_name>
            2. Type: INTEGER
                - __lesser_than__<field_name>
                - __greater_than__<field_name>
                - __equals__<field_name>
            3. Type: BOOLEAN
                - __equals__<field_name>
            4. Type: DATETIME
                - __from__<field_name>
                - __to__<field_name>
                - __equals__<field_name>

        Returns [{
            'key': <field_name>,
            'values': [<value1>, <value2>],
            'operator': <filter_operator>,
        }]
        """

        filters_list = []
        for filter_key_with_operator in filter_map:
            # If multiple values are present in the filter, use a comma
            # to separate them
            if ',' in filter_map[filter_key_with_operator]:
                values = filter_map[filter_key_with_operator].split(',')
            else:
                values = [ filter_map[filter_key_with_operator] ]

            filter_ = {
                'key': None,
                'values': values,
                'operator': None,
            }
            if filter_key_with_operator.startswith('__'):
                # First segment will be an empty string
                segments = filter_key_with_operator.split('__')[1:]
                filter_['operator'] = segments[0]
                filter_['key'] = segments[1]
            else:
                filter_['operator'] = 'equals'
                filter_['key'] = filter_key_with_operator

            filters_list.append(filter_)

        return filters_list


    # TODO: Needs refactoring
    @classmethod
    def load_from_csv(cls, f_path, column_index, delimiter=',', header=True,
            empty_check_col=1, repr_col=1, row_commit=False):
        """
        This function takes a relative path of a csv file and populates
        the database with the contents of the csv file.

        :param str f_path: The relative path to the file
        :param dict column_index: Model field_name, CSV index mapper
        :param bool header: Flag to determine whether to skip first line of CSV
        :param int empty_check_col: The column count if empty marks last line of CSV
        :param int repr_col: The value to be printed for each row in log messages
        :param bool row_commit: If True, commit immediately after adding to session

        :return bool: True
        """

        objects = []
        duplicates = []
        rows = get_rows_from_csv(
            f_path,
            delimiter=delimiter,
            header=header,
            empty_check_col=empty_check_col,
        )
        for row_index, row in enumerate(rows):
            # logger.debug('Loading {} `{}` from CSV..'.format(cls.__name__, row[repr_col]))
            data = {}
            for k, v in column_index.items():
                if type(v) == dict:  # Handling nested dictionary
                    data[k] = {}
                    for sk, sv in v.items():  # sk: sub_key, sv: sub_value :P
                        cls._add_key_from_csv_row(data[k], sk, sv, row)
                else:
                    cls._add_key_from_csv_row(data, k, v, row)

            # The following try-except block applies only for user
            # Skip row if error occurs
            try:
                obj = cls(data, from_seed_file=True)
            except InvalidRequestData as e:
                if hasattr(e, 'duplicate') and e.duplicate:
                    duplicates.append(e.duplicate.get_details())
                e.row = row_index
                continue
            db.session.add(obj)

            if row_commit:
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()

            objects.append(obj)

        res = {
            'objects': objects,
            'total_non_empty_rows': len(rows),
        }

        if duplicates:
            res['duplicates'] = duplicates

        return res

    @classmethod
    def add_filters_to_query(cls, q, filters_map, filterable_fields):
        # Convert filters map to filters list
        filters = cls._convert_filters_map_to_list(filters_map)

        if os.environ.get('APP_ENV', None) in (None, 'dev', 'development'):
            logger.info('----------------------------------------')
            logger.info(f'Filters fields to be applied : {filters}')
            logger.info('----------------------------------------')
            logger.info(f'Allowed filters fields : {filterable_fields}')
            logger.info('----------------------------------------')

        for filter_ in filters:
            if filter_['key'] in filterable_fields:
                filter_attr = filterable_fields[f"{filter_['key']}"]
                field_type = filter_attr.type
            else:
                logger.info(f'Ignoring invalid filters : {filter_}')
                continue

            if isinstance(field_type, String):
                if filter_['operator'] == 'starts_with':
                    q = q.filter(
                        or_(
                            *[filter_attr.ilike(v+'%') for v in filter_['values']]
                        )
                    )
                elif filter_['operator'] == 'ends_with':
                    q = q.filter(
                        or_(
                            *[filter_attr.ilike('%'+v) for v in filter_['values']]
                        )
                    )
                elif filter_['operator'] == 'contains':
                    q = q.filter(
                        or_(
                            *[filter_attr.ilike('%'+v+'%') for v in filter_['values']]
                        )
                    )
                elif filter_['operator'] == 'equals':
                    q = q.filter(
                        or_(
                            *[func.lower(filter_attr) == v.lower() for v in filter_['values']]
                        )
                    )
                else:
                    logger.warn(
                        f'Ignoring invalid operator `{filter_["operator"]}`'
                    )
            elif isinstance(field_type, Integer):
                filter_['values'] = [
                    int(v) for v in filter_['values']
                    if v and v.isdigit()
                ]

                if not filter_['values']:
                    continue

                if filter_['operator'] == 'lesser_than':
                    q = q.filter(
                        or_(*[
                            (filter_attr < v for v in filter_['values']),
                        ])
                    )
                elif filter_['operator'] == 'greater_than':
                    q = q.filter(
                        or_(*[
                            (filter_attr > v for v in filter_['values']),
                        ])
                    )
                elif filter_['operator'] == 'equals':
                    q = q.filter(
                        or_(*[
                            (filter_attr == v for v in filter_['values']),
                        ])
                    )
                else:
                    logger.warn(
                        f'Ignoring invalid operator `{filter_["operator"]}`'
                    )
            elif isinstance(field_type, DateTime):
                filter_['values'] = list(filter(
                    lambda v: is_valid_datetime(v, '%Y-%m-%d'),
                    filter_['values'],
                ))

                if not filter_['values']:
                    continue

                if filter_['operator'] == 'from':
                    q = q.filter(
                        or_(*[
                            filter_attr >= v for v in filter_['values']
                        ])
                    )
                elif filter_['operator'] == 'to':
                    q = q.filter(
                        or_(*[
                            filter_attr <= v for v in filter_['values']
                        ])
                    )
                elif filter_['operator'] == 'equals':
                    q = q.filter(
                        or_(*[
                            filter_attr == v for v in filter_['values']
                        ])
                    )
                else:
                    logger.warn(
                        f'Ignoring invalid operator `{filter_["operator"]}`'
                    )
            elif isinstance(field_type, Boolean):
                # Remove values that are neither 'true' nor 'false'
                filter_['values'] = list(filter(
                    lambda v: v.lower() in ('true', 'false'),
                    filter_['values'],
                ))

                if not filter_['values']:
                    continue

                q = q.filter(
                    or_(*[
                        (filter_attr == v for v in filter_['values']),
                    ])
                )
            else:
                logger.warn(f'Field type not handled {field_type}')

        return q

    # NOTE: Doesn't do any joins
    @classmethod
    def get_one(cls, id_or_token, status='active'):
        """
        Returns the object from the database based on whether the
        filter is the id or the token. Returns None if the object
        is not found.

        Pass status=None if you don't want the status filter to be
        applied.
        """

        # id_or_token contains the id
        if type(id_or_token) == int:
            obj = cls.query.get(id_or_token)

            if status is None:
                return obj

            if obj and obj.status == status:
                return obj

            return None

        # id_or_token contains the token
        elif type(id_or_token) == str:
            if status is None:
                obj = cls.query.filter_by(token=id_or_token).first()
            else:
                obj = cls.query.filter(
                    cls.token == id_or_token,
                    cls.status == status,
                ).first()

            return obj

        else:
            raise ValueError

    # NOTE: Doesn't do any joins
    @classmethod
    def get_all(cls, status='active'):
        """
        Returns all the objects from the database.
        Pass status=None if you don't want the status filter to be applied.
        """

        if status is None:
            return cls.query.all()
        return cls.query.filter_by(status=status).all()

    # TODO: Accept multiple statuses
    @classmethod
    def get_all_objects_details(cls, joins=[], filters_map={}, status='active', pagination={}):
        """
        Pass status=None if you don't want the status filter to be
        applied.
        """

        # Do the status filtering
        if status is None:
            q = cls.query
        else:
            q = cls.query.filter(cls.status==status)

        # Do any custom filtering
        q = cls.add_filters_to_query(q, filters_map)

        # Do all necessary joins
        for join in joins:
            q = (
                q.outerjoin(join[0], getattr(cls, join[1]) == join[0].id_)
                .add_entity(join[0])
            )

        # Do the default ordering (using the `id` field)
        q = q.order_by(
            cls.id_,
        )

        # Get the total retrieved results
        count = q.count()

        # Get paginated_query
        q = cls.add_pagination_to_query(
            q=q,
            page=pagination.get('page'),
            page_size=pagination.get('page_size'),
        )

        # Fetch the results
        results = q.all()

        objects_details = []
        for result in results:
            # If not joined, `result` represents the object else,
            # need to get the details via the attribute in the
            # result object
            if len(joins) > 0:
                details = getattr(result, cls.__name__).get_details()
            else:
                details = result.get_details()

            for join in joins:
                details[join[2]] = getattr(result, join[0].__name__).get_details()
            objects_details.append(details)

        # If the `with_summary` param is set, return the data with the
        # pagination details
        if pagination.get('with_summary'):
            return (objects_details, count)

        return objects_details

    @staticmethod
    def add_ordering_to_query(q, allowed_fields, order_by=None, reverse=False):
        """
        Function to add sorting to the given query

        :param q str: Constructed query
        :param sortable_fields dict: Map of fields allowed for sorting
        :param order_by str: Order by field
        :param reverse bool: Flag to decide whether to sort ascending or descending

        :return str: Constructed query
        """

        try:
            if reverse.lower() in ('1', 'true'):
                reverse = True
            else:
                reverse = False
        except (TypeError, ValueError, AttributeError):
            reverse = False
        
        if order_by and order_by in allowed_fields:
            logger.info(f'Allowed order by field : {order_by}')
            param = allowed_fields[order_by]

            if reverse:
                param = desc(param)

            q = q.order_by(param)

        return q

    @staticmethod
    def add_pagination_to_query(q, page, page_size):
        """
        This function is to add pagination related clauses to the
        given query.

        :param q str: Constructed query
        :param page int: Page number
        :param page_size int: Page size

        :return str: Constructed query
        """

        # If page is None, do not apply pagination
        if page:
            # If valid page number is not given, default it to page 1 of size 100
            try:
                page = int(page)
                if page <= 0:
                    raise ValueError
            except:
                page = 1
        else:
            return q

        # If valid page size is not given, default it to zero
        try:
            page_size = int(page_size)
            if page_size <= 0:
                raise ValueError
        except:
            page_size = 100

        q = (
            q.limit(page_size)
            .offset((page-1) * page_size)
        )

        return q

    # NOTE: This doesn't do any joins
    def get_details(self):
        base_details = self._get_base_details()
        main_details = {}

        for field in self.readable_fields:
            field_type = type(self).__table__.c[field].type
            if isinstance(field_type, DateTime):
                main_details[field] = serialize_datetime(getattr(self, field), '%Y-%m-%d %H:%M:%S.%f')
            elif isinstance(field_type, Date):
                main_details[field] = serialize_datetime(getattr(self, field), '%Y-%m-%d')
            elif isinstance(field_type, Time):
                main_details[field] = serialize_datetime(getattr(self, field), '%H:%M')
            else:
                main_details[field] = getattr(self, field)

        return {**base_details, **main_details}

    def update(self, data):
        """
        This function directly updates all the elements in the `data`
        dictionary by copying their values into the corresponding
        object attribute with the same key name. All validations have
        to be take care of properly beforehand.
        """

        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        self.last_updated_at = datetime.datetime.now()
        base_details = self._get_base_details()
        return {**base_details, **data}

    def soft_delete(self):
        """
        This function sets the status of an object (row) to `deleted`
        and sets the value of the `deleted_at` to the current time.
        This function does not commit the changes to the database,
        that has to be taken care of in the actions layer.

        Only currently `active` objects can be deleted.
        """

        self.status = 'deleted'
        self.deleted_data = self.get_details()
        self.token = None
        self.deleted_at = datetime.datetime.now()

        return self


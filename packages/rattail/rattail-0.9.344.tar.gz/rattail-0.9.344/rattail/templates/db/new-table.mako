## -*- coding: utf-8; mode: python; -*-
# -*- coding: utf-8; -*-
"""
Table schema for ${model_title_plural}
"""

import sqlalchemy as sa
# from sqlalchemy import orm

from rattail.db import model


class ${model_name}(model.Base):
    """
    ${description}
    """
    __tablename__ = '${table_name}'
    model_title = "${model_title}"
    model_title_plural = "${model_title_plural}"
    % if versioned:
    % if all([c['versioned'] for c in columns]):
    __versioned__ = {}
    % else:
    __versioned__ = {
        'exclude': [
        % for column in columns:
        % if not column['versioned']:
        '${column['name']}',
        % endif
        % endfor
        ],
    }
    % endif
    % endif
    % for column in columns:

    % if column['name'] == 'uuid':
    uuid = model.uuid_column()
    % else:
    ${column['name']} = sa.Column(sa.${column['data_type']}, nullable=${column['nullable']}, doc="""
    ${column['description']}
    """)
    % endif
    % endfor

    # TODO: you usually should define the __str__() method

    # def __str__(self):
    #     return self.name or ""

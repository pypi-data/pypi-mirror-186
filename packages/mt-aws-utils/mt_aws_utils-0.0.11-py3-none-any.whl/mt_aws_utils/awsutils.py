'''Mark This database utility module.'''
import json
from functools import lru_cache
from mt_aws_utils.dbutil import Db


class AWSMarkThis(Db):
    '''AWS MarkThis database access layer'''

    def style_insert(self, style, positions):
        '''Insert question positions for style.  position should be a dict, will be
        stored as json'''

        qry = '''INSERT into style
                 (style, positions, created_at)
                 VALUES(%s, %s, NOW())'''

        return self.singlequery(qry, (style, json.dumps(positions)))

    @lru_cache(maxsize=40)
    def style_get(self, style):
        '''gets question positions for style.  Returns dict {qno: Rect}'''
        qry = 'SELECT positions FROM style WHERE style=%s'

        for row in self.namedselect(qry, (style,)):
            return json.loads(row['positions'])

        return {}

    def style_delete(self, style):
        '''deletes info for style'''
        return self.singlequery('DELETE FROM style WHERE style=%s', (style,))

    def sheet_insert(self, rows):
        '''Insert sheets.
        rows is a list of tuples.  Each row has the following items in order
        sheetid, owner, title, style, answers_csv, positions '''

        qry = '''INSERT into sheet
                 (sheetid, owner, title, style, answers_csv, positions, created_at)
                 VALUES(%s, %s, %s, %s, %s, %s, NOW())'''

        return self.executemany(qry, rows)

    @lru_cache(maxsize=100)
    def sheet_get(self, sheetid):
        '''gets sheet info for sheetid'''
        qry = 'SELECT * FROM sheet WHERE sheetid=%s'

        for row in self.namedselect(qry, (sheetid,)):
            return row

        return None

    def sheet_ids_exist(self, sheetids):
        '''Returns any sheet ids in sheetids that exist'''

        ids =','.join(s for s in sheetids)

        qry = f'SELECT sheetid FROM sheet WHERE sheetid IN ({ids})'

        found = set()

        for row in self.namedselect(qry):
            found.add(row['sheetid'])

        return found

    def page_insert(self, rows):
        '''Insert pages from list of rows (tuples).
        Tuples in following order.
        stackid, page_number, original'''

        qry = '''INSERT into page
                 (stackid, page_number, queued_at, original)
                 VALUES(%s, %s, NOW(), %s)'''

        return self.executemany(qry, rows)

    def page_get(self, stackid, page_number):
        '''gets a page based on stackid and page_number'''

        qry = 'SELECT * FROM page WHERE stackid=%s AND page_number=%s'

        for row in self.namedselect(qry, (stackid, page_number)):
            return row

        return None

    def page_get_all(self, stackid):
        '''gets all pages with specific stackid'''
        qry = 'SELECT * FROM page WHERE stackid=%s'

        for row in self.namedselect(qry, (stackid,)):
            return row

        return None

    def stack_insert(self, stack):
        '''Insert stack'''

        arglist = ()
        columns = []

        for key, val in stack.items():
            columns += [key]
            arglist += (val,)

        qry = 'INSERT into stack (' + ', '.join(columns) + ') ' +\
              'VALUES(' + ', '.join(['%s'] * len(columns)) + ')'

        return self.singlequery(qry, arglist)

    def stack_get(self, stackid):
        '''gets stack from stackid'''
        qry = 'SELECT * FROM stack WHERE stackid=%s'

        for row in self.namedselect(qry, (stackid,)):
            return row

        return None

    def stack_processed_update(self, stackid, status='done'):
        '''marks stack as processsed'''

        qry = '''UPDATE stack
                 SET processed_at=NOW(), status_message=%s
                 WHERE id=%s'''

        return self.singlequery(qry, (status, stackid))

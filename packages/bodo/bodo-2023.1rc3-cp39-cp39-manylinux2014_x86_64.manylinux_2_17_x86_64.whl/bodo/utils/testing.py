import os
import shutil
from contextlib import contextmanager
import pandas as pd
import bodo


@bodo.jit
def get_rank():
    return bodo.libs.distributed_api.get_rank()


@bodo.jit
def barrier():
    return bodo.libs.distributed_api.barrier()


@contextmanager
def ensure_clean(filename):
    try:
        yield
    finally:
        try:
            barrier()
            if get_rank() == 0 and os.path.exists(filename) and os.path.isfile(
                filename):
                os.remove(filename)
        except Exception as dxkhw__uqo:
            print('Exception on removing file: {error}'.format(error=
                dxkhw__uqo))


@contextmanager
def ensure_clean_dir(dirname):
    try:
        yield
    finally:
        try:
            barrier()
            if get_rank() == 0 and os.path.exists(dirname) and os.path.isdir(
                dirname):
                shutil.rmtree(dirname)
        except Exception as dxkhw__uqo:
            print('Exception on removing directory: {error}'.format(error=
                dxkhw__uqo))


@contextmanager
def ensure_clean2(pathname):
    try:
        yield
    finally:
        barrier()
        if get_rank() == 0:
            try:
                if os.path.exists(pathname) and os.path.isfile(pathname):
                    os.remove(pathname)
            except Exception as dxkhw__uqo:
                print('Exception on removing file: {error}'.format(error=
                    dxkhw__uqo))
            try:
                if os.path.exists(pathname) and os.path.isdir(pathname):
                    shutil.rmtree(pathname)
            except Exception as dxkhw__uqo:
                print('Exception on removing directory: {error}'.format(
                    error=dxkhw__uqo))


@contextmanager
def ensure_clean_mysql_psql_table(conn, table_name_prefix='test_small_table'):
    import uuid
    from mpi4py import MPI
    from sqlalchemy import create_engine
    occ__pbu = MPI.COMM_WORLD
    try:
        shtu__jtz = None
        if bodo.get_rank() == 0:
            shtu__jtz = f'{table_name_prefix}_{uuid.uuid4().hex}'
        shtu__jtz = occ__pbu.bcast(shtu__jtz)
        yield shtu__jtz
    finally:
        bodo.barrier()
        qsv__svdxp = None
        if bodo.get_rank() == 0:
            try:
                pvbai__lkp = create_engine(conn)
                ruiie__pgt = pvbai__lkp.connect()
                ruiie__pgt.execute(f'drop table if exists {shtu__jtz}')
            except Exception as dxkhw__uqo:
                qsv__svdxp = dxkhw__uqo
        qsv__svdxp = occ__pbu.bcast(qsv__svdxp)
        if isinstance(qsv__svdxp, Exception):
            raise qsv__svdxp


@contextmanager
def ensure_clean_snowflake_table(conn, table_name_prefix='test_table',
    parallel=True):
    import uuid
    from mpi4py import MPI
    occ__pbu = MPI.COMM_WORLD
    try:
        shtu__jtz = None
        if bodo.get_rank() == 0 or not parallel:
            shtu__jtz = f'{table_name_prefix}_{uuid.uuid4().hex}'.upper()
        if parallel:
            shtu__jtz = occ__pbu.bcast(shtu__jtz)
        yield shtu__jtz
    finally:
        if parallel:
            bodo.barrier()
        qsv__svdxp = None
        if bodo.get_rank() == 0 or not parallel:
            try:
                pd.read_sql(f'drop table if exists {shtu__jtz}', conn)
            except Exception as dxkhw__uqo:
                qsv__svdxp = dxkhw__uqo
        if parallel:
            qsv__svdxp = occ__pbu.bcast(qsv__svdxp)
        if isinstance(qsv__svdxp, Exception):
            raise qsv__svdxp

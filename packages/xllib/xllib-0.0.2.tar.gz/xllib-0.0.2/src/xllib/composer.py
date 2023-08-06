from math import ceil
from pathlib import Path
from .utils import *


class CT:
    def __init__(self, x, 
                 sep=", ", sheet=0, in_encoding="utf-8", pd_colnames=True):
        self.x = self.__load_data(x, sheet=sheet, encoding=in_encoding, pd_colnames=pd_colnames)
        self.sep = sep

    def __repr__(self) -> str:
        tbl = []
        for row in self.x:
            fmt = '{' + f'0:>{self.max_el_width()}' + '}'
            row_repr = '[' + self.sep.join(
                fmt.format(f'"{el}"') if (isinstance(el, str) and len(el) > 0) 
                else fmt.format(el)
                for el in row) + ']'
            tbl.append(row_repr)
        return '[' + '\n '.join(tbl) + ']'
    
    def max_el_width(self):
        val = max( len(str(el)) for row in self.x for el in row )
        has_str = any( (isinstance(el, str) and len(el) > 0) for row in self.x for el in row)
        if has_str: val += 2
        if val == 0: val += 1
        return val

    def __mul__(self, tbl):
        if isinstance(tbl, list):
            merged = tbl_cbind([self.x, tbl])
        else:
            merged = tbl_cbind([self.x, tbl.x])
        return CT(merged)

    def __truediv__(self, tbl):
        if isinstance(tbl, list):
            merged = tbl_rbind([self.x, tbl])
        else:
            merged = tbl_rbind([self.x, tbl.x])
        return CT(merged)
    
    def __load_data(self, x, encoding, sheet, pd_colnames):
        if isinstance(x, list):
            return x
        elif type(x).__name__ == 'DataFrame':
            if pd_colnames:
                return [ x.columns.values.tolist() ] + x.values.tolist()
            return x.values.tolist()
        elif isinstance(x, str):
            x = Path(x)
            if x.suffix == '.xlsx':
                return readxl(x, sheet=sheet)
            elif x.suffix == '.csv':
                return read_csv(x, encoding=encoding)
            elif x.suffix == '.tsv':
                return read_csv(x, encoding=encoding, delimiter='\t')
            elif x.suffix == '.json':
                return read_json_tbl(x)
            else:
                raise Exception('Unsupported input format! Supports only `.xlsx/.csv/.tsv/.json`.')

    def cbind(self, tbl):
        return self.__mul__(tbl)
    
    def rbind(self, tbl):
        return self.__truediv__(tbl)
    
    def replace(self, old, replacement):
        tbl = deepcopy(self.x)
        for i, row in enumerate(self.x):
            for j, col in enumerate(row):
                if col == old:
                    tbl[i][j] = replacement
        return CT(tbl)
    
    def t(self):
        return CT(transpose(self.x))

    def reorder_rows(self, indices: list):
        new_tbl = []
        for i in indices:
            new_tbl.append(self.x[i])
        return CT(new_tbl)
    
    def reorder_cols(self, indices: list):
        old_tbl = transpose(self.x)
        new_tbl = []
        for i in indices:
            new_tbl.append(old_tbl[i])
        return CT(transpose(new_tbl))

    def to_csv(self, fp=None, encoding="utf-8", sep=","):
        write_csv(self.x, fp=fp, encoding=encoding, sep=sep)
    
    def to_xlsx(self, fp=None):
        writexl(self.x, fp)


def R(n=1, data=""):
    if isinstance(data, list) or isinstance(data, tuple):
        tbl = []
        n_el = len(data)
        n_el_per_row = ceil(n_el / n)
        added = 0
        for i in range(n):
            row = []
            for j in range(n_el_per_row):
                if added < n_el:
                    row.append(data[added])
                else:
                    row.append("")
                added += 1
                if j == n_el_per_row - 1:
                    tbl.append(row)
        return CT(tbl)
    return CT([ [data] ] * n)


def C(n=1, data=""):
    return CT(transpose(R(n, data).x))


def rbind(tbls, fill=""):
    merged = tbl_rbind(tbls, fill)
    return CT(merged)

def cbind(tbls, fill=""):
    merged = tbl_cbind(tbls, fill)
    return CT(merged)

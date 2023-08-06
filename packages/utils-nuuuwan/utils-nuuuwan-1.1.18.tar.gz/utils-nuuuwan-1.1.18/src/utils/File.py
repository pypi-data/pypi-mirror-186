import csv
import json
import os
import zipfile

from utils.FileOrDirectory import FileOrDirectory

DIALECT = 'excel'
DELIMITER_CSV = ','
DELIMITER_TSV = '\t'
DELIM_LINE = '\n'


class File(FileOrDirectory):
    def __init__(self, path):
        self.path = path

    @property
    def ext(self):
        return self.name.split('.')[-1]

    def read(self):
        with open(self.path, 'r') as fin:
            content = fin.read()
            fin.close()
        return content

    def readBinary(self):
        with open(self.path, 'rb') as fin:
            content = fin.read()
            fin.close()
        return content

    def write(self, content):
        with open(self.path, 'w') as fout:
            fout.write(content)
            fout.close()

    def writeBinary(self, content):
        with open(self.path, 'wb') as fout:
            fout.write(content)
            fout.close()

    def read_lines(self):
        content = File.read(self)
        return content.split(DELIM_LINE)

    def write_lines(self, lines):
        content = DELIM_LINE.join(lines)
        File.write(self, content)


class JSONFile(File):
    def read(self):
        content = File.read(self)
        return json.loads(content)

    def write(self, data):
        content = json.dumps(data, indent=2)
        File.write(self, content)


class XSVFile(File):
    def __init__(self, path, delimiter):
        File.__init__(self, path)
        self.delimiter = delimiter

    @staticmethod
    def _readHelper(delimiter: str, xsv_lines: list):
        data_list = []
        field_names = None
        reader = csv.reader(
            xsv_lines,
            dialect=DIALECT,
            delimiter=delimiter,
        )
        for row in reader:
            if not field_names:
                field_names = row
            else:
                data = dict(
                    zip(
                        field_names,
                        row,
                    )
                )
                if data:
                    data_list.append(data)
        return data_list

    def read(self):
        xsv_lines = File.read_lines(self)
        return XSVFile._readHelper(self.delimiter, xsv_lines)

    def write(self, data_list):
        with open(self.path, 'w') as fout:
            writer = csv.writer(
                fout,
                dialect=DIALECT,
                delimiter=self.delimiter,
            )

            field_names = list(data_list[0].keys())
            writer.writerow(field_names)
            writer.writerows(
                list(
                    map(
                        lambda data: list(
                            map(
                                lambda field_name: data[field_name],
                                field_names,
                            )
                        ),
                        data_list,
                    )
                ),
            )
            fout.close()


class CSVFile(XSVFile):
    def __init__(self, path):
        return XSVFile.__init__(self, path, DELIMITER_CSV)


class TSVFile(XSVFile):
    def __init__(self, path):
        return XSVFile.__init__(self, path, DELIMITER_TSV)


class Zip:
    def __init__(self, path):
        self.path = path

    @property
    def zip_path(self):
        return self.path + '.zip'

    @property
    def arc_name(self):
        return os.path.basename(os.path.normpath(self.path))

    @property
    def dir_zip(self):
        return os.path.dirname(os.path.normpath(self.path))

    def zip(self, skip_delete=False):
        assert os.path.exists(self.path)
        with zipfile.ZipFile(
            self.zip_path,
            mode='w',
            compression=zipfile.ZIP_DEFLATED,
        ) as zip_file:
            zip_file.write(self.path, arcname=self.arc_name)
            assert os.path.exists(self.zip_path)

        if not skip_delete:
            os.remove(self.path)
            assert not os.path.exists(self.path)

    def unzip(self, skip_delete=False):
        assert os.path.exists(self.zip_path)
        with zipfile.ZipFile(self.zip_path) as zip_file:
            zip_file.extractall(self.dir_zip)
            assert os.path.exists(self.path)

        if not skip_delete:
            os.remove(self.zip_path)
            assert not os.path.exists(self.zip_path)

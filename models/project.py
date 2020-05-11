class Project(object):

    def __init__(self, vals):
        self.name = vals[0]
        self.number = vals[1]
        self.pis = vals[2]
        self.end_date = vals[3]
        self.organization = vals[4]
        self.abstract = vals[5]

    @staticmethod
    def get(excel_file):
        import xlrd

        wb = xlrd.open_workbook(excel_file)
        sheet = wb.sheet_by_index(0)
        projects = []
        for row in range(1, sheet.nrows):
            values = []
            for col in range(sheet.ncols):
                values.append(sheet.cell(row, col).value)
            projects.append(Project(values))

        return projects

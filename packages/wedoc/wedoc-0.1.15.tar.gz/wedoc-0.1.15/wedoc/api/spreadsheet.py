from wedoc.api.base import WedocApiBase


class Spreadsheet(WedocApiBase):
    def __init__(self, docid: str = None, client: object = None) -> None:
        super().__init__(client)
        self.docid = docid
        self.sheet_metadata = self.get_sheet_properties()

    def get_sheet_properties(self) -> dict:
        """
        获取表格行列信息

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> wb = client.workbook("docid")
        >>> wb.get_sheet_properties()
        """

        api = "/wedoc/spreadsheet/get_sheet_properties"
        pyload = {"docid": self.docid}
        res = self.request("post", api, pyload=pyload)
        return res

    def get_sheet_range_data(self, sheet_id, range):
        """
        获取表格行列信息
        :param docid:
        :param sheet_id:
        :param range:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.wb.get_sheet_range_data("docid", "range")
        """
        api = "/wedoc/spreadsheet/get_sheet_range_data"
        pyload = {"docid": self.docid, "sheet_id": sheet_id, "range": range}
        res = self.request("post", api, pyload=pyload)
        return res

    def batch_update(self, pyload):
        """
        编辑表格内容
        :param docid:
        :return:

        使用示例

        >>> from wedoc import WedocClient
        >>> client = WedocClient("corpid", "corpsecret")
        >>> client.wb.batch_update("docid")
        """

        api = "/wedoc/spreadsheet/get_sheet_range_data"

        res = self.request("post", api, pyload=pyload)
        return res

    def get_sheet_names(self) -> list:
        """
        获取所有的 sheet 页数据
        :return:
        """
        res = self.get_sheet_properties(docid=self.docid)
        return [item.get("title") for item in res.get("data")]

    def get_active_sheet(self) -> str:
        res = self.get_sheet_properties(docid=self.docid)
        return [item.get("title") for item in res.get("data")][0]

    def get_sheet_id(self, sheet_name):
        for item in self.sheet_metadata:
            if item.get("title") == sheet_name:
                return item.get("sheet_id")
        else:
            raise ValueError("找不到 s% sheet 页" % sheet_name)

    def add_sheet(
        self, sheet_name: str, row_count: int = 10, column_count: int = 10
    ) -> dict:
        """
        添加 sheet 页
        :param docid: str,
        :param sheet_name: str,
        :param row_count: int = 10,
        :param column_count: int = 10,
        :return:
        """
        pyload = {
            "docid": self.docid,
            "requests": [
                {
                    "add_sheet_request": {
                        "title": sheet_name,
                        "row_count": row_count,
                        "column_count": column_count,
                    }
                },
            ],
        }
        return self.batch_update(pyload=pyload)

    def delete_sheet(self, sheet_name: str) -> dict:
        """
        删除 sheet 页
        :param sheet_id: str
        :retrun:
        """
        sheet_id = self.get_sheet_id(sheet_name=sheet_name)
        pyload = {
            "docid": self.docid,
            "requests": [
                {"delete_sheet_request": {"sheet_id": sheet_id}},
            ],
        }

        return self.batch_update(pyload=pyload)

    def rename_sheet(self):
        """
        重命名 sheet 页, 暂不支持
        """
        pass

    def get_row_counts(self, sheet_name: str = None):
        """
        获取总行数
        :param sheet_name: str
        :return: int
        """
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)

        for item in self.sheet_metadata:
            if item.get("sheet_id") == sheet_id:
                return item.get("row_count")

    def get_column_count(self, sheet_name=None):
        """
        获取总列数
        :param sheet_name: str
        :return: int
        """
        sheet_name = sheet_name if sheet_name else self.get_active_sheet()
        sheet_id = self.get_sheet_id(sheet_name)

        for item in self.sheet_metadata:
            if item.get("sheet_id") == sheet_id:
                return item.get("column_count")

    def get_cell(self, sheet_name=None):
        """
        读取单元格
        """
        pass

    def set_cell(self, sheet_name=None):
        """
        设置单元格数据
        """
        pass

    def get_range(self, sheet_name=None):
        """
        读取区域数据
        """
        pass

    def set_range(self, sheet_name=None):
        """
        读取区域数据
        """
        pass

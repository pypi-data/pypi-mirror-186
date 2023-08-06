class Model:
    """
    The Model represents the workspace (file-gdb or enterprise-gdb)

    catalog_path examples:
        c:/data.gdb
        c:/enterprise_gdb.sde
    """

    def __init__(self, name, catalog_path):
        self.name: str = name
        self.catalog_path: str = catalog_path

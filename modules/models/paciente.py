class Paciente:
    def __init__(self, df):
        self.df = df
        self.next_id = self._get_next_id()

    def _get_next_id(self):
        if "ID" in self.df.columns and not self.df["ID"].empty:
            try:
                return str(self.df["ID"].astype(int).max() + 1)
            except:
                print("Error al interpretar IDs. Usando '1'.")
                return "1"
        return "1"
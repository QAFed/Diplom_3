from datetime import datetime


class LoginPassName:
    def __init__(self):
        self.gen_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.name = f"name{self.gen_id}"
        self.email = f"FedorIdolenkov_{self.gen_id}@ya.ya"
        self.password = f"psswrd{self.gen_id}"
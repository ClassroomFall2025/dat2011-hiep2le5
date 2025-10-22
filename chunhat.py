class chunhat:
    def __init__(self,rong,dai):
        self.rong = rong
        self.dai = dai

    def get_chu_vi(self):
        return (self.rong + self.dai) * 2
    def get_dien_tich(self):
        return self.rong * self.dai
    
    def xuat(self):
        print(f"chieu rong: {self.rong}")
        print(f"chieu dai: {self.dai}")
        print(f"chu vi: {self.get_chu_vi()}")
        print(f"dien tich: {self.get_dien_tich()}")

class Vuong(chunhat):
    def __init__(self,canh):
        super().__init__(canh,canh)


    def xuat(self):
        print(f"canh: {self.dai}")
        print(f"chu vi: {self.get_chu_vi()}")
        print(f"dien tich: {self.get_dien_tich()}")
   
    def get_chu_vi(self):
        return self.dai * 4
    def get_dien_tich(self):
        return self.dai * self.dai
    def xuat(self):
        print(f"canh: {self.dai}")
        print(f"chu vi: {self.get_chu_vi()}")
        print(f"dien tich: {self.get_dien_tich()}")



   

    
    


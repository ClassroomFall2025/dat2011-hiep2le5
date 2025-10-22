class SinhVienPoly:
    def __init__(self,ho_ten,nganh_hoc):
        self.ho_ten = ho_ten
        self.nganh_hoc = nganh_hoc

    def get__diem(self):
        pass

    def get_hoc_luc(self): 
        if self.get__diem() >=9 and self.get__diem() <=10:
            hoc_luc = "Xuất sắc"
        elif  self.get__diem() >=8:
            hoc_luc = "Giỏi"
        elif self.get__diem() >=7:
            hoc_luc = "Khá"
        elif self.get__diem() >=5:
            hoc_luc = "Trung bình"
        elif self.get__diem() >=0:
            hoc_luc = "yếu"
        else:
            print("diem khong hop le ")
        return hoc_luc
    
    def __str__(self):

        
        return f"{self.ho_ten},{self.nganh_hoc},{self.get__diem()},{self.get_hoc_luc()}"
    def xuat(self):
        print( f"{self.ho_ten},{self.nganh_hoc},{self.get__diem()},{self.get_hoc_luc()}")
    
    
class SinhVienIT(SinhVienPoly):
    def __init__(self,ho_ten,nganh_hoc,diem_java,diem_html,diem_css):
         super().__init__(ho_ten,nganh_hoc)
         self.diem_java = diem_java
         self.diem_html = diem_html
         self.diem_css = diem_css
    def get__diem(self):
        return (self.diem_java*2 + self.diem_html + self.diem_css) /4

class SinhVienBiz(SinhVienPoly):
    def __init__(self,ho_ten,nganh_hoc,diem_marketing,diem_sales):
         super().__init__(ho_ten,nganh_hoc)
         self.__diem_marketing = diem_marketing
         self.__diem_sales = diem_sales 
    def get__diem(self):
        return (self.__diem_marketing * 2 + self.__diem_sales) / 3
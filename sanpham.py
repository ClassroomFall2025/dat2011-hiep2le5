class sanpham:
    def __init__(self,ten_san_pham,gia,giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self._giam_gia = giam_gia

   # def doc_giam_gia(self):
    #    return self._giam_gia
    
    #def ghi_giam_gia(self,giam_gia_moi):
       # self._giam_gia = giam_gia_moi

    def thue_nhap_khau(self):
        return self.gia * 0.1
    
    def nhap_thong_tin_san_pham(self):
        self.ten_san_pham = input("nhap ten san pham: ")
        self.gia = float(input("nhap gia : "))
        self._giam_gia = float(input("nhap giam gia san pham: "))
        
    def xuat_thong_tin_san_pham(self):
        print(f"san pham: {self.ten_san_pham} co gia: {self.gia} duoc giam gia:{self._giam_gia} thue nhap khau: {self.thue_nhap_khau()}")
    def __str__(self):
        return(f"san pham: {self.ten_san_pham} co gia: {self.gia} duoc giam gia:{self._giam_gia} thue nhap khau: {self.thue_nhap_khau()}")

class sanpham :
    def __init__(self,ten_san_pham,don_gia,so_luong):
        self.ten_san_pham = ten_san_pham
        self.don_gia = don_gia
        self.so_luong = so_luong
        


def tinh_nguyen_lieu (sl_btc,sl_dx,Sl_bd):
    banh_dau_xanh ={"dung": 0.04,"dau":0.07}
    banh_thap_cam ={"duong":0.06,"dau":0}
    banh_deo = {"dung":0.05,"dau":0.02}
    nguyen_lieu = {}
    duong_hop_banh = sl_dx * banh_dau_xanh["duong"] + sl_btc * banh_thap_cam["duong"] + Sl_bd * banh_deo["dung"]
    dau_hop_banh = sl_dx * banh_dau_xanh["dau"] + sl_btc * banh_thap_cam["dau"] + Sl_bd * banh_deo["dau"]
    nguyen_lieu["duong"] = duong_hop_banh
    nguyen_lieu["dau"] = dau_hop_banh
    return nguyen_lieu
def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 10000, 12000, 15000)
    if so_nuoc <= 10 and so_nuoc >=0:
        tien_nuoc_thang = so_nuoc*gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc_thang = 20 * gia_ban_nuoc[0] + (so_nuoc - 20) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc_thang = 20 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 30) * gia_ban_nuoc[2]
    else:
        tien_nuoc_thang = 20 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 40) * gia_ban_nuoc[3]     
        return tien_nuoc_thang
    menu = {
        "1" : "tinh tien nuoc",
        "2" : "tinh nguyen lieu",
        "3" : "thoat"
    }
    while True:
        print (================ MENU ========)
        for k,v in menu.items():
            print (k,":",v)
        lua_chon = input("Nhap lua chon cua ban: ")
        if lua_chon == "3":
            print("Cam on ban da su dung chuong trinh!")
            break
        elif lua_chon == "1":
            so_nuoc = float(input("so nuoc: "))
             print("tien nuoc thang la:", tinh_tien_nuoc(so_nuoc))
            print("Lua chon khong hop le, vui long chon lai!")
    

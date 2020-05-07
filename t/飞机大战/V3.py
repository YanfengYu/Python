import configparser


cfg = configparser.ConfigParser()
cfg.read("peizhiwenjian.ini")

sp_name = cfg.get("SmallPlane", "width")
print(sp_name)


import PySimpleGUI as sg

monkey_list = ["Dart","Boomer","Bomb","Tack","Ice","Glue","Sniper","Sub","Bucc","Ace","Heli","Morter",
               "Dartling","Wizard","Super","Ninja","Alch","Druid","Banana","Spactory","Village","Engineer","Beast"]

dart_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
boomer_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
bomb_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
tack_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
ice_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
glue_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
sniper_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
sub_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
bucc_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
ace_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
heli_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
morter_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
dartling_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
wizard_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
super_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
ninja_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
alch_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
druid_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
banana_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
spactory_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
village_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
engineer_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
beast_dic = {"000":"don't have","001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
            "002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
            "003":"don't have","013":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
            "004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
            "005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have",}
monkey_dic = {"Dart":dart_dic,"Boomer": boomer_dic,"Bomb":bomb_dic,"Tack":tack_dic,"Ice":ice_dic,"Glue":glue_dic,"Sniper": sniper_dic,
              "Sub":sub_dic,"Bucc":bucc_dic,"Ace":ace_dic,"Heli":heli_dic,"Morter":morter_dic,"Dartling":dartling_dic,"Wizard":wizard_dic,
              "Super":super_dic,"Ninja":ninja_dic,"Alch":alch_dic,"Druid":druid_dic,"Banana":banana_dic,"Spactory":spactory_dic,
              "Village": village_dic,"Engineer":engineer_dic,"Beast":beast_dic}

def create_main_window():
    layout = [
        [sg.Text("Hello")],
        [sg.Button("View"), sg.Button("Check")],
        [sg.Button("Settings")], 
        [sg.Button("Exit")]
    ]
    return sg.Window("BTD6 Insta Checker", layout, margins=(200,200))

def create_settings_window():
    layout = [
        [sg.Button("Back")],
    ]
    return sg.Window("Settings", layout, margins=(200,200))

def create_check_window():
    layout = [
        [sg.Button("Back")],
        [sg.Text("Enter the monkey Crosspath")],
        [
            sg.Combo(monkey_list, enable_events=True, default_value="Dart", key="-MONKEY-"),
            sg.Text('Path', size=(3, 1)), sg.Input(enable_events=True, key="-PATH-")
        ],
        [sg.Button("Clear"), sg.Button("Find")],
        [sg.Text(size=(40,1), key = "-OUTPUT-")],
        [sg.Button("Already Got", key="-HAVE-", visible = False), sg.Button("Just Got", key = "-JUST_GOT-", visible=False)]
    ]
    return sg.Window("View", layout, margins=(200,200))

def create_view_window():
    monkey_name_layout = [
        [sg.Text("Primary")],
        [sg.Button("Dart"), sg.Button("Boomer"), sg.Button("Bomb"), sg.Button("Tack"), sg.Button("Ice"), sg.Button("Glue")],
        [sg.Text("Military")],
        [sg.Button("Sniper"), sg.Button("Sub"), sg.Button("Bucc"), sg.Button("Ace"), sg.Button("Heli"), sg.Button("Morter"), sg.Button("Dartling")],
        [sg.Text("Magic")],
        [sg.Button("Wizard"), sg.Button("Super"), sg.Button("Ninja"), sg.Button("Alch"), sg.Button("Druid")],
        [sg.Text("Support")],
        [sg.Button("Banana"), sg.Button("Spatory"), sg.Button("Village"), sg.Button("Enginner"),sg.Button("Beast")],
    ]
    tier_list_layout = [
        [sg.Listbox(values=[], enable_events=True, size=(20, 20), key="-FILE LIST-")]
    ]
    layout = [
        [sg.Button("Back")],
        [
            sg.Column(monkey_name_layout),
            sg.VSeparator(),
            sg.Column(tier_list_layout),
        ]
    ]
    return sg.Window("View", layout, margins=(200,200))

def main():
    main_window = create_main_window()
    count = 0       #Used in Check Window to see if 2 paths are greater than 2
    correct = 0     #Check if the crosspath is right

    while True:
        event, values = main_window.read()

        #Exit out of application
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        #Enter the View window
        if event == "View":
            main_window.close()
            view_window = create_view_window()
            while True:
                event, values = view_window.read()

                #Exits out of application
                if event == sg.WINDOW_CLOSED:
                    view_window.close()
                    break
                #Returns back to main page
                if event == "Back":
                    view_window.close()
                    main_window = create_main_window()
                    break
        
        #Enter the Check window
        if event == "Check":
            main_window.close()
            check_window = create_check_window()
            while True:
                event, values = check_window.read()

                #Exits out of application
                if event == sg.WINDOW_CLOSED or event == 'Exit':
                    check_window.close()
                    break
                #Returns back to main page
                if event == "Back":
                    check_window.close()
                    main_window = create_main_window()
                    break
                    
                if event == "-PATH-" and values["-PATH-"]:
                    if values["-PATH-"][-1] not in ('012345'):
                        sg.popup("Only digits between 0-5 are allowed")
                        check_window['-PATH-'].update(values['-PATH-'][:-1])
                    if len(values["-PATH-"]) > 3:
                        sg.popup("Length cannot be greater than 3")
                        check_window['-PATH-'].update(values['-PATH-'][:-1])
                    if int(values["-PATH-"][-1]) > 2:               #######Needs to be improved#####
                        count += 1
                        if count == 2:
                            sg.popup("Can't have 2 crosspaths greater than 2")
                            check_window['-PATH-'].update(values['-PATH-'][:-1])
                            count -= 1
                
                if event == "Clear" or event == "-HAVE-":
                    check_window["-PATH-"].update('')
                    count = 0     
                    correct = 0
                    check_window["-HAVE-"].update(visible = False)
                    check_window["-JUST_GOT-"].update(visible = False)
                    check_window["-OUTPUT-"].update('')

                if event == "Find":
                    if len(values["-PATH-"]) == 3:
                        m = [*values.values()]
                        for i in monkey_dic.keys():
                            if i == m[0]:
                                for j in monkey_dic[i].keys():
                                    if j == m[1]:
                                        correct = 1
                                        check_window["-OUTPUT-"].update(f'You entered {m[0]} {m[1]} : you {monkey_dic[i][j]} the crosspath!')
                                        check_window["-HAVE-"].update(visible = True)
                                        check_window["-JUST_GOT-"].update(visible = True)
                                if correct == 0:
                                    sg.popup("No crosspath!")
                                    correct = 0
                    else:
                        sg.popup("Length must be exactly 3")
                
                if event == "-JUST_GOT-":
                    monkey_dic[i][j]= "have"
                    check_window["-OUTPUT-"].update(f'You entered {m[0]} {m[1]} : you {monkey_dic[i][j]} the crosspath!')

        #Access user settings for application
        if event == "Settings":
            main_window.close()
            settings_window = create_settings_window()
            while True:
                event, values =settings_window.read()

                #Exits out of application
                if event == sg.WINDOW_CLOSED:
                    settings_window.close()
                    break
                #Returns back to main page
                if event == "Back":
                    settings_window.close()
                    main_window = create_main_window()
                    break
    main_window.close()

if __name__ == '__main__':
    main()
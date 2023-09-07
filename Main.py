import PySimpleGUI as sg
import json

monkey_list = ["Dart","Boomer","Bomb","Tack","Ice","Glue","Sniper","Sub","Bucc","Ace","Heli","Morter",
               "Dartling","Wizard","Super","Ninja","Alch","Druid","Banana","Spactory","Village","Engineer","Beast"]
#1 Tier-0, 6 Tier-1s, 12 Tier-2s, 15 Tier-3s, 15 Tier-4s, and 15 Tier-5s.
dart_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
boomer_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
bomb_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
tack_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
ice_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
glue_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
sniper_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
sub_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
bucc_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
ace_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
heli_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
morter_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
dartling_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
wizard_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
super_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
ninja_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
alch_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
druid_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
banana_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
spactory_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
village_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
engineer_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}
beast_dic = {"000":"don't have",
"001":"don't have","010":"don't have","011":"don't have","100":"don't have","101":"don't have","110":"don't have",
"002":"don't have","012":"don't have","102":"don't have","020":"don't have","021":"don't have","120":"don't have","022":"don't have","200":"don't have","201":"don't have","210":"don't have","202":"don't have","220":"don't have",
"003":"don't have","013":"don't have","103":"don't have","023":"don't have","203":"don't have","030":"don't have","031":"don't have","130":"don't have","032":"don't have","230":"don't have","300":"don't have","301":"don't have","310":"don't have","302":"don't have","320":"don't have",
"004":"don't have","014":"don't have","104":"don't have","024":"don't have","204":"don't have","040":"don't have","041":"don't have","140":"don't have","042":"don't have","240":"don't have","400":"don't have","401":"don't have","410":"don't have","402":"don't have","420":"don't have",
"005":"don't have","015":"don't have","105":"don't have","025":"don't have","205":"don't have","050":"don't have","051":"don't have","150":"don't have","052":"don't have","250":"don't have","500":"don't have","501":"don't have","510":"don't have","502":"don't have","520":"don't have"}

monkey_dic = {"Dart":dart_dic,"Boomer": boomer_dic,"Bomb":bomb_dic,"Tack":tack_dic,"Ice":ice_dic,"Glue":glue_dic,"Sniper": sniper_dic,
              "Sub":sub_dic,"Bucc":bucc_dic,"Ace":ace_dic,"Heli":heli_dic,"Morter":morter_dic,"Dartling":dartling_dic,"Wizard":wizard_dic,
              "Super":super_dic,"Ninja":ninja_dic,"Alch":alch_dic,"Druid":druid_dic,"Banana":banana_dic,"Spactory":spactory_dic,
              "Village": village_dic,"Engineer":engineer_dic,"Beast":beast_dic}

dic_json = [dart_dic,boomer_dic,bomb_dic,tack_dic,ice_dic,glue_dic,sniper_dic,
              sub_dic,bucc_dic,ace_dic,heli_dic,morter_dic,dartling_dic,wizard_dic,
              super_dic,ninja_dic,alch_dic,druid_dic,banana_dic,spactory_dic,
              village_dic,engineer_dic,beast_dic]

# Create a UserSettings object. The JSON file will be saved in the same folder as this .py file
window_monkey = sg.UserSettings(path='.', filename='mysettings.json')

def create_main_window(theme):
    
    sg.theme(theme)
    layout = [
        [sg.Text("Hello")],
        [sg.Button("View"), sg.Button("Check")],
        [sg.Button("Settings"), sg.Button("Load")], 
        [sg.Button("Exit")]
    ]
    return sg.Window("BTD6 Insta Checker", layout, margins=(200,200), resizable=True)

def create_settings_window(theme):
    sg.theme(theme)
    layout = [
        [sg.Button("Back")],
        [sg.Combo(sg.theme_list(), default_value=theme, enable_events=True, key='-THEMES-')]
    ]
    return sg.Window("Settings", layout, margins=(200,200), resizable=True)

def create_check_window(theme):
    sg.theme(theme)
    layout = [
        [sg.Button("Back")],
        [sg.Text("Enter the monkey Crosspath")],
        [
            sg.Combo(monkey_list, enable_events=True, default_value="Dart", key="-MONKEY-"),
            sg.Text('Path', size=(3, 1)), sg.Input(enable_events=True, key="-PATH-")
        ],
        [sg.Button("Clear"), sg.Button("Find", bind_return_key = True, key = '-FIND-')],
        [sg.Text(size=(40,1), key = "-OUTPUT-")],
        [sg.Button("Already Got", key="-HAVE-", visible = False), sg.Button("Just Got", key = "-JUST_GOT-", bind_return_key = False, visible=False), 
         sg.Text(size=(8, 1),key = "-BLANK-", visible=False), sg.Button("Save", key = 'Save', visible=False), sg.Button("Reset", key = 'Reset', visible=False)]
    ]
    return sg.Window("View", layout, margins=(200,200), resizable=True)

def create_view_window(theme):
    sg.theme(theme)
    monkey_name_layout = [
        [sg.Text("Primary")],
        [sg.Button("Dart"), sg.Button("Boomer"), sg.Button("Bomb"), sg.Button("Tack"), sg.Button("Ice"), sg.Button("Glue")],
        [sg.Text("Military")],
        [sg.Button("Sniper"), sg.Button("Sub"), sg.Button("Bucc"), sg.Button("Ace"), sg.Button("Heli"), sg.Button("Morter"), sg.Button("Dartling")],
        [sg.Text("Magic")],
        [sg.Button("Wizard"), sg.Button("Super"), sg.Button("Ninja"), sg.Button("Alch"), sg.Button("Druid")],
        [sg.Text("Support")],
        [sg.Button("Banana"), sg.Button("Spactory"), sg.Button("Village"), sg.Button("Engineer"),sg.Button("Beast")],
    ]
    tier_list_layout = [
        [sg.Text(key = "-NAME-")],
        [sg.Multiline(size=(40,10),key = "-NOHAVE-", autoscroll=True)],
        [sg.Multiline(size=(40,10),key = "-HAVE-", autoscroll=True)]
    ]
    layout = [
        [sg.Button("Back")],
        [
            sg.Column(monkey_name_layout),
            sg.VSeparator(),
            sg.Column(tier_list_layout),
        ]
    ]
    return sg.Window("View", layout, margins=(200,200), resizable=True)

def main():
    # Requires version 4.29.0.16+
    try:
        saved_theme = sg.user_settings_get_entry('theme', 'Python')
    except:
        print("Your PySimpleGUI version doesn't have user settings API\n",
              "You need PySimpleGUI version 4.29.0.16 and above")
        saved_theme = 'Python'

    main_window = create_main_window(saved_theme)
    count = 0       #Used in Check Window to see if 2 paths are greater than 2
    correct = 0     #Check if the crosspath is right
    mon = ''        #Monkey 
    p = ''          #Crosspath
    loadCounter = 0
    jsonloaderCount = 0

    havestr = ''
    temph = ''
    donthavestr = ''
    tempdh = ''
    tier0 = 0;tier1 = 0;tier2 = 0;tier3 = 0;tier4 = 0;tier5 = 0
    tier1count = [0,0];tier2count = [0,0];tier3count = [0,0];tier4count = [0,0];tier5count = [0,0]

    while True:
        event, values = main_window.read()

        #Exit out of application
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        #Enter the View window
        if event == "View":
            main_window.close()
            view_window = create_view_window(saved_theme)
            while True:
                event, values = view_window.read()

                #Exits out of application
                if event == sg.WINDOW_CLOSED:
                    view_window.close()
                    break
                #Returns back to main page
                if event == "Back":
                    view_window.close()
                    main_window = create_main_window(saved_theme)
                    break

                if event in monkey_list:
                    view_window["-NAME-"].update(event)
                    havestr = 'HAVE\n'
                    donthavestr = 'DON\'T HAVE\n'
                    for x,y in monkey_dic[event].items():
                        if y == 'have':
                            if tier0 < 1 and x in ['000']:
                                tier0 += 1
                                havestr = havestr + 'Tier 0 (1/1)\n' + x + '\n\nTier 1 ('
                                donthavestr = donthavestr + 'Tier 0 (0/1)\n\n\nTier 1 ('
                            elif tier1 < 6 and x in ['001', '010','011','100','101','110']:
                                tier1 += 1
                                tier1count[0] += 1
                                temph = temph + x + '  '
                                if tier1 == 6:
                                    havestr = havestr + f'{tier1count[0]}' + '/6)\n'+ temph + '\n\nTier 2 ('
                                    donthavestr = donthavestr + f'{tier1count[1]}' + '/6)\n' + tempdh + '\n\nTier 2 ('
                                    temph = ''; tempdh = ''
                            elif tier2 < 12 and x in ['002','012','102','020','021','120','022','200','201','210','202','220']:
                                tier2 += 1
                                tier2count[0] += 1
                                temph = temph + x + '  '
                                if tier2count[0] == 9:
                                    temph = temph + '\n'
                                if tier2 == 12:
                                    havestr = havestr + f'{tier2count[0]}' + '/12)\n' + temph + '\n\nTier 3 ('
                                    donthavestr = donthavestr + f'{tier2count[1]}' + '/12)\n' + tempdh + '\n\nTier 3 ('
                                    temph = ''; tempdh = ''
                            elif tier3 < 15 and x in ['003','013','103','023','203','030','031','130','032','230','300','301','310','302','320']:
                                tier3 += 1
                                tier3count[0] += 1
                                temph = temph + x + '  '
                                if tier3count[0] == 9:
                                    temph = temph + '\n'
                                if tier3 == 15:
                                    havestr = havestr + f'{tier3count[0]}' + '/15)\n' + temph + '\n\nTier 4 ('
                                    donthavestr = donthavestr + f'{tier3count[1]}' + '/15)\n' + tempdh + '\n\nTier 4 (' 
                                    temph = ''; tempdh = ''      
                            elif tier4 < 15 and x in ['004','014','104','024','204','040','041','140','042','240','400','401','410','402','420']:                 
                                tier4 += 1
                                tier4count[0] += 1
                                temph = temph + x + '  '
                                if tier4count[0] == 9:
                                    temph = temph + '\n'
                                if tier4 == 15:
                                    havestr = havestr + f'{tier4count[0]}' + '/15)\n' + temph + '\n\nTier 5 ('
                                    donthavestr = donthavestr + f'{tier4count[1]}' + '/15)\n' + tempdh + '\n\nTier 5 (' 
                                    temph = ''; tempdh = ''    
                            elif tier5 < 15 and x in ['005','015','105','025','205','050','051','150','052','250','500','501','510','502','520']:
                                tier5 += 1
                                tier5count[0] += 1
                                temph = temph + x + '  '
                                if tier5count[0] == 9:
                                    temph = temph + '\n'
                                if tier5 == 15:
                                    havestr = havestr + f'{tier5count[0]}' + '/15)\n' + temph
                                    donthavestr = donthavestr + f'{tier5count[1]}' + '/15)\n' + tempdh
                                    temph = ''; tempdh = '' 
                        else:
                            if tier0 < 1 and x in ['000']:
                                tier0 += 1
                                donthavestr = donthavestr + 'Tier 0 (1/1)\n' + x + '\n\nTier 1 ('
                                havestr = havestr + 'Tier 0 (0/1)\n\n\nTier 1 ('
                            elif tier1 < 6 and x in ['001', '010','011','100','101','110']:
                                tier1 += 1
                                tier1count[1] += 1
                                tempdh = tempdh + x + '  '
                                if tier1 == 6:
                                    havestr = havestr + f'{tier1count[0]}' + '/6)\n'+ temph + '\n\nTier 2 ('
                                    donthavestr = donthavestr + f'{tier1count[1]}' + '/6)\n' + tempdh + '\n\nTier 2 ('
                                    temph = ''; tempdh = ''
                            elif tier2 < 12 and x in ['002','012','102','020','021','120','022','200','201','210','202','220']:
                                tier2 += 1
                                tier2count[1] += 1
                                tempdh = tempdh + x + '  '
                                if tier2count[1] == 9:
                                    tempdh = tempdh + '\n'
                                if tier2 == 12:
                                    havestr = havestr + f'{tier2count[0]}' + '/12)\n' + temph + '\n\nTier 3 ('
                                    donthavestr = donthavestr + f'{tier2count[1]}' + '/12)\n' + tempdh + '\n\nTier 3 ('
                                    temph = ''; tempdh = ''
                            elif tier3 < 15 and x in ['003','013','103','023','203','030','031','130','032','230','300','301','310','302','320']:
                                tier3 += 1
                                tier3count[1] += 1
                                tempdh = tempdh + x + '  '
                                if tier3count[1] == 9:
                                    tempdh = tempdh + '\n'
                                if tier3 == 15:
                                    havestr = havestr + f'{tier3count[0]}' + '/15)\n' + temph + '\n\nTier 4 ('
                                    donthavestr = donthavestr + f'{tier3count[1]}' + '/15)\n' + tempdh + '\n\nTier 4 (' 
                                    temph = ''; tempdh = ''        
                            elif tier4 < 15 and x in ['004','014','104','024','204','040','041','140','042','240','400','401','410','402','420']:                 
                                tier4 += 1
                                tier4count[1] += 1
                                tempdh = tempdh + x + '  '
                                if tier4count[1] == 9:
                                    tempdh = tempdh + '\n'                               
                                if tier4 == 15:
                                    havestr = havestr + f'{tier4count[0]}' + '/15)\n' + temph + '\n\nTier 5 ('
                                    donthavestr = donthavestr + f'{tier4count[1]}' + '/15)\n' + tempdh + '\n\nTier 5 (' 
                                    temph = ''; tempdh = ''   
                            elif tier5 < 15 and x in ['005','015','105','025','205','050','051','150','052','250','500','501','510','502','520']:
                                tier5 += 1
                                tier5count[1] += 1
                                tempdh = tempdh + x + '  '
                                if tier5count[1] == 9:
                                    tempdh = tempdh + '\n'
                                if tier5 == 15:
                                    havestr = havestr + f'{tier5count[0]}' + '/15)\n' + temph
                                    donthavestr = donthavestr + f'{tier5count[1]}' + '/15)\n' + tempdh
                                    temph = ''; tempdh = '' 

                    tier0 = 0;tier1 = 0;tier2 = 0;tier3 = 0;tier4 = 0;tier5 = 0
                    tier1count = [0,0];tier2count = [0,0];tier3count = [0,0];tier4count = [0,0];tier5count = [0,0]
                    view_window["-HAVE-"].update(havestr)
                    view_window["-NOHAVE-"].update(donthavestr)
                    havestr = ''
                    donthavestr = ''
        
        #Enter the Check window
        if event == "Check":
            main_window.close()
            check_window = create_check_window(saved_theme)
            while True:
                event, values = check_window.read()

                #Exits out of application
                if event == sg.WINDOW_CLOSED or event == 'Exit':
                    check_window.close()
                    break
                #Returns back to main page
                if event == "Back":
                    check_window.close()
                    main_window = create_main_window(saved_theme)
                    break
                    
                if event == "-PATH-" and values["-PATH-"]:
                    if values["-PATH-"][-1] not in ('012345'):
                        sg.popup_auto_close("Only digits between 0-5 are allowed")
                        check_window['-PATH-'].update(values['-PATH-'][:-1])
                    if len(values["-PATH-"]) > 3:
                        sg.popup_auto_close("Length cannot be greater than 3")
                        check_window['-PATH-'].update(values['-PATH-'][:-1])
                    '''
                    if int(values["-PATH-"][-1]) > 2:               #######Needs to be improved#####
                        count += 1
                        if count == 2:
                            sg.popup_auto_close("Can't have 2 crosspaths greater than 2")
                            check_window['-PATH-'].update(values['-PATH-'][:-1])
                            count -= 1
                    '''
                
                if event == "Clear" or event == "-HAVE-":
                    check_window["-PATH-"].update('')
                    count = 0     
                    correct = 0
                    check_window["-HAVE-"].update(visible = False)
                    check_window["-JUST_GOT-"].update(visible = False)
                    check_window["-BLANK-"].update(visible = False)
                    check_window["Save"].update(visible = False)
                    check_window["-OUTPUT-"].update('')
                    check_window["-FIND-"].BindReturnKey = True
                    check_window["-JUST_GOT-"].BindReturnKey = False
                    check_window["Reset"].update(visible = False)

                if event == "-FIND-":
                    if len(values["-PATH-"]) == 3:
                        m = [*values.values()]
                        for i in monkey_dic.keys():
                            if i == m[0]:
                                mon = m[0]
                                for j in monkey_dic[i].keys():
                                    if j == m[1]:
                                        p = m[1]
                                        correct = 1
                                        check_window["-OUTPUT-"].update(f'You entered {m[0]} {m[1]} : you {monkey_dic[i][j]} the crosspath!')
                                        check_window["-HAVE-"].update(visible = True)
                                        check_window["-JUST_GOT-"].update(visible = True)
                                        check_window["-BLANK-"].update(visible = True)
                                        check_window["Save"].update(visible = True)
                                        check_window["-FIND-"].BindReturnKey = False
                                        check_window["-JUST_GOT-"].BindReturnKey = True
                                        check_window["Reset"].update(visible = True)
                                if correct == 0:
                                    sg.popup_auto_close("No crosspath!")
                                    correct = 0
                    else:
                        sg.popup_auto_close("Length must be exactly 3")
                
                if event == "-JUST_GOT-":
                    if monkey_dic[mon][p] != "have":
                        monkey_dic[mon][p]= "have"
                        #check_window.FindElement("-PATH-").update("have")
                        check_window["-OUTPUT-"].update(f'You entered {m[0]} {m[1]} : you {monkey_dic[mon][p]} the crosspath!')
                        check_window["-FIND-"].BindReturnKey = True
                        check_window["-JUST_GOT-"].BindReturnKey = False
                    else:
                        sg.popup_auto_close("Already have!")

                if event == "Save":
                    with open('monkey.json', 'w') as f:
                        json.dump(dic_json, f)
                
                if event == "Reset":
                    if monkey_dic[mon][p] != "don't have":
                        monkey_dic[mon][p]= "don't have"
                        check_window["-OUTPUT-"].update(f'You entered {m[0]} {m[1]} : you {monkey_dic[mon][p]} the crosspath!')   
                    else:
                        sg.popup_auto_close("Already don't have!")
        # if event == "Load":
        if event == "Load":
            if jsonloaderCount == 0:
                try:
                    with open('monkey.json', 'r') as f:
                        load = json.load(f)
                
                    while loadCounter < 23:
                        for j in load[loadCounter]:
                            dic_json[loadCounter][j] = load[loadCounter][j]
                        loadCounter += 1
                    loadCounter = 0
                    sg.popup_auto_close("Loaded!")
                    jsonloaderCount += 1
                except:
                    sg.popup_auto_close("No file found!")
            else:
                sg.popup_auto_close("File Loaded Already!")

        #Access user settings for application
        if event == "Settings":
            main_window.close()
            settings_window = create_settings_window(saved_theme)
            while True:
                event, values =settings_window.read()

                #Exits out of application
                if event == sg.WINDOW_CLOSED:
                    settings_window.close()
                    break
                #Returns back to main page
                if event == "Back":
                    settings_window.close()
                    main_window = create_main_window(saved_theme)
                    break
                if values['-THEMES-']:
                    settings_window.close()
                    settings_window = create_settings_window(values['-THEMES-'])
                    try:
                        #sg.user_settings_set_entry('theme', values['-THEMES-'])
                        saved_theme = values['-THEMES-']
                    except:
                        pass  # already warned about settings at start
    main_window.close()

if __name__ == '__main__':
    main()


'''
NOTES

Settings -> -THEME-, copied from https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Buttons_Base64_User_Settings.py
Saving Data -> Load, https://www.geeksforgeeks.org/python-replace-dictionary-value-from-other-dictionary/
Binding Enter key for 2 buttons -> https://stackoverflow.com/questions/70070821/how-can-i-disable-the-return-bind-key-in-pysimplegui


'''
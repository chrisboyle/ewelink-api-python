from enum import Enum

class DeviceType(Enum):
    UNKNOWN = 0
    SOCKET = 1
    SOCKET_2 = 2
    SOCKET_3 = 3
    SOCKET_4 = 4
    SWITCH = 6
    SOCKET_POWER = 5
    SWITCH_2 = 7
    SWITCH_3 = 8
    SWITCH_4 = 9
    OSPF = 10
    CURTAIN = 11
    EW_RE = 12
    FIREPLACE = 13
    SWITCH_CHANGE = 14
    THERMOSTAT = 15
    COLD_WARM_LED = 16
    THREE_GEAR_FAN = 17
    SENSORS_CENTER = 18
    HUMIDIFIER = 19
    RGB_BALL_LIGHT = 22
    NEST_THERMOSTAT = 23
    GSM_SOCKET = 24
    AROMATHERAPY = 25
    BJ_THERMOSTAT = 26
    GSM_UNLIMIT_SOCKET = 27
    RF_BRIDGE = 28
    GSM_SOCKET_2 = 29
    GSM_SOCKET_3 = 30
    GSM_SOCKET_4 = 31
    POWER_DETECTION_SOCKET = 32
    LIGHT_BELT = 33
    FAN_LIGHT = 34
    EZVIZ_CAMERA = 35
    SINGLE_CHANNEL_DIMMER_SWITCH = 36
    HOME_KIT_BRIDGE = 38
    FUJIN_OPS = 40
    CUN_YOU_DOOR = 41
    SMART_BEDSIDE_AND_NEW_RGB_BALL_LIGHT = 42
    DOWN_CEILING_LIGHT = 45
    AIR_CLEANER = 46
    MACHINE_BED = 49
    COLD_WARM_DESK_LIGHT = 51
    DOUBLE_COLOR_DEMO_LIGHT = 52
    ELECTRIC_FAN_WITH_LAMP = 53
    SWEEPING_ROBOT = 55
    RGB_BALL_LIGHT_4 = 56
    MONOCHROMATIC_BALL_LIGHT = 57
    MEARICAMERA = 59
    BLADELESS_FAN = 1001
    NEW_HUMIDIFIER = 1002
    WARM_AIR_BLOWER = 1003

class PowerState(Enum):
    off = 0
    on = 1
    toggle = 2

class DeviceChannelLengh(Enum):
    SOCKET = 1
    SWITCH_CHANGE = 1
    GSM_UNLIMIT_SOCKET = 1
    SWITCH = 1
    THERMOSTAT = 1
    SOCKET_POWER = 1
    GSM_SOCKET = 1
    POWER_DETECTION_SOCKET = 1
    SOCKET_2 = 2
    GSM_SOCKET_2 = 2
    SWITCH_2 = 2
    SOCKET_3 = 3
    GSM_SOCKET_3 = 3
    SWITCH_3 = 3
    SOCKET_4 = 4
    GSM_SOCKET_4 = 4
    SWITCH_4 = 4
    CUN_YOU_DOOR = 4

class Region(Enum):
    US = 'us'
    AS = 'as'
    EU = 'eu'
    CN = 'cn'

class CountryCodes(Enum):
    UNKNOWN = "0"
    China = "+86"
    Afghanistan = "+93"
    Albania = "+355"
    Algeria = "+213"
    Andorra = "+376"
    Angola = "+244"
    Anguilla = "+1264"
    Ascension = "+247"
    Antigua_and_Barbuda = "+1268"
    Argentina = "+54"
    Armenia = "+374"
    Aruba = "+297"
    Australia = "+61"
    Austria = "+43"
    Azerbaijan = "+994"
    Bahamas = "+1242"
    Bahrain = "+973"
    Bangladesh = "+880"
    Barbados = "+1246"
    Belarus = "+375"
    Belgium = "+32"
    Belize = "+501"
    Benin = "+229"
    Bermuda = "+1441"
    Kingdom_of_Bhutan = "+975"
    Bolivia = "+591"
    Bosnia_and_Herzegovina = "+387"
    Botswana = "+267"
    Brazil = "+55"
    Brunei = "+673"
    Bulgaria = "+359"
    Burkina_Faso = "+226"
    Burundi = "+257"
    Cambodia = "+855"
    Cameroon = "+237"
    Canada = "+1"
    Cape_Verde_Republic = "+238"
    Cayman_Islands = "+1345"
    Central_African_Republic = "+236"
    Chad = "+235"
    Chile = "+56"
    Colombia = "+57"
    Islamic_Federal_Republic_of_Comoros = "+269"
    Republic_of_Congo = "+242"
    Democratic_Republic_of_Congo = "+243"
    Cook_Islands = "+682"
    Costa_Rica = "+506"
    Ivory_Coast = "+225"
    Croatia = "+385"
    Cuba = "+53"
    Cyprus = "+357"
    Czech = "+420"
    Denmark = "+45"
    Djibouti = "+253"
    Dominica = "+1767"
    Dominican_Republic = "+1809"
    Ecuador = "+593"
    Egypt = "+20"
    El_Salvador = "+503"
    Estonia = "+372"
    Ethiopia = "+251"
    Faroe_Islands = "+298"
    Fiji = "+679"
    Finland = "+358"
    France = "+33"
    French_Guiana = "+594"
    French_Polynesia = "+689"
    Gabon = "+241"
    Gambia = "+220"
    Georgia = "+995"
    Germany = "+49"
    Ghana = "+233"
    Gibraltar = "+350"
    Greece = "+30"
    Greenland = "+299"
    Grenada = "+1473"
    Guadeloupe = "+590"
    Guam = "+1671"
    Guatemala = "+502"
    Guinea = "+240"
    Guernsey = "+44"
    Guyana = "+592"
    Haiti = "+509"
    Honduras = "+504"
    Hong_Kong_China = "+852"
    Myanmar = "+95"
    Hungary = "+36"
    Iceland = "+354"
    India = "+91"
    Indonesia = "+62"
    Iran = "+98"
    Republic_of_Iraq = "+964"
    Ireland = "+353"
    Isle_of_Man = "+44"
    Israel = "+972"
    Italian = "+39"
    Jamaica = "+1876"
    Japan = "+81"
    Jersey = "+44"
    Jordan = "+962"
    Republic_of_Kazakhstan = "+7"
    Kenya = "+254"
    Kosovo = "+383"
    Kuwait = "+965"
    Kyrgyzstan = "+996"
    Laos = "+856"
    Latvia = "+371"
    Lebanon = "+961"
    Lesotho = "+266"
    Liberia = "+231"
    Libya = "+218"
    Liechtenstein = "+423"
    Lithuania = "+370"
    Luxembourg = "+352"
    Macau_China = "+853"
    Republic_of_Macedonia = "+389"
    Madagascar = "+261"
    Malawi = "+265"
    Malaysia = "+60"
    Maldives = "+960"
    Mali = "+223"
    Malta = "+356"
    Martinique = "+596"
    Mauritania = "+222"
    Mauritius = "+230"
    Mayotte = "+262"
    Mexico = "+52"
    Moldova = "+373"
    Monaco = "+377"
    Mongolia = "+976"
    Montenegro = "+382"
    Montserrat = "+1664"
    Morocco = "+212"
    Mozambique = "+258"
    Namibia = "+264"
    Nepal = "+977"
    Netherlands = "+31"
    Netherlands_Antilles = "+599"
    New_Caledonia = "+687"
    New_Zealand = "+64"
    Nicaragua = "+505"
    Niger = "+227"
    Nigeria = "+234"
    Norway = "+47"
    Oman = "+968"
    Pakistan = "+92"
    Palestine = "+970"
    Panama = "+507"
    Papua_New_Guinea = "+675"
    Paraguay = "+595"
    Peru = "+51"
    Philippines = "+63"
    Poland = "+48"
    Portugal = "+351"
    Puerto_Rico = "+1"
    Qatar = "+974"
    Reunion = "+262"
    Romania = "+40"
    Russia = "+7"
    Rwanda = "+250"
    Eastern_Samoa_US = "+684"
    Western_Samoa = "+685"
    San_Marino = "+378"
    Sao_Tome_and_Principe = "+239"
    Saudi_Arabia = "+966"
    Senegal = "+221"
    Serbia = "+381"
    Seychelles = "+248"
    Sierra_Leone = "+232"
    Singapore = "+65"
    Slovakia = "+421"
    Slovenia = "+386"
    South_Africa = "+27"
    South_Korea = "+82"
    Spain = "+34"
    Sri_Lanka = "+94"
    Saint_Kitts_and_Nevis = "+1869"
    Saint_Lucia = "+1758"
    Saint_Vincent = "+1784"
    Sultan = "+249"
    Suriname = "+597"
    Swaziland = "+268"
    Sweden = "+46"
    Switzerland = "+41"
    Syria = "+963"
    Taiwan_China = "+886"
    Tajikistan = "+992"
    Tanzania = "+255"
    Thailand = "+66"
    East_Timor = "+670"
    Togo = "+228"
    Tonga = "+676"
    Trinidad_and_Tobago = "+1868"
    Tunisia = "+216"
    Turkey = "+90"
    Turkmenistan = "+993"
    Turks_and_Caicos = "+1649"
    Uganda = "+256"
    Ukraine = "+380"
    United_Arab_Emirates = "+971"
    UK = "+44"
    United_States = "+1"
    Uruguay = "+598"
    Uzbekistan = "+998"
    Vanuatu = "+678"
    Venezuela = "+58"
    Vietnam = "+84"
    Wilk_Islands = "+1340"
    Yemen = "+967"
    Zambia = "+260"
    Zimbabwe = "+263"
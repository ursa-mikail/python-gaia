from datetime import datetime
import pytz
from pytz import timezone

from time import gmtime, strftime
import time

# status: incomplete
# version: 2017-09-15_0204hr_27sec

class local_time():
    dtformat ="%Y-%m-%d %H:%M:%S %Z%z"

    def __init__(self, tz, here = False):
        self.tz = tz                    #time zone
        self.tzs = '{:<20}'.format(tz)  #justified string
        now = datetime.utcnow()
        print("now:", now)
        print("now > ", now.astimezone(timezone(tz)))
        self.t = now.astimezone(timezone(tz))   #timestamp
        # self.t = now.localize(datehere)
        self.string = self.t.strftime(local_time.dtformat) #timestring
        self.here = here

    def as_string(self):
        string = "%s:\t%s" % (self.tzs,self.string)
        if self.here:
            string += "\t <- you are HERE"
        return string

class timezone_lib():
    def list_timezones(self, all_zones):
        tzs = []

        for i,tz in all_zones:
            if i == 'p' or i == 'h': #p for print, h for here
                tzs.append(local_time(tz, here=(i=='h')))

        #sort by time
        tzs = sorted(tzs, key=lambda x: x.string, reverse=True)

        for t in tzs:
            print(t.as_string())

        return None


    all_zones =  [
(' ','America/Adak'),                               (' ','Africa/Abidjan'),                             (' ','Atlantic/Azores'),                            (' ','GB'),
(' ','America/Anchorage'),                          (' ','Africa/Accra'),                               (' ','Atlantic/Bermuda'),                           (' ','GB-Eire'),
(' ','America/Anguilla'),                           (' ','Africa/Addis_Ababa'),                         (' ','Atlantic/Canary'),                            (' ','GMT'),
(' ','America/Antigua'),                            (' ','Africa/Algiers'),                             (' ','Atlantic/Cape_Verde'),                        (' ','GMT+0'),
(' ','America/Araguaina'),                          (' ','Africa/Asmara'),                              (' ','Atlantic/Faeroe'),                            (' ','GMT-0'),
(' ','America/Argentina/Buenos_Aires'),             (' ','Africa/Asmera'),                              (' ','Atlantic/Faroe'),                             (' ','GMT0'),
(' ','America/Argentina/Catamarca'),                (' ','Africa/Bamako'),                              (' ','Atlantic/Jan_Mayen'),                         (' ','Greenwich'),
(' ','America/Argentina/ComodRivadavia'),           (' ','Africa/Bangui'),                              (' ','Atlantic/Madeira'),                           (' ','HST'),
(' ','America/Argentina/Cordoba'),                  (' ','Africa/Banjul'),                              (' ','Atlantic/Reykjavik'),                         (' ','Hongkong'),
(' ','America/Argentina/Jujuy'),                    (' ','Africa/Bissau'),                              (' ','Atlantic/South_Georgia'),                     (' ','Iceland'),
(' ','America/Argentina/La_Rioja'),                 (' ','Africa/Blantyre'),                            (' ','Atlantic/St_Helena'),
(' ','America/Argentina/Mendoza'),                  (' ','Africa/Brazzaville'),                         (' ','Atlantic/Stanley'),                           (' ','Indian/Antananarivo'),
(' ','America/Argentina/Rio_Gallegos'),             (' ','Africa/Bujumbura'),                                                                               (' ','Indian/Chagos'),
(' ','America/Argentina/Salta'),                    (' ','Africa/Cairo'),                               (' ','Australia/ACT'),                              (' ','Indian/Christmas'),
(' ','America/Argentina/San_Juan'),                 (' ','Africa/Casablanca'),                          (' ','Australia/Adelaide'),                         (' ','Indian/Cocos'),
(' ','America/Argentina/San_Luis'),                 (' ','Africa/Ceuta'),                               (' ','Australia/Brisbane'),                         (' ','Indian/Comoro'),
(' ','America/Argentina/Tucuman'),                  (' ','Africa/Conakry'),                             (' ','Australia/Broken_Hill'),                      (' ','Indian/Kerguelen'),
(' ','America/Argentina/Ushuaia'),                  (' ','Africa/Dakar'),                               (' ','Australia/Canberra'),                         (' ','Indian/Mahe'),
(' ','America/Aruba'),                              (' ','Africa/Dar_es_Salaam'),                       (' ','Australia/Currie'),                           (' ','Indian/Maldives'),
(' ','America/Asuncion'),                           (' ','Africa/Djibouti'),                            (' ','Australia/Darwin'),                           (' ','Indian/Mauritius'),
(' ','America/Atikokan'),                           (' ','Africa/Douala'),                              (' ','Australia/Eucla'),                            (' ','Indian/Mayotte'),
(' ','America/Atka'),                               (' ','Africa/El_Aaiun'),                            (' ','Australia/Hobart'),                           (' ','Indian/Reunion'),
(' ','America/Bahia'),                              (' ','Africa/Freetown'),                            (' ','Australia/LHI'),
(' ','America/Bahia_Banderas'),                     (' ','Africa/Gaborone'),                            (' ','Australia/Lindeman'),                         (' ','Iran'),
(' ','America/Barbados'),                           (' ','Africa/Harare'),                              (' ','Australia/Lord_Howe'),                        (' ','Israel'),
(' ','America/Belem'),                              (' ','Africa/Johannesburg'),                        (' ','Australia/Melbourne'),                        (' ','Jamaica'),
(' ','America/Belize'),                             (' ','Africa/Juba'),                                (' ','Australia/NSW'),                              (' ','Japan'),
(' ','America/Blanc-Sablon'),                       (' ','Africa/Kampala'),                             (' ','Australia/North'),                            (' ','Kwajalein'),
(' ','America/Boa_Vista'),                          (' ','Africa/Khartoum'),                            (' ','Australia/Perth'),                            (' ','Libya'),
(' ','America/Bogota'),                             (' ','Africa/Kigali'),                              (' ','Australia/Queensland'),                       (' ','MET'),
(' ','America/Boise'),                              (' ','Africa/Kinshasa'),                            (' ','Australia/South'),                            (' ','MST'),
(' ','America/Buenos_Aires'),                       (' ','Africa/Lagos'),                               ('p','Australia/Sydney'),                           (' ','MST7MDT'),
(' ','America/Cambridge_Bay'),                      (' ','Africa/Libreville'),                          (' ','Australia/Tasmania'),
(' ','America/Campo_Grande'),                       (' ','Africa/Lome'),                                (' ','Australia/Victoria'),                         (' ','Mexico/BajaNorte'),
(' ','America/Cancun'),                             (' ','Africa/Luanda'),                              (' ','Australia/West'),                             (' ','Mexico/BajaSur'),
(' ','America/Caracas'),                            (' ','Africa/Lubumbashi'),                          (' ','Australia/Yancowinna'),                       (' ','Mexico/General'),
(' ','America/Catamarca'),                          (' ','Africa/Lusaka'),                                                                                  (' ','NZ'),
(' ','America/Cayenne'),                            (' ','Africa/Malabo'),                              (' ','Brazil/Acre'),                                (' ','NZ-CHAT'),
(' ','America/Cayman'),                             (' ','Africa/Maputo'),                              (' ','Brazil/DeNoronha'),                           (' ','Navajo'),
(' ','America/Chicago'),                            (' ','Africa/Maseru'),                              (' ','Brazil/East'),                                (' ','PRC'),
(' ','America/Chihuahua'),                          (' ','Africa/Mbabane'),                             (' ','Brazil/West'),                                (' ','PST8PDT'),
(' ','America/Coral_Harbour'),                      (' ','Africa/Mogadishu'),
(' ','America/Cordoba'),                            (' ','Africa/Monrovia'),                            ('h','CET'),                                        (' ','Pacific/Apia'),
(' ','America/Costa_Rica'),                         (' ','Africa/Nairobi'),                             (' ','CST6CDT'),                                    (' ','Pacific/Auckland'),
(' ','America/Creston'),                            (' ','Africa/Ndjamena'),                                                                                (' ','Pacific/Chatham'),
(' ','America/Cuiaba'),                             (' ','Africa/Niamey'),                              (' ','Canada/Atlantic'),                            (' ','Pacific/Chuuk'),
(' ','America/Curacao'),                            (' ','Africa/Nouakchott'),                          (' ','Canada/Central'),                             (' ','Pacific/Easter'),
(' ','America/Danmarkshavn'),                       (' ','Africa/Ouagadougou'),                         (' ','Canada/East-Saskatchewan'),                   (' ','Pacific/Efate'),
(' ','America/Dawson'),                             (' ','Africa/Porto-Novo'),                          (' ','Canada/Eastern'),                             (' ','Pacific/Enderbury'),
(' ','America/Dawson_Creek'),                       (' ','Africa/Sao_Tome'),                            (' ','Canada/Mountain'),                            (' ','Pacific/Fakaofo'),
(' ','America/Denver'),                             (' ','Africa/Timbuktu'),                            (' ','Canada/Newfoundland'),                        (' ','Pacific/Fiji'),
(' ','America/Detroit'),                            (' ','Africa/Tripoli'),                             (' ','Canada/Pacific'),                             (' ','Pacific/Funafuti'),
(' ','America/Dominica'),                           (' ','Africa/Tunis'),                               (' ','Canada/Saskatchewan'),                        (' ','Pacific/Galapagos'),
(' ','America/Edmonton'),                           (' ','Africa/Windhoek'),                            (' ','Canada/Yukon'),                               (' ','Pacific/Gambier'),
(' ','America/Eirunepe'),                                                                               (' ','Chile/Continental'),                          (' ','Pacific/Guadalcanal'),
(' ','America/El_Salvador'),                        (' ','Antarctica/Casey'),                           (' ','Chile/EasterIsland'),                         (' ','Pacific/Guam'),
(' ','America/Ensenada'),                           (' ','Antarctica/Davis'),                           (' ','Cuba'),                                       (' ','Pacific/Honolulu'),
(' ','America/Fort_Wayne'),                         (' ','Antarctica/DumontDUrville'),                                                                      (' ','Pacific/Johnston'),
(' ','America/Fortaleza'),                          (' ','Antarctica/Macquarie'),                       ('p','EET'),                                        (' ','Pacific/Kiritimati'),
(' ','America/Glace_Bay'),                          (' ','Antarctica/Mawson'),                          (' ','EST'),                                        (' ','Pacific/Kosrae'),
(' ','America/Godthab'),                            (' ','Antarctica/McMurdo'),                         (' ','EST5EDT'),                                    (' ','Pacific/Kwajalein'),
(' ','America/Goose_Bay'),                          (' ','Antarctica/Palmer'),                          (' ','Egypt'),                                      (' ','Pacific/Majuro'),
(' ','America/Grand_Turk'),                         (' ','Antarctica/Rothera'),                         (' ','Eire'),                                       (' ','Pacific/Marquesas'),
(' ','America/Grenada'),                            (' ','Antarctica/South_Pole'),                      (' ','Etc/GMT'),                                    (' ','Pacific/Midway'),
(' ','America/Guadeloupe'),                         (' ','Antarctica/Syowa'),                           (' ','Etc/GMT+0'),                                  (' ','Pacific/Nauru'),
(' ','America/Guatemala'),                          (' ','Antarctica/Vostok'),                          (' ','Etc/GMT+1'),                                  (' ','Pacific/Niue'),
(' ','America/Guayaquil'),                                                                              (' ','Etc/GMT+10'),                                 (' ','Pacific/Norfolk'),
(' ','America/Guyana'),                             (' ','Arctic/Longyearbyen'),                        (' ','Etc/GMT+11'),                                 (' ','Pacific/Noumea'),
(' ','America/Halifax'),                                                                                (' ','Etc/GMT+12'),                                 (' ','Pacific/Pago_Pago'),
(' ','America/Havana'),                             (' ','Asia/Aden'),                                  (' ','Etc/GMT+2'),                                  (' ','Pacific/Palau'),
(' ','America/Hermosillo'),                         (' ','Asia/Almaty'),                                (' ','Etc/GMT+3'),                                  (' ','Pacific/Pitcairn'),
(' ','America/Indiana/Indianapolis'),               (' ','Asia/Amman'),                                 (' ','Etc/GMT+4'),                                  (' ','Pacific/Pohnpei'),
(' ','America/Indiana/Knox'),                       (' ','Asia/Anadyr'),                                (' ','Etc/GMT+5'),                                  (' ','Pacific/Ponape'),
(' ','America/Indiana/Marengo'),                    (' ','Asia/Aqtau'),                                 (' ','Etc/GMT+6'),                                  (' ','Pacific/Port_Moresby'),
(' ','America/Indiana/Petersburg'),                 (' ','Asia/Aqtobe'),                                (' ','Etc/GMT+7'),                                  (' ','Pacific/Rarotonga'),
(' ','America/Indiana/Tell_City'),                  (' ','Asia/Ashgabat'),                              (' ','Etc/GMT+8'),                                  (' ','Pacific/Saipan'),
(' ','America/Indiana/Vevay'),                      (' ','Asia/Ashkhabad'),                             (' ','Etc/GMT+9'),                                  (' ','Pacific/Samoa'),
(' ','America/Indiana/Vincennes'),                  (' ','Asia/Baghdad'),                               (' ','Etc/GMT-0'),                                  (' ','Pacific/Tahiti'),
(' ','America/Indiana/Winamac'),                    (' ','Asia/Bahrain'),                               (' ','Etc/GMT-1'),                                  (' ','Pacific/Tarawa'),
(' ','America/Indianapolis'),                       (' ','Asia/Baku'),                                  (' ','Etc/GMT-10'),                                 (' ','Pacific/Tongatapu'),
(' ','America/Inuvik'),                             (' ','Asia/Bangkok'),                               (' ','Etc/GMT-11'),                                 (' ','Pacific/Truk'),
(' ','America/Iqaluit'),                            (' ','Asia/Beirut'),                                (' ','Etc/GMT-12'),                                 (' ','Pacific/Wake'),
(' ','America/Jamaica'),                            (' ','Asia/Bishkek'),                               (' ','Etc/GMT-13'),                                 (' ','Pacific/Wallis'),
(' ','America/Jujuy'),                              (' ','Asia/Brunei'),                                (' ','Etc/GMT-14'),                                 (' ','Pacific/Yap'),
(' ','America/Juneau'),                             (' ','Asia/Calcutta'),                              (' ','Etc/GMT-2'),
(' ','America/Kentucky/Louisville'),                (' ','Asia/Choibalsan'),                            (' ','Etc/GMT-3'),                                  (' ','Poland'),
(' ','America/Kentucky/Monticello'),                (' ','Asia/Chongqing'),                             (' ','Etc/GMT-4'),                                  (' ','Portugal'),
(' ','America/Knox_IN'),                            (' ','Asia/Chungking'),                             (' ','Etc/GMT-5'),                                  (' ','ROC'),
(' ','America/Kralendijk'),                         (' ','Asia/Colombo'),                               (' ','Etc/GMT-6'),                                  (' ','ROK'),
(' ','America/La_Paz'),                             (' ','Asia/Dacca'),                                 (' ','Etc/GMT-7'),                                  (' ','Singapore'),
(' ','America/Lima'),                               (' ','Asia/Damascus'),                              (' ','Etc/GMT-8'),                                  (' ','Turkey'),
('p','America/Los_Angeles'),                        (' ','Asia/Dhaka'),                                 (' ','Etc/GMT-9'),
(' ','America/Louisville'),                         (' ','Asia/Dili'),                                  (' ','Etc/GMT0'),                                   (' ','UCT'),
(' ','America/Lower_Princes'),                      (' ','Asia/Dubai'),                                 (' ','Etc/Greenwich'),
(' ','America/Maceio'),                             (' ','Asia/Dushanbe'),                              (' ','Etc/UCT'),                                    (' ','US/Alaska'),
(' ','America/Managua'),                            (' ','Asia/Gaza'),                                  (' ','Etc/UTC'),                                    (' ','US/Aleutian'),
(' ','America/Manaus'),                             (' ','Asia/Harbin'),                                (' ','Etc/Universal'),                              (' ','US/Arizona'),
(' ','America/Marigot'),                            (' ','Asia/Hebron'),                                (' ','Etc/Zulu'),                                   (' ','US/Central'),
(' ','America/Martinique'),                         (' ','Asia/Ho_Chi_Minh'),                                                                               (' ','US/East-Indiana'),
(' ','America/Matamoros'),                          ('p','Asia/Hong_Kong'),                             (' ','Europe/Amsterdam'),                           (' ','US/Eastern'),
(' ','America/Mazatlan'),                           (' ','Asia/Hovd'),                                  (' ','Europe/Andorra'),                             (' ','US/Hawaii'),
(' ','America/Mendoza'),                            (' ','Asia/Irkutsk'),                               (' ','Europe/Athens'),                              (' ','US/Indiana-Starke'),
(' ','America/Menominee'),                          (' ','Asia/Istanbul'),                              (' ','Europe/Belfast'),                             (' ','US/Michigan'),
(' ','America/Merida'),                             (' ','Asia/Jakarta'),                               (' ','Europe/Belgrade'),                            (' ','US/Mountain'),
(' ','America/Metlakatla'),                         (' ','Asia/Jayapura'),                              (' ','Europe/Berlin'),                              (' ','US/Pacific'),
(' ','America/Mexico_City'),                        (' ','Asia/Jerusalem'),                             (' ','Europe/Bratislava'),                          (' ','US/Pacific-New'),
(' ','America/Miquelon'),                           (' ','Asia/Kabul'),                                 (' ','Europe/Brussels'),                            (' ','US/Samoa'),
(' ','America/Moncton'),                            (' ','Asia/Kamchatka'),                             (' ','Europe/Bucharest'),
(' ','America/Monterrey'),                          (' ','Asia/Karachi'),                               (' ','Europe/Budapest'),                            ('p','UTC'),
(' ','America/Montevideo'),                         (' ','Asia/Kashgar'),                               (' ','Europe/Chisinau'),                            (' ','Universal'),
(' ','America/Montreal'),                           (' ','Asia/Kathmandu'),                             (' ','Europe/Copenhagen'),                          (' ','W-SU'),
(' ','America/Montserrat'),                         (' ','Asia/Katmandu'),                              (' ','Europe/Dublin'),                              (' ','WET'),
(' ','America/Nassau'),                             (' ','Asia/Kolkata'),                               (' ','Europe/Gibraltar'),                           (' ','Zulu'),
('p','America/New_York'),                           (' ','Asia/Krasnoyarsk'),                           (' ','Europe/Guernsey'),
(' ','America/Nipigon'),                            (' ','Asia/Kuala_Lumpur'),                          (' ','Europe/Helsinki'),
(' ','America/Nome'),                               (' ','Asia/Kuching'),                               (' ','Europe/Isle_of_Man'),
(' ','America/Noronha'),                            (' ','Asia/Kuwait'),                                (' ','Europe/Istanbul'),
(' ','America/North_Dakota/Beulah'),                (' ','Asia/Macao'),                                 (' ','Europe/Jersey'),
(' ','America/North_Dakota/Center'),                (' ','Asia/Macau'),                                 (' ','Europe/Kaliningrad'),
(' ','America/North_Dakota/New_Salem'),             (' ','Asia/Magadan'),                               (' ','Europe/Kiev'),
(' ','America/Ojinaga'),                            (' ','Asia/Makassar'),                              (' ','Europe/Lisbon'),
(' ','America/Panama'),                             (' ','Asia/Manila'),                                (' ','Europe/Ljubljana'),
(' ','America/Pangnirtung'),                        (' ','Asia/Muscat'),                                ('p','Europe/London'),
(' ','America/Paramaribo'),                         (' ','Asia/Nicosia'),                               (' ','Europe/Luxembourg'),
(' ','America/Phoenix'),                            (' ','Asia/Novokuznetsk'),                          (' ','Europe/Madrid'),
(' ','America/Port-au-Prince'),                     (' ','Asia/Novosibirsk'),                           (' ','Europe/Malta'),
(' ','America/Port_of_Spain'),                      (' ','Asia/Omsk'),                                  (' ','Europe/Mariehamn'),
(' ','America/Porto_Acre'),                         (' ','Asia/Oral'),                                  (' ','Europe/Minsk'),
(' ','America/Porto_Velho'),                        (' ','Asia/Phnom_Penh'),                            (' ','Europe/Monaco'),
(' ','America/Puerto_Rico'),                        (' ','Asia/Pontianak'),                             (' ','Europe/Moscow'),
(' ','America/Rainy_River'),                        (' ','Asia/Pyongyang'),                             (' ','Europe/Nicosia'),
(' ','America/Rankin_Inlet'),                       (' ','Asia/Qatar'),                                 (' ','Europe/Oslo'),
(' ','America/Recife'),                             (' ','Asia/Qyzylorda'),                             (' ','Europe/Paris'),
(' ','America/Regina'),                             (' ','Asia/Rangoon'),                               (' ','Europe/Podgorica'),
(' ','America/Resolute'),                           (' ','Asia/Riyadh'),                                (' ','Europe/Prague'),
(' ','America/Rio_Branco'),                         (' ','Asia/Saigon'),                                (' ','Europe/Riga'),
(' ','America/Rosario'),                            (' ','Asia/Sakhalin'),                              (' ','Europe/Rome'),
(' ','America/Santa_Isabel'),                       (' ','Asia/Samarkand'),                             (' ','Europe/Samara'),
(' ','America/Santarem'),                           (' ','Asia/Seoul'),                                 (' ','Europe/San_Marino'),
(' ','America/Santiago'),                           (' ','Asia/Shanghai'),                              (' ','Europe/Sarajevo'),
(' ','America/Santo_Domingo'),                      ('p','Asia/Singapore'),                             (' ','Europe/Simferopol'),
(' ','America/Sao_Paulo'),                          (' ','Asia/Taipei'),                                (' ','Europe/Skopje'),
(' ','America/Scoresbysund'),                       (' ','Asia/Tashkent'),                              (' ','Europe/Sofia'),
(' ','America/Shiprock'),                           (' ','Asia/Tbilisi'),                               (' ','Europe/Stockholm'),
(' ','America/Sitka'),                              (' ','Asia/Tehran'),                                (' ','Europe/Tallinn'),
(' ','America/St_Barthelemy'),                      (' ','Asia/Tel_Aviv'),                              (' ','Europe/Tirane'),
(' ','America/St_Johns'),                           (' ','Asia/Thimbu'),                                (' ','Europe/Tiraspol'),
(' ','America/St_Kitts'),                           (' ','Asia/Thimphu'),                               (' ','Europe/Uzhgorod'),
(' ','America/St_Lucia'),                           (' ','Asia/Tokyo'),                                 (' ','Europe/Vaduz'),
(' ','America/St_Thomas'),                          (' ','Asia/Ujung_Pandang'),                         (' ','Europe/Vatican'),
(' ','America/St_Vincent'),                         (' ','Asia/Ulaanbaatar'),                           (' ','Europe/Vienna'),
(' ','America/Swift_Current'),                      (' ','Asia/Ulan_Bator'),                            (' ','Europe/Vilnius'),
(' ','America/Tegucigalpa'),                        (' ','Asia/Urumqi'),                                (' ','Europe/Volgograd'),
(' ','America/Thule'),                              (' ','Asia/Vientiane'),                             (' ','Europe/Warsaw'),
(' ','America/Thunder_Bay'),                        (' ','Asia/Vladivostok'),                           (' ','Europe/Zagreb'),
(' ','America/Tijuana'),                            (' ','Asia/Yakutsk'),                               (' ','Europe/Zaporozhye'),
(' ','America/Toronto'),                            (' ','Asia/Yekaterinburg'),                         (' ','Europe/Zurich'),
(' ','America/Tortola'),                            (' ','Asia/Yerevan'),
(' ','America/Vancouver'),
(' ','America/Virgin'),
(' ','America/Whitehorse'),
(' ','America/Winnipeg'),
(' ','America/Yakutat'),
(' ','America/Yellowknife'),

]



if __name__ == "__main__":
    timezone_object = timezone_lib()
    # print(timezone_object.all_zones)

    timezone_object.list_timezones(timezone_object.all_zones)
    print ("My Time Zone")
    print (strftime("%z", gmtime()))
    print (time.tzname)

    #now = datetime.utcnow().replace(tzinfo=pytz.pst)  # set to UTC time
    now = datetime.utcnow().replace(tzinfo=pytz.utc) # set to UTC time
    now = datetime.utcnow()
    print(now)


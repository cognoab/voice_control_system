from enum import StrEnum


# fmt: off
class Language_ISO639_1(StrEnum):
    """2-word language code follows the ISO 639-1 standard."""

    AFAR              = "aa"
    ABKHAZIAN         = "ab"
    AFRIKAANS         = "af"
    AKAN              = "ak"
    ALBANIAN          = "sq"
    AMHARIC           = "am"
    ARABIC            = "ar"
    ARAGONESE         = "an"
    ARMENIAN          = "hy"
    ASSAMESE          = "as"
    AVARIC            = "av"
    AVESTAN           = "ae"
    AYMARA            = "ay"
    AZERBAIJANI       = "az"
    BASHKIR           = "ba"
    BAMBARA           = "bm"
    BASQUE            = "eu"
    BELARUSIAN        = "be"
    BENGALI           = "bn"
    BISLAMA           = "bi"
    BOSNIAN           = "bs"
    BRETON            = "br"
    BULGARIAN         = "bg"
    BURMESE           = "my"
    CATALAN           = "ca"
    CHAMORRO          = "ch"
    CHECHEN           = "ce"
    CHICHEWA          = "ny"
    CHINESE           = "zh"
    CHURCH_SLAVIC     = "cu"
    CHUVASH           = "cv"
    CORNISH           = "kw"
    CORSICAN          = "co"
    CREE              = "cr"
    CROATIAN          = "hr"
    CZECH             = "cs"
    DAKOTA            = "da"
    DANISH            = "da"
    DIVEHI            = "dv"
    DUTCH             = "nl"
    DZONGKHA          = "dz"
    ENGLISH           = "en"
    ESPERANTO         = "eo"
    ESTONIAN          = "et"
    EWE               = "ee"
    FAROESE           = "fo"
    FIJIAN            = "fj"
    FINNISH           = "fi"
    FRENCH            = "fr"
    FULAH             = "ff"
    GAELIC            = "gd"
    GALICIAN          = "gl"
    GANDA             = "lg"
    GEORGIAN          = "ka"
    GERMAN            = "de"
    GREEK             = "el"
    GREENLANDIC       = "kl"
    GUARANI           = "gn"
    GUJARATI          = "gu"
    HAITIAN           = "ht"
    HAUSA             = "ha"
    HEBREW            = "he"
    HERERO            = "hz"
    HINDI             = "hi"
    HIRI_MOTU         = "ho"
    HUNGARIAN         = "hu"
    ICELANDIC         = "is"
    IDO               = "io"
    IGBO              = "ig"
    INDONESIAN        = "id"
    INTERLINGUA       = "ia"
    INTERLINGUE       = "ie"
    INUKTITUT         = "iu"
    INUPIAQ           = "ik"
    IRISH             = "ga"
    ITALIAN           = "it"
    JAPANESE          = "ja"
    JAVANESE          = "jv"
    KANNADA           = "kn"
    KANURI            = "kr"
    KASHMIRI          = "ks"
    KAZAKH            = "kk"
    KHMER             = "km"
    KIKUYU            = "ki"
    KINYARWANDA       = "rw"
    KIRGHIZ           = "ky"
    KOMI              = "kv"
    KONGO             = "kg"
    KOREAN            = "ko"
    KUANYAMA          = "kj"
    KURDISH           = "ku"
    LAO               = "lo"
    LATIN             = "la"
    LATVIAN           = "lv"
    LIMBURGISH        = "li"
    LINGALA           = "ln"
    LITHUANIAN        = "lt"
    LUXEMBOURGISH     = "lb"
    MACEDONIAN        = "mk"
    MALAGASY          = "mg"
    MALAY             = "ms"
    MALAYALAM         = "ml"
    MALTESE           = "mt"
    MANX              = "gv"
    MAORI             = "mi"
    MARATHI           = "mr"
    MARSHALLESE       = "mh"
    MONGOLIAN         = "mn"
    NAURU             = "na"
    NAVAJO            = "nv"
    NORTHERN_NDEBELE  = "nd"
    NORWEGIAN_BOKMAL  = "nb"
    NORWEGIAN_NYNORSK = "nn"
    NYANKOLE          = "ny"
    OCCITAN           = "oc"
    OJIBWA            = "oj"
    ORIYA             = "or"
    OROMO             = "om"
    OSSETIAN          = "os"
    PALAUAN           = "pau"
    PASHTO            = "ps"
    PERSIAN           = "fa"
    POLISH            = "pl"
    PORTUGUESE        = "pt"
    PUSHTO            = "ps"
    QUECHUA           = "qu"
    ROMANIAN          = "ro"
    ROMANSH           = "rm"
    RUNDI             = "rn"
    RUSSIAN           = "ru"
    SAMOAN            = "sm"
    SANGO             = "sg"
    SANSKRIT          = "sa"
    SERBIAN           = "sr"
    SHONA             = "sn"
    SINDHI            = "sd"
    SINHALA           = "si"
    SLOVAK            = "sk"
    SLOVENIAN         = "sl"
    SOMALI            = "so"
    SPANISH           = "es"
    SWAHILI           = "sw"
    SWATI             = "ss"
    SWEDISH           = "sv"
    TAGALOG           = "tl"
    TAHITIAN          = "ty"
    TAJIK             = "tg"
    TAMIL             = "ta"
    TATAR             = "tt"
    TELUGU            = "te"
    THAI              = "th"
    TIBETAN           = "bo"
    TIGRINYA          = "ti"
    TONGA             = "to"
    TSONGA            = "ts"
    TSWANA            = "tn"
    TURKISH           = "tr"
    TURKMEN           = "tk"
    TWI               = "tw"
    UIGHUR            = "ug"
    UKRAINIAN         = "uk"
    URDU              = "ur"
    UZBEK             = "uz"
    VENDA             = "ve"
    VIETNAMESE        = "vi"
    VOLAPUK           = "vo"
    WALLOON           = "wa"
    WELSH             = "cy"
    WESTERN_FRISIAN   = "fy"
    WOLOF             = "wo"
    XHOSA             = "xh"
    YIDDISH           = "yi"
    YORUBA            = "yo"
    ZHUANG            = "za"
    ZULU              = "zu"


class Language_ISO639_2(StrEnum):
    """3-word language code follows the ISO 639-2 standard."""

    AFAR                              = "aar"
    ABKHAZIAN                         = "abk"
    ACHINESE                          = "ace"
    ACOLI                             = "ach"
    ADANGME                           = "ada"
    ADYGHE                            = "ady"
    AFRIKAANS                         = "afr"
    AFRO_ASIATIC_LANGUAGES            = "afa"
    AFRIHILI                          = "afh"
    AINU                              = "ain"
    AKAN                              = "aka"
    AKKADIAN                          = "akk"
    ALBANIAN                          = "sqi"
    ALEUT                             = "ale"
    ALGONQUIAN_LANGUAGES              = "alg"
    SOUTHERN_ALTAI                    = "alt"
    AMHARIC                           = "amh"
    OLD_ENGLISH                       = "ang"
    ANGIKA                            = "anp"
    APACHE_LANGUAGES                  = "apa"
    ARABIC                            = "ara"
    ARAMAIC                           = "arc"
    ARAGONESE                         = "arg"
    ARMENIAN                          = "hye"
    MAPUDUNGUN                        = "arn"
    ARAPAHO                           = "arp"
    ARTIFICIAL_LANGUAGES              = "art"
    ARAWAK                            = "arw"
    ASSAMESE                          = "asm"
    ASTURIAN                          = "ast"
    ATHAPASCAN_LANGUAGES              = "ath"
    AUSTRALIAN_LANGUAGES              = "aus"
    AVARIC                            = "ava"
    AVESTAN                           = "ave"
    AWADHI                            = "awa"
    AYMARA                            = "aym"
    AZERBAIJANI                       = "aze"
    BANDA_LANGUAGES                   = "bad"
    BAMILEKE_LANGUAGES                = "bai"
    BASHKIR                           = "bak"
    BALUCHI                           = "bal"
    BAMBARA                           = "bam"
    BALINESE                          = "ban"
    BASQUE                            = "eus"
    BASA                              = "bas"
    BALTIC_LANGUAGES                  = "bat"
    BEJA                              = "bej"
    BELARUSIAN                        = "bel"
    BEMBA                             = "bem"
    BENGALI                           = "ben"
    BERBER_LANGUAGES                  = "ber"
    BHOJPURI                          = "bho"
    BIHARI_LANGUAGES                  = "bih"
    BIKOL                             = "bik"
    BINI                              = "bin"
    BISLAMA                           = "bis"
    SIKSIKA                           = "bla"
    BANTU_LANGUAGES                   = "bnt"
    TIBETAN                           = "bod"
    BOSNIAN                           = "bos"
    BRAJ                              = "bra"
    BRETON                            = "bre"
    BATAK_LANGUAGES                   = "btk"
    BURIAT                            = "bua"
    BUGINESE                          = "bug"
    BULGARIAN                         = "bul"
    BURMESE                           = "mya"
    BLIN                              = "byn"
    CADDO                             = "cad"
    CENTRAL_AMERICAN_INDIAN_LANGUAGES = "cai"
    GALIBI_CARIB                      = "car"
    CATALAN                           = "cat"
    CAUCASIAN_LANGUAGES               = "cau"
    CEBUANO                           = "ceb"
    CELTIC_LANGUAGES                  = "cel"
    CZECH                             = "ces"
    CHAMORRO                          = "cha"
    CHIBCHA                           = "chb"
    CHECHEN                           = "che"
    CHAGATAI                          = "chg"
    CHINESE                           = "zho"
    CHUUKES                           = "chk"
    MARI                              = "chm"
    CHINOOK_JARGON                    = "chn"
    CHOCTAW                           = "cho"
    CHIPEWYAN                         = "chp"
    CHEROKEE                          = "chr"
    CHURCH_SLAVIC                     = "chu"
    CHUVASH                           = "chv"
    CHEYENNE                          = "chy"
    CHAMIC_LANGUAGES                  = "cmc"
    MONTENEGRIN                       = "cnr"
    COPTIC                            = "cop"
    CORNISH                           = "cor"
    CORSICAN                          = "cos"
    CREOLES_ENGLISH_BASED             = "cpe"
    CREOLES_FRENCH_BASED              = "cpf"
    CREOLES_PORTUGUESE_BASED          = "cpp"
    CREE                              = "cre"
    CRIMEAN_TATAR                     = "crh"
    CREOLES_AND_PIDGINS               = "crp"
    KASHUBIAN                         = "csb"
    CUSHITIC_LANGUAGES                = "cus"
    WELSH                             = "cym"
    DAKOTA                            = "dak"
    DANISH                            = "dan"
    DARGWA                            = "dar"
    LAND_DAYAK_LANGUAGES              = "day"
    DELAWARE                          = "del"
    SLAVE                             = "den"
    GERMAN                            = "deu"
    DOGRIB                            = "dgr"
    DINKA                             = "din"
    DIVEHI                            = "div"
    DOGRI                             = "doi"
    DRAVIDIAN_LANGUAGES               = "dra"
    LOWER_SORBIAN                     = "dsb"
    DUALA                             = "dua"
    MIDDLE_DUTCH                      = "dum"
    DUTCH                             = "nld"
    DYULA                             = "dyu"
    DZONGKHA                          = "dzo"
    EFIK                              = "efi"
    EGYPTIAN                          = "egy"
    EKAJUK                            = "eka"
    MODERN_GREEK                      = "ell"
    ELAMITE                           = "elx"
    ENGLISH                           = "eng"
    MIDDLE_ENGLISH                    = "enm"
    ESPERANTO                         = "epo"
    ESTONIAN                          = "est"
    EWE                               = "ewe"
    EWONDO                            = "ewo"
    FANG                              = "fan"
    FAROESE                           = "fao"
    PERSIAN                           = "fas"
    FANTI                             = "fat"
    FIJIAN                            = "fij"
    FILIPINO                          = "fil"
    FINNISH                           = "fin"
    FINNO_UGRIAN_LANGUAGES            = "fiu"
    FON                               = "fon"
    FRENCH                            = "fra"
    MIDDLE_FRENCH                     = "frm"
    OLD_FRENCH                        = "fro"
    NORTHERN_FRISIAN                  = "frr"
    EASTERN_FRISIAN                   = "frs"
    WESTERN_FRISIAN                   = "fry"
    FULAH                             = "ful"
    FRIULIAN                          = "fur"
    GA                                = "gaa"
    GAYO                              = "gay"
    GBAYA                             = "gba"
    GERMANIC_LANGUAGES                = "gem"
    GEORGIAN                          = "kat"
    GEEZ                              = "gez"
    GILBERTESE                        = "gil"
    GAELIC                            = "gla"
    IRISH                             = "gle"
    GALICIAN                          = "glg"
    MANX                              = "glv"
    MIDDLE_HIGH_GERMAN                = "gmh"
    OLD_HIGH_GERMAN                   = "goh"
    GONDI                             = "gon"
    GORONTALO                         = "gor"
    GOTHIC                            = "got"
    GREBO                             = "grb"
    ANCIENT_GREEK                     = "grc"
    GUARANI                           = "grn"
    SWISS_GERMAN                      = "gsw"
    GUJARATI                          = "guj"
    GWICHIN                           = "gwi"
    HAIDA                             = "hai"
    HAITIAN                           = "hat"
    HAUSA                             = "hau"
    HAWAIIAN                          = "haw"
    HEBREW                            = "heb"
    HERERO                            = "her"
    HILIGAYNON                        = "hil"
    HIMACHALI_LANGUAGES               = "him"
    HINDI                             = "hin"
    HITTITE                           = "hit"
    HMONG                             = "hmn"
    HIRI_MOTU                         = "hmo"
    CROATIAN                          = "hrv"
    UPPER_SORBIAN                     = "hsb"
    HUNGARIAN                         = "hun"
    HUPA                              = "hup"
    IBAN                              = "iba"
    IGBO                              = "ibo"
    ICELANDIC                         = "isl"
    IDO                               = "ido"
    SICHUAN_YI                        = "iii"
    IJO_LANGUAGES                     = "ijo"
    INUKTITUT                         = "iku"
    INTERLINGUE                       = "ile"
    ILOKO                             = "ilo"
    INTERLINGUA                       = "ina"
    INDIC_LANGUAGES                   = "inc"
    INDONESIAN                        = "ind"
    INDO_EUROPEAN_LANGUAGES           = "ine"
    INGUSH                            = "inh"
    INUPIAQ                           = "ipk"
    IRANIAN_LANGUAGES                 = "ira"
    IROQUOIAN_LANGUAGES               = "iro"
    ITALIAN                           = "ita"
    JAVANESE                          = "jav"
    LOJBAN                            = "jbo"
    JAPANESE                          = "jpn"
    JUDEO_PERSIAN                     = "jpr"
    JUDEO_ARABIC                      = "jrb"
    KARA_KALPAK                       = "kaa"
    KABYLE                            = "kab"
    KACHIN                            = "kac"
    GREENLANDIC                       = "kal"
    KAMBA                             = "kam"
    KANNADA                           = "kan"
    KAREN_LANGUAGES                   = "kar"
    KASHMIRI                          = "kas"
    KANURI                            = "kau"
    KAWI                              = "kaw"
    KAZAKH                            = "kaz"
    KABARDIAN                         = "kbd"
    KHASI                             = "kha"
    KHOISAN_LANGUAGES                 = "khi"
    KHMER                             = "khm"
    KHOTANESE                         = "kho"
    KIKUYU                            = "kik"
    KINYARWANDA                       = "kin"
    KIRGHIZ                           = "kir"
    KIMBUNDU                          = "kmb"
    KONKANI                           = "kok"
    KOMI                              = "kom"
    KONGO                             = "kon"
    KOREAN                            = "kor"
    KOSRAEAN                          = "kos"
    KPELLE                            = "kpe"
    KARACHAY_BALKAR                   = "krc"
    KARELIAN                          = "krl"
    KRU_LANGUAGES                     = "kro"
    KURUKH                            = "kru"
    KUANYAMA                          = "kua"
    KUMYK                             = "kum"
    KURDISH                           = "kur"
    KUTENAI                           = "kut"
    LADINO                            = "lad"
    LAHNDA                            = "lah"
    LAMBA                             = "lam"
    LAO                               = "lao"
    LATIN                             = "lat"
    LATVIAN                           = "lav"
    LEZGHIAN                          = "lez"
    LIMBURGISH                        = "lim"
    LINGALA                           = "lin"
    LITHUANIAN                        = "lit"
    MONGO                             = "lol"
    LOZI                              = "loz"
    LUXEMBOURGISH                     = "ltz"
    LUBA_LULUA                        = "lua"
    LUBA_KATANGA                      = "lub"
    GANDA                             = "lug"
    LUISENO                           = "lui"
    LUNDA                             = "lun"
    LUO                               = "luo"
    LUSHAI                            = "lus"
    MACEDONIAN                        = "mkd"
    MADURESE                          = "mad"
    MAGAHI                            = "mag"
    MARSHALLESE                       = "mah"
    MAITHILI                          = "mai"
    MAKASAR                           = "mak"
    MALAYALAM                         = "mal"
    MANDINGO                          = "man"
    MAORI                             = "mri"
    AUSTRONESIAN_LANGUAGES            = "map"
    MARATHI                           = "mar"
    MASAI                             = "mas"
    MALAY                             = "msa"
    MOKSHA                            = "mdf"
    MANDAR                            = "mdr"
    MENDE                             = "men"
    MIDDLE_IRISH                      = "mga"
    MIKMAQ                            = "mic"
    MINANGKABAU                       = "min"
    MON_KHMER_LANGUAGES               = "mkh"
    MALAGASY                          = "mlg"
    MALTESE                           = "mlt"
    MANCHU                            = "mnc"
    MANIPURI                          = "mni"
    MANOBO_LANGUAGES                  = "mno"
    MOHAWK                            = "moh"
    MONGOLIAN                         = "mon"
    MOSSI                             = "mos"
    MULTIPLE_LANGUAGES                = "mul"
    MUNDA_LANGUAGES                   = "mun"
    CREEK                             = "mus"
    MIRANDESE                         = "mwl"
    MARWARI                           = "mwr"
    MAYAN_LANGUAGES                   = "myn"
    ERZYA                             = "myv"
    NAHUATL_LANGUAGES                 = "nah"
    NORTH_AMERICAN_INDIAN_LANGUAGES   = "nai"
    NEAPOLITAN                        = "nap"
    NAURU                             = "nau"
    NAVAJO                            = "nav"
    SOUTHERN_NDEBELE                  = "nbl"
    NORTHERN_NDEBELE                  = "nde"
    NDONGA                            = "ndo"
    LOW_GERMAN                        = "nds"
    NEPALI                            = "nep"
    NEPAL_BHASA                       = "new"
    NIAS                              = "nia"
    NIGER_KORDOFANIAN_LANGUAGES       = "nic"
    NIUEAN                            = "niu"
    NORWEGIAN_NYNORSK                 = "nno"
    BOKMAL                            = "nob"
    NOGAI                             = "nog"
    OLD_NORSE                         = "non"
    NORWEGIAN                         = "nor"
    NKO                               = "nqo"
    PEDI                              = "nso"
    NUBIAN_LANGUAGES                  = "nub"
    CLASSICAL_NEWARI                  = "nwc"
    CHICHEWA                          = "nya"
    NYAMWEZI                          = "nym"
    NYANKOLE                          = "nyn"
    NYORO                             = "nyo"
    NZIMA                             = "nzi"
    OCCITAN                           = "oci"
    OJIBWA                            = "oji"
    ORIYA                             = "ori"
    OROMO                             = "orm"
    OSAGE                             = "osa"
    OSSETIAN                          = "oss"
    OTTOMAN_TURKISH                   = "ota"
    OTOMIAN_LANGUAGES                 = "oto"
    PAPUAN_LANGUAGES                  = "paa"
    PANGASINAN                        = "pag"
    PAHLAVI                           = "pal"
    PAMPANGA                          = "pam"
    PANJABI                           = "pan"
    PAPIAMENTO                        = "pap"
    PALAUAN                           = "pau"
    OLD_PERSIAN                       = "peo"
    PHILIPPINE_LANGUAGES              = "phi"
    PHOENICIAN                        = "phn"
    PALI                              = "pli"
    POLISH                            = "pol"
    POHNPEIAN                         = "pon"
    PORTUGUESE                        = "por"
    PRAKRIT_LANGUAGES                 = "pra"
    PROVENÇAL                         = "pro"
    PASHTO                            = "pus"
    QUECHUA                           = "que"
    RAJASTHANI                        = "raj"
    RAPANUI                           = "rap"
    RAROTONGAN                        = "rar"
    ROMANCE_LANGUAGES                 = "roa"
    ROMANSH                           = "roh"
    ROMANY                            = "rom"
    ROMANIAN                          = "ron"
    RUNDI                             = "run"
    AROMANIAN                         = "rup"
    RUSSIAN                           = "rus"
    SANDAWE                           = "sad"
    SANGO                             = "sag"
    YAKUT                             = "sah"
    SOUTH_AMERICAN_INDIAN_LANGUAGES   = "sai"
    SALISHAN_LANGUAGES                = "sal"
    SAMARITAN_ARAMAIC                 = "sam"
    SANSKRIT                          = "san"
    SASAK                             = "sas"
    SANTALI                           = "sat"
    SICILIAN                          = "scn"
    SCOTS                             = "sco"
    SELKUP                            = "sel"
    SEMITIC_LANGUAGES                 = "sem"
    OLD_IRISH                         = "sga"
    SIGN_LANGUAGES                    = "sgn"
    SHAN                              = "shn"
    SIDAMO                            = "sid"
    SINHALA                           = "sin"
    SIOUAN_LANGUAGES                  = "sio"
    SINO_TIBETAN_LANGUAGES            = "sit"
    SLAVIC_LANGUAGES                  = "sla"
    SLOVAK                            = "slk"
    SLOVENIAN                         = "slv"
    SOUTHERN_SAMI                     = "sma"
    NORTHERN_SAMI                     = "sme"
    SAMI_LANGUAGES                    = "smi"
    LULE_SAMI                         = "smj"
    INARI_SAMI                        = "smn"
    SAMOAN                            = "smo"
    SKOLT_SAMI                        = "sms"
    SHONA                             = "sna"
    SINDHI                            = "snd"
    SONINKE                           = "snk"
    SOGDIAN                           = "sog"
    SOMALI                            = "som"
    SONGHAI_LANGUAGES                 = "son"
    SOUTHERN_SOTHO                    = "sot"
    SPANISH                           = "spa"
    SARDINIAN                         = "srd"
    SRANAN_TONGO                      = "srn"
    SERBIAN                           = "srp"
    SERER                             = "srr"
    NILO_SAHARAN_LANGUAGES            = "ssa"
    SWATI                             = "ssw"
    SUKUMA                            = "suk"
    SUNDANESE                         = "sun"
    SUSU                              = "sus"
    SUMERIAN                          = "sux"
    SWAHILI                           = "swa"
    SWEDISH                           = "swe"
    CLASSICAL_SYRIAC                  = "syc"
    SYRIAC                            = "syr"
    TAHITIAN                          = "tah"
    TAI_LANGUAGES                     = "tai"
    TAMIL                             = "tam"
    TATAR                             = "tat"
    TELUGU                            = "tel"
    TIMNE                             = "tem"
    TERENO                            = "ter"
    TETUM                             = "tet"
    TAJIK                             = "tgk"
    TAGALOG                           = "tgl"
    THAI                              = "tha"
    TIGRE                             = "tig"
    TIGRINYA                          = "tir"
    TIV                               = "tiv"
    TOKELAU                           = "tkl"
    KLINGON                           = "tlh"
    TLINGIT                           = "tli"
    TAMASHEK                          = "tmh"
    TONGA_NYASA                       = "tog"
    TONGA_ISLANDS                     = "ton"
    TOK_PISIN                         = "tpi"
    TSIMSHIAN                         = "tsi"
    TSWANA                            = "tsn"
    TSONGA                            = "tso"
    TURKMEN                           = "tuk"
    TUMBUKA                           = "tum"
    TUPI_LANGUAGES                    = "tup"
    TURKISH                           = "tur"
    ALTAIC_LANGUAGES                  = "tut"
    TUVALU                            = "tvl"
    TWI                               = "twi"
    TUVINIAN                          = "tyv"
    UDMURT                            = "udm"
    UGARITIC                          = "uga"
    UIGHUR                            = "uig"
    UKRAINIAN                         = "ukr"
    UMBUNDU                           = "umb"
    UNDETERMINED                      = "und"
    URDU                              = "urd"
    UZBEK                             = "uzb"
    VAI                               = "vai"
    VENDA                             = "ven"
    VIETNAMESE                        = "vie"
    VOLAPUK                           = "vol"
    VOTIC                             = "vot"
    WAKASHAN_LANGUAGES                = "wak"
    WOLAITA                           = "wal"
    WARAY                             = "war"
    WASHO                             = "was"
    SORBIAN_LANGUAGES                 = "wen"
    WALLOON                           = "wln"
    WOLOF                             = "wol"
    KALMYK                            = "xal"
    XHOSA                             = "xho"
    YAO                               = "yao"
    YAPESE                            = "yap"
    YIDDISH                           = "yid"
    YORUBA                            = "yor"
    YUPIK_LANGUAGES                   = "ypk"
    ZAPOTEC                           = "zap"
    BLISSYMBOLS                       = "zbl"
    ZENAGA                            = "zen"
    STANDARD_MOROCCAN_TAMAZIGHT       = "zgh"
    ZHUANG                            = "zha"
    ZANDE_LANGUAGES                   = "znd"
    ZULU                              = "zul"
    ZUNI                              = "zun"
    NO_LINGUISTIC_CONTENT             = "zxx"
    ZAZA                              = "zza"
# fmt: on

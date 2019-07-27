def nexrad_station_info():
    """
        Name:
		NEXRAD_STATION_INFO
        Purpose:
		This is a function to read a NEXRAD station info file. 
        Calling sequence:
		value = nexrad_station_info()
    Inputs:
		None.
    Output:
		Dictionary of station IDs and coordinates
    Keywords:
        	None.
    Author and history:
		Cameron R. Homeyer  2010-10-20.
				  2015-06-07. Pasted contents from look-up file within to support
							IDL vm scripts for real-time processing.
    """

    km_to_ft = 3280.84; #Set conversion factor for elevation

    #script = FILE_WHICH('nexrad_station_info.pro')
    #path   = STRMID(script, 0, STRLEN(script) -23)
    #infile = path + 'nexrad_stations.txt'																		;Set input filepath
    #nlines = FILE_LINES(infile) -2																				;Get number of lines in file
    #header = STRARR(2)																								;Create header array
    #line   = ' '

    lines = [
		'30001794 KABR 14929 ABERDEEN                       UNITED STATES        SD BROWN                          45.45583  -98.41306  1302   +6     NEXRAD                                           ',
		'30001795 KABX 03019 ALBUQUERQUE                    UNITED STATES        NM BERNALILLO                     35.14972  -106.82333 5870   +7     NEXRAD                                           ',
		'30001796 KAKQ 93773 NORFOLK RICH                   UNITED STATES        VA SUSSEX                         36.98389  -77.0075   112    +5     NEXRAD                                           ',
		'30001797 KAMA 23047 AMARILLO                       UNITED STATES        TX POTTER                         35.23333  -101.70889 3587   +6     NEXRAD                                           ',
		'30001798 KAMX 12899 MIAMI                          UNITED STATES        FL DADE                           25.61056  -80.41306  14     +5     NEXRAD                                           ',
		'30001799 KAPX 04837 GAYLORD                        UNITED STATES        MI ANTRIM                         44.90722  -84.71972  1464   +5     NEXRAD                                           ',
		'30001800 KARX 94987 LA CROSSE                      UNITED STATES        WI LA CROSSE                      43.82278  -91.19111  1276   +6     NEXRAD                                           ',
		'30001801 KATX 94287 SEATTLE                        UNITED STATES        WA ISLAND                         48.19472  -122.49444 494    +8     NEXRAD                                           ',
		'30001802 KBBX 93240 BEALE AFB                      UNITED STATES        CA BUTTE                          39.49611  -121.63167 173    +8     NEXRAD                                           ',
		'30001807 KBGM 04725 BINGHAMTON                     UNITED STATES        NY BROOME                         42.19972  -75.985    1606   +5     NEXRAD                                           ',
		'30001808 KBHX 94289 EUREKA                         UNITED STATES        CA HUMBOLDT                       40.49833  -124.29194 2402   +8     NEXRAD                                           ',
		'30001809 KBIS 24011 BISMARCK                       UNITED STATES        ND BURLEIGH                       46.77083  -100.76028 1658   +6     NEXRAD                                           ',
		'30001811 KBLX 94046 BILLINGS                       UNITED STATES        MT YELLOWSTONE                    45.85389  -108.60611 3598   +7     NEXRAD                                           ',
		'30001812 KBMX 53823 BIRMINGHAM                     UNITED STATES        AL SHELBY                         33.17194  -86.76972  645    +6     NEXRAD                                           ',
		'30001813 KBOX 54765 BOSTON                         UNITED STATES        MA BRISTOL                        41.95583  -71.1375   118    +5     NEXRAD                                           ',
		'30001814 KBRO 12919 BROWNSVILLE                    UNITED STATES        TX CAMERON                        25.91556  -97.41861  23     +6     NEXRAD                                           ',
		'30001815 KBUF 14733 BUFFALO                        UNITED STATES        NY ERIE                           42.94861  -78.73694  693    +5     NEXRAD                                           ',
		'30001816 KBYX 92804 KEY WEST                       UNITED STATES        FL MONROE                         24.59694  -81.70333  8      +5     NEXRAD                                           ',
		'30001781 KCAE 13883 COLUMBIA                       UNITED STATES        SC LEXINGTON                      33.94861  -81.11861  231    +5     NEXRAD                                           ',
		'30001782 KCBW 94625 HOULTON                        UNITED STATES        ME AROOSTOOK                      46.03917  -67.80694  746    +5     NEXRAD                                           ',
		'30001817 KCBX 04101 BOISE                          UNITED STATES        ID ADA                            43.49083  -116.23444 3061   +7     NEXRAD                                           ',
		'30001783 KCCX 54764 STATE COLLEGE                  UNITED STATES        PA CENTRE                         40.92306  -78.00389  2405   +5     NEXRAD                                           ',
		'30001818 KCLE 14820 CLEVELAND                      UNITED STATES        OH CUYAHOGA                       41.41306  -81.86     763    +5     NEXRAD                                           ',
		'30001819 KCLX 53845 CHARLESTON                     UNITED STATES        SC BEAUFORT                       32.65556  -81.04222  97     +5     NEXRAD                                           ',
		'30001821 KCRP 12924 CORPUS CHRISTI                 UNITED STATES        TX NUECES                         27.78389  -97.51083  45     +6     NEXRAD                                           ',
		'30001822 KCXX 54774 BURLINGTON                     UNITED STATES        VT CHITTENDEN                     44.51111  -73.16639  317    +5     NEXRAD                                           ',
		'30001823 KCYS 24018 CHEYENNE                       UNITED STATES        WY LARAMIE                        41.15194  -104.80611 6128   +7     NEXRAD                                           ',
		'30001824 KDAX 93235 SACRAMENTO                     UNITED STATES        CA YOLO                           38.50111  -121.67667 30     +8     NEXRAD                                           ',
		'30001825 KDDC 13985 DODGE CITY                     UNITED STATES        KS FORD                           37.76083  -99.96833  2590   +6     NEXRAD                                           ',
		'30001826 KDFX 22015 LAUGHLIN AFB                   UNITED STATES        TX KINNEY                         29.2725   -100.28028 1131   +6     NEXRAD                                           ',
		'30001827 KDGX       JACKSON BRANDON                UNITED STATES        MS RANKIN                         32.28     -89.98444  610    +6     NEXRAD                                           ',
		'30001828 KDIX 93377 PHILADELPHIA                   UNITED STATES        NJ BURLINGTON                     39.94694  -74.41111  149    +5     NEXRAD                                           ',
		'30001829 KDLH 14913 DULUTH                         UNITED STATES        MN ST. LOUIS                      46.83694  -92.20972  1428   +6     NEXRAD                                           ',
		'30001830 KDMX 94984 DES MOINES                     UNITED STATES        IA POLK                           41.73111  -93.72278  981    +6     NEXRAD                                           ',
		'30001831 KDOX 93770 DOVER AFB                      UNITED STATES        DE SUSSEX                         38.82556  -75.44     50     +5     NEXRAD                                           ',
		'30001832 KDTX 04830 DETROIT                        UNITED STATES        MI OAKLAND                        42.69972  -83.47167  1072   +5     NEXRAD                                           ',
		'30001833 KDVN 94982 DAVENPORT                      UNITED STATES        IA SCOTT                          41.61167  -90.58083  754    +6     NEXRAD                                           ',
		'30001834 KDYX 03987 DYESS AFB                      UNITED STATES        TX SHACKELFORD                    32.53833  -99.25417  1517   +6     NEXRAD                                           ',
		'30001835 KEAX 03983 KANSAS CITY                    UNITED STATES        MO CASS                           38.81028  -94.26417  995    +6     NEXRAD                                           ',
		'30001836 KEMX 53112 TUCSON                         UNITED STATES        AZ PIMA                           31.89361  -110.63028 5202   +7     NEXRAD                                           ',
		'30001837 KENX 54766 ALBANY                         UNITED STATES        NY ALBANY                         42.58639  -74.06444  1826   +5     NEXRAD                                           ',
		'30001838 KEOX 53851 FT RUCKER                      UNITED STATES        AL DALE                           31.46028  -85.45944  434    +6     NEXRAD                                           ',
		'30001839 KEPZ 03020 EL PASO                        UNITED STATES        NM DONA ANA                       31.87306  -106.6975  4104   +7     NEXRAD                                           ',
		'30001841 KESX 53110 LAS VEGAS                      UNITED STATES        NV CLARK                          35.70111  -114.89139 4867   +8     NEXRAD                                           ',
		'30001842 KEVX 53825 EGLIN AFB                      UNITED STATES        FL WALTON                         30.56417  -85.92139  140    +5     NEXRAD                                           ',
		'30001843 KEWX 12971 AUSTIN SAN ANTONIO             UNITED STATES        TX COMAL                          29.70361  -98.02806  633    +6     NEXRAD                                           ',
		'30001943 KEYX 53114 EDWARDS                        UNITED STATES        CA SANTA BARBARA                  35.09778  -117.56    2757   +8     NEXRAD                                           ',
		'30001844 KFCX 53831 ROANOKE                        UNITED STATES        VA FLOYD                          37.02417  -80.27417  2868   +5     NEXRAD                                           ',
		'30001845 KFDR 03981 ALTUS AFB                      UNITED STATES        OK TILLMAN                        34.36222  -98.97611  1267   +6     NEXRAD                                           ',
		'30001846 KFDX 03022 CANNON AFB                     UNITED STATES        NM CURRY                          34.63528  -103.62944 4650   +7     NEXRAD                                           ',
		'30001847 KFFC 53819 ATLANTA                        UNITED STATES        GA FAYETTE                        33.36333  -84.56583  858    +5     NEXRAD                                           ',
		'30001944 KFSD 14944 SIOUX FALLS                    UNITED STATES        SD MINNEHAHA                      43.58778  -96.72889  1430   +6     NEXRAD                                           ',
		'30001848 KFSX 53113 FLAGSTAFF                      UNITED STATES        AZ COCONINO                       34.57444  -111.19694 1430   +7     NEXRAD                                           ',
		'30001849 KFTG 03018 DENVER FRONT RANGE AP          UNITED STATES        CO ARAPAHOE                       39.78667  -104.54528 5497   +7     NEXRAD                                           ',
		'30001850 KFWS 03985 DALLAS                         UNITED STATES        TX TARRANT                        32.57278  -97.30278  683    +6     NEXRAD                                           ',
		'30001851 KGGW 94008 GLASGOW                        UNITED STATES        MT VALLEY                         48.20639  -106.62417 2276   +7     NEXRAD                                           ',
		'30001852 KGJX 03025 GRAND JUNCTION                 UNITED STATES        CO MESA                           39.06222  -108.21306 9992   +7     NEXRAD                                           ',
		'30001853 KGLD 23065 GOODLAND                       UNITED STATES        KS SHERMAN                        39.36694  -101.7     3651   +6     NEXRAD                                           ',
		'30001854 KGRB 14898 GREEN BAY                      UNITED STATES        WI BROWN                          44.49833  -88.11111  682    +6     NEXRAD                                           ',
		'30001855 KGRK 03992 FT HOOD                        UNITED STATES        TX BELL                           30.72167  -97.38278  538    +6     NEXRAD                                           ',
		'30001856 KGRR 94860 GRAND RAPIDS                   UNITED STATES        MI KENT                           42.89389  -85.54472  778    +5     NEXRAD                                           ',
		'30001857 KGSP 03870 GREER                          UNITED STATES        SC SPARTANBURG                    34.88306  -82.22028  940    +5     NEXRAD                                           ',
		'30001858 KGWX 53837 COLUMBUS AFB                   UNITED STATES        MS MONROE                         33.89667  -88.32889  476    +6     NEXRAD                                           ',
		'30001859 KGYX 54762 PORTLAND                       UNITED STATES        ME CUMBERLAND                     43.89139  -70.25694  409    +5     NEXRAD                                           ',
		'30001945 KHDX 03023 HOLLOMAN AFB                   UNITED STATES        NM DONA ANA                       33.07639  -106.12222 4222   +7     NEXRAD                                           ',
		'30001860 KHGX 03980 HOUSTON                        UNITED STATES        TX GALVESTON                      29.47194  -95.07889  18     +6     NEXRAD                                           ',
		'30001861 KHNX 53111 SAN JOAQUIN VALLEY             UNITED STATES        CA KINGS                          36.31417  -119.63111 243    +8     NEXRAD                                           ',
		'30001862 KHPX 53839 FT CAMPBELL                    UNITED STATES        KY TODD                           36.73667  -87.285    576    +6     NEXRAD                                           ',
		'30001863 KHTX 53857 HUNTSVILLE                     UNITED STATES        AL JACKSON                        34.93056  -86.08361  1760   +6     NEXRAD                                           ',
		'30001864 KICT 03928 WICHITA                        UNITED STATES        KS SEDGWICK                       37.65444  -97.4425   1335   +6     NEXRAD                                           ',
		'30001865 KICX 53118 CEDAR CITY                     UNITED STATES        UT IRON                           37.59083  -112.86222 10600  +7     NEXRAD                                           ',
		'30001866 KILN 13841 CINCINNATI                     UNITED STATES        OH CLINTON                        39.42028  -83.82167  1056   +5     NEXRAD                                           ',
		'30001867 KILX 04833 LINCOLN                        UNITED STATES        IL LOGAN                          40.15056  -89.33667  582    +6     NEXRAD                                           ',
		'30001868 KIND 93819 INDIANAPOLIS                   UNITED STATES        IN MARION                         39.7075   -86.28028  790    +5     NEXRAD                                           ',
		'30001869 KINX 03984 TULSA                          UNITED STATES        OK ROGERS                         36.175    -95.56444  668    +6     NEXRAD                                           ',
		'30001870 KIWA 23104 PHOENIX                        UNITED STATES        AZ MARICOPA                       33.28917  -111.66917 1353   +7     NEXRAD                                           ',
		'30001871 KIWX 04844 FT WAYNE                       UNITED STATES        IN KOSCIUSKO                      41.40861  -85.7      960    +5     NEXRAD                                           ',
		'30001872 KJAX 13889 JACKSONVILLE                   UNITED STATES        FL DUVAL                          30.48444  -81.70194  33     +5     NEXRAD                                           ',
		'30001873 KJGX 53824 ROBINS AFB                     UNITED STATES        GA TWIGGS                         32.675    -83.35111  521    +5     NEXRAD                                           ',
		'30001874 KJKL 03889 JACKSON                        UNITED STATES        KY BREATHITT                      37.59083  -83.31306  1364   +5     NEXRAD                                           ',
		'30001875 KLBB 23042 LUBBOCK                        UNITED STATES        TX LUBBOCK                        33.65417  -101.81361 3259   +6     NEXRAD                                           ',
		'30001876 KLCH 03937 LAKE CHARLES                   UNITED STATES        LA CALCASIEU                      30.125    -93.21583  13     +6     NEXRAD                                           ',
		'30001877 KLIX 53813 NEW ORLEANS                    UNITED STATES        LA ST. TAMMANY                    30.33667  -89.82528  24     +6     NEXRAD                                           ',
		'30001878 KLNX 94049 NORTH PLATTE                   UNITED STATES        NE LOGAN                          41.95778  -100.57583 2970   +6     NEXRAD                                           ',
		'30001879 KLOT 04831 CHICAGO                        UNITED STATES        IL WILL                           41.60444  -88.08472  663    +6     NEXRAD                                           ',
		'30001880 KLRX 04108 ELKO                           UNITED STATES        NV LANDER                         40.73972  -116.80278 6744   +8     NEXRAD                                           ',
		'30001881 KLSX 03982 ST LOUIS                       UNITED STATES        MO ST. CHARLES                    38.69889  -90.68278  608    +6     NEXRAD                                           ',
		'30001882 KLTX 93774 WILMINGTON                     UNITED STATES        NC BRUNSWICK                      33.98917  -78.42917  64     +5     NEXRAD                                           ',
		'30001883 KLVX 53827 LOUISVILLE                     UNITED STATES        KY HARDIN                         37.97528  -85.94389  719    +5     NEXRAD                                           ',
		'30001884 KLWX 93767 STERLING                       UNITED STATES        VA LOUDOUN                        38.97528  -77.47806  272    +5     NEXRAD                                           ',
		'30001885 KLZK 03952 LITTLE ROCK                    UNITED STATES        AR PULASKI                        34.83639  -92.26194  20     +6     NEXRAD                                           ',
		'30001886 KMAF 23023 MIDLAND ODESSA                 UNITED STATES        TX MIDLAND                        31.94333  -102.18889 2868   +6     NEXRAD                                           ',
		'30001887 KMAX 94296 MEDFORD                        UNITED STATES        OR JACKSON                        42.08111  -122.71611 7513   +8     NEXRAD                                           ',
		'30001888 KMBX 94048 MINOT AFB                      UNITED STATES        ND MCHENRY                        48.3925   -100.86444 1493   +6     NEXRAD                                           ',
		'30001889 KMHX 93768 MOREHEAD CITY                  UNITED STATES        NC CARTERET                       34.77583  -76.87639  31     +5     NEXRAD                                           ',
		'30001890 KMKX 04834 MILWAUKEE                      UNITED STATES        WI WAUKESHA                       42.96778  -88.55056  958    +6     NEXRAD                                           ',
		'30001891 KMLB 12838 MELBOURNE                      UNITED STATES        FL BREVARD                        28.11306  -80.65444  35     +5     NEXRAD                                           ',
		'30001892 KMOB 13894 MOBILE                         UNITED STATES        AL MOBILE                         30.67944  -88.23972  208    +6     NEXRAD                                           ',
		'30001893 KMPX 94983 MINNEAPOLIS                    UNITED STATES        MN CARVER                         44.84889  -93.56528  946    +6     NEXRAD                                           ',
		'30001894 KMQT 94850 MARQUETTE                      UNITED STATES        MI MARQUETTE                      46.53111  -87.54833  1411   +5     NEXRAD                                           ',
		'30001895 KMRX 53832 KNOXVILLE                      UNITED STATES        TN HAMBLEN                        36.16833  -83.40194  1337   +5     NEXRAD                                           ',
		'30001896 KMSX 04103 MISSOULA                       UNITED STATES        MT MISSOULA                       47.04111  -113.98611 7855   +7     NEXRAD                                           ',
		'30001897 KMTX 04104 SALT LAKE CITY                 UNITED STATES        UT SALT LAKE                      41.26278  -112.44694 6460   +7     NEXRAD                                           ',
		'30001898 KMUX 93236 SAN FRANCISCO                  UNITED STATES        CA SANTA CLARA                    37.15528  -121.8975  3469   +8     NEXRAD                                           ',
		'30001899 KMVX 94986 GRAND FORKS                    UNITED STATES        ND TRAILL                         47.52806  -97.325    986    +6     NEXRAD                                           ',
		'30001900 KMXX 53826 MAXWELL AFB                    UNITED STATES        AL TALLAPOOSA                     32.53667  -85.78972  400    +6     NEXRAD                                           ',
		'30001901 KNKX 53115 SAN DIEGO                      UNITED STATES        CA SAN DIEGO                      32.91889  -117.04194 955    +8     NEXRAD                                           ',
		'30001902 KNQA 93839 MEMPHIS                        UNITED STATES        TN SHELBY                         35.34472  -89.87333  282    +5     NEXRAD                                           ',
		'30001903 KOAX 94980 OMAHA                          UNITED STATES        NE DOUGLAS                        41.32028  -96.36639  1148   +6     NEXRAD                                           ',
		'30001904 KOHX 53833 NASHVILLE                      UNITED STATES        TN WILSON                         36.24722  -86.5625   579    +5     NEXRAD                                           ',
		'30001905 KOKX 94703 NEW YORK CITY                  UNITED STATES        NY SUFFOLK                        40.86556  -72.86444  85     +5     NEXRAD                                           ',
		'30001906 KOTX 04106 SPOKANE                        UNITED STATES        WA SPOKANE                        47.68056  -117.62583 2384   +8     NEXRAD                                           ',
		'30001907 KPAH 03816 PADUCAH                        UNITED STATES        KY MCCRACKEN                      37.06833  -88.77194  392    +6     NEXRAD                                           ',
		'30001908 KPBZ 04832 PITTSBURGH                     UNITED STATES        PA ALLEGHENY                      40.53167  -80.21833  1185   +5     NEXRAD                                           ',
		'30001909 KPDT 24155 PENDLETON                      UNITED STATES        OR UMATILLA                       45.69056  -118.85278 1515   +8     NEXRAD                                           ',
		'30001910 KPOE 03993 FT POLK                        UNITED STATES        LA VERNON                         31.15528  -92.97583  408    +6     NEXRAD                                           ',
		'30001911 KPUX 03021 PUEBLO                         UNITED STATES        CO PUEBLO                         38.45944  -104.18139 5249   +7     NEXRAD                                           ',
		'30001912 KRAX 93772 RALEIGH DURHAM                 UNITED STATES        NC WAKE                           35.66528  -78.49     348    +5     NEXRAD                                           ',
		'30001913 KRGX 53104 RENO                           UNITED STATES        NV WASHOE                         39.75417  -119.46111 8299   +8     NEXRAD                                           ',
		'30001914 KRIW 24061 RIVERTON                       UNITED STATES        WY FREMONT                        43.06611  -108.47667 5568   +7     NEXRAD                                           ',
		'30001915 KRLX 53834 CHARLESTON                     UNITED STATES        WV KANAWHA                        38.31194  -81.72389  1080   +5     NEXRAD                                           ',
		'30001916 KRTX 94288 PORTLAND                       UNITED STATES        OR WASHINGTON                     45.715    -122.96417 1572   +8     NEXRAD                                           ',
		'30001917 KSFX 04107 POCATELLO                      UNITED STATES        ID BINGHAM                        43.10583  -112.68528 4474   +7     NEXRAD                                           ',
		'30001918 KSGF 13995 SPRINGFIELD                    UNITED STATES        MO GREENE                         37.23528  -93.40028  1278   +6     NEXRAD                                           ',
		'30001920 KSHV 13957 SHREVEPORT                     UNITED STATES        LA CADDO                          32.45056  -93.84111  273    +6     NEXRAD                                           ',
		'30001921 KSJT 23034 SAN ANGELO                     UNITED STATES        TX TOM GREEN                      31.37111  -100.49222 1890   +6     NEXRAD                                           ',
		'30001922 KSOX 53117 SANTA ANNA MOUNTAINS           UNITED STATES        CA ORANGE                         33.81778  -117.635   3027   +8     NEXRAD                                           ',
		'30001948 KSRX 53906 FT SMITH                       UNITED STATES        AR SEBASTIAN                      35.29056  -94.36167  1516   +6     NEXRAD                                           ',
		'30001923 KTBW 92801 TAMPA                          UNITED STATES        FL HILLSBOROUGH                   27.70528  -82.40194  41     +5     NEXRAD                                           ',
		'30001925 KTFX 04102 GREAT FALLS                    UNITED STATES        MT CASCADE                        47.45972  -111.38444 3714   +7     NEXRAD                                           ',
		'30001924 KTLH 93805 TALLAHASSEE                    UNITED STATES        FL LEON                           30.3975   -84.32889  63     +5     NEXRAD                                           ',
		'30001926 KTLX 03979 OKLAHOMA CITY                  UNITED STATES        OK OKLAHOMA                       35.33306  -97.2775   1213   +6     NEXRAD                                           ',
		'30001927 KTWX 03986 TOPEKA                         UNITED STATES        KS WABAUNSEE                      38.99694  -96.2325   1367   +6     NEXRAD                                           ',
		'30001946 KTYX 54776 FT DRUM                        UNITED STATES        NY LEWIS                          43.75583  -75.68     1846   +5     NEXRAD                                           ',
		'30001928 KUDX 94047 RAPID CITY                     UNITED STATES        SD PENNINGTON                     44.125    -102.82944 3016   +6     NEXRAD                                           ',
		'30001929 KUEX 94981 HASTINGS                       UNITED STATES        NE WEBSTER                        40.32083  -98.44167  1976   +6     NEXRAD                                           ',
		'00000000 KVAX 53856 MOODY AFB                      UNITED STATES        GA                                30.39028  -83.001663 173    +5     NEXRAD                                           ',
		'30001930 KVBX 93234 VANDENBERG AFB                 UNITED STATES        CA SANTA BARBARA                  34.83806  -120.39583 1233   +8     NEXRAD                                           ',
		'30001931 KVNX 03995 VANCE AFB                      UNITED STATES        OK ALFALFA                        36.74083  -98.1275   1210   +6     NEXRAD                                           ',
		'30001932 KVTX 53101 LOS ANGELES                    UNITED STATES        CA VENTURA                        34.41167  -119.17861 2726   +8     NEXRAD                                           ',
		'30001609 KVWX 63845 EVANSVILLE                     UNITED STATES        IN GIBSON                         38.26     -87.72472  623    +6     NEXRAD                                           ',
		'30001938 LPLA 13201 LAJES AB                       AZORES                                                 38.73028  -27.32167  3334          NEXRAD                                           ',
		'30001939 PABC       BETHEL FAA                     UNITED STATES        AK BETHEL                         60.79278  -161.87417 162    +9     NEXRAD                                           ',
		'30001940 PACG 25361 SITKA                          UNITED STATES        AK SITKA                          56.85278  -135.52917 270    +9     NEXRAD                                           ',
		'30001941 PAEC 26641 NOME                           UNITED STATES        AK NOME                           64.51139  -165.295   54     +9     NEXRAD                                           ',
		'30001942 PAHG 26548 ANCHORAGE                      UNITED STATES        AK KENAI PENINSULA                60.72639  -151.34917 242    +9     NEXRAD                                           ',
		'30001958 PAIH 25404 MIDDLETON ISLAND               UNITED STATES        AK VALDEZ-CORDOVA                 59.46194  -146.30111 67     +9     NEXRAD                                           ',
		'30001959 PAKC 25503 KING SALMON                    UNITED STATES        AK BRISTOL BAY                    58.67944  -156.62944 63     +9     NEXRAD                                           ',
		'30001960 PAPD 24690 FAIRBANKS                      UNITED STATES        AK FAIRBANKS NORTH STAR           65.03556  -147.49917 2593   +9     NEXRAD                                           ',
		'30001962 PHKI 22548 SOUTH KAUAI                    UNITED STATES        HI KAUAI                          21.89417  -159.55222 179    +10    NEXRAD                                           ',
		'30001963 PHKM 22550 KAMUELA                        UNITED STATES        HI HAWAII                         20.12556  -155.77778 3812   +10    NEXRAD                                           ',
		'30001964 PHMO 22547 MOLOKAI                        UNITED STATES        HI HAWAII                         21.13278  -157.18    1363   +8     NEXRAD                                           ',
		'30001965 PHWA 22513 SOUTH SHORE                    UNITED STATES        HI HAWAII                         19.095    -155.56889 1370   +10    NEXRAD                                           ',
		'30001967 RKJK 43219 KUNSAN                         KOREA, SOUTH                                           35.92417  126.62222  78     -9     NEXRAD                                           ',
		'30001968 RKSG 43216 CAMP HUMPHREYS                 KOREA, SOUTH                                           36.95972  127.01833  52     -9     NEXRAD                                           ',
		'30001969 RODN 42219 KADENA                         JAPAN                                                  26.30194  127.90972  218           NEXRAD                                           ',
		'30001966 TJUA 11655 SAN JUAN                       UNITED STATES        PR SAN JUAN                       18.1175   -66.07861  2794   +4     NEXRAD                                           ',
		'30001961      41417 ANDERSEN AFB AGANA             GUAM                 GU GUAM                           13.45444  144.80833  264    +8     NEXRAD                                           ']
    nlines = len( lines )
    data   = {  'statid' : [],
                'lon'    : [],
                'lat'    : [],
                'alt'    : []}
    for line in lines:
        print
        data['statid'].append( line[9:13] )
        data['lon'].append(    (float(line[116:126]) + 360.0) % 360.0 )
        data['lat'].append(    float(line[106:115]) )
        data['alt'].append(    float(line[127:133]) / km_to_ft )
    return data
# pip install fonttools
# python .\script.py nerdfonts_regular.ttf > regular.rs

from itertools import chain
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode
import sys

with TTFont(
    sys.argv[1], 0, allowVID=0, ignoreDecompileErrors=True, fontNumber=-1
) as ttf:
    chars = chain.from_iterable(
        [y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables
    )
    lines_seen = set() # holds lines already seen

    for char in chars:
        symbol_name = char[1].upper().replace('-', '_').replace(' ', '_').replace('#', '_').replace('!', '_').replace('(', '_').replace(')', '_').replace('.', '_').replace('/', '_')
        code = r"\u" + "{" + f"{char[0]:X}" + "}"
        
        match symbol_name:
            case "_NULL":
                continue
            case "500PX":
                continue
            # replace symbol_names on specific codes (to avoid duplicates)
            case "ANGLE_RIGHT":
                if code == r"\u{F0939}":
                    symbol_name = "ANGLE_RIGHT_MD"
            case "APPLE":
                if code == r"\u{F302}":
                    symbol_name = "APPLE_LINUX";
            case "ARROW_DOWN":
                if code == r"\u{F063}":
                    symbol_name = "ARROW_DOWN_FA";
            case "ARROW_LEFT":
                if code == r"\u{F060}":
                    symbol_name = "ARROW_LEFT_FA";
            case "ARROW_RIGHT":
                if code == r"\u{F061}":
                    symbol_name = "ARROW_RIGHT_FA";
            case "ARROW_UP":
                if code == r"\u{F062}":
                    symbol_name = "ARROW_UP_FA";
            case "BABY_CARRIAGE":
                if code == r"\u{EF34}":
                    symbol_name = "BABY_CARRIAGE_FA";
            case "BELL_SLASH": 
                if code == r"\u{F1F6}":
                    symbol_name = "BELL_SLASH_FA";
            case "BOOK_OPEN": 
                if code == r"\u{EDE2}":
                    symbol_name = "BOOK_OPEN_FA";
            case "BORDER_ALL": 
                if code == r"\u{EFA3}":
                    symbol_name = "BORDER_ALL_FA";
            case "BORDER_NONE": 
                if code == r"\u{EFA4}":
                    symbol_name = "BORDER_NONE_FA";
            case "BREAD_SLICE": 
                if code == r"\u{EF79}":
                    symbol_name = "BREAD_SLICE_FA";
            case "CALENDAR_CHECK": 
                if code == r"\u{F274}":
                    symbol_name = "CALENDAR_CHECK_FA";
            case "CALENDAR_MINUS": 
                if code == r"\u{F272}":
                    symbol_name = "CALENDAR_MINUS_FA";
            case "CALENDAR_PLUS": 
                if code == r"\u{F271}":
                    symbol_name = "CALENDAR_PLUS_FA";
            case "CALENDAR_WEEK": 
                if code == r"\u{EF38}":
                    symbol_name = "CALENDAR_WEEK_FA";
            case "CART_ARROW_DOWN": 
                if code == r"\u{F218}":
                    symbol_name = "CART_ARROW_DOWN_FA";
            case "CART_PLUS": 
                if code == r"\u{F217}":
                    symbol_name = "CART_PLUS_FA";
            case "CAR_BATTERY": 
                if code == r"\u{EE9E}":
                    symbol_name = "CAR_BATTERY_FA";
            case "CAR_SIDE": 
                if code == r"\u{EEA0}":
                    symbol_name = "CAR_SIDE_FA";
            case "CASH_REGISTER": 
                if code == r"\u{EF3C}":
                    symbol_name = "CASH_REGISTER_FA";
            case "CENTOS": 
                if code == r"\u{EF3D}":
                    symbol_name = "CENTOS_EF";
            case "CHART_BAR": 
                if code == r"\u{F080}":
                    symbol_name = "CHART_BAR_FA";
            case "CHART_LINE": 
                if code == r"\u{F201}":
                    symbol_name = "CHART_LINE_FA";
            case "CHART_PIE": 
                if code == r"\u{F200}":
                    symbol_name = "CHART_PIE_FA";
            case "CHESS_BISHOP": 
                if code == r"\u{ED60}":
                    symbol_name = "CHESS_BISHOP_FA";
            case "CHESS_KING": 
                if code == r"\u{ED62}":
                    symbol_name = "CHESS_KING_FA";
            case "CHESS_KNIGHT": 
                if code == r"\u{ED63}":
                    symbol_name = "CHESS_KNIGHT_FA";
            case "CHESS_PAWN": 
                if code == r"\u{ED64}":
                    symbol_name = "CHESS_PAWN_FA";
            case "CHESS_QUEEN": 
                if code == r"\u{ED65}":
                    symbol_name = "CHESS_QUEEN_FA";
            case "CHESS_ROOK": 
                if code == r"\u{ED66}":
                    symbol_name = "CHESS_ROOK_FA";
            case "CHEVRON_DOWN": 
                if code == r"\u{F078}":
                    symbol_name = "CHEVRON_DOWN_FA";
            case "CHEVRON_LEFT": 
                if code == r"\u{F053}":
                    symbol_name = "CHEVRON_LEFT_FA";
            case "CHEVRON_RIGHT": 
                if code == r"\u{F054}":
                    symbol_name = "CHEVRON_RIGHT_FA";
            case "CHEVRON_UP": 
                if code == r"\u{F077}":
                    symbol_name = "CHEVRON_UP_FA";
            case "CLIPBOARD_CHECK": 
                if code == r"\u{ED7A}":
                    symbol_name = "CLIPBOARD_CHECK_FA";
            case "CLIPBOARD_LIST": 
                if code == r"\u{ED7B}":
                    symbol_name = "CLIPBOARD_LIST_FA";
            case "CREATIVE_COMMONS": 
                if code == r"\u{F25E}":
                    symbol_name = "CREATIVE_COMMONS_FA";
            case "CREDIT_CARD": 
                if code == r"\u{F09D}":
                    symbol_name = "CREDIT_CARD_FA";
            case "DEBIAN":
                if code == r"\u{F306}":
                    symbol_name = "DEBIAN_LINUX";
            case "DICE_1":
                if code == r"\u{EDEC}":
                    symbol_name = "DICE_1_FA";
            case "DICE_D20":
                if code == r"\u{EEF5}":
                    symbol_name = "DICE_D20_FA";
            case "DICE_D6":
                if code == r"\u{EEF6}":
                    symbol_name = "DICE_D6_FA";
            case "DIGITAL_OCEAN":
                if code == r"\u{F1EF}":
                    symbol_name = "DIGITAL_OCEAN_FA";
            case "DOCKER":
                if code == r"\u{F21F}":
                    symbol_name = "DOCKER_FA";
            case "DOOR_CLOSED":
                if code == r"\u{EDF4}":
                    symbol_name = "DOOR_CLOSED_FA";
            case "DOOR_OPEN":
                if code == r"\u{EDF5}":
                    symbol_name = "DOOR_OPEN_FA";
            case "ENVELOPE_OPEN":
                if code == r"\u{F2B6}":
                    symbol_name = "ENVELOPE_OPEN_FA";
            case "ENVELOPE_OPEN_O":
                if code == r"\u{F2B7}":
                    symbol_name = "ENVELOPE_OPEN_O_FA";
            case "FACEBOOK_MESSENGER":
                if code == r"\u{F25F}":
                    symbol_name = "FACEBOOK_MESSENGER_FA";
            case "FEDORA":
                if code == r"\u{F30A}":
                    symbol_name = "FEDORA_LINUX";
            case "FILE_CODE": 
                if code == r"\u{F1C9}": 
                    symbol_name = "FILE_CODE_FA";
            case "FILE_EXCEL": 
                if code == r"\u{F1C3}": 
                    symbol_name = "FILE_EXCEL_FA";
            case "FILE_EXPORT": 
                if code == r"\u{EE37}": 
                    symbol_name = "FILE_EXPORT_FA";
            case "FILE_IMAGE": 
                if code == r"\u{F1C5}": 
                    symbol_name = "FILE_IMAGE_FA";
            case "FILE_IMPORT": 
                if code == r"\u{EE38}": 
                    symbol_name = "FILE_IMPORT_FA";
            case "FILE_PDF": 
                if code == r"\u{F1C1}": 
                    symbol_name = "FILE_PDF_FA";
            case "FILE_POWERPOINT": 
                if code == r"\u{F1C4}": 
                    symbol_name = "FILE_POWERPOINT_FA";
            case "FILE_VIDEO": 
                if code == r"\u{F1C8}": 
                    symbol_name = "FILE_VIDEO_FA";
            case "FILE_WORD": 
                if code == r"\u{F1C2}": 
                    symbol_name = "FILE_WORD_FA";
            case "FIRE_EXTINGUISHER": 
                if code == r"\u{F134}": 
                    symbol_name = "FIRE_EXTINGUISHER_FA";
            case "FLAG_CHECKERED": 
                if code == r"\u{F11E}": 
                    symbol_name = "FLAG_CHECKERED_FA";
            case "FOLDER_OPEN": 
                if code == r"\u{F07C}": 
                    symbol_name = "FOLDER_OPEN_FA";
            case "FOLDER_PLUS": 
                if code == r"\u{EEC7}": 
                    symbol_name = "FOLDER_PLUS_FA";
            case "FONT_AWESOME": 
                if code == r"\u{F2B4}": 
                    symbol_name = "FONT_AWESOME_FA";
            case "FREEBSD": 
                if code == r"\u{F28F}": 
                    symbol_name = "FREEBSD_FA";
            case "GENTOO": 
                if code == r"\u{F30D}": 
                    symbol_name = "GENTOO_LINUX";
            case "GITHUB_ALT": 
                if code == r"\u{F113}": 
                    symbol_name = "GITHUB_ALT_FA";
            case "GNOME": 
                if code == r"\u{F361}": 
                    symbol_name = "GNOME_LINUX";
            case "GOOGLE_DRIVE": 
                if code == r"\u{F2DF}": 
                    symbol_name = "GOOGLE_DRIVE_FA";
            case "GOOGLE_PLAY": 
                if code == r"\u{F2E1}": 
                    symbol_name = "GOOGLE_PLAY_FA";
            case "GOOGLE_PLUS": 
                if code == r"\u{F0D5}": 
                    symbol_name = "GOOGLE_PLUS_FA";
            case "GREATER_THAN": 
                if code == r"\u{EDFB}": 
                    symbol_name = "GREATER_THAN_FA";
            case "HAND_PEACE": 
                if code == r"\u{F25B}": 
                    symbol_name = "HAND_PEACE_FA";
            case "HEART_PULSE": 
                if code == r"\u{F21E}": 
                    symbol_name = "HEART_PULSE_FA";
            case "HOCKEY_PUCK": 
                if code == r"\u{ED6C}": 
                    symbol_name = "HOCKEY_PUCK_FA";
            case "ICE_CREAM": 
                if code == r"\u{EF88}": 
                    symbol_name = "ICE_CREAM_FA";
            case "ID_BADGE": 
                if code == r"\u{F2C1}": 
                    symbol_name = "ID_BADGE_FA";
            case "ID_CARD": 
                if code == r"\u{F2C2}": 
                    symbol_name = "ID_CARD_FA";
            case "LESS_THAN": 
                if code == r"\u{EFC3}": 
                    symbol_name = "LESS_THAN_FA";
            case "LINUX_MINT": 
                if code == r"\u{F30E}": 
                    symbol_name = "LINUX_MINT_2";
            case "LOCK_OPEN": 
                if code == r"\u{F2FC}": 
                    symbol_name = "LOCK_OPEN_FA";
            case "MANJARO": 
                if code == r"\u{F312}": 
                    symbol_name = "MANJARO_LINUX";
            case "MORTAR_PESTLE": 
                if code == r"\u{EE70}": 
                    symbol_name = "MORTAR_PESTLE_FA";
            case "NONMARKINGRETURN": 
                if code == r"\u{D}": 
                    symbol_name = "NONMARKINGRETURN_2";
            case "NOT_EQUAL": 
                if code == r"\u{EFCB}": 
                    symbol_name = "NOT_EQUAL_FA";
            case "OSI": 
                if code == r"\u{ED45}": 
                    symbol_name = "OSI_FA";
            case "PIGGY_BANK": 
                if code == r"\u{EDA3}": 
                    symbol_name = "PIGGY_BANK_FA";
            case "POWER_OFF": 
                if code == r"\u{F011}": 
                    symbol_name = "POWER_OFF_FA";
            case "RASPBERRY_PI": 
                if code == r"\u{EF5C}": 
                    symbol_name = "RASPBERRY_PI_FA";
            case "RASPBERRY_PI": 
                if code == r"\u{F315}": 
                    symbol_name = "RASPBERRY_PI_LINUX";
            case "REPLY_ALL": 
                if code == r"\u{F122}": 
                    symbol_name = "REPLY_ALL_FA";
            case "ROTATE_LEFT": 
                if code == r"\u{F2EA}": 
                    symbol_name = "ROTATE_LEFT_FA";
            case "ROTATE_RIGHT": 
                if code == r"\u{F2F9}": 
                    symbol_name = "ROTATE_RIGHT_FA";
            case "SCALE_UNBALANCED": 
                if code == r"\u{EDDF}": 
                    symbol_name = "SCALE_UNBALANCED_FA";
            case "SKULL_CROSSBONES": 
                if code == r"\u{EF0E}": 
                    symbol_name = "SKULL_CROSSBONES_FA";
            case "SOLAR_PANEL": 
                if code == r"\u{EE81}": 
                    symbol_name = "SOLAR_PANEL_FA";
            case "STACK_EXCHANGE": 
                if code == r"\u{F18D}": 
                    symbol_name = "STACK_EXCHANGE_FA";
            case "STACK_OVERFLOW": 
                if code == r"\u{F16C}": 
                    symbol_name = "STACK_OVERFLOW_FA";
            case "STAR_HALF": 
                if code == r"\u{F089}": 
                    symbol_name = "STAR_HALF_FA";
            case "TRAFFIC_LIGHT": 
                if code == r"\u{EEB7}": 
                    symbol_name = "TRAFFIC_LIGHT_FA";
            case "TRASH_CAN": 
                if code == r"\u{F014}": 
                    symbol_name = "TRASH_CAN_FA";
            case "TRUCK_FAST": 
                if code == r"\u{ED8B}": 
                    symbol_name = "TRUCK_FAST_FA";
            case "UBUNTU": 
                if code == r"\u{F31B}": 
                    symbol_name = "UBUNTU_LINUX";
            case "UMBRELLA_BEACH": 
                if code == r"\u{EE91}": 
                    symbol_name = "UMBRELLA_BEACH_FA";
            case "VECTOR_SQUARE": 
                if code == r"\u{EE92}": 
                    symbol_name = "VECTOR_SQUARE_FA";
            case "VOLUME_HIGH": 
                if code == r"\u{F028}": 
                    symbol_name = "VOLUME_HIGH_FA";
            case "VOLUME_LOW": 
                if code == r"\u{F027}": 
                    symbol_name = "VOLUME_LOW_FA";
            case "VOLUME_OFF": 
                if code == r"\u{F026}": 
                    symbol_name = "VOLUME_OFF_FA";
            case "WINDOW_MAXIMIZE": 
                if code == r"\u{F2D0}": 
                    symbol_name = "WINDOW_MAXIMIZE_FA";
            case "WINDOW_MINIMIZE": 
                if code == r"\u{F2D1}": 
                    symbol_name = "WINDOW_MINIMIZE_FA";
            case "WINDOW_RESTORE": 
                if code == r"\u{F2D2}": 
                    symbol_name = "WINDOW_RESTORE_FA";
            case "YIN_YANG": 
                if code == r"\u{EEE9}": 
                    symbol_name = "YIN_YANG_FA";

        line = f"pub const {symbol_name}: &str = \"{code}\";"

        if line not in lines_seen: # not a duplicate
            lines_seen.add(line)

    print(f"#![allow(unused)]")

    for line_seen in sorted(lines_seen):
        print(line_seen)
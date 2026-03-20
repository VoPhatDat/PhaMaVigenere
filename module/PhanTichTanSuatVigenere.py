
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from collections import Counter

BASE_FONT_FAMILY = "Consolas"
HEADER_FONT_SIZE = 16       
SUMMARY_FONT_SIZE = 13      
PLAINTEXT_FONT_SIZE = 13    
CAESAR_FONT_SIZE = 12       
MATRIX_FONT_SIZE = 11       

BEST_HIGHLIGHT_COLOR = "#A5FFD6" 

#Tần suất chữ cái trong tiếng Anh

FREQ_ENGLISH = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702,
    'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153,
    'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507,
    'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974,
    'Z': 0.074
}

COMMON_WORDS = [
'THE','BE','TO','OF','AND','A','IN','THAT','HAVE','I','IT','FOR','NOT','ON','WITH','HE','AS','YOU','DO','AT',
'THIS','BUT','HIS','BY','FROM','THEY','WE','SAY','HER','SHE','OR','AN','WILL','MY','ONE','ALL','WOULD','THERE','THEIR','WHAT',
'SO','UP','OUT','IF','ABOUT','WHO','GET','WHICH','GO','ME','WHEN','MAKE','CAN','LIKE','TIME','NO','JUST','HIM','KNOW','TAKE',
'PEOPLE','INTO','YEAR','YOUR','GOOD','SOME','COULD','THEM','SEE','OTHER','THAN','THEN','NOW','LOOK','ONLY','COME','ITS','OVER','THINK','ALSO',
'BACK','AFTER','USE','TWO','HOW','OUR','WORK','FIRST',' WELL','WAY','EVEN','NEW','WANT','BECAUSE','ANY','THESE','GIVE','DAY','MOST','US',
'AM','WAS','ARE','WERE','HAS','HAD','DID','MADE','SAID','MANY','LONG','OWN','DOWN','OFF','GOT','LEFT','RIGHT','EVERY','NEVER',
'MUST','SHALL','SHOULD','MAY','MIGHT','YOUNG','OLD','LARGE','SMALL','LITTLE','BIG','GREAT','HIGH','LOW','EARLY','LATE','ABLE','BETTER','BEST',
'BETWEEN','BELOW','ABOVE','UNDER','AGAIN','AGAINST','AROUND','AFTERNOON','ALMOST','ALREADY','ALONG','ALWAYS','ANYONE','ANYTHING','ANYWHERE','AREA',
'ASK','ANSWER','HELP','TRY','FIND','FEEL','BELIEVE','SEEM','APPEAR','BEGIN','START','STOP','KEEP','HOLD','BRING','CARRY','MOVE','LIVE','DIE',
'EAT','DRINK','SLEEP','READ','WRITE','WATCH','LISTEN','SPEAK','TALK','CALL','PAY','BUY','SELL','SEND','RECEIVE','OPEN','CLOSE','FOLLOW','LEAD',
'RUN','WALK','TURN','CHANGE','CONTINUE','LEARN','STUDY','TEACH','UNDERSTAND','REMEMBER','FORGET','DECIDE','CHOOSE','PROVIDE','CREATE','BUILD','SPEND','WIN','LOSE',
'PLAY','WORK','DRIVE','FLY','TRAVEL','MEET','VISIT','RETURN','STAY','WAIT','HOPE','PLAN','AGREE','OFFER','ORDER','NEED','WISH','LOVE','HATE',
'HAPPY','SAD','ANGRY','TIRED','READY','IMPORTANT','INTERESTING','USEFUL','DIFFERENT','SIMILAR','TRUE','FALSE','REAL','FACT','PROBLEM','ANSWER','QUESTION','IDEA','REASON',
'FAMILY','FRIEND','MAN','WOMAN','CHILD','CHILDREN','STUDENT','TEACHER','MOTHER','FATHER','BROTHER','SISTER','HOUSE','HOME','ROOM','SCHOOL','PLACE','COUNTRY','CITY',
'WORLD','EARTH','WATER','FOOD','AIR','MONEY','JOB','COMPANY','OFFICE','MARKET','STORE','ROAD','CAR','BUS','TRAIN','PHONE','COMPUTER','SYSTEM','PROGRAM',
'NUMBER','NAME','WORD','LINE','FORM','GROUP','PART','END','POINT','LEVEL','POWER','ORDER','LAW','RULE','GOVERNMENT','SERVICE','RESULT','CENTER','REPORT',
'MONTH','WEEK','TODAY','TOMORROW','YESTERDAY','MORNING','NIGHT','HOUR','MINUTE','SECOND','HAND','HEAD','FACE','BODY','EYE','EAR','MOUTH','NOSE','BLOOD',
'LIGHT','DARK','COLOR','RED','BLUE','GREEN','BLACK','WHITE','FULL','EMPTY','HOT','COLD','WARM','DRY','WET','CLEAN','DIRTY','QUIET','LOUD',
'HARD','SOFT','STRONG','WEAK','FAST','SLOW','DEEP','SHALLOW','NEAR','FAR','INSIDE','OUTSIDE','FRONT','BACK','TOP','BOTTOM','NORTH','SOUTH','EAST','WEST',
'MUSIC','MOVIE','BOOK','STORY','GAME','NEWS','HISTORY','SCIENCE','MATH','ART','LANGUAGE','SKILL','HEALTH','MEDICINE','SPORT','ANIMAL','PLANT','TREE','FLOWER',
'RIVER','MOUNTAIN','SEA','OCEAN','ISLAND','FOREST','SPACE','STAR','SUN','MOON','ENERGY','MACHINE','DEVICE','INFORMATION','DATA','MESSAGE','SIGN','NETWORK','INTERNET',
'THINKING','THINKS','THINKED','THINKING','THINKER','THINKERS','THINKABLE','REALITY','REALITIES','REALISTIC','REALISM','REASONING','REASONS','REASONABLE',
'USE','USES','USED','USING','USER','USERS','USEFULNESS','IMPORTANTLY','IMPORTANCE','INTEREST','INTERESTED','INTERESTINGLY','SIMILARITY','SIMILARITIES',
'DIFFERENCE','DIFFERENCES','TRUE','TRULY','FALSELY','FAKE','FAKES','FACTS','PROBLEMS','QUESTIONED','QUESTIONING','ANSWERING','IDEAS','REASONS','REASONABLE',
'WORKS','WORKED','WORKING','WORKER','WORKERS','WORKPLACE','PLAYED','PLAYING','PLAYER','PLAYERS','TRAVELING','TRAVELED','TRAVELER','TRAVELERS','STUDYING','STUDIED',
'STUDIES','LEARNING','LEARNED','LEARNER','LEARNERS','TEACHING','TEACHINGS','TEACHER','TEACHERS','UNDERSTANDING','UNDERSTANDS','FORGETS','FORGOT','FORGOTTEN',
'DECIDES','DECIDED','CHOOSING','CHOSEN','CREATES','CREATED','CREATING','BUILDS','BUILT','BUILDING','BUILDINGS','SPENDS','SPENT','WINNING','LOSING','LOSINGS','WINNER','WINNERS',
'DRIVES','DRIVING','DROVE','DRIVEN','FLIES','FLYING','FLEW','TRAVELS','TRAVELED','TRAVELERS','MEETING','MEETINGS','VISITS','VISITED','VISITING','RETURNS','RETURNED','RETURNING',
'STAYING','WAITS','WAITED','WAITING','HOPES','HOPING','PLANS','PLANNED','AGREES','AGREED','OFFERED','ORDERED','NEEDS','NEEDED','LOVES','LOVING','HATES','HATED',
'HAPPINESS','SADNESS','ANGER','TIREDNESS','READINESS','IMPORTANCE','USEFULNESSES','DIFFERENCES','SIMILARITIES','TRUTH','REALITIES','FACTUAL','PROBLEMSOLVING','ANSWERS','QUESTIONABLE',
'FAMILIES','FRIENDS','WOMEN','MEN','CHILDHOOD','CHILDLIKE','STUDENTS','TEACHINGS','COUNTRIES','CITIES','HOUSES','ROOMS','SCHOOLS','PLACES','WORLDS','EARTHLY','WATERS','FOODS','MONEYS',
'JOBS','COMPANIES','OFFICES','MARKETS','STORES','ROADS','CARS','BUSES','TRAINS','PHONES','COMPUTERS','SYSTEMS','PROGRAMS','NUMBERS','WORDS','LINES','FORMS','GROUPS','POINTS','LEVELS',
'POWERS','ORDERS','LAWS','RULES','SERVICES','RESULTS','CENTERS','REPORTS','MONTHS','WEEKS','MORNINGS','NIGHTS','HOURS','MINUTES','SECONDS','HANDS','HEADS','FACES','BODIES',
'EYES','EARS','MOUTHS','NOSES','BLOODS','LIGHTS','DARKS','COLORS','REDS','BLUES','GREENS','BLACKS','WHITES','HOTTER','COLDEST','WARMER','DRIER','WETTER','CLEANER','DIRTIER','QUIETER',
'LOUDER','HARDEST','SOFTEST','STRONGER','WEAKER','FASTER','SLOWER','DEEPER','NEARER','FARTHER','INSIDES','OUTSIDES','FRONTS','BACKS','TOPS','BOTTOMS','NORTHERN','SOUTHERN','EASTERN','WESTERN',
'MUSICS','MOVIES','BOOKS','STORIES','GAMES','NEWSLETTERS','SCIENCES','MATHEMATICS','ARTS','LANGUAGES','SKILLS','HEALTHY','MEDICAL','SPORTS','ANIMALS','PLANTS','TREES','FLOWERS','RIVERS',
'MOUNTAINS','SEAS','OCEANS','ISLANDS','FORESTS','SPACES','STARS','SUNS','MOONS','ENERGIES','MACHINES','DEVICES','INFORMATIONS','DATAS','MESSAGES','SIGNS','NETWORKS','INTERNETS','KNOWLEDGE',
'COMMUNICATION','COMMUNICATIONS','EDUCATION','EDUCATIONS','EXPERIENCE','EXPERIENCES','TECHNOLOGY','TECHNOLOGIES','NATURE','NATURAL','CULTURE','CULTURAL','COMMUNITY','COMMUNITIES','HISTORY','HISTORIES',
'SCIENCE','SCIENTIFIC','MATHEMATIC','MATHEMATICAL','DISCUSS','DISCUSSION','DISCUSSIONS','AGREEMENT','AGREEMENTS','IMPROVE','IMPROVEMENT','IMPROVEMENTS','GLOBAL','GLOBALIZATION','LOCAL','LOCALIZATION',
'HUMAN','HUMANS','SOCIAL','SOCIALIZE','SOCIETY','SOCIETIES','PROFESSIONAL','PROFESSION','PROFESSIONS','SUCCESS','SUCCESSFUL','SUCCEED','SUCCEEDED','FAIL','FAILURE','FAILED','TRYING','ACHIEVE','ACHIEVEMENT',
'ABILITY','ABILITIES','POSSIBLE','POSSIBILITY','POSSIBILITIES','CHANCE','CHANCES','CHANGEABLE','STRATEGY','STRATEGIES','PROJECT','PROJECTS','PROCESS','PROCESSES','ANALYZE','ANALYZING','ANALYSIS','ANALYTICAL',
'EVIDENCE','EVIDENCES','RESEARCH','RESEARCHER','RESEARCHERS','RESEARCHING','STUDY','STUDIES','DATASET','DATASETS','ALGORITHM','ALGORITHMS','MODEL','MODELS','TRAIN','TRAINING','TEST','TESTING',
'DEVELOP','DEVELOPER','DEVELOPERS','DEVELOPING','PROGRAMMER','PROGRAMMERS','PROGRAMMING','APPLICATION','APPLICATIONS','PLATFORM','PLATFORMS','SYSTEMATIC','SECURITY','CYBER','CYBERSECURITY','ATTACK','ATTACKS',
'DEFENSE','DEFENSIVE','ENCRYPT','ENCRYPTION','DECRYPT','DECRYPTION','CIPHER','CIPHERS','KEY','KEYS','HASH','HASHING','PASSWORD','PASSWORDS','BREACH','BREACHES','THREAT','THREATS',
'FORENSIC','FORENSICS','DIGITAL','INVESTIGATION','INVESTIGATIONS','EVIDENCES','LOG','LOGS','METADATA','SIGNATURE','SIGNATURES','ANOMALY','ANOMALIES','PATTERN','PATTERNS','BEHAVIOR','BEHAVIORS','ACCESS','PERMISSION',
'CONTROL','CONTROLLED','ADMIN','ADMINISTRATION','POLICY','POLICIES','PROTOCOL','PROTOCOLS','FIREWALL','FIREWALLS','NETWORKING','PACKET','PACKETS','MONITOR','MONITORING','ANALYZE','INSPECT','DETECT','DETECTION',
'ALERT','ALERTS','REPORTING','INCIDENT','INCIDENTS','RESPONSE','RESPONSES','RECOVERY','RECOVER','RECOVERED','PATCH','PATCHES','UPDATE','UPDATES','VERSION','VERSIONS','SERVER','SERVERS',
'CLIENT','CLIENTS','BROWSER','BROWSERS','REQUEST','REQUESTS','RESPONSE','RESPONSES','DATABASE','DATABASES','QUERY','QUERIES','SCRIPT','SCRIPTS','EXECUTE','EXECUTION','VULNERABILITY','VULNERABILITIES','EXPLOIT','EXPLOITS'
]


# Xử lý 

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_list(numbers):
    if not numbers:
        return 1
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

def get_factors(n, max_factor=30):
    factors = []
    for i in range(2, min(n + 1, max_factor + 1)):
        if n % i == 0:
            factors.append(i)
    return factors

# Kasiski

def find_repeated_sequences(ciphertext, min_length=3):

    text = ''.join(c for c in ciphertext.upper() if c.isalpha())
    repeated = {}

    for length in range(min(len(text) // 2, 20), min_length - 1, -1):
        seen = {}
        for i in range(len(text) - length + 1):
            seq = text[i:i + length]
            if seq in seen:
                repeated.setdefault(seq, set()).add(seen[seq])
                repeated[seq].add(i)
            else:
                seen[seq] = i

    result = {
        seq: sorted(pos)
        for seq, pos in repeated.items()
        if len(pos) >= 2
    }
    return result

# chi bình phương
def chi_squared_test(text, freq_expected):
    text = ''.join(c for c in text.upper() if c.isalpha())
    total = len(text)
    if total == 0:
        return float('inf')
    freq_obs = Counter(text)
    chi = 0.0
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        observed = freq_obs.get(letter, 0)
        expected = (freq_expected[letter] / 100.0) * total
        if expected > 0:
            chi += (observed - expected) ** 2 / expected
    return chi

def decrypt_caesar(ciphertext, shift):
    out = []
    for c in ciphertext.upper():
        if c.isalpha():
            base = ord('A')
            out.append(chr((ord(c) - base - shift) % 26 + base))
        else:
            out.append(c)
    return ''.join(out)

def count_common_words(text):
    text = text.upper()
    words = ''.join(c if c.isalpha() or c.isspace() else ' ' for c in text).split()
    return sum(1 for w in words if w in COMMON_WORDS)

def list_common_words_in_text(text):
    text = text.upper()
    words = ''.join(c if c.isalpha() or c.isspace() else ' ' for c in text).split()
    return sorted({w for w in words if w in COMMON_WORDS})

#full giải mã

def decrypt_full(ciphertext, key):
    key = key.upper()
    result = []
    idx = 0

    for ch in ciphertext:
        if ch.isalpha():
            shift = ord(key[idx % len(key)]) - ord('A')

            if ch.isupper():
                base = ord('A')
                dec = chr((ord(ch) - base - shift) % 26 + base)
            else:
                base = ord('a')
                dec = chr((ord(ch) - base - shift) % 26 + base)

            result.append(dec)
            idx += 1
        else:
            result.append(ch)

    return ''.join(result)


# Phân tích với độ dài khóa cho trước

def analyze_key_length(ciphertext, key_length):
    text = ''.join(c for c in ciphertext.upper() if c.isalpha())
    columns = [''] * key_length
    for i, ch in enumerate(text):
        columns[i % key_length] += ch

    key_chars = []
    column_results = []

    for col_idx, col in enumerate(columns):
        best_shift = 0
        best_chi = float('inf')
        all_shifts = []
        for shift in range(26):
            dec = decrypt_caesar(col, shift)
            chi = chi_squared_test(dec, FREQ_ENGLISH)
            all_shifts.append({
                "shift": shift,
                "letter": chr(shift + ord('A')),
                "chi": chi,
                "preview": dec[:50]
            })
            if chi < best_chi:
                best_chi = chi
                best_shift = shift

        key_char = chr(best_shift + ord('A'))
        key_chars.append(key_char)
        column_results.append({
            "column_index": col_idx,
            "best_shift": best_shift,
            "best_letter": key_char,
            "best_chi": best_chi,
            "all_shifts": all_shifts
        })

    key = ''.join(key_chars)
    plaintext = decrypt_full(ciphertext, key)

    letters_only = ''.join(c for c in plaintext.upper() if c.isalpha())
    chi_total = chi_squared_test(letters_only, FREQ_ENGLISH)
    cw_count = count_common_words(plaintext)
    cw_list = list_common_words_in_text(plaintext)

    score = (1 / (chi_total + 1)) * 100 + cw_count * 5

    return {
        "key_length": key_length,
        "key": key,
        "plaintext": plaintext,
        "chi_squared": chi_total,
        "common_words": cw_count,
        "common_words_list": cw_list,
        "score": score,
        "column_results": column_results,
    }

# Kasiski

def kasiski_analysis(ciphertext, min_seq_length=3):

    seqs = find_repeated_sequences(ciphertext, min_length=min_seq_length)

    if not seqs:
        return None, []

    all_distances = []
    sequence_info = []

    sorted_seqs = sorted(seqs.items(), key=lambda x: (-len(x[0]), -len(x[1])))

    for seq, positions in sorted_seqs:
        distances = []
        for i in range(len(positions) - 1):
            dist = positions[i + 1] - positions[i]
            distances.append(dist)
            all_distances.append(dist)

        factors = set()
        for d in distances:
            factors.update(get_factors(d))

        sequence_info.append({
            "sequence": seq,
            "length": len(seq),
            "positions": positions,
            "count": len(positions),
            "distances": distances,
            "factors": sorted(factors),
        })

    likely_lengths = []
    if all_distances:
        factor_count = Counter()
        for d in all_distances:
            for f in get_factors(d):
                factor_count[f] += 1
        likely_lengths = [f for f, _ in factor_count.most_common(15)]

    if not likely_lengths:
        likely_lengths = list(range(1, 11))  

    return sequence_info, likely_lengths

# trình bày

def build_summary_report(text_only, sequence_info, all_results):
    best = all_results[0]

    report = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   🌟 KẾT QUẢ PHÂN TÍCH VIGENÈRE (KASISKI + χ²) 🌟
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 THÔNG TIN CƠ BẢN:
   • Tổng số ký tự (A-Z): {len(text_only)}
   • Số chuỗi lặp Kasiski: {len(sequence_info)}

📝 CHUỖI LẶP LẠI (tối đa 10):
"""
    for idx, info in enumerate(sequence_info[:10], 1):
        report += f"\n   {idx}. '{info['sequence']}' (dài {info['length']})\n"
        report += f"      • Vị trí xuất hiện: {info['positions']}\n"
        report += f"      • Khoảng cách: {info['distances']}\n"
        report += f"      • Ước số (cho từng khoảng cách): {info['factors']}\n"

    all_distances = []
    for info in sequence_info:
        all_distances.extend(info["distances"])

    if all_distances:
        common_gcd = gcd_list(all_distances)
        factor_count = Counter()
        for d in all_distances:
            for f in get_factors(d):
                factor_count[f] += 1

        report += "\n📐 PHÂN TÍCH KHOẢNG CÁCH:\n"
        report += f"   • Tổng số khoảng cách: {len(all_distances)}\n"
        report += f"   • GCD (ước chung lớn nhất): {common_gcd}\n"
        report += f"   • Các ước xuất hiện nhiều nhất:\n"
        for f, c in factor_count.most_common(10):
            pct = c / len(all_distances) * 100
            report += f"      {f:2d}: {c:2d}/{len(all_distances)} lần ({pct:5.1f}%)\n"

    report += "\n🎯 KẾT QUẢ TỐT NHẤT (THEO ĐIỂM):\n"
    report += f"   ✨ Độ dài khóa: {best['key_length']}\n"
    report += f"   🔑 Khóa: {best['key']}\n"
    report += f"   📊 Chi-square (χ²): {best['chi_squared']:.2f}\n"
    report += f"   📚 Số từ phổ biến tìm thấy: {best['common_words']}\n"

    if best["common_words_list"]:
        report += "   🔤 Một số từ phổ biến: "
        report += ", ".join(best["common_words_list"][:15]) + "\n"

    report += f"   ⭐ Điểm tổng hợp: {best['score']:.2f}\n"

    report += "\n📋 CÁC ĐỘ DÀI KHÓA KHÁC:\n"
    for idx, r in enumerate(all_results[1:6], 2):
        report += (
            f"   {idx}. Len={r['key_length']:2d}, Key='{r['key']}' "
            f"(χ²={r['chi_squared']:.1f}, CW={r['common_words']}, Score={r['score']:.1f})\n"
        )

    return report

#Hàm xử lý khi gọi đến
def run_analysis_for_gui(input_text3, output_text3_analysis, output_text3_decrypted, use_ic=True, min_seq=3):

    ciphertext = input_text3.get("1.0", "end-1c")

    if not ciphertext.strip():
        output_text3_analysis.delete("1.0", "end")
        output_text3_analysis.insert("1.0z", "⚠️ Vui lòng nhập ciphertext trước khi phân tích.")
        output_text3_decrypted.delete("1.0", "end")
        return None, None, None, None

    text_only = ''.join(c for c in ciphertext.upper() if c.isalpha())

    sequence_info, likely_lengths = kasiski_analysis(ciphertext, min_seq_length=min_seq)
    if not sequence_info:
        output_text3_analysis.delete("1.0", "end")
        output_text3_analysis.insert(
            "1.0",
            "❌ Không tìm thấy chuỗi lặp Kasiski.\n"
            "Văn bản có thể quá ngắn hoặc không phải Vigenère."
        )
        output_text3_decrypted.delete("1.0", "end")
        return None, None, None, None

    all_results = []
    for length in likely_lengths[:10]:
        if length <= 0:
            continue
        res = analyze_key_length(ciphertext, length)
        all_results.append(res)

    if not all_results:
        for length in [1, 2, 3]:
            res = analyze_key_length(ciphertext, length)
            all_results.append(res)

    all_results.sort(key=lambda r: r["score"], reverse=True)
    best = all_results[0]

    report = build_summary_report(text_only, sequence_info, all_results)

    output_text3_analysis.delete("1.0", "end")
    output_text3_analysis.insert("1.0", report)

    output_text3_decrypted.delete("1.0", "end")
    output_text3_decrypted.insert("1.0", best["plaintext"])

    return report, best["plaintext"], best["key"], all_results


def open_detailed_analysis_window(parent, all_results):
    """
    Cửa sổ chi tiết:
    - Mỗi tab = 1 độ dài khóa
    - Khóa = 1: bảng Caesar 26 dòng
    - Khóa >= 2: ma trận χ² (Treeview, 26 cột A-Z)
    - Dùng Treeview cho nhẹ, highlight best = cả dòng bằng màu mint.
    """
    if not all_results:
        return

    win = ctk.CTkToplevel(parent)
    win.title("📈 Phân tích chi tiết Vigenère")
    win.geometry("1280x800")

    tabview = ctk.CTkTabview(win)
    tabview.pack(fill="both", expand=True, padx=10, pady=10)

    # Style chung cho Treeview
    style = ttk.Style(win)
    style.configure(
        "Caesar.Treeview",
        font=(BASE_FONT_FAMILY, CAESAR_FONT_SIZE),
        rowheight=CAESAR_FONT_SIZE + 8
    )
    style.configure(
        "Caesar.Treeview.Heading",
        font=(BASE_FONT_FAMILY, CAESAR_FONT_SIZE, "bold")
    )
    style.configure(
        "Matrix.Treeview",
        font=(BASE_FONT_FAMILY, MATRIX_FONT_SIZE),
        rowheight=MATRIX_FONT_SIZE + 8
    )
    style.configure(
        "Matrix.Treeview.Heading",
        font=(BASE_FONT_FAMILY, MATRIX_FONT_SIZE, "bold")
    )

    def make_scrollable_table(parent_frame):
        """Tạo khung chứa Treeview + scrollbar dọc/ngang."""
        container = tk.Frame(parent_frame)
        container.pack(fill="both", expand=True, padx=5, pady=5)

        tree = ttk.Treeview(container)
        vsb = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(container, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        return tree

    for res in all_results:
        key_len = res["key_length"]
        tab_name = f"Len = {key_len}"
        tabview.add(tab_name)
        tab = tabview.tab(tab_name)

        main_frame = ctk.CTkFrame(tab)
        main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # HEADER
        header = ctk.CTkLabel(
            main_frame,
            text=f"Độ dài khóa: {key_len}   |   Khóa đề xuất: {res['key']}",
            font=(BASE_FONT_FAMILY, HEADER_FONT_SIZE, "bold")
        )
        header.pack(anchor="w", padx=10, pady=(8, 4))

        # SUMMARY (ĐÃ BỎ IC)
        cw_preview = ", ".join(res["common_words_list"][:15]) if res["common_words_list"] else "(không tìm thấy)"
        overview_text = (
            f"📊 THÔNG TIN TỔNG QUAN:\n"
            f"• Chi-square (χ²): {res['chi_squared']:.2f}\n"
            f"• Số từ phổ biến tìm thấy: {res['common_words']}\n"
            f"• Một số từ phổ biến: {cw_preview}\n"
            f"• Điểm tổng hợp: {res['score']:.2f}\n"
        )
        overview_label = ctk.CTkLabel(
            main_frame,
            text=overview_text,
            font=(BASE_FONT_FAMILY, SUMMARY_FONT_SIZE),
            justify="left"
        )
        overview_label.pack(anchor="w", padx=10, pady=(4, 8))

        # ===== BẢNG CHI TIẾT =====
        if key_len == 1:
            # ===== BẢNG CAESAR =====
            caesar_frame = ctk.CTkFrame(main_frame)
            caesar_frame.pack(fill="both", expand=True, padx=10, pady=(5, 10))

            title = ctk.CTkLabel(
                caesar_frame,
                text="📋 Bảng 26 khả năng dịch (Caesar):",
                font=(BASE_FONT_FAMILY, SUMMARY_FONT_SIZE, "bold")
            )
            title.pack(anchor="w", padx=5, pady=(5, 3))

            tree = make_scrollable_table(caesar_frame)
            tree.configure(
                columns=("shift", "key", "chi", "preview"),
                show="headings",
                style="Caesar.Treeview"
            )

            tree.heading("shift", text="Shift")
            tree.heading("key", text="Key")
            tree.heading("chi", text="χ²")
            tree.heading("preview", text="Preview")

            tree.column("shift", width=60, anchor="center")
            tree.column("key", width=60, anchor="center")
            tree.column("chi", width=80, anchor="center")
            tree.column("preview", width=800, anchor="w")

            # Tag best row = nền mint
            tree.tag_configure("best", background=BEST_HIGHLIGHT_COLOR)

            col_res = res["column_results"][0]
            for s_info in col_res["all_shifts"]:
                shift = s_info["shift"]
                letter = s_info["letter"]
                chi = s_info["chi"]
                preview = s_info["preview"]
                tags = ()
                if shift == col_res["best_shift"]:
                    tags = ("best",)
                tree.insert(
                    "",
                    "end",
                    values=(shift, letter, f"{chi:.2f}", preview),
                    tags=tags
                )

        else:
            # ===== MA TRẬN χ² =====
            matrix_outer = ctk.CTkFrame(main_frame)
            matrix_outer.pack(fill="both", expand=True, padx=10, pady=(5, 10))

            ctk.CTkLabel(
                matrix_outer,
                text="🔢 Ma trận chi-square (χ²) cho từng vị trí khóa:",
                font=(BASE_FONT_FAMILY, SUMMARY_FONT_SIZE, "bold")
            ).pack(anchor="w", padx=5, pady=(5, 3))

            tree = make_scrollable_table(matrix_outer)
            letters = [chr(ord('A') + i) for i in range(26)]
            columns = ["pos"] + letters

            tree.configure(
                columns=columns,
                show="headings",
                style="Matrix.Treeview"
            )

            tree.heading("pos", text="Vị trí")
            tree.column("pos", width=70, anchor="center")

            for ch in letters:
                tree.heading(ch, text=ch)
                tree.column(ch, width=60, anchor="center")

            # Tag cho row highlight (chứa best shift)
            tree.tag_configure("rowbest", background=BEST_HIGHLIGHT_COLOR)

            for col_res in res["column_results"]:
                row_vals = []
                row_vals.append(f"K[{col_res['column_index']}]")

                chi_values = {s["shift"]: s["chi"] for s in col_res["all_shifts"]}
                best_chi = col_res["best_chi"]

                for shift in range(26):
                    chi = chi_values.get(shift, None)
                    if chi is None:
                        row_vals.append("")
                    else:
                        mark = "*" if abs(chi - best_chi) < 1e-9 else ""
                        row_vals.append(f"{chi:.1f}{mark}")

                tree.insert("", "end", values=row_vals)

        # ===== PLAIN TEXT =====
        dec_label = ctk.CTkLabel(
            main_frame,
            text="📄 Văn bản giải mã với độ dài khóa hiện tại:",
            font=(BASE_FONT_FAMILY, SUMMARY_FONT_SIZE, "bold")
        )
        dec_label.pack(anchor="w", padx=10, pady=(10, 3))

        dec_box = ctk.CTkTextbox(
            main_frame,
            height=200,
            font=(BASE_FONT_FAMILY, PLAINTEXT_FONT_SIZE),
            wrap="word"
        )
        dec_box.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        dec_box.insert("1.0", res["plaintext"])
        dec_box.configure(state="disabled")

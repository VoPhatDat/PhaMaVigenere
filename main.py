import customtkinter as ctk
import tkinter as tk

from module.Vigenere import encrypt_vigenere, decrypt_vigenere
from module.PhanTichTanSuatVigenere import (
    run_analysis_for_gui,
    open_detailed_analysis_window,
)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

FONT_FAMILY = "Segoe UI"
FONT_SMALL  = (FONT_FAMILY, 13)
FONT_NORMAL = (FONT_FAMILY, 15)
FONT_LARGE  = (FONT_FAMILY, 17)
FONT_TITLE  = (FONT_FAMILY, 20, "bold")

TEXTBOX_IN            = 200
TEXTBOX_OUT           = 200
TEXTBOX_OUT3_ANALYSIS = 170
TEXTBOX_OUT3_DECRYPT  = 200

_last_all_results = None
_last_key = None

def run_analysis_and_store(input_text3, output_text3_analysis, output_text3_decrypted, btn_detail, root, min_seq_length):
    global _last_all_results, _last_key
    try:
        report, plain, key, all_results = run_analysis_for_gui(
            input_text3,
            output_text3_analysis,
            output_text3_decrypted,
            use_ic=True,
            min_seq=min_seq_length
        )
        _last_all_results = all_results
        _last_key = key

        if all_results and key:
            btn_detail.configure(state="normal")
        else:
            btn_detail.configure(state="disabled")
    except Exception as e:
        output_text3_analysis.delete("1.0", "end")
        output_text3_analysis.insert("1.0", f"Lỗi: {e}")
        btn_detail.configure(state="disabled")

def build_gui():
    app = ctk.CTk()
    app.title("Công cụ Vigenère – Mã hóa & Phân tích")
    app.geometry("1150x850")
    app.minsize(1000, 750)

    tabview = ctk.CTkTabview(app)
    tabview.pack(padx=12, pady=12, fill="both", expand=True)

    tabview.add("Mã hóa")
    tabview.add("Giải mã (có khóa)")
    tabview.add("Giải mã (phân tích)")

    # ================= TAB 1: MÃ HÓA =================
    tab1 = tabview.tab("Mã hóa")

    frame1 = ctk.CTkFrame(tab1, fg_color="transparent")
    frame1.pack(fill="x", padx=15, pady=15)

    title1 = ctk.CTkLabel(frame1, text="🔒 Mã hóa Vigenère", font=FONT_TITLE)
    title1.pack(pady=(0, 15))

    label1 = ctk.CTkLabel(frame1, text="Văn bản gốc (Plaintext):", font=FONT_LARGE)
    label1.pack(anchor="w", pady=(0, 5))

    input_text1 = ctk.CTkTextbox(frame1, height=TEXTBOX_IN, font=FONT_NORMAL, corner_radius=6)
    input_text1.pack(fill="x", pady=(0, 12))

    key_frame1 = ctk.CTkFrame(frame1, fg_color="transparent")
    key_frame1.pack(fill="x", pady=(0, 8))

    label_key1 = ctk.CTkLabel(key_frame1, text="Khóa (Key):", font=FONT_LARGE, width=100)
    label_key1.pack(side="left", padx=(0, 10))

    key_entry1 = ctk.CTkEntry(key_frame1, font=FONT_LARGE, corner_radius=6)
    key_entry1.pack(side="left", fill="x", expand=True)

    btn_frame1 = ctk.CTkFrame(frame1, fg_color="transparent")
    btn_frame1.pack(pady=(10, 5))

    output_text1 = ctk.CTkTextbox(tab1, height=TEXTBOX_OUT, font=FONT_NORMAL, corner_radius=6)

    def run_encrypt():
        try:
            plaintext = input_text1.get("1.0", "end-1c")
            key = key_entry1.get()
            if not key:
                output_text1.delete("1.0", "end")
                output_text1.insert("1.0", "⚠️ Vui lòng nhập khóa!")
                return
            result = encrypt_vigenere(plaintext, key)
            output_text1.delete("1.0", "end")
            output_text1.insert("1.0", result)
        except Exception as e:
            output_text1.delete("1.0", "end")
            output_text1.insert("1.0", f"Lỗi: {e}")

    def clear_tab1():
        input_text1.delete("1.0", "end")
        key_entry1.delete(0, "end")
        output_text1.delete("1.0", "end")

    ctk.CTkButton(
        btn_frame1, text="Mã hóa", width=150, font=FONT_LARGE,
        command=run_encrypt
    ).pack(side="left", padx=8)

    ctk.CTkButton(
        btn_frame1, text="Xóa", width=120, font=FONT_LARGE,
        fg_color="#D32F2F", hover_color="#B71C1C",
        command=clear_tab1
    ).pack(side="left", padx=8)

    label_result1 = ctk.CTkLabel(tab1, text="Kết quả (Ciphertext):", font=FONT_LARGE, padx=15)
    label_result1.pack(anchor="w", pady=(4, 5))

    output_text1.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    # ================= TAB 2: GIẢI MÃ (CÓ KHÓA) =================
    tab2 = tabview.tab("Giải mã (có khóa)")

    frame2 = ctk.CTkFrame(tab2, fg_color="transparent")
    frame2.pack(fill="x", padx=15, pady=15)

    title2 = ctk.CTkLabel(frame2, text="🔓 Giải mã Vigenère (biết khóa)", font=FONT_TITLE)
    title2.pack(pady=(0, 15))

    label2 = ctk.CTkLabel(frame2, text="Văn bản mã hóa (Ciphertext):", font=FONT_LARGE)
    label2.pack(anchor="w", pady=(0, 5))

    input_text2 = ctk.CTkTextbox(frame2, height=TEXTBOX_IN, font=FONT_NORMAL, corner_radius=6)
    input_text2.pack(fill="x", pady=(0, 12))

    key_frame2 = ctk.CTkFrame(frame2, fg_color="transparent")
    key_frame2.pack(fill="x", pady=(0, 8))

    label_key2 = ctk.CTkLabel(key_frame2, text="Khóa (Key):", font=FONT_LARGE, width=100)
    label_key2.pack(side="left", padx=(0, 10))

    key_entry2 = ctk.CTkEntry(key_frame2, font=FONT_LARGE, corner_radius=6)
    key_entry2.pack(side="left", fill="x", expand=True)

    btn_frame2 = ctk.CTkFrame(frame2, fg_color="transparent")
    btn_frame2.pack(pady=(10, 5))

    output_text2 = ctk.CTkTextbox(tab2, height=TEXTBOX_OUT, font=FONT_NORMAL, corner_radius=6)

    def run_decrypt():
        try:
            ciphertext = input_text2.get("1.0", "end-1c")
            key = key_entry2.get()
            if not key:
                output_text2.delete("1.0", "end")
                output_text2.insert("1.0", "⚠️ Vui lòng nhập khóa!")
                return
            result = decrypt_vigenere(ciphertext, key)
            output_text2.delete("1.0", "end")
            output_text2.insert("1.0", result)
        except Exception as e:
            output_text2.delete("1.0", "end")
            output_text2.insert("1.0", f"Lỗi: {e}")

    def clear_tab2():
        input_text2.delete("1.0", "end")
        key_entry2.delete(0, "end")
        output_text2.delete("1.0", "end")

    ctk.CTkButton(
        btn_frame2, text="Giải mã", width=150, font=FONT_LARGE,
        command=run_decrypt
    ).pack(side="left", padx=8)

    ctk.CTkButton(
        btn_frame2, text="Xóa", width=120, font=FONT_LARGE,
        fg_color="#D32F2F", hover_color="#B71C1C",
        command=clear_tab2
    ).pack(side="left", padx=8)

    label_result2 = ctk.CTkLabel(tab2, text="Kết quả (Plaintext):", font=FONT_LARGE, padx=15)
    label_result2.pack(anchor="w", pady=(4, 5))

    output_text2.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    # ================= TAB 3: GIẢI MÃ (PHÂN TÍCH) =================
    tab3 = tabview.tab("Giải mã (phân tích)")

    frame3 = ctk.CTkFrame(tab3, fg_color="transparent")
    frame3.pack(fill="x", padx=15, pady=15)

    title3 = ctk.CTkLabel(frame3, text="Giải mã Vigenère bằng phân tích tần suất", font=FONT_TITLE)
    title3.pack(pady=(0, 10))

    desc3 = ctk.CTkLabel(
        frame3,
        text="Kasiski + Chi-square (χ²) + Common Words",
        font=FONT_SMALL,
        text_color="#555"
    )
    desc3.pack(pady=(0, 10))

    label3 = ctk.CTkLabel(frame3, text="Văn bản mã hóa (Ciphertext):", font=FONT_LARGE)
    label3.pack(anchor="w", pady=(0, 5))

    # Input min sequence length
    min_seq_frame = ctk.CTkFrame(frame3, fg_color="transparent")
    min_seq_frame.pack(fill="x", pady=(0, 8))

    label_min_seq = ctk.CTkLabel(min_seq_frame, text="Độ dài chuỗi lặp tối thiểu:", font=FONT_LARGE, width=230)
    label_min_seq.pack(side="left", padx=(0, 10))

    entry_min_seq = ctk.CTkEntry(min_seq_frame, font=FONT_LARGE, corner_radius=6, width=80)
    entry_min_seq.insert(0, "3")  # default=3
    entry_min_seq.pack(side="left")


    input_text3 = ctk.CTkTextbox(frame3, height=TEXTBOX_IN, font=FONT_NORMAL, corner_radius=6)
    input_text3.pack(fill="x", pady=(0, 12))

    btn_frame3 = ctk.CTkFrame(frame3, fg_color="transparent")
    btn_frame3.pack(pady=(0, 10))

    output_text3_analysis = ctk.CTkTextbox(
        tab3,
        height=TEXTBOX_OUT3_ANALYSIS,
        font=FONT_NORMAL,
        corner_radius=6
    )
    output_text3_decrypted = ctk.CTkTextbox(
        tab3,
        height=TEXTBOX_OUT3_DECRYPT,
        font=FONT_NORMAL,
        corner_radius=6
    )

    btn_view_detail = ctk.CTkButton(
        btn_frame3,
        text="📈 Xem chi tiết",
        width=180,
        font=FONT_LARGE,
        state="disabled"
    )

    def on_run_analysis():
        try:
            min_seq = int(entry_min_seq.get())
            if min_seq < 2:
                min_seq = 2
            run_analysis_and_store(input_text3, output_text3_analysis, output_text3_decrypted, btn_view_detail, app, min_seq)
        except:
            run_analysis_and_store(input_text3, output_text3_analysis, output_text3_decrypted, btn_view_detail, app, 3)

    def on_view_detail():
        global _last_all_results
        if _last_all_results:
            open_detailed_analysis_window(app, _last_all_results)

    def clear_tab3():
        global _last_all_results, _last_key
        input_text3.delete("1.0", "end")
        output_text3_analysis.delete("1.0", "end")
        output_text3_decrypted.delete("1.0", "end")
        _last_all_results = None
        _last_key = None
        btn_view_detail.configure(state="disabled")

    btn_run_analysis = ctk.CTkButton(
        btn_frame3,
        text="📊 Phân tích & Giải mã",
        width=230,
        font=FONT_LARGE,
        fg_color="#1976D2",
        hover_color="#115293",
        command=on_run_analysis
    )
    btn_run_analysis.pack(side="left", padx=8)

    btn_view_detail.configure(command=on_view_detail)
    btn_view_detail.pack(side="left", padx=8)

    ctk.CTkButton(
        btn_frame3,
        text="Xóa",
        width=120,
        font=FONT_LARGE,
        fg_color="#D32F2F",
        hover_color="#B71C1C",
        command=clear_tab3
    ).pack(side="left", padx=8)

    label_analysis = ctk.CTkLabel(
        tab3,
        text="Kết quả phân tích (Kasiski + χ²):",
        font=FONT_LARGE,
        padx=15
    )
    label_analysis.pack(anchor="w", pady=(0, 5))

    output_text3_analysis.pack(fill="both", expand=True, padx=15, pady=(0, 10))

    label_decrypt = ctk.CTkLabel(
        tab3,
        text="Văn bản giải mã (dự đoán tốt nhất):",
        font=FONT_LARGE,
        padx=15
    )
    label_decrypt.pack(anchor="w", pady=(0, 5))

    output_text3_decrypted.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    app.mainloop()

if __name__ == "__main__":
    build_gui()

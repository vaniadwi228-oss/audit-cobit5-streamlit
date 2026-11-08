import streamlit as st
import pandas as pd

st.set_page_config(page_title="Audit Sistem Informasi COBIT 5 - CV Tjahyono Abadi", page_icon="📊", layout="wide")

st.title("Form Audit Sistem Informasi COBIT 5")
st.subheader("CV Tjahyono Abadi")
st.markdown("Audit sistem informasi distribusi barang menggunakan kerangka kerja COBIT 5.")
st.info("Aplikasi prototipe untuk pembelajaran. Hasil pengisian bukan hasil audit resmi perusahaan.")

# Identitas Auditor
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    nama_auditor = st.text_input("Nama Auditor", value="Vania Dwi Rahmawati")
    nim_auditor = st.text_input("NIM", value="202453141")
with col2:
    nama_responden = st.text_input("Nama Responden / Perusahaan", value="")
    tanggal_audit = st.date_input("Tanggal Audit")

# Data Lengkap Sesuai Dokumen Asli
domains = {
    "EDM (Evaluate, Direct and Monitor)": [
        ("EDM01", "Apakah perusahaan memiliki pembagian tanggung jawab yang jelas dalam pengambilan keputusan terkait penggunaan sistem informasi distribusi barang?"),
        ("EDM01", "Apakah terdapat kebijakan atau arahan dari pemimpinan mengenai penggunaan sistem informasi dalam kegiatan distribusi barang?"),
        ("EDM02", "Apakah penggunaan sistem informasi dievaluasi berdasarkan manfaatnya terhadap kegiatan distribusi barang?"),
        ("EDM03", "Apakah risiko yang dapat mengganggu kegiatan distribusi berbasis sistem informasi diperhatikan oleh pihak yang bertanggung jawab?"),
        ("EDM04", "Apakah perusahaan melakukan pengawasan terhadap penggunaan sumber daya yang mendukung sistem informasi distribusi barang?"),
        ("EDM05", "Apakah pimpinan menerima informasi atau laporan yang relevan untuk memantau pelaksanaan sistem informasi distribusi barang?"),
    ],
    "APO (Align, Plan and Organize)": [
        ("APO01", "Apakah terdapat pembagian tugas dan tanggung jawab yang jelas bagi pengguna sistem informasi distribusi barang?"),
        ("APO02", "Apakah perencanaan penggunaan sistem informasi telah mempertimbangkan kebutuhan proses distribusi barang?"),
        ("APO06", "Apakah biaya yang berkaitan dengan penggunaan dan pemeliharaan sistem informasi dikelola atau dicatat dengan baik?"),
        ("APO07", "Apakah penggunaan sistem informasi memperoleh pengarahan atau pelatihan yang sesuai dengan tugasnya?"),
        ("APO12", "Apakah perusahaan mengidentifikasi risiko yang berkaitan dengan penggunaan sistem informasi distribusi barang?"),
        ("APO13", "Apakah terdapat kebijakan atau prosedur untuk menjaga keamanan informasi yang digunakan dalam kegiatan distribusi barang?"),
    ],
    "BAI (Build, Acquire and Implement)": [
        ("BAI02", "Apakah kebutuhan pengguna terkait pencatatan dan pemantauan distribusi barang telah diidentifikasi sebelum sistem diterapkan atau dikembangkan?"),
        ("BAI03", "Apakah sistem informasi yang digunakan mendukung kebutuhan pencatatan dan pengelolaan data distribusi barang?"),
        ("BAI05", "Apakah pengguna memperoleh informasi atau pelatihan ketika terdapat penerapan sistem baru atau perubahan sistem?"),
        ("BAI06", "Apakah perubahan pada sistem informasi dilakukan melalui proses persetujuan dan pencatatan yang jelas?"),
        ("BAI07", "Apakah pengujian dilakukan sebelum perubahan sistem diterapkan pada kegiatan operasional?"),
        ("BAI10", "Apakah dokumentasi konfigurasi atau komponen sistem informasi dipelihara apabila diperlukan untuk pengelolaan dan pemeliharaan sistem?"),
    ],
    "DSS (Deliver, Service and Support)": [
        ("DSS01", "Apakah pencatatan barang masuk, barang keluar, dan transaksi distribusi dilakukan sesuai prosedur yang ditetapkan?"),
        ("DSS01", "Apakah gangguan atau kendala penggunaan sistem informasi dicatat dan ditangani oleh pihak yang bertanggung jawab?"),
        ("DSS02", "Apakah masalah sistem yang berulang dianalisis untuk mengetahui penyebabnya?"),
        ("DSS03", "Apakah permasalahan sistem yang terjadi berulang kali diidentifikasi untuk dicari penyebabnya?"),
        ("DSS04", "Apakah perusahaan memiliki prosedur pencadangan data dan langkah pemulihan apabila data atau sistem mengalami gangguan?"),
        ("DSS05", "Apakah akses terhadap sistem informasi dan data distribusi dibatasi berdasarkan kewenangan masing-masing pengguna?"),
    ],
    "MEA (Monitor, Evaluate and Assess)": [
        ("MEA01", "Apakah kinerja sistem informasi distribusi barang dipantau secara berkala oleh pihak yang bertanggung jawab?"),
        ("MEA01", "Apakah terdapat laporan atau catatan yang digunakan untuk memantau kegiatan distribusi barang?"),
        ("MEA02", "Apakah pengendalian internal terhadap pencatatan dan pengelolaan data distribusi barang dievaluasi secara berkala?"),
        ("MEA02", "Apakah perusahaan melakukan pemeriksaan atau rekonsiliasi untuk mengetahui kesesuaian catatan persediaan dengan bukti pendukung yang tersedia?"),
        ("MEA03", "Apakah pengelolaan sistem informasi memperhatikan kebijakan internal dan ketentuan yang relevan dengan kegiatan perusahaan?"),
        ("MEA02", "Apakah kelemahan pengendalian yang ditemukan dicatat dan ditindaklanjuti oleh pihak yang bertanggung jawab?"),
    ]
}

st.markdown("---")
summary_data = []

for domain_name, questions in domains.items():
    st.subheader(f"Domain: {domain_name}")
    ya, tdk, na = 0, 0, 0
    for idx, (kode, q_text) in enumerate(questions, 1):
        col_q, col_opt, col_note = st.columns([3, 2, 2])
        with col_q:
            st.markdown(f"**{idx}. [{kode}]** {q_text}")
        with col_opt:
            jawab = st.radio(f"Pilihan_{domain_name}_{idx}", ["Ya", "Tidak", "N/A"], horizontal=True, key=f"r_{domain_name}_{idx}")
        with col_note:
            st.text_input(f"Catatan_{domain_name}_{idx}", placeholder="Catatan Auditor", key=f"c_{domain_name}_{idx}")
        
        if jawab == "Ya": ya += 1
        elif jawab == "Tidak": tdk += 1
        else: na += 1
        
    summary_data.append({"Domain COBIT 5": domain_name.split()[0], "Jumlah Pertanyaan": len(questions), "Ya": ya, "Tidak": tdk, "N/A": na})
    st.markdown("---")

st.header("Rekapitulasi Penilaian")
st.table(pd.DataFrame(summary_data))
st.success("Aplikasi lengkap sesuai dokumen tugas berhasil dimuat!")

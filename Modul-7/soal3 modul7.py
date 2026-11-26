undangan = set()
webinar_A = set()
webinar_B = set()

print("\nDaftar Undangan")
undangan = set(input("Masukkan nama undangan : ").split(","))

print("\nPeserta Webinar A")
webinar_A = set(input("Masukkan peserta webinar A : ").split(","))

print("\nPeserta Webinar B")
webinar_B = set(input("Masukkan peserta webinar B : ").split(","))

semua_peserta = webinar_A.union(webinar_B)
kedua_webinar = webinar_A.intersection(webinar_B)
satu_webinar = webinar_A.symmetric_difference(webinar_B)
tidak_hadir = undangan.difference(semua_peserta)

print("\nHASIL PENGELOLAAN WEBINAR")
print("\nSemua peserta kedua webinar: ", semua_peserta)
print("\nPeserta yang hadir di kedua webinar: ", kedua_webinar)
print("\nPeserta yang hadir di salah satu webinar: ", satu_webinar)
print("\nUndangan yang tidak hadir di webinar manapun: ", tidak_hadir)
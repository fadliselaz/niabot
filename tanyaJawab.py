
with open("tanyaJawab/tanyaRumah.txt", "r") as tr:
    tanyaRumah = tr.read().splitlines()

with open("tanyaJawab/jawabRumah.txt", "r") as jr:
    jawabRumah = jr.read().splitlines()

with open("tanyaJawab/tanyaNama.txt", "r") as tn:
    tanyaNama = tn.read().splitlines()

with open("tanyaJawab/jawabNama.txt", "r") as jn:
    jawabNama = jn.read().splitlines()




niaBingung = ["maskudnya apa..?", "hmm.. maaf aku kurang paham..", "sorryy..?, bisa di ulangi..?", "maaf kak, ngak perhatiin tadi, bisa ulangi..?"]

pc = ["""
mungkin kamu lupa memasukan tanda TANYA (?)
diakhir pertanyaan kamu..
atau tanda SERU (!) diakhir PERNYATAAN kamu..

silakan ulangi berbicara dengan nia..
have fun..
""",
"""
mungkin pertanyaan atau pernyataan kamu kurang
bisa dimengerti oleh nia,
ingat nia hanyalah sebuah bot yang polos dan belum
mengerti semua hal,
silakan ungkapkan sesuatu yang mudah dimengerti"""]

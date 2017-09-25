fig = raw_input("Enter figure with 4 digit: ")
fig1 = fig[0]
fig2 = fig[1]
fig3 = fig[2]
fig4 = fig[3]
rez = "int(fig1) * int(fig2) * int(fig3) * int(fig4)"
print eval(rez)
rev = fig[::-1]
print "Your reverse figure is: {}".format(rev)

sor = sorted(fig)
sor_rez = ''.join(sor)
print "Our sorted figure: {}".format(sor_rez)
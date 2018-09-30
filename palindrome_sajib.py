def palin_sajib(char_vec):
	char_vec=char_vec.lower()
	char_vec=char_vec.replace(" ","").replace(",","")
	h=0
	t=len(char_vec)-1
	while (h<=t):
		if (char_vec[h]!=char_vec[t]):
			return False
		h=h+1
		t=t-1
	return True
			

print(palin_sajib("samas"))
print (palin_sajib("samasa"))
print (palin_sajib(""))
print("Red Roses run no risk sir  on nurses order".replace(" ","").lower())
print (palin_sajib("Red Roses run no risk, sir, on nurses order"))
print(palin_sajib("redrosesrunnorisk,sir,onnursesorder"))


l=[(1,23),
   (4,5,6),
   ("x",'y','z',0)
  ]

for t in l:
    for item in t:
        if type(item)==type(3):
            print(item)
            continue
        else:
			break
        print("Hola")
	if t[0]:
		pass